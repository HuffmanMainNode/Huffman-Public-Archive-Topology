# Huffman Public Archive Topology

A public, evidence-led map of original repositories owned by [HuffmanMainNode](https://github.com/HuffmanMainNode). This repository separates authored projects from upstream forks and describes verified project relationships without presenting conceptual groupings as runtime dependencies.

**Scope:** Public repositories across HuffmanMainNode and five explicitly supplied alternate accounts. Private repositories remain outside this publication boundary.

## Snapshot

- Snapshot date: 2026-11-22
- Current account search returned: 51 public repositories
- Original, non-fork repositories: 37 (including the profile repository and this topology index)
- Upstream forks: 14
- Portfolio source projects: 35 before this topology index; the topology index is the 36th non-profile project repository
- Branches: current branch names indexed for all 37 original repositories
- Inventory source: GitHub repository metadata, branch endpoints, and publicly available project documentation

This is a refreshed completeness snapshot from 2026-11-22. GitHub search returned 51 results across one populated page; all 51 repository records were checked against each repository's metadata, including the authoritative `fork` flag. The 37 non-forks and 14 forks reconcile exactly to the search result. The catalog records evidence and limitations; it does not imply every repository is production-ready.

## Federated snapshot

- Six public accounts: [HuffmanMainNode](https://github.com/HuffmanMainNode), [PCakes303](https://github.com/PCakes303), [HuffmanRepositories](https://github.com/HuffmanRepositories), [midnightlolz31337](https://github.com/midnightlolz31337), [roberthuffman](https://github.com/roberthuffman), and [Ryzean84](https://github.com/Ryzean84).
- 107 public repositories reconciled: 83 original project repositories, 17 GitHub-confirmed forks, 1 controlled test copy, and 6 profile repositories.
- Five alternate accounts contribute 56 public repositories; see [MULTI-ACCOUNT-TOPOLOGY.md](MULTI-ACCOUNT-TOPOLOGY.md) and [ALT-ACCOUNT-ROSTER.md](ALT-ACCOUNT-ROSTER.md).
- Machine-readable federation: [accounts](data/accounts.json), [all repositories](data/federated-repositories.json), and [cross-account relationships](data/cross-account-relationships.json).

## Start here

- [Federated public catalog](FEDERATED-CATALOG.md): direct links to every repository across all six accounts
- [Agent entrypoint](AGENT-ENTRYPOINT.md): machine-consumer discovery and interpretation rules
- [System overview](SYSTEM-OVERVIEW.md): how the entire public portfolio fits together
- [Catalog](CATALOG.md): original repositories and evidence-based summaries
- [Topology](TOPOLOGY.md): project families and explicit integration edges
- [Architecture overlays](OVERLAYS.md): cross-cutting planes and maturity layers
- [Branch index](BRANCH-INDEX.md): observed branches on original repositories
- [External forks](EXTERNAL-FORKS.md): fork inventory and upstream attribution
- [Architecture notes](ARCHITECTURE.md): reading the topology without overclaiming
- [Methodology](METHODOLOGY.md): scope, evidence grades, and refresh procedure
- [Catalogue synchronization](docs/CATALOGUE-SYNCHRONIZATION.md): refresh behavior, boundaries, and troubleshooting
- [Primary-account repositories](data/repositories.json), [branches](data/branches.json), [overlays](data/overlays.json), [primary-account forks](data/external-forks.json)

## Reading rules

1. **Original work vs fork:** GitHub's `fork` metadata is authoritative for fork lineage. Profile repositories and the explicitly labeled USS controlled test copy are not counted as original projects. Forks remain separate and are not represented as authored projects.
2. **Verified vs inferred:** a relationship explicitly documented by a repository is marked documented. A grouping based on subject matter is marked conceptual. No conceptual grouping should be read as a software dependency.
3. **Status honesty:** a repository may be a prototype, research initiative, catalog, announcement, empty repository, or implemented tool. A public repository is not automatically a working or maintained product.
4. **Branches are not releases:** branch names are a point-in-time inventory, not a claim that every branch is current, merged, protected, or deployable.
5. **Public projection only:** no private repository names, paths, branch names, identifiers, or private architecture are included.

## Update policy

The [scheduled catalogue workflow](.github/workflows/refresh-federated-catalog.yml) refreshes public repository metadata for all six configured accounts daily and supports manual runs. See [Catalogue Synchronization](docs/CATALOGUE-SYNCHRONIZATION.md) for scope and limitations. Project-family and interoperability relationships remain editorially reviewed; metadata refresh does not certify implementation or maturity.
