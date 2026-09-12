# Qwen serving comparison — 9 September 2026 UTC

The [native Mac A2App cache test](a2app-cache-speed/README.md) now covers
weather, stock and news: median follow-up card loading fell from 14.50 s to
6.76 s, with 99.78% input-token reuse after fixing repeated reference copies
and native rendering work.

**Latest:** the H100 now uses DeepGEMM / swapAB kernels. A fresh comparison
reduced warm completion from **8.340 s to 6.644 s** (20.3%), with identical
output. See the [optimization report](h100-latency/README.md) and
[latency dashboard](h100-latency/index.html). The phone was disconnected for
that round. The benchmark table and phone captures below preserve the earlier
measurements before this kernel change.

FreeToken is running on the RTX PRO 6000 Blackwell 96GB. It is functional but
slower for this dense Qwen workload. The replacement H100 80GB passes CUDA and
runs the existing SGLang + DFlash2 setup; the Mate 70 Air now uses that H100.

## Same final-generation app request

| Configuration | Warm completion median | Decode estimate | First app request |
|---|---:|---:|---:|
| RTX / SGLang target-only (earlier) | 44.208 s | 41.4 tokens/s | — |
| RTX / SGLang + DFlash2 (earlier) | 11.543 s | 168.4 tokens/s | 27.563 s |
| RTX / FreeToken | 45.959 s | 39.7 tokens/s | 66.470 s |
| H100 / SGLang + DFlash2 | 8.432 s | 242.0 tokens/s | 17.579 s |

FreeToken used four fully warm samples; H100 used three. The H100's intermediate
partial-cache sample (14.165 s) is excluded. The H100 configuration reduces warm
completion time by **26.9%** relative to RTX DFlash2. FreeToken takes **3.98 times
as long** as RTX DFlash2 on this request. These are final model-call timings,
not complete phone generation times.

All ten newly generated full cards match the prior output byte for byte:
1,787 output tokens, 6,705 characters. All requests have the same wire payload
hash. SGLang counts 78,528 prompt tokens; FreeToken counts 77,849. The reason for
that count difference has not been isolated, so identical tokenized input is
not established. FreeToken uses BF16 KV, SGLang FP8 KV. H100 uses
FA3 attention and RTX uses FlashInfer. This compares serving configurations,
not isolated hardware or KV effects. One prompt does not establish universal
generation parity.

Prefix caching works in both: FreeToken reused 77,824/77,849 tokens (99.97%),
and SGLang reused 78,464/78,528 (99.92%). FreeToken's slower decode is not a
prefix-cache failure. This FreeToken revision has no DFlash2 serving path.
The model is dense and resident on GPU; MoE expert offloading does not apply.

## Phone and API validation

Studio build 55 generated the Taskplan weather page through H100 in **14.088 s**
(first content 6.623 s). WidgetTreeDump, WidgetSnapshot, WidgetQuery and Screenshot
captured **126 native descendants**, Taskplan kit composition, a hidden loading
overlay, and no horizontal overflow beyond the 2-pixel tolerance or wrapped
numeric values. Visual inspection passed this viewport. The satellite section
continues below the scrolling viewport.

Build 56 repeated the same context without Studio display/keep-awake extras:
**12.355 s** complete, 4.874 s first content. The phone remains in that standalone
run. Earlier RTX phone observations were 17.453–18.334 s, but used two provider
turns versus one here; that comparison does not isolate GPU performance.

FreeToken passed the complete final-generation replay and streamed a first-turn
tool call with a name and valid JSON arguments. The generated command was not
executed. Its short JSON control preserved the values but omitted SGLang's
Markdown fence. A complete FreeToken-driven native phone workflow, concurrency,
thinking mode and a broad design corpus have not been validated. Existing news
visual findings remain open.

## Running endpoints and reproduction

- Phone: H100 through the existing USB/Mac/SSH relay, local port 30882.
- H100 direct test through SSH: `http://127.0.0.1:30883/v1`.
- RTX FreeToken test through SSH: `http://127.0.0.1:30891/v1`.
- Both GPU containers use Docker `unless-stopped` restart policy.

The endpoints bind loopback. The phone still requires the USB/Mac relay.
FreeToken was restarted after the controlled trial and completed another short
request. The temporary experiment supervisor has exited; it will not later
restore the RTX SGLang container over FreeToken.

See [FreeToken Docker and launch recipe](../../../lab/demo/FREETOKEN.md),
[Hopper configuration](../../../lab/demo/h200-dflash2.json),
[DFlash2 reproduction](../../../lab/demo/H200-DFLASH2.md),
[benchmark summary](benchmark-summary.json), [FreeToken observations](freetoken-rtx.json),
[H100 observations](dflash2-h100.json), and [deployment metadata](deployment.json).
Requests, credentials, generated shell arguments and raw device logs remain
outside the repository.

![Native H100 Taskplan weather capture](weather-taskplan-h100/screen.png)
