# The Infrastructure Supply Chain Behind Over-the-Air AI Services

**ORI contribution to the FCC TAC AI/ML and Computing Working Group: kickoff draft**

*Status: internal ORI working draft, started October 3, 2026. These are not positions of the TAC or any of its working groups. All claims are connected to `references.md`. Label estimates and inferences clearly.*

---

## 1. Why

AI services on phones (assistants, translation, camera understanding, agents) are delivered over the air. Whether they work depends on a chain that runs from the handset through the radio access network (RAN), backhaul, any core network, edge compute, and cloud inference sites. All of that runs on the power grid.

The FCC sees part of that chain. Its outage reporting rules (47 CFR Part 4, which covers the NORS and DIRS systems) apply to wireless, wireline, cable, satellite, and interconnected VoIP providers. As written, those rules don't cover cloud, data center, or AI inference providers. [R1.1] 

The working group's charter slides talk about "cloud computing infrastructure" only in a privacy context. They never mention data centers. Even so, the group's own tasks (network resiliency, security and reliability, emergency preparedness) all depend on that part of the chain.

**Working thesis:** an AI service delivered over the air is only as available as the weakest link in its supply chain. To understand the resiliency of these services, the Commission needs to look at the whole chain, not just the parts it already regulates. There are two potential outage sensitivities. First, an outage that causes **content** delivery to fail because the content itself cannot be generated. Second, an outage that is due to the network itself failing because a network **control** pane that requires AI to work correctly has failed.

## 2. Goals

1. **Model the chain.** Define the entities, the interfaces between them, and their dependencies, from the handset to the inference cluster to the grid. This domain model comes first, and everything else hangs on it. The AI Traffic Taxonomy document is intended to be a component of achieving this goal.
2. **Document how it fails,** using real, sourced incidents rather than hypotheticals. 
3. **Quantify the traffic shift.** Collect the published forecasts on AI-driven uplink growth and what they imply for capacity and spectrum demand. The AI Traffic Taxonomy document is intended to be a component of achieving this goal.
4. **Map the visibility gaps.** Which failures in the chain would show up in the FCC's reporting systems, and which wouldn't?
5. **Frame questions and candidate recommendations for the working group.** The full committee decides what goes to the FCC.

**Non-goals:** energy policy, data-center siting, permitting, and arguing for or against data centers. The grid appears only as a dependency in the chain.

## 3. How the paper maps to the charter

| Paper section | WG charter task (Oct 1 deck) | FCC Strategic Plan |
|---|---|---|
| Chain model and failure modes | AIC-a, AI/ML and Networks: network resiliency | Obj. 2.2: resiliency and rapid restoration |
| Visibility and reporting gaps | AIC-b, AI/ML and Security/Reliability | Obj. 2.2 |
| Outages and emergency use | AIC-c, Broadband analytics: emergency preparedness and network resiliency | Obj. 2.2 |
| Uplink and traffic shift | AIC-g, Convergence of AI and IoT: data velocity, real-time network demand | Obj. 1.2: broadband deployment |
| Cloud dependency and privacy | AIC-d, AI/ML and Consumer Protection: "cloud computing infrastructure" | — |
| Edge and AI-RAN | EWB-d (Open RAN, AI-RAN) and the common-themes slide | — |

## 4. Draft outline (skeleton)

1. **Executive summary**
2. **The service chain as a domain model**
   - Entities: device, RAN, transport and backhaul, core network, edge compute (MEC and AI-RAN), cloud inference region, power.
   - Where the inference runs: on the device, at the edge, or in the cloud. Real products use a hybrid. For example, Apple runs models on the device first and falls back to "Private Cloud Compute." [R6.3] This section should be relatively easy to write. 
   - Diagram: a dependency graph, with the portion the FCC currently sees shaded. 
3. **Failure modes and case studies**
   - AWS us-east-1, October 19–20, 2025: a DNS race condition that cascaded across services. [R3.1]
   - OpenAI, December 11, 2024: a telemetry deployment overloaded the control plane, and "DNS relies on the control plane." [R3.4]
   - OpenAI, February 19, 2025: a misconfiguration overwhelmed the inference infrastructure. [R3.6]
   - CrowdStrike, July 2024: a bad software update spread across 8.5 million hosts. [R3.2, R3.3]
   - Pattern to test: control-plane and configuration failures, concentrated regions, and correlated dependencies.
   - Counterpoint: CSRIC VIII said "cloud platforms at scale are intrinsically highly resilient to failures." [R5.2] Does the incident record support that claim? Anecdotally it seems like reliability has been eroded. 
