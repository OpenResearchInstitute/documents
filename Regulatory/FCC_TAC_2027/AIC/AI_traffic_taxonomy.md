# A Taxonomy of AI Traffic for Communications Networks

**ORI contribution to the FCC TAC AI/ML and Computing Working Group: draft for discussion**

*ORI working draft, started October 14, 2026. These are not positions of the TAC or any working group. Sources are numbered as in `references.md`. Anything labeled "ORI's reading" is our interpretation, not a sourced fact.*

**Relevant to which mandates?**
- AIC-a: "traffic pattern prediction and network resiliency"
- AIC-g: "data velocity, volume, and veracity... real time network demand"
- AIC-d: "networks increasingly dependent on cloud computing infrastructure"

---

## 1. Why?

"AI traffic" is used as if it means one particular thing. It doesn't. At least two credible studies presented to or cited by this working group show the problem.

- **Ericsson** measured traffic from 21 named consumer AI apps, such as chatbots and image generators. The data came from one mobile operator's network over one week in April 2025. Ericsson explicitly excluded AI features built into other apps. Result: 0.06% of total traffic, split 74% downlink and 26% uplink. [R2.1]
- **Cisco** measured inference calls to programming interfaces (APIs) for large language models (LLMs), such as api.openai.com and api.anthropic.com, at a service provider's access edge from 2025 into early 2026. It explicitly excluded consumer chat websites as traffic that appears like any other websites. The goal was to capture API calls. Mobile, fixed wireless, and fixed users were combined. A notable result was that AI flows are longer and have a lower average rate than other flows. [R10.1]

The two studies count different things. Both are reasonable and illuminating. Neither can be directly compared against the other, and neither can be quoted simply as "AI traffic" without causing an "apples to oranges" comparison.

Unqualified figures cause two kinds of error. 
1. **Traffic disappears.** A narrow definition, or one that only counts identifiable traffic, makes AI demand look negligible.
2. **Traffic inflates.** A broad definition, such as counting AI-generated video as AI traffic, makes AI demand look enormous.

We want neither of these figures. Policy built on either error will be wrong. Spectrum planning, outage reporting, and network resiliency analysis each need to know *which* AI traffic is under discussion.

