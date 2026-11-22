# Methodology and Publication Rules

## Scope

This snapshot covers public repositories returned by GitHub repository search for `user:HuffmanMainNode is:public` on 2026-11-22. It excludes private repositories and repositories owned by alternate accounts. The topology repository itself was created after the discovery snapshot and is not included in the 36-source-project count.

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

This pass is an inventory and architecture map, not a full code/security audit of all 36 repositories.

## Relationship classification

- **Documented integration:** an explicit public README, manifest, or integration contract identifies the connection.
- **Project-family grouping:** shared standards or explicit umbrella positioning, but no direct dependency is claimed.
- **Conceptual adjacency:** related domains only; no runtime or source dependency asserted.

Mermaid solid arrows in TOPOLOGY.md represent documented relationships. Dotted arrows represent family grouping or conceptual adjacency.

## Branch interpretation

Branch names are listed as observed. This snapshot does not establish:
- whether a branch is merged, stale, protected, or abandoned;
- whether its head commit is reachable from the default branch;
- whether branch protections or rulesets exist;
- whether a branch contains releasable code.

Branch protection values were returned as false for branches in the first inspected set; protection state is not generalized beyond observed API results.

## Known limitations

- GitHub search is a snapshot and can change as repositories are created, made private, renamed, or deleted.
- One repository, Halloween2-OSINT-2026, was reported empty at snapshot time and has no branch list.
- Some repositories have minimal descriptions or documentation; their status is intentionally conservative.
- No private account, alternate account, or private archive data is used here.
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
