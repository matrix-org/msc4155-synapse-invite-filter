# msc4155-synapse-invite-filter

> [!WARNING]
> This module is ***highly experimental*** and subject to breakage, change, and deprecation with no or limited
> notice. **Use at your own risk** (but let us know if there's bugs).

> [!WARNING]
> This module may have performance implications for your server.

> [!IMPORTANT]
> Uninstall this module as soon as possible. This module exists exclusively as an unstable implementation and will never have a release.

A Synapse module which implements a [variant](https://github.com/matrix-org/matrix-spec-proposals/pull/4155/files#r2025643976) of MSC4155 invite conditions.

Features:
* [ ] Ignoring invites
* [x] Blocking invites
* [x] Allowing invites (ie: default behaviour of invites)

## Installing

In your Synapse environment:

```bash
pip install git+https://github.com/matrix-org/msc4155-synapse-invite-filter#egg=msc4155-synapse-invite-filter
```

In your Synapse config:

```yaml
modules:
  - module: "msc4155.Filter"
    config: {}
```