**Prior work (ORI's search, October 14, 2026):**
- Web-security vendors classify automated AI traffic by its effect on websites: crawlers, agents, and named bots. [R11.1] 
- IETF and 3GPP drafts organize AI work by use case and by requirement. [R11.2, R2.8]
- We found no published taxonomy that classifies AI traffic **as a communications network sees it**: by who starts it, what path it takes, how it behaves on the link, and whether it can be identified. This draft tries to fill that gap. *This is a limited search, so please tell us if you know of prior work!*

## 2. Approach

A simple flat list of categories invites argument over edge cases. It's difficult to validate or verify a list of brain-stormed categories, even if they come from an experienced individual or group. It's difficult to avoid listing nested or dependent categories as independent categories. It's easy to have inadvertent gaps in a list of categories. In order to produce as high quality a taxonomy as possible, we describe each kind of traffic by using five independent qualities, or **facets**, and then we name the **classes** that emerge from these qualities. A new kind of traffic gets placed by its facets. Its name can come later. This allows the taxonomy to adjust and adapt to observed reality as types of traffic continue to develop over time. The term facets is borrowed from gaming (e.g Dragon) dice and game theory. Choosing the die with the right number of sides makes the game work well. 

| Facet | Question it answers | Possible Values |
|---|---|---|
| **F1. Initiator** | Who or what started this traffic, and is someone waiting on it? (Age of Information relevance) | Human, interactive (someone is waiting). Agent, autonomous (acting for a person, nobody waiting on each step). Background system (updates, sync). Network-internal (the network managing itself) |
| **F2. Inference location** | Where does the model run? | On the device. At the network edge (multi-access edge computing, AI-RAN). In the cloud or a data center |
| **F3. Path** | Which links does the traffic cross? | Device to/from service (crosses the access network: radio, fixed wireless, or wired). Cloud to cloud (never touches the access network). Cloud to open web (agents and crawlers reaching websites) |
| **F4. Payload role** | What is being carried? | Prompt or context (usually uplink). Streamed response (usually downlink). Media upload: image, audio, video, screen (uplink). Generated media (downlink). Model weights (downlink, large, occasional). Continuous sensor stream (uplink). Management and telemetry data |
| **F5. Identifiability** | Can an operator tell this is AI traffic? | Dedicated AI endpoint (identifiable by host name). Shared first-party domain (AI mixed with other services, usually not separable). Embedded or proxied (hidden inside another app's traffic) |

**Why these facets matter for the FCC (ORI's reading):**
- **F3** decides whether the traffic loads the radio access network at all. Cloud-to-cloud AI traffic matters for supply-chain resiliency, not necessarily or directly for spectrum. There may be indirect spectrum effects. 
- **F1** decides how sensitive the traffic is to delay and outages. A waiting human notices a two-second stall. A background update doesn't.
- **F5** decides whether a measurement can see the traffic in the first place. Most of the measurement disagreements trace back to this facet.

## 3. Classes

| Class | Name | F1 Initiator | F2 Inference | F3 Path | F4 Main payload | F5 Identifiable? |
|---|---|---|---|---|---|---|
| **T1** | Interactive text chat (app or web) | Human | Cloud | Device to/from service | Short prompt up, streamed text down | Often, through a dedicated app or site |
| **T2** | Interactive multimodal (voice, camera, screen sharing with an AI) | Human | Cloud or edge | Device to/from service | **Media upload**, short response down | Sometimes |
| **T3** | AI features embedded in general apps and operating systems (search answers, photo tools, assistant offload) | Human | Device first, cloud fallback | Device to/from service | Mixed | **Rarely** (shared domains!) |
| **T4** | Programmatic API calls from user devices (developer tools, coding agents, apps calling model APIs directly) | Agent or human | Cloud | Device to/from service | Large context up, streamed response down | Yes, through API host names |
| **T5a** | Device-hosted agent actions (an agent on the device browsing or acting on the user's behalf) | Agent | Device or cloud | Device to/from web and services | Ordinary web traffic, generated by an agent | **Rarely** (looks like normal browsing!) |
| **T5b** | Cloud-hosted agent actions (an agent in a data center acting for a user. Only results reach the device) | Agent | Cloud | Cloud to/from open web, then a small result sent to the device | Web fetches in the cloud | At websites, by agent identity. Not on the access network |
| **T6** | Cloud-to-cloud AI traffic (inference between services, training data, crawlers) | System | Cloud | Cloud to/from cloud, cloud to/from web | Bulk data | At data centers and websites only |
| **T7** | Model distribution (downloading and updating models stored on the device) | Background system | Device | Device to/from service | **Model weights down** (large, occasional) | Sometimes |
| **T8** | Continuous sensing streams (smart glasses, wearables, always-listening assistants) | Human or system | Edge or cloud | Device to/from service | **Sustained uplink** | Sometimes |
| **T9** | Network-internal AI (RAN intelligent controller data, AI-RAN, network telemetry) | Network-internal | Edge or network | Inside the operator's network | Telemetry and control | Operator only |

### Explicitly not AI traffic

**X1. AI-generated content consumed as ordinary media.** An AI-generated video watched on a streaming platform behaves on the network exactly like any other video. It is an **AI content** question, about provenance and labeling. It is not an **AI traffic** question. Counting it as AI traffic inflates the figures and tells a network planner nothing new. 

## 4. What to measure for each class

A share of bytes alone is not enough. Each measurement should report:

1. **Vantage point:** where the measurement was taken (radio access network, access edge, core, data center, or website), and over what dates.
2. **Access type:** mobile, fixed wireless access, or fixed broadband, **reported separately**.
3. **Identification method:** host-name lists, app signatures, operator labels, or inference. Also, **what the method cannot see**.
4. **Volume in each direction:** downlink and uplink, and the ratio between them.
5. **Rates:** average, **peak, and 95th-percentile per-user rates**. An average over a long flow hides bursts, which are something network planners really need to know. 
6. **Flow duration and connection hold time:** long-lived flows keep phones' radios in their connected state and occupy network state tables, even at low data rates. *ORI's reading: could this cost the network more than the bytes do?*
7. **Latency sensitivity:** whether a human is waiting (F1). This is an Age of Information question.

**Classes where the byte share is likely misleading (ORI's reading):**
- T2 and T8: uplink bursts and sustained uplink streams.
- T4: long flows at low average rates.
- T7: rare but very large downloads. 

## 5. Mapping existing studies to the classes

| Study | Classes measured | Vantage point and access type | What it cannot see |
|---|---|---|---|
| Ericsson, June 2025 [R2.1] | **T1**, plus parts of T2 inside the same 21 apps | One mobile operator, one week in April 2025 | T3 by design (embedded features excluded); T4; anything unidentifiable |
| Cisco, October 14, 2026 presentation [R10.1] | **T4** | Service provider's access "edge". Mobile, fixed wireless, and fixed **combined** | T1 by design (consumer sites excluded); T3; T5a |
| HUMAN Security, March 2026 [R11.1] | **T5b and T6**, plus T5a where it reaches websites | Website side ("Human Defense Platform"), not the access network | Anything that doesn't hit a protected website, access-network load |
| Nokia Global Network Traffic Report, 2025 [R2.4] | Forecast of "AI traffic" and "agentic AI" machine-to-machine traffic | Forecast model | **To check:** Nokia's definitions, and how they map to these classes |
| GSMA Intelligence, July 2026 [R2.6] | Forecasts of uplink-to-downlink ratios | Forecast | **To check:** the definition used |
| Montieri, Nascita, Pescapè, October 2025 [R2.7] | ChatGPT, Copilot, Gemini: T1, and possibly T3 for Gemini and Copilot | Measurement study | **To check:** app or web, and the capture point |
| 3GPP SA1 draft, 6G [R2.8] | Requirements for "AI traffic characteristics" | Standards requirements | Has no class definitions, but could adopt one |

## 6. Rules of The Road (proposed for the working group)

1. **Never say "AI traffic" without saying which classes.** Write "T1 and T4 traffic," or define the term inline.
2. **Always state the vantage point and access type.** A combined mobile-plus-fixed figure cannot really answer a wireless spectrum question.
3. **Always state what the identification method cannot see.** Most of the "disappearing" traffic lives in T3 and T5a.
4. **Report peaks and flow duration alongside byte share.**
5. **Don't count X1 (AI-generated content) as AI traffic.**

## 7. Open questions for ORI and the working group

1. **Is five facets the right number?** Candidates for a sixth: **energy per request** (which ties to data-center supply chains), and **security posture** (whether the traffic is authenticated and attributable, which ties to EWB-d "non-repudiation").
2. **T4 versus T5a:** a coding agent on a laptop calls a model API (T4) *and* fetches web pages (T5a). Should a single agent session be counted as one unit across both classes?
3. **T3 is the largest unknown.** Can it ever be measured from the network, or only through operating system and app vendors? Would vendor-reported data be acceptable to the FCC? Is there a way to build some telemetry stations or use an existing Internet observatory? 
4. **Satellite direct-to-device links:** do any classes behave differently over them? Does a satellite link fundamentally change anything?
5. **DEF CON RF Village:** can traffic in each class be fingerprinted from encrypted flows (packet timing and size patterns), without decrypting? There are privacy and ethics questions here as well as technical ones. We know that side channel information and metadata are widely used to extract information from encrypted data. Information can lead to knowledge about the message. Are there any repercussions for spectrum management? 
6. **Measurement:** could ORI run a small open, reproducible test-network study that reports T1, T2, and T4 on a mobile link, using the metrics in Section 4? 

## 8. Requests to presenters (proposed)

When future speakers present AI traffic data to the working group, we could ask them to state:
- the classes measured;
- the vantage point;
- the access-type breakdown;
- the identification method and its blind spots;
- peak and 95th-percentile rates.

A one-slide template could make this very easy. We'd be able to disambiguate "AI Traffic" and by the end of the term be able to compare and contrast claims, results, and studies in a way that improves the advice we will bring to TAC. 
