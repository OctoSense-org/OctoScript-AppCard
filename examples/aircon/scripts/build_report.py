#!/usr/bin/env python3
"""Summarize existing native evidence without manufacturing acceptance."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, html, json

ROOT = Path(__file__).resolve().parents[1]
def read(p): return json.loads(Path(p).read_text())
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p, value): Path(p).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def build():
    scenes = []
    for d in sorted((ROOT / 'cards').glob('aircon-*')):
        latest = read(d / 'latest.json')
        r = d / 'rounds' / latest['round']
        gate, proof, mapping = read(r / 'gate.json'), read(r / 'provenance.json'), read(r / 'mapping.json')
        scenes.append({'id': d.name, 'round': latest['round'], 'build_id': latest['build_id'],
            'native_structure_pass': gate['native_structure_pass'],
            'semantic_mapping_pass': gate['semantic_mapping_pass'],
            'image_structure_pass': gate['image_structure_pass'], 'strict_image_accepted': gate['accepted'],
            'native_nodes': len(mapping['elements']),
            'native_controls': sum(e['kind'] == 'button' for e in mapping['elements']),
            'input_current': sha(d / 'mapped.json') == sha(r / 'mapped.json'),
            'image_findings': gate['image_errors'], 'native_findings': gate['native_errors'],
            'provenance_sha256': sha(r / 'provenance.json'), 'native_sha256': sha(r / 'native.png'),
            'evidence': str(r.relative_to(ROOT))})
    standalone = read(ROOT / 'evidence/standalone-latest.json')
    flow = read(ROOT / 'evidence/native-flow-latest.json')
    catalogue = read(ROOT / 'service-cards/catalogue.json')
    tests = read(ROOT / 'service/validation.json')
    native_pass = all(s['native_structure_pass'] and s['semantic_mapping_pass'] and s['input_current'] for s in scenes)
    report = {'schema_version': 1, 'recorded_at': datetime.now(timezone.utc).isoformat(),
        'native_conversion_validated': native_pass and standalone['passed'] and flow['passed'] and tests['passed'],
        'strict_reference_parity_accepted': all(s['strict_image_accepted'] for s in scenes),
        'scene_count': len(scenes), 'standalone_card_count': len(catalogue['cards']),
        'native_nodes': sum(s['native_nodes'] for s in scenes),
        'native_controls': sum(s['native_controls'] for s in scenes),
        'native_flow_checks': len(flow['checks']), 'local_service_tests': tests['tests_run'],
        'source_atlas_sha256': sha(ROOT / 'source/atlas.png'),
        'runtime_infrastructure_sha256': sha(ROOT / 'runtime/infrastructure.json'),
        'scenes': scenes,
        'standalone_evidence': standalone['directory'], 'service_flow_evidence': flow['directory'],
        'scope': 'Actual Makepad Studio RunItem, WidgetTreeDump, WidgetSnapshot, WidgetQuery, layout, Screenshot and Click',
        'limitations': ['Service providers and payment are deterministic local fixtures; no production network operations',
            'Scene layout is fixed at 406 × 776; independent cards use their measured dimensions, not responsive reflow',
            'Exact reference-image gates retain unresolved typography/OCR, vector-detail and surface-effect differences',
            'Shopping interior has two source-derived screens; other app routes expose native service data previews'],
        'source_files': {str(p.relative_to(ROOT)): sha(p) for base in ['scripts', 'service', 'runtime']
                         for p in (ROOT / base).glob('*.py')},
        'evidence_receipts': {name: sha(ROOT / name) for name in ['evidence/standalone-latest.json',
            'evidence/native-flow-latest.json', 'service/validation.json', 'runtime/image-pipeline.patch']}}
    write(ROOT / 'evidence/conversion-report.json', report)
    lines = ['# 空调到家 · Makepad Service App Card 转换报告', '',
        f"{len(scenes)} 个完整场景、{len(catalogue['cards'])} 个独立卡片，归属订单、物流、安装、日历和支付服务。",
        '', f"原生转换验证：{'通过' if report['native_conversion_validated'] else '尚未全部通过'}。"
        f"Makepad 实际读取 {report['native_nodes']} 个场景组件、检查 {report['native_controls']} 个原生按钮；"
        f"完整服务流程 {report['native_flow_checks']} 个检查点，另有 {tests['tests_run']} 项本地状态与绑定测试。", '',
        '文字、按钮、卡面与图标分别由原生 Label、Button、View、Svg 绘制。图片仅用于经过核对的商品摄影与头像，界面没有整屏图片热点。', '',
        '严格图像一致性与原生功能分别验收。原图中的字形、图标细节、阴影与背景纹理仍有差异；图像 gate 的未通过结果完整保留，未调宽容差。', '',
        '| 场景 | 原生结构 | 语义映射 | 严格图像验收 | 证据 |', '| --- | --- | --- | --- | --- |']
    for s in scenes:
        yes = lambda v: '通过' if v else '待修'
        lines.append(f"| {s['id']} | {yes(s['native_structure_pass'])} | {yes(s['semantic_mapping_pass'])} | {yes(s['strict_image_accepted'])} | [第 {s['round']} 轮](../{s['evidence']}/gate.json) |")
    lines += ['', '## 可验证的服务行为', '',
        '- 购买订单、物流更新、送达、安装预约、师傅出发及付款由共享服务状态驱动',
        '- 冲突时段禁用，预约成功写入同一日历事件；日历确认只表示已阅',
        '- 撤销日历保留安装预约，重新加入恢复原事件',
        '- 撤销待支付请求保留已完成安装；真实原生重复点击支付只产生一次模拟付款',
        '', f"- [完整原生服务流程](../{flow['directory']}/report.json)",
        f"- [独立卡片挂载与输入验证](../{standalone['directory']}/report.json)",
        '- [本地状态测试](../service/validation.json)', '- [Studio 运行环境与兼容补丁](../runtime/infrastructure.json)',
        '', '## 使用边界', '',
        '本地演示不连接商家、物流或支付平台。其他应用详情路由目前为原生服务数据预览。完整场景使用固定画板；独立卡片已使用各自实际宽高挂载，尚不承诺任意尺寸的响应式布局。', '',
        '运行方法见 [README](../README.md)。源图与历史验证轮次保持不变。']
    (ROOT / 'evidence/conversion-report.md').write_text('\n'.join(lines) + '\n')
    print(json.dumps({k: report[k] for k in ['native_conversion_validated', 'strict_reference_parity_accepted', 'scene_count', 'standalone_card_count', 'native_flow_checks']}, ensure_ascii=False))

if __name__ == '__main__': build()
