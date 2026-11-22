# Architecture Reading Guide

Read [SYSTEM-OVERVIEW.md](SYSTEM-OVERVIEW.md) first for the complete portfolio-level system description.

## Portfolio layers

The public portfolio can be navigated through four broad layers:

1. **Foundations:** standards, schemas, taxonomies, and evidence contracts (Open Intelligence Fabric; Huffman Protocol).
2. **Capabilities:** communication, orchestration, cognition, research, and defensive utilities (OIX, Open-Swarm, OIF family, CAS-XDP family).
3. **Integration:** public projects that document cross-project handoffs (Huffman Defensive Intelligence).
4. **Archive governance:** repository mesh design and the archivist engine (repo-mesh-blueprint and mesh-archivist-engine).

These layers describe roles in a portfolio. They do not establish a universal runtime or a single shared dependency graph.

## Important boundaries

- **Protocol boundary:** OIX is a communication framework. Huffman Protocol is an interoperability/conformance initiative. Multi-Agent Swarm Guardrails focuses on safety and policy. Keep their specifications distinct.
- **Execution boundary:** research plans, catalogs, conformance fixtures, and architecture documents do not imply autonomous execution.
- **Security boundary:** defensive tools must be evaluated individually for scope, privileges, rollback behavior, and platform compatibility.
- **Evidence boundary:** source provenance and reproducibility are necessary for trustworthy intelligence, but do not by themselves establish truth or attribution.
- **Publication boundary:** the public topology is a one-way, sanitized projection. It must not contain private repository metadata or inferred private architecture.

## Suggested reading sequence

1. Read [METHODOLOGY.md](METHODOLOGY.md) to understand evidence labels.
2. Read [CATALOG.md](CATALOG.md) for the individual repository roles.
3. Read [TOPOLOGY.md](TOPOLOGY.md) for explicitly documented edges and conceptual families.
4. Read [OVERLAYS.md](OVERLAYS.md) for cross-cutting planes and maturity tiers.
5. Use [BRANCH-INDEX.md](BRANCH-INDEX.md) as a point-in-time branch roster, not as a merge-status report.

## Future machine-readable contract

As project manifests become available, the archive can add explicit records for:
- stable project identifier and repository URL;
- owner and GitHub fork/upstream provenance;
- supported platforms and runtime requirements;
- declared dependencies with version/range and evidence source;
- protocol interfaces and schema versions;
- security privilege profile and rollback guarantees;
- conformance status, test command, and last verified result;
- release artifact and source commit digest.

Until these fields are published and validated by each project, the topology must not invent them.
