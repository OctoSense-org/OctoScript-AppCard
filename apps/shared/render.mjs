/** Bind service state to measured L0/kit source. All visible controls remain Makepad widgets. */
import fontMetrics from './font-metrics.mjs';
const escape = value => value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
const clone = value => structuredClone(value);

export function buildNativePayload(bundle, view, {assetBase, id}) {
  if (!bundle.scenes[String(view.frameId)]) throw new Error(`Unknown scene ${view.frameId}`);
  const scene = JSON.parse(JSON.stringify(bundle.scenes[String(view.frameId)]).replaceAll('__OCTOSENSE_ASSETS__/', assetBase));
  let {card} = scene;
  const {data, kit, mapping} = scene;
  const placements = data.$kit.placements;
  const nodes = Object.fromEntries(mapping.elements.map(node => [node.source_id, node]));
  const styles = new Map();
  function style(key, values) {
    const placement = placements[key];
    if (!placement) throw new Error(`Missing native style target ${key}`);
    if (!styles.has(key)) {
      const original = placement.component, name = `${original}_bound_${key}`;
      const definition = card.match(new RegExp(`component ${escape(original)}\\([^\\n]*\\) \\{\\n[^\\n]*\\n\\}\\n`));
      if (!definition) throw new Error(`Missing native component ${original}`);
      kit.components[name] = clone(kit.components[original]);
      const replacement = definition[0].replace(`component ${original}(`, `component ${name}(`).replace(`component: "${original}"`, `component: "${name}"`);
      card = card.replace('\nview root ', `\n${replacement}\nview root `)
        .replace(`${original}(instance: ${JSON.stringify(key)}`, `${name}(instance: ${JSON.stringify(key)}`);
      placement.component = name;
      styles.set(key, name);
    }
    Object.assign(kit.components[placement.component].style, values);
  }
  function text(key, value) {
    if (!placements[key] || !nodes[key]) throw new Error(`Missing native text target ${key}`);
    if (typeof value !== 'string') throw new Error(`Native copy must be text: ${key}`);
    const pattern = new RegExp(`(copy ${escape(key)}_text \\{ class: user-copy, en: )"(?:[^"\\\\]|\\\\.)*"( \\})`);
    if (!pattern.test(card)) throw new Error(`Missing native copy ${key}`);
    card = card.replace(pattern, (_, start, end) => start + JSON.stringify(value) + end);
    nodes[key].text = value;
  }
  function enabled(key, value) {
    const nodeId = nodes[key]?.kind === 'button' ? key : `${key}_control`;
    if (!nodes[nodeId]) throw new Error(`Missing native button ${key}`);
    const pattern = new RegExp(`(state ${escape(nodeId)}_enabled \\{ shape: bool, initial: )(true|false)( \\})`);
    if (!pattern.test(card)) throw new Error(`Missing enabled state ${nodeId}`);
    card = card.replace(pattern, (_, start, _old, end) => start + String(Boolean(value)) + end);
    nodes[nodeId].enabled = Number(Boolean(value));
  }
  for (const [key, value] of Object.entries(view.nativeText || {})) text(key, value);
  for (const [key, values] of Object.entries(view.nativeLayout || {})) {
    if (!placements[key]) throw new Error(`Missing native layout target ${key}`);
    const dx = values.x === undefined ? 0 : values.x - placements[key].layout.x;
    const dy = values.y === undefined ? 0 : values.y - placements[key].layout.y;
    for (const [property,value] of Object.entries(values)) {
      if (!['x','y','w','h'].includes(property) || !Number.isFinite(value) || (['w','h'].includes(property) && value <= 0)) throw new Error(`Invalid native layout ${key}.${property}`);
      placements[key].layout[property] = value;
    }
    // The compiler stores absolute coordinates. Moving a container moves its
    // native descendants as a group, while preserving their relative positions.
    if (dx || dy) {
      const descendants = new Set([key]);
      for (const node of mapping.elements) if (descendants.has(node.parent)) {
        descendants.add(node.source_id);
        placements[node.source_id].layout.x += dx;
        placements[node.source_id].layout.y += dy;
      }
    }
  }
  for (const [key, value] of Object.entries(view.nativeEnabled || {})) enabled(key, value);
  for (const control of view.nativeControls) {
    enabled(control.sourceId, control.enabled);
    if (control.textIds?.length === 1) {
      const key = control.textIds[0], bounds = placements[control.sourceId].layout;
      text(key, control.label);
      Object.assign(placements[key].layout, {x: bounds.x + 8, w: bounds.w - 16});
      style(key, {alignx: .5, tracking: 0});
    }
  }
  for (const [key, values] of Object.entries(view.nativeStyles || {})) style(key, values);
  // Use the actual embedded font's glyph advances for both translated and dynamic copy.
  // Preserve a readable 10 px minimum; insufficient geometry must be fixed in the flow.
  {
    for (const node of mapping.elements) {
      if (typeof node.text !== 'string') continue;
      const placement = placements[node.source_id];
      const properties = kit.components[placement.component].style;
      const resolve = value => value?.$token ? kit.tokens[value.$token]?.value : value;
      const size = Number(resolve(properties.size) || 14);
      const font = String(resolve(properties.font_src) || 'Regular');
      const metrics = fontMetrics[font.includes('Bold') ? 'Bold' : font.includes('Medium') ? 'Medium' : 'Regular'];
      const em = Math.max(...node.text.split('\n').map(line => [...line].reduce((sum, char) => sum + (metrics.advance[char.codePointAt(0)] ?? metrics.default), 0)));
      const fitted = Math.min(size, Math.max(10, (placement.layout.w - 3) / Math.max(1, em)));
      style(node.source_id, {size: fitted, tracking: 0});
    }
  }
  for (const key of view.nativeHidden || []) {
    if (!placements[key]) throw new Error(`Missing native visibility target ${key}`);
    const pattern = new RegExp(`^([ \\t]*)[A-Za-z0-9_]+\\(instance: ${escape(JSON.stringify(key))}[^\\n]*\\n`, 'm');
    const match = pattern.exec(card);
    if (!match) throw new Error(`Missing native instance ${key}`);
    let end = match.index + match[0].length;
    if (match[0].trimEnd().endsWith('{')) {
      const closing = new RegExp(`^${escape(match[1])}\\}\\n`, 'm').exec(card.slice(end));
      if (!closing) throw new Error(`Unbalanced native instance ${key}`);
      end += closing.index + closing[0].length;
    }
    const removed = new Set([key]);
    for (let changed = true; changed;) {
      changed = false;
      for (const node of mapping.elements) if (removed.has(node.parent) && !removed.has(node.source_id)) {removed.add(node.source_id); changed = true;}
    }
    if (view.nativeControls.some(control => removed.has(control.sourceId))) throw new Error('Hidden controls must be removed from the service view');
    card = card.slice(0, match.index) + card.slice(end);
    mapping.elements = mapping.elements.filter(node => !removed.has(node.source_id));
    for (const sourceId of removed) {delete placements[sourceId]; delete nodes[sourceId];}
  }
  const childCounts = {};
  for (const node of mapping.elements) {
    const placement = placements[node.source_id];
    node.bounds = ['x', 'y', 'w', 'h'].map(key => placement.layout[key] || 0);
    node.component = placement.component;
    const index = childCounts[node.parent] || 0; childCounts[node.parent] = index + 1;
    node.native_id = node.parent ? `${nodes[node.parent].native_id}_${index}` : `beauty_${index}`;
  }
  return {id, frameId: view.frameId, card, data, kit, mapping, width: bundle.artboard[0], height: bundle.artboard[1]};
}
