# Huffman Public Archive Topology

A public, evidence-led map of original repositories owned by [HuffmanMainNode](https://github.com/HuffmanMainNode). This repository separates authored projects from upstream forks and describes verified project relationships without presenting conceptual groupings as runtime dependencies.

> **Scope:** Public repositories under the HuffmanMainNode account only. Private repositories and alternate accounts are outside this publication boundary.

## Snapshot

- Snapshot date: 2026-11-22
- Account search returned: 50 repositories before this topology repository was created
- Original repositories: 36
- Forks: 14
- This topology repository: 1 additional index repository, excluded from the 36-project source count
- Inventory source: GitHub repository metadata, branch endpoints, and publicly available project documentation

Counts describe the discovery snapshot. The catalog records per-repository evidence and limitations; it does not imply every repository is production-ready.

## Start here

- [Catalog](CATALOG.md): original repositories and evidence-based summaries
- [Topology](TOPOLOGY.md): project families and explicit integration edges
- [Architecture overlays](OVERLAYS.md): cross-cutting planes and maturity layers
- [Branch index](BRANCH-INDEX.md): observed branches on original repositories
- [External forks](EXTERNAL-FORKS.md): fork inventory and upstream attribution
- [Architecture notes](ARCHITECTURE.md): reading the topology without overclaiming
- [Methodology](METHODOLOGY.md): scope, evidence grades, and refresh procedure
- [Machine-readable repositories](data/repositories.json), [branches](data/branches.json), [overlays](data/overlays.json), [external forks](data/external-forks.json)

## Reading rules

1. **Original work vs fork:** only repositories whose GitHub metadata reports `fork=false` enter the original-project catalog. Forks remain in a separate register and are not represented as authored projects.
2. **Verified vs inferred:** a relationship explicitly documented by a repository is marked documented. A grouping based on subject matter is marked conceptual. No conceptual grouping should be read as a software dependency.
3. **Status honesty:** a repository may be a prototype, research initiative, catalog, announcement, empty repository, or implemented tool. A public repository is not automatically a working or maintained product.
4. **Branches are not releases:** branch names are a point-in-time inventory, not a claim that every branch is current, merged, protected, or deployable.
5. **Public projection only:** no private repository names, paths, branch names, identifiers, or private architecture are included.

## Update policy

Refresh repository metadata and branches from GitHub before publishing a new snapshot. Record the snapshot date, preserve upstream attribution for forks, and review all proposed relationship edges against public documentation before adding them.
