# Native repositories

Makepad and the Octoscript engines are independent Git repositories in the
organization workspace. They are not AppCards submodules or application folders.

```text
home/
  Octosense-Service-AppCards/
    apps/{aircon,mail,school,health,reunion}/
    lab/
    tools/
  octosense-org/
    makepad/
    octoscript/
    octoscript-makepad/
    .appcard-native/mail/      # isolated pinned build checkouts
```

`OCTOSENSE_WORKSPACE` overrides the organization workspace path. The default is
the AppCards parent when it is named `octosense-org`, otherwise its sibling
`octosense-org` directory. `lab/core/native_paths.py` resolves all three paths.
`OCTOS_APPCARD_NATIVE_ROOT` selects another prepared set for pipeline compilation.

| Directory | Repository |
| --- | --- |
| `makepad` | `https://github.com/OctoSense-org/makepad.git` |
| `octoscript` | `https://github.com/OctoSense-org/Octoscript.git` |
| `octoscript-makepad` | `https://github.com/OctoSense-org/Octoscript-Makepad.git` |

The pinned upstream revisions still use Rust crate names such as `splash-ui-l0`
and `splash-makepad`. Those crate names and historical patch/lock identifiers
remain intact. Repository directory names are `octoscript` and
`octoscript-makepad`. The setup helper adapts the two upstream Cargo manifests
that reference the old sibling directory `splash/`.

Mail's [setup command](../apps/mail/README.md) creates its pinned checkouts under
`$OCTOSENSE_WORKSPACE/.appcard-native/mail/`, using the same three directory names.
`OCTOS_MAIL_NATIVE_ROOT` overrides that isolated location. This lets the app use
its verified compatibility patches while preserving work in the shared repos.
Native source checkouts must stay outside AppCards. App runtime state stays in
ignored `apps/mail/runtime/` and `apps/mail/private/`.

New native testing uses [Makepad's built-in instrument](../lab/core/NATIVE-INSTRUMENT.md)
with standalone release binaries and hidden windows. Historical receipt paths
describe their original runs, not the current checkout layout.
