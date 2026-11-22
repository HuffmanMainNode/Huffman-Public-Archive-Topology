# Methodology

## Federation extension

The federation snapshot covers HuffmanMainNode and five user-supplied alternate accounts. The scheduled refresh queries all six public account inventories with pagination and updates the unified ledger. See [FEDERATED-CATALOG.md](FEDERATED-CATALOG.md), [MULTI-ACCOUNT-TOPOLOGY.md](MULTI-ACCOUNT-TOPOLOGY.md), and [data/accounts.json](data/accounts.json). Private repositories remain excluded.

## Publication Rules

## Scope

The original account-only snapshot below is historical context. The current federated ledger is authoritative for the six configured public accounts. The refresh script uses the GitHub user-repositories endpoint with pagination and reconciles each returned repository's metadata. Private repositories are excluded.

## Ownership classification

GitHub repository metadata field `fork` is the deciding field:
- `fork=false`: original-account repository, included in the owned-project catalog.
- `fork=true`: fork, excluded from the owned-project catalog and listed separately with its upstream parent/source.

A fork may contain original changes, but this catalog does not reclassify it as original work. Attribution remains with the upstream repository unless separately documented.

## Evidence hierarchy

1. GitHub API repository metadata: ownership, fork flag, upstream, archive state, default branch, timestamps.
2. GitHub branch endpoint: branch names and current head SHAs as observed during the snapshot.
3. Public README and repository documentation: intended purpose, declared features, constraints, integration statements.
4. Source-level review and tests: required before stronger claims about actual behavior, correctness, or production readiness.

This pass is an inventory and architecture map, not a full code/security audit of every source-project repository across the six accounts.

## Relationship classification

- **Documented integration:** an explicit public README, manifest, or integration contract identifies the connection.
- **Project-family grouping:** shared standards or explicit umbrella positioning, but no direct dependency is claimed.
- **Conceptual adjacency:** related domains only; no runtime or source dependency asserted.

Mermaid solid arrows in TOPOLOGY.md represent documented relationships. Dotted arrows represent family grouping or conceptual adjacency.

## Branch interpretation

Branch names were re-fetched from the GitHub branches endpoint for every one of the 37 non-fork repositories, including this topology repository. This snapshot does not establish:
- whether a branch is merged, stale, protected, or abandoned;
- whether its head commit is reachable from the default branch;
- whether branch protections or rulesets exist;
- whether a branch contains releasable code.

Branch protection values were returned as false for branches in the first inspected set; protection state is not generalized beyond observed API results.

## Known limitations

- GitHub search is a snapshot and can change as repositories are created, made private, renamed, or deleted.
- One repository, Halloween2-OSINT-2026, was reported empty at snapshot time and has no branch list.
- Some repositories have minimal descriptions or documentation; their status is intentionally conservative.
- Only the six explicitly configured public account inventories are queried; private repositories and private archive data are excluded.
- This pass does not execute project code or reproduce every project's CI.

## Refresh procedure

1. Re-run account-scoped public repository search and paginate until no results remain.
2. Fetch repository metadata for every result and classify fork status from GitHub's `fork` field.
3. For original repositories, fetch branch names and default-branch documentation.
4. Inspect README, manifests, and dependency declarations before changing topology edges.
5. Update machine-readable data first, then regenerate human-readable indexes.
6. Review the public diff for private data leakage and unsupported claims.
7. Record the new snapshot date and commit.

## Responsible use

Treat OSINT and security project outputs as leads requiring corroboration. Do not infer guilt, attribution, identity, or threat status from a single indicator or automated score.