4. **Traffic: defining AI traffic, then the uplink shift**
   - **Define the traffic classes first.** Published figures count very different things. Draft classes:
     - (a) Interactive text chat
     - (b) Interactive multi-modal
     - (c) AI features embedded in general apps and operating systems (search answers, photo tools, assistant offload)
     - (d) Programmatic API calls from user devices (developer tools, coding agents, apps calling model APIs directly)
     - (e) Device-hosted agent actions (an agent on the device browsing or acting on the user's behalf)
     - (f) Cloud-hosted agent actions (an agent in a data center acting for a user. Only results reach the device)
     - (g) Cloud-to-cloud AI traffic (inference between services, training data, crawlers)
     - (h) Model distribution (downloading and updating models stored on the device)
     - (i) Continuous sensing streams (smart glasses, wearables, always-listening assistants)
     - (j) Network-internal AI (RAN intelligent controller data, AI-RAN, network telemetry)
     
     Each source must be mapped to the classes it actually measures.
   - **Measure more than byte share.** Also report peak uplink rate per user, burstiness, and latency sensitivity. Explain that a service can be a tiny share of bytes and still drive uplink capacity planning.
   - Example: Ericsson's 0.06% covers only class (a). It counts 21 named apps on **one operator's network during one week in April 2025**, extrapolated to a month. It **excludes** AI features embedded in regular apps and covers "only traffic that can be clearly identified." The figure is a share of **total traffic in both directions**. Its split is 74% downlink and 26% uplink, compared with a typical 90/10. [R2.1]
   - GSMA Intelligence projects that the uplink-to-downlink ratio narrows from today's 1:9 to 1:15 to between 1:3 and 1:6 by 2030. [R2.6]
   - Ericsson: uplink could be 3 to 5 times higher by 2031. [R2.2]
   - Nokia's counterweight: the overall network impact stays "modest." [R2.4]
   - 3GPP 6G requirements work on AI traffic characteristics. [R2.8]
   - Implication for spectrum planning (to hand off to the SMR group): uplink-heavy demand changes which bands and duplex arrangements are valuable.
5. **The visibility and reporting gap**
   - Part 4: who must report, the outage definition, and the reporting thresholds. [R1.1]
   - DIRS and the 2026 Resilient Networks order (FCC 26-34). [R1.2, R1.3]
   - Question: when a cloud failure degrades a carrier's AI service, but not the carrier's own network, does any reporting obligation apply?
6. **Edge compute and AI-RAN: moving the dependency, not removing it**
   - SoftBank/NVIDIA AITRAS. [R4.4, R4.5]
   - The AI-RAN Alliance. [R4.1]
   - NTIA's AI-native wireless funding opportunity, July 2026. [R4.6]
   - Trade-offs: power and backup at cell sites, and whether failures become more or less correlated.
7. **Transparency: open source and provenance for AI in the network**
   - CSRIC VIII WG2 recommended SBOMs and code signing for xApps and rApps. [R7.3]
   - NTIA's SBOM minimum elements. [R7.1]
   - Question: should the same provenance expectations apply to AI models and inference services that network functions depend on?
8. **Questions and candidate recommendations for the working group**

## 5. Discussion points for ORI

Please weigh in on any of these, briefly or at length.

1. **Scope.** Should satellite direct-to-device AI delivery be included? Should it cover only consumer AI, or also AI used inside the network to run it (RAN optimization, the RAN Intelligent Controller (RIC))?
2. **The domain model.** Is this entity list right? What's missing? Candidates: DNS, identity and authentication services, content delivery networks (CDNs), model-weight distribution, GPU supply.
3. **Reporting.** Should outage visibility be extended, and how would that work? Or is this better handled through voluntary information sharing? Where does the FCC's authority actually reach? *(Needs legal grounding. We are not lawyers.)*
4. **Measurement (ORI and DEFCON folks).** Can we measure uplink and downlink behavior of AI apps on our own test networks, along the lines of the Napoli study [R2.7]? What would an ethical, reproducible method look like?
5. **Security (DEFCON folks).** Which attacks on the cloud or inference layer turn into denial of service for an over-the-air service? Is there a published red-team or incident literature we should cite?
6. **Edge versus cloud.** Does AI-RAN reduce correlated failure, or does it just spread the dependency on power and GPUs across thousands of sites? 
7. **Uplink and spectrum.** What evidence would convince a spectrum planner that uplink demand is real and not just forecast hype? The current number, 0.06% of traffic, is small. It feels like it's undercounted. 
8. **Open-source angle.** Is there a credible argument that open models, open inference stacks, or SBOMs for AI components improve resiliency and accountability? We need to make that argument. 
9. **Counterarguments.** What is the strongest case that this is not the FCC's concern? We should address it directly.
10. **Data-center framing.** How do we keep the paper on communications reliability so it doesn't read as taking a side in any political or cultural fight over data centers? 

## 6. Research to-do

| # | Task | Owner | Status |
|---|---|---|---|
| 1 | Get the full NSA/CISA Open RAN security PDF and check whether it covers AI/ML apps | | open |
| 2 | Check 3GPP Rel-18/19/20 AI/ML-for-NR items against primary 3GPP pages | | open |
| 3 | Find any ATIS or NG Alliance work on AI traffic characteristics | | open |
| 4 | Find FCC TAC AI working group reports for 2022–2024 (the minutes returned an error) | | open |
| 5 | Qualcomm hybrid-AI white papers: they wouldn't render, so retrieve and verify them | | open |
| 6 | Legal question: where the FCC's authority over cloud and AI providers begins and ends | | open |
| 7 | Find a primary source for the CrowdStrike 8.5 million figure (Microsoft blog) | | open |
| 8 | Look for academic work on correlated failure in cloud-dependent mobile services | | open |
