# Catalogue Synchronization

## What happens when another account changes?

Changes in any of the six configured GitHub accounts do not automatically appear here merely because the accounts belong to the same person. Each GitHub repository has its own files and history.

The scheduled workflow checks the public repositories for all six configured accounts once per day and can also be run manually from the Actions tab.

## Schedule

- Daily at 12:30 UTC.
- Manual execution: Actions → Refresh federated public catalogue → Run workflow.
- The workflow reads public GitHub metadata without requiring credentials for the five alternate accounts.
- The collector accepts an optional GITHUB_TOKEN environment variable for higher API rate limits, but the scheduled workflow does not require it.

## What it refreshes

- Public repository inventory, with pagination.
- Canonical repository URLs and owner/name identifiers.
- GitHub fork status and upstream parent/source links.
- Default branch, archived state, descriptions, language, topics, license identifier, and repository timestamps.
- Account totals, machine-readable JSON, verified fork-lineage edges, and the human-readable federated catalogue.

Curated project-family labels and editorial descriptions are retained where possible. Newly discovered repositories receive conservative default classifications.

## What it does not do

- It does not clone or mirror source code from other accounts.
- It does not synchronize commits, branches, issues, releases, or files from one repository into another.
- It does not inspect private repositories.
- It does not certify functionality, security, licensing compliance, or production readiness.
- It does not automatically infer new conceptual or interoperability relationships.

## Failure and review behavior

A failed API request or empty account response stops the run before publication. The script checks uniqueness, account totals, catalogue row counts, and fork reconciliation before generated changes can be committed. Review the Actions run log after failures and inspect the generated commit after successful runs.

The schedule is UTC. 12:30 UTC corresponds to 5:30 AM Mountain Standard Time and 6:30 AM Mountain Daylight Time. GitHub scheduled workflows can start later than the exact scheduled minute.
