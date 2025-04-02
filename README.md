# msc4155-synapse-invite-filter

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
