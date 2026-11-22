# Agent Entry Point: Huffman Public Knowledge Library

This repository is a public, evidence-led directory of repositories across six GitHub accounts. It is a catalogue and navigation layer, not a hosted API, runtime orchestrator, or proof that every listed project is production-ready.

## Start here

1. Read [README.md](README.md) for the human landing page.
2. Read [FEDERATED-CATALOG.md](FEDERATED-CATALOG.md) for the complete linked directory.
3. Load [data/federated-repositories.json](data/federated-repositories.json) as the canonical repository ledger.
4. Load [data/accounts.json](data/accounts.json) for account scope and roles.
5. Load [data/cross-account-relationships.json](data/cross-account-relationships.json) for recorded cross-account relationships.
6. Read [METHODOLOGY.md](METHODOLOGY.md) before making claims about ownership, maturity, or integration.

## Consumer rules

- Use each record's `url` as the canonical human-facing repository URL.
- Use `full_name` as the stable owner/repository identifier; do not infer ownership from a display name.
- Preserve the `classification` field. Do not merge original projects, upstream forks, controlled test copies, and profile repositories into one authorship category.
- Preserve fork attribution. A fork is not an original project merely because it appears in this collection.
- Treat `family` as a discovery grouping, not a dependency declaration.
- Treat descriptions and project claims as declared intent unless independently supported by source review, tests, releases, or other evidence.
- Treat the snapshot date and per-record verification timestamp as the last successful metadata observation. The scheduled workflow refreshes public metadata daily, but it is not a live feed and can be delayed or fail. Check the latest successful Actions run before claiming freshness.
- Do not infer private repositories, private infrastructure, private relationships, or unpublished implementation details.
- When reporting a capability, cite the specific repository and evidence that supports it.

## Suggested discovery workflow

Filter the JSON ledger by `account`, `classification`, or `family`; then open the canonical `url`. The scheduled refresh checks all six configured accounts daily; see [Catalogue Synchronization](docs/CATALOGUE-SYNCHRONIZATION.md). For implementation questions, inspect the repository's default branch, README, manifests, source, tests, and release history. Record uncertainty rather than filling gaps with assumptions.

## Schema

The ledger currently uses schema version `1.0.0`. Fields include repository name, owner, canonical URL, fork/archive flags, default branch, project family, description, account, classification, evidence level, and full name. Optional fields may be absent; consumers should tolerate missing values.
