# Multi-Account Public Ecosystem Topology

## Executive summary

The public Huffman Systems portfolio is distributed across six GitHub accounts: the primary `HuffmanMainNode` account and five explicitly identified alternates. This is a federation of independently versioned repositories, not one monolithic application and not a single live runtime.

**Snapshot: 2026-11-22**

| Measure | Count |
|---|---:|
| Public repositories across six accounts | **107** |
| Original project repositories | **83** |
| GitHub-confirmed forks | **17** |
| Controlled test copies with fork=false | **1** |
| Profile/landing repositories | **6** |
| Accounts | **6** |

The arithmetic reconciles: 83 original project repositories + 17 upstream forks + 1 controlled test copy + 6 profile repositories = 107 public repositories.

The five alternate accounts contain 56 public repositories: 47 original projects, 3 GitHub-confirmed forks, 1 controlled test copy, and 5 profile repositories.

## Account roster

| Account | Public repos | Original projects | Forks | Special classification | Primary public role |
|---|---:|---:|---:|---:|---|
| [HuffmanMainNode](https://github.com/HuffmanMainNode) | 51 | 36 | 14 | 1 profile | Primary systems, protocols, OSINT, defensive security, and public archive topology |
| [PCakes303](https://github.com/PCakes303) | 33 | 32 | 0 | 1 profile | MrCakes931 Agent Intelligence Ecosystem |
| [HuffmanRepositories](https://github.com/HuffmanRepositories) | 12 | 11 | 0 | 1 profile | Ecosystem navigation, compatibility research, and agent reliability fixtures |
| [midnightlolz31337](https://github.com/midnightlolz31337) | 5 | 4 | 0 | 1 profile | ELITE protocols, ingestion, agent commons, and network atlas |
| [roberthuffman](https://github.com/roberthuffman) | 4 | 0 | 2 | 1 controlled test copy + 1 profile | Controlled testing copies and profile |
| [Ryzean84](https://github.com/Ryzean84) | 2 | 0 | 1 | 1 profile | Research workspace profile and OSINT tools fork |

Counts use account-scoped public repository search followed by individual repository metadata checks. GitHub's `fork` property determines fork classification. A profile repository is not counted as a project. The controlled test copy is not counted as original authored work.

## 1. PCakes303: Agent Intelligence Ecosystem

This is the largest alternate-account project family: 32 public project repositories plus the profile repository. The canonical registry is [agent-intelligence-ecosystem](https://github.com/PCakes303/agent-intelligence-ecosystem); the human-facing guide is [mrcakes931-ecosystem](https://github.com/PCakes303/mrcakes931-ecosystem).

The public registry divides the portfolio into these functional layers:

- **Control plane and discovery:** canonical repository registry, dependency graph, governance, discovery metadata, human onboarding, and cross-repository integration profiles.
- **Foundation and security:** normative foundation requirements, resource manifests, schema registry, identity/trust contracts, supply-chain metadata, default-deny policy evaluation, audit/provenance, emergency-control contracts, and compliance governance.
- **Protocols:** AIX Core semantic message contracts, AIX Codecs canonical serialization, and an experimental transport-neutral gateway boundary for HTTP, MCP, and A2A.
- **Swarm:** agent discovery, capability registry, runtime contracts, task coordination, and state/context mesh.
- **Intelligence:** public-source registry, authorized collection framework, evidence metadata, bounded public-entity candidate matching, and a provenance-aware knowledge graph.
- **Adoption and conformance:** tool adapters, declarative skill packages, sandbox admission contracts, conformance testing, and federation declarations.
- **Research:** adaptive swarm compression and information representation.

The registry reports most components as scaffolding, with selected reference implementations marked experimental. It explicitly distinguishes repository existence, implementation, and verification. Many components are contract validators or single-process reference implementations, not deployed distributed services. For example, the policy engine is not a resource enforcement boundary; the sandbox repository does not implement OS isolation; the emergency-control project is not an operational kill switch; and OSINT evidence hashing does not establish truth or legal chain of custody.

The public machine-readable dependency graph is the authoritative source for PCakes-declared edges. Those edges describe declared prerequisites or optional integrations, not proof that every dependency is installed, tested, or connected at runtime.

## 2. HuffmanRepositories: Open Agent Compatibility and reliability fixtures

This account has 11 public project repositories plus its profile repository. Its public directory is [Huffman-Ecosystem-Root](https://github.com/HuffmanRepositories/Huffman-Ecosystem-Root), with [Huffman-Ecosystem-Guide](https://github.com/HuffmanRepositories/Huffman-Ecosystem-Guide) as human onboarding.

The portfolio divides into:

- **Mission and coordination:** [Open-Source-AI-Independence](https://github.com/HuffmanRepositories/Open-Source-AI-Independence).
- **Compatibility research:** [Open-Agent-Compatibility](https://github.com/HuffmanRepositories/Open-Agent-Compatibility) and [Open-Agent-Compatibility-Fixtures](https://github.com/HuffmanRepositories/Open-Agent-Compatibility-Fixtures). OAC maps existing protocols and documents mismatches; it is not another protocol, runtime, or certification body.
- **Usage representation:** [Open-Agent-Run-Metrics-Interop](https://github.com/HuffmanRepositories/Open-Agent-Run-Metrics-Interop), a draft fixture/research effort, not a billing system.
- **Reliability fixture series:** [P10 memory portability](https://github.com/HuffmanRepositories/Agent-Memory-Portability-Tests), [P11 evaluation-oracle integrity](https://github.com/HuffmanRepositories/Agent-Evaluation-Oracle-Integrity-Fixtures), [P12 retry/idempotency](https://github.com/HuffmanRepositories/Agent-Tool-Retry-Idempotency-Fixtures), [P13 delegation-scope boundaries](https://github.com/HuffmanRepositories/Agent-Delegation-Scope-Boundary-Fixtures), and [P14 delegated-budget enforcement](https://github.com/HuffmanRepositories/Agent-Delegated-Budget-Enforcement-Fixtures).
- **P15 user-controlled stop:** an in-memory reference model and synthetic tests housed inside Huffman-Ecosystem-Root. It is not a separate repository or deployed kill switch.

The public catalog consistently labels fixtures as synthetic/offline and warns that structural validation is not security conformance, runtime integration, or production authorization.

## 3. midnightlolz31337: ELITE and ecosystem atlas

Four original project repositories plus the account profile:

- [ELITE Protocol](https://github.com/midnightlolz31337/ELITE-Protocol): draft evidence/claim/review envelopes and trust boundaries. It distinguishes source observations, analyst claims, and reviewer conclusions. It explicitly does not claim certified standard status or production security.
- [ELITE Ingestion Core](https://github.com/midnightlolz31337/ELITE-Ingestion-Core): local JSONL/CSV ingestion prototype with bounded input handling, record digests, source references, and quarantine. An operator-supplied authorization flag is not proof of authority or policy enforcement.
- [ELITE Agent Commons](https://github.com/midnightlolz31337/ELITE-Agent-Commons): curated machine-readable discovery and coordination catalogue. It does not execute agents, install tools, or establish trust from self-declared capabilities.
- [Huffman Network Atlas](https://github.com/midnightlolz31337/Huffman-Network-Atlas): federated ecosystem index with evidence levels, provenance, and account/repository records. Its own README says the earlier account audit was incomplete and required refresh; this six-account topology now supplies the expanded public roster.

ELITE Protocol describes intended interoperability with Huffman Protocol and OIX, but states that adapters are future work. The relationship is therefore an intended compatibility path, not verified conformance.

## 4. Ryzean84: profile and OSINT fork

The account currently has two public repositories:

- [Ryzean84](https://github.com/Ryzean84/Ryzean84), the research-workspace profile.
- [Curated-Modern-OSINT-Tools-ForkBy_Ryzean84](https://github.com/Ryzean84/Curated-Modern-OSINT-Tools-ForkBy_Ryzean84), a GitHub-confirmed fork of [HuffmanMainNode/Curated-Modern-OSINT-Tools](https://github.com/HuffmanMainNode/Curated-Modern-OSINT-Tools).

The profile README also links to OIF and Project AVI repositories under the Ryzean84 namespace. Those named links currently return 404 and are not present in the account's live public repository search. They are treated as stale or moved references, not additional owned repositories. The linked OIF projects exist under other public portfolio namespaces and are counted under their actual owners only.

## 5. roberthuffman: controlled test copies

The account currently has four public repositories:

- [roberthuffman](https://github.com/roberthuffman/roberthuffman), the profile repository.
- [Protocol-Helios-ControlledTestFork](https://github.com/roberthuffman/Protocol-Helios-ControlledTestFork), a GitHub-confirmed fork of HuffmanMainNode/Protocol-Helios.
- [Cui-Bono-Audit-Tool-TestFork](https://github.com/roberthuffman/Cui-Bono-Audit-Tool-TestFork), a GitHub-confirmed fork of HuffmanMainNode/Cui-Bono-Audit-Tool.
- [uss-sdk-wrapper-TESTFORK](https://github.com/roberthuffman/uss-sdk-wrapper-TESTFORK), whose GitHub metadata says `fork=false`, but whose description explicitly calls it a controlled test fork. It is therefore classified separately as a controlled test copy and not counted as an original project.

The USS SDK README contains claims about local data molecularization, memory scrubbing, and a simulated post-quantum wrapper. Those are repository claims, not independently validated cryptographic assurances. The README itself labels the post-quantum wrapper as simulated. Do not treat this repository as a verified security product.

## Cross-account relationships and integration spine

### Verified fork lineage

Seven direct cross-account fork edges were confirmed by GitHub metadata:

- Ryzean84's curated OSINT tools fork points to the HuffmanMainNode original.
- roberthuffman's two controlled test forks point to Protocol-Helios and Cui-Bono-Audit-Tool on HuffmanMainNode.
- HuffmanMainNode's Huffman Network Atlas and three ELITE forks point to the four originals under midnightlolz31337.

These are repository lineage edges, not evidence that fork changes have been synchronized or merged upstream.

### Documented interoperability references

- OAC in HuffmanRepositories explicitly references OIX in HuffmanMainNode, Agent Ecosystem Integration in PCakes303, and Agent Foundation Spec in PCakes303 as neighboring projects for compatibility mapping.
- ELITE Protocol in midnightlolz31337 describes intended interoperability with Huffman Protocol and OIX; adapters are future work.
- PCakes303's dependency registry supplies its own directed component graph and dependency semantics.

### Primary-account integration spine

The previously documented HuffmanMainNode integration spine remains separate: OIX, Open-Swarm, Halloween OSINT, HCO, and HDI have staged integration documentation. The cross-account portfolio adds protocols, test fixtures, evidence ingestion, discovery, policy, and governance projects around that spine. Do not flatten all of these into a single runtime.

## Evidence and limitations

- Repository counts are a dated snapshot, not timeless facts.
- Repository metadata establishes existence, visibility, fork status, and declared metadata; it does not establish authorship of every file or quality.
- README and registry inspection establishes documented scope and self-described maturity, not independent implementation correctness.
- Declared dependencies, portfolio links, and intended interoperability are distinct relationship types.
- This public map includes only public repositories. Private repositories, private branches, private dependency details, and internal operational material are excluded.
- This is not a full source-code, security, licensing, or runtime audit of all 107 repositories.

## Machine-readable companion files

- [data/accounts.json](data/accounts.json): six account records and reconciled counts.
- [data/federated-repositories.json](data/federated-repositories.json): unified public repository roster.
- [data/cross-account-relationships.json](data/cross-account-relationships.json): verified fork lineage and documented interoperability edges.
- [data/repositories.json](data/repositories.json): original HuffmanMainNode inventory.
- [data/external-forks.json](data/external-forks.json): HuffmanMainNode upstream fork register.
