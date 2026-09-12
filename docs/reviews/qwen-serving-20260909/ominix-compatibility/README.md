# OminiX-SGLang compatibility check — 9 September 2026

The public OminiX-SGLang `main` checkout does not currently contain the
DFlash2 runtime required by the active Qwen3.8-27B-FP8 service. The working
service remains on upstream SGLang; no inference-server replacement or
performance comparison was performed.

Checked revision: `1d657d7d38bed8a0b0773c481a9e59c1d71a4c89`.
The repository exposes one branch, `main`; its two pull-request heads cover
the published C2Rust recipe and native 256K context update.

The checkout was cloned onto the GPU host. Executing its actual
`SpeculativeAlgorithm.from_string("DFLASH")` returned:

```text
ValueError: Unknown speculative algorithm name: DFLASH
```

Its algorithm enum contains `EAGLE`, `EAGLE3`, `STANDALONE`, `NGRAM`, and
`NONE`. The DFlash model module is absent. The published
[C2Rust DFlash recipe](https://github.com/OminiX-ai/OminiX-SGLang/blob/1d657d7d38bed8a0b0773c481a9e59c1d71a4c89/docs/ominix/C2RUST_QWEN35_27B_FP8_DFLASH_HOPPER.md)
explicitly documents this limitation and uses an external SGLang 0.5.16
image. Its derived Dockerfile installs Accelerate; it does not install
this fork's Python package. The published Qwen3.8 launcher selects NGRAM.

The active service still reports upstream revision `5f55db35e`, DFLASH
enabled, a 262,144-token context, radix caching enabled, and per-request
cache reporting enabled. Hardware identifies itself as H100 80GB HBM3.

To test the user's OminiX DFlash2 implementation, the missing input is its
branch, commit, or runnable image. No claim about that implementation's
performance or cache-hit rate follows from this compatibility check.
