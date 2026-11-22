# Architectural Overlays

The overlays apply across the wider six-account public portfolio. The complete account-by-account mapping and integration relationships are in [MULTI-ACCOUNT-TOPOLOGY.md](MULTI-ACCOUNT-TOPOLOGY.md).

The complete narrative of the public portfolio is in [SYSTEM-OVERVIEW.md](SYSTEM-OVERVIEW.md). The refreshed account snapshot contains 37 non-fork repositories (including the profile and this index) and 14 forks.

This document overlays the public portfolio using functional planes and maturity tiers. The overlays are an organizing model for the public archive, not a claim that every project participates in a single deployed system.

## Six functional planes

| Plane | Purpose | Public repositories |
|---|---|---|
| P1. Archive and evidence | Cataloging, source provenance, historical/contextual research | Protocol-Helios; Project-Helios-US-Archive; Project_Lazarus_OSINT; Curated-Modern-OSINT-Tools; OIF-Research-Observatory |
| P2. Exchange and protocol | Agent identity, messages, interoperability, conformance, trust boundaries | Open-Intelligence-Exchange; Huffman-Protocol; Open-Intelligence-Fabric; Multi-Agent-Swarm-Guardrails |
| P3. Orchestration and cognition | Agent tasking, swarm composition, reasoning, collective intelligence, workspace | -Open-Swarm; OI-Swarm-Intelligence; OIF-Cognitive-Systems; OIF-Collective-Intelligence; OpenWorkSpace |
| P4. Defensive security | Host inspection, ingress filtering, artifact trust, canaries, AI security, cyber intelligence | Huffman-Cyber-Observatory; Huffman-Defensive-Intelligence; cas-xdp-supervisor; posix-containment-kit; xdp-ingress-primitives; cas-threat-index; canary-labyrinth-httpd; OIF-Cyber-Intelligence; OIF-AI-Security |
| P5. Model and systems research | Model analysis, systems intelligence, reverse engineering | OIF-Model-Intelligence; OIF-Systems-Intelligence; Huffman-Reverse-Intelligence |
| P6. Archive governance and tooling | Repository discovery, topology, reproducibility, public projection | repo-mesh-blueprint; mesh-archivist-engine; this repository |

A repository can occupy multiple planes. Placement is a navigation aid, not an exclusive classification.

## Maturity tiers

| Tier | Meaning | Public examples |
|---|---|---|
| T0. Announcement / empty | Public presence without a substantive implementation to assess | Coming-Soon-Project-AVI; Happy-Halloween-2026 (announcement/index); Halloween2-OSINT-2026 (empty at snapshot) |
| T1. Research / specification | Research, taxonomy, standards, curated catalogs, or planned capabilities | Open-Intelligence-Fabric; OIF-Research-Observatory; Huffman-Reverse-Intelligence; Protocol-Helios |
| T2. Prototype / bounded utility | Working or described components with explicit limits; requires project-level verification | OpenWorkSpace; Huffman-Protocol; Multi-Agent-Swarm-Guardrails; canary-labyrinth-httpd; CAS components |
| T3. Integration / orchestration | Multiple public components with documented handoff or integration work | Huffman-Defensive-Intelligence; Open-Intelligence-Exchange; -Open-Swarm |
| T4. Archive infrastructure | Tools and standards intended to support reproducible inventory and controlled publication | repo-mesh-blueprint; mesh-archivist-engine |

Tiers are descriptive and conservative. They are not security certifications, release grades, or production-readiness ratings. A project can move between tiers as evidence changes.

## Federated mesh notation

The archive engineering standard uses the notation **M × (1 + 1 + N)** for a federated mesh: one authoritative namespace/root, one controlled public projection, and N participating repositories or nodes. This is a design model documented by `repo-mesh-blueprint`, not a claim that this public topology repository is already a live controller for all account repositories.

## Evidence and trust overlay

Every relationship should carry one of these evidence labels:

- **D1: Direct documentation**: an explicit integration statement, manifest, or contract in a public repository.
- **D2: Repository metadata**: GitHub fork status, upstream parent/source, branch list, archived flag, or repository description.
- **I1: Strongly inferred grouping**: public purpose and project-family naming align, but no direct dependency is asserted.
- **U: Unverified**: a plausible relationship or feature that requires source-level or runtime validation.

The current map uses D1 for HDI's documented project integrations, D2 for ownership/fork/branch facts, I1 for OIF/CAS functional families, and U where no adequate public evidence was inspected.
