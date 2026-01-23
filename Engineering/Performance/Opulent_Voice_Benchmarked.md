# Digital Voice Protocol Benchmark Comparison

**Open Research Institute**  
*Draft for FOSDEM 2026*

---

## 1. Introduction

This document provides a technical comparison of digital voice protocols used in amateur radio and public safety communications. The comparison includes the Opulent Voice Protocol (OVP) developed by Open Research Institute alongside established protocols: P-25, D-STAR, DMR, NXDN, Yaesu System Fusion (YSF), and M17.

The benchmark focuses on objective, measurable parameters rather than subjective audio quality assessments. For audio quality comparisons, standardized testing using PESQ/POLQA metrics on controlled datasets are the standard approach.

---

## 2. Benchmark Metrics Defined

**Quantitative Metrics:** Data rate (bps), spectral efficiency (bits/Hz), BER performance curves, latency, and robustness to fading.

**Architectural Metrics:** Vocoder type and bitrate, FEC scheme, modulation type, channel bandwidth, and access method (FDMA/TDMA).

**Openness Metrics:** License status, patent encumbrance, and availability of open-source implementations.

---

## 3. Technical Comparison

| Parameter | OVP | M17 | P-25 Phase I | P-25 Phase II | D-STAR | DMR | NXDN | YSF |
|-----------|-----|-----|--------------|---------------|--------|-----|------|-----|
| **Modulation** | MSK | 4FSK | C4FM/CQPSK | H-DQPSK/H-CPM | GMSK | 4FSK | 4FSK | C4FM |
| **Symbol Rate** | 27.1 ksym/s | 4.8 ksym/s | 4.8 ksym/s | 6.0 ksym/s | 4.8 ksym/s | 4.8 ksym/s | 2.4 ksym/s | 4.8 ksym/s |
| **Data Rate** | 54.2 kbps | 9.6 kbps | 9.6 kbps | 12 kbps | 4.8 kbps | 9.6 kbps | 4.8 kbps | 9.6 kbps |
| **Channel BW** | ~80 kHz | 9 kHz | 12.5 kHz | 12.5 kHz | 6.25 kHz | 12.5 kHz | 6.25 kHz | 12.5 kHz |
| **Access Method** | FDMA | FDMA | FDMA | TDMA (2-slot) | FDMA | TDMA (2-slot) | FDMA | FDMA |
| **Vocoder** | Opus | Codec2 | IMBE | AMBE+2 | AMBE+ | AMBE+2 | AMBE+2 | AMBE+2 |
| **Voice Bitrate** | 16+ kbps | 3.2 kbps | 4.4 kbps | 2.45 kbps | 2.4 kbps | 2.45 kbps | 2.45 kbps | 2.45–4.4 kbps |
| **FEC Scheme** | K=7 Conv. r=1/2 | Golay + Conv. | Golay + Conv. | Golay + Conv. | Conv. | BPTC/Trellis | See §7.1 | Conv. |
| **FEC Gain** | ~7 dB (soft) | ~5 dB | ~5 dB | ~5 dB | ~3 dB | ~3 dB | See §7.1 | ~3 dB |
| **Sync Word** | 24 bits | 16 bits | 48 bits | 48 bits | 24 bits | 48 bits | 20 bits | 40 bits |
| **Sync PSLR** | 8:1 | 2.67:1 | 3:1 | 3:1 | 2.4:1 | ~3:1 | ~2.5–3:1 | ~3:1 |
| **Frame Duration** | 40 ms | 40 ms | 180 ms | 30 ms | N/A (stream) | 60 ms | 20 ms | 100 ms |
| **Spectral Eff.** | 0.68 b/Hz | 1.07 b/Hz | 0.77 b/Hz | 0.96 b/Hz | 0.77 b/Hz | 0.77 b/Hz | 0.77 b/Hz | 0.77 b/Hz |

---

## 4. Licensing and Openness

| Aspect | OVP | M17 | P-25 Phase I | P-25 Phase II | D-STAR | DMR | NXDN | YSF |
|--------|-----|-----|--------------|---------------|--------|-----|------|-----|
| **Protocol Spec** | Open (GPL) | Open (GPL) | Open (TIA) | Open (TIA) | Open (JARL) | Open (ETSI) | Open (NXDN Forum) | Proprietary |
| **Vocoder License** | BSD (Opus) | LGPL (Codec2) | DVSI License | DVSI License | DVSI License | DVSI License | DVSI License | DVSI License |
| **Patent Status** | Royalty-free | Royalty-free | Encumbered | Encumbered | Encumbered | Encumbered | Encumbered | Encumbered |
| **Open Source Impl.** | Yes | Yes | Partial (OP25) | Partial (OP25) | Partial | Partial (MMDVM) | Partial (MMDVM) | Partial (MMDVM) |
| **Homebrew HW** | Yes (e.g. LibreSDR) | Yes | Difficult | Difficult | Yes | Yes | Limited | Limited |

---

## 5. Design Philosophy Comparison

**Opulent Voice Protocol (OVP):** Designed for wideband, high-quality voice with full IP stack integration (RTP/UDP/IP). Uses Opus codec for superior audio quality at the cost of higher bandwidth. Optimized for UHF and above. Target applications include amateur radio space and terrestrial deployments.

**M17:** Community-developed protocol prioritizing openness and spectral efficiency. Uses Codec2 for royalty-free voice encoding. Designed for VHF/UHF amateur radio within existing 12.5 kHz channel allocations. Emphasis on minimal overhead and compatibility with existing narrowband infrastructure.

**P-25:** Public safety standard with emphasis on interoperability, reliability, and encryption support. Phase I provides straightforward migration from analog FM. Phase II doubles spectral efficiency via TDMA. Proprietary IMBE/AMBE vocoders add licensing costs but ensure vendor interoperability.

**D-STAR:** First amateur digital voice standard with native IP networking and callsign routing. GMSK modulation provides narrowest bandwidth (6.25 kHz). Internet gateway linking built into protocol design. Single vendor (Icom) limits hardware options.

**DMR:** Commercial standard adapted for amateur use. TDMA provides two voice channels per 12.5 kHz allocation. Wide vendor support drives competitive pricing. Tier II/III trunking capabilities for larger systems.

**NXDN:** Joint Icom/Kenwood protocol targeting 6.25 kHz narrowband operation. Uses integrated vocoder-FEC architecture where AMBE+2 chip handles both voice coding and error correction internally. Achieves true 6.25 kHz operation for maximum spectral efficiency. FDMA access method with optional 12.5 kHz dual-channel mode.

**Yaesu System Fusion:** Amateur-focused protocol with automatic mode selection between digital and analog. Supports multiple data rates for voice quality vs. robustness tradeoffs. WIRES-X provides Internet linking. Single vendor ecosystem.

---

## 6. Synchronization Word Analysis

Sync word quality is characterized by Peak Sidelobe-to-Mainlobe Ratio (PSLR). Higher PSLR means better discrimination between true sync detection and false alarms, particularly important in multipath environments.

### PSLR Comparison

| Protocol | Sync Length | PSLR | Peak Sidelobe | Analysis Level | Method |
|----------|-------------|------|---------------|----------------|--------|
| **OVP** | 24 bits | 8:1 (18.1 dB) | 3 | Bit | Exhaustive search |
| **M17** | 16 bits | 2.67:1 (8.5 dB) | 6 | Bit | Digits of π |
| **P-25** | 48 bits (24 symbols) | 3:1 (9.5 dB) | 8 | Dibit | Manual design |
| **D-STAR** | 24 bits | 2.4:1 (7.6 dB) | 10 | Bit | Preamble + sync |
| **DMR** | 48 bits (24 symbols) | ~3:1 | — | Dibit | Manual design |
| **NXDN** | 20 bits (10 symbols) | ~2.5–3:1 | — | Dibit | Manual design |
| **YSF** | 40 bits (20 symbols) | ~3:1 | — | Dibit | Manual design |

### Key Findings

**OVP Sync Word (0x02b8db):** Found via exhaustive search of all 2²⁴ = 16,777,216 possible sequences. The search identified 6,864 sequences achieving the optimal 8:1 PSLR. Selection criteria included DC balance (11 ones, 13 zeros) and maximum run length (6 zeros). Mnemonic: "oh to be eight dB."

**M17:** M17's 16-bit sync words were selected from digits of pi without optimization.

**P-25 Symbol-Level Analysis:** P-25 uses 4-level modulation (dibits), so sync analysis must be performed at the symbol level (24 symbols), not bit level (48 bits). The 3:1 PSLR represents reasonable 1990s-era manual design.

**D-STAR Preamble Trade-off:** D-STAR's 24-bit sync includes a 10-bit alternating preamble (1010101010) optimized for clock recovery rather than PSLR. This was a conscious design choice given receiver technology of the early 2000s.

### Multipath Performance

Higher PSLR provides substantial improvement in multipath conditions common on VHF/UHF terrestrial paths. Testing shows OVP's 8:1 PSLR sync word significantly outperforms 3:1 PSLR sequences when delayed signal copies arrive at the receiver. 

The improvement is most pronounced when using correlation-based detection rather than Hamming distance thresholding. OVP's optimized sync word is "future-proof". Implementations can upgrade from hard to soft detection methods without protocol changes.

### Why Not Classical Sequences?

**Barker Codes:** Optimal only at specific lengths (max 13 bits). Concatenating Barker-11 + Barker-13 yields only 3:1 PSLR for 24 bits.

**M-Sequences:** Perfect *periodic* autocorrelation, but sync detection requires *aperiodic* correlation. A truncated 31-bit m-sequence achieves only 1.14:1 PSLR.

**Zadoff-Chu:** Complex-valued sequences with perfect periodic properties. Quantizing to binary destroys the "perfect" autocorrelation; 24-bit quantized ZC yields only 2.18:1 PSLR.

**Lesson:** For arbitrary-length binary sync words, exhaustive search is computationally feasible and guarantees the global optimum.

---

## 7. Forward Error Correction Analysis

### 7.1 FEC Architecture Approaches

Digital voice protocols use two fundamentally different approaches to forward error correction:

**Protocol-Layer FEC:** The protocol specification defines FEC separately from the vocoder. The vocoder outputs compressed voice bits, and a distinct FEC encoder adds redundancy before transmission. This approach allows independent optimization of codec and FEC, and permits open-source FEC implementations.

*Protocols using this approach:* OVP, M17, P-25 Phase I, D-STAR

**Integrated Vocoder-FEC:** The vocoder chip (typically DVSI AMBE+2) handles both voice compression and forward error correction internally. The protocol simply receives "channel bits" from the chip. The FEC parameters are configured via chip registers but are not visible in the air interface specification.

*Protocols using this approach:* NXDN, DMR, P-25 Phase II, YSF

**Implications:**

| Aspect | Protocol-Layer FEC | Integrated Vocoder-FEC |
|--------|-------------------|------------------------|
| **FEC parameters** | Publicly specified | Proprietary to DVSI chip |
| **Interleaver details** | Documented | Internal to chip |
| **Open-source FEC** | Possible | Requires DVSI chip |
| **Soft decision** | Implementation choice | Chip-dependent (can be up to 4-bit) |
| **Flexibility** | High | Limited to chip modes |

NXDN specifically uses the AMBE+2 chip's integrated FEC with configurable voice and FEC rate allocation. The chip supports rates from 2.0 to 9.6 kbps total, split between voice coding (as low as 2.0 kbps) and FEC (up to 7.2 kbps). The NXDN 6.25 kHz mode uses approximately 2.45 kbps voice plus 1.15 kbps for an FEC of 3.6 kbps total. The specific FEC codes (block and convolutional) and interleaver are proprietary to DVSI.

### 7.2 OVP FEC Architecture

The Opulent Voice Protocol uses a K=7, rate-1/2 convolutional code with soft-decision Viterbi decoding. The complete FEC chain includes payload delivery to LFSR randomization, convolutional encoding at rate 1/2, and then a 67 by 32 row column interleaver. The bits are delivered to the MSK modultor. For demodulation, a soft decision synchronization detector delivers bits to the deinterleaver, then soft decision Viterbi decoding, then derandomization, which returns the transmitted paylod.  

**CCSDS LFSR Randomization:**
The polynomial is: x^8 + x^7 + x^5 + x^3 + 1. The seed is 0xFF and is reset per frame. The purpose of the randomizer is to increase the number of transitions, which is important for MSK symbol recovery. 

**Convolutional Encoder:**
The constraint length is K = 7. This results in a 64-state trellis. Code rate is r = 1/2. Each input bit results in 2 output bits. Generator polynomials are G1=171 (octal) or 0x79 (hex), G2=133 (octal) or 0x5B (hex). This is the NASA/CCSDS standard "Voyager" code. Input is 1072 bits (134 bytes) and output is 2144 bits (268 bytes). Trellis is unterminated in the reference implementation. 

**Soft-Decision Viterbi Decoder:**
3-bit soft quantization is used with a traceback depth of 35 (5 * K). Coding gain is ~7 dB at BER=10^-5 (vs. ~5 dB for hard decisions). The reference implementation handles unterminated trellis by searching all 64 final states.

**67×32 Bit Interleaver:**
Matrix of 67 rows × 32 columns is our 2144 bits. Write is Row-major (fill rows sequentially) and the read is Column-major (read columns sequentially). Consecutive bits separated by 67 positions. The burst tolerance is a 64-bit burst results in 64 single-bit errors spread over 2048-bit span. 

### 7.3 Why Soft Decisions Matter

Hard decision Viterbi sees only "hit or miss". Each bit is 0 or 1 with no confidence information. Soft decision Viterbi sees the "die roll", which is quantized to a 3-bit confidence value indicating how certain the demodulator was.

```
Hard:  bit = 0 or 1 (confidence discarded)
Soft:  000 = strong '0', 111 = strong '1', 011 = uncertain (erasure zone)
```

This ~2 dB gain from soft decisions, combined with the K=7 code's inherent strength, yields approximately 7 dB total coding gain. This is better than the ~3-5 dB typical of other amateur digital voice protocols.

### 7.4 FEC Comparison

| Protocol | FEC Type | Code Rate | Coding Gain | Soft Decision | FEC Architecture |
|----------|----------|-----------|-------------|---------------|------------------|
| **OVP** | K=7 Conv. | 1/2 | ~7 dB | Yes (3-bit) | Protocol-layer |
| **M17** | Golay + K=5 Conv. | varies | ~5 dB | No | Protocol-layer |
| **P-25 Phase I** | Golay + Hamming | varies | ~5 dB | No | Protocol-layer |
| **P-25 Phase II** | Golay (integrated) | varies | ~5 dB | Chip-dependent | Integrated |
| **D-STAR** | Conv. | 1/2 | ~3 dB | No | Protocol-layer |
| **DMR** | BPTC Hamming | varies | ~3 dB | Chip-dependent | Integrated |
| **NXDN** | Proprietary (DVSI) | Configurable | ~3–5 dB | Up to 4-bit | Integrated |
| **YSF** | Conv. (integrated) | varies | ~3 dB | Chip-dependent | Integrated |

### 7.5 Interleaver Comparison

| Protocol | Interleaver Type | Parameters | Burst Tolerance |
|----------|------------------|------------|-----------------|
| **OVP** | Block matrix | 67×32 bits, row-write/column-read | 64-bit burst on 2048-bit spread |
| **M17** | QPP (Quadratic Permutation Polynomial) | p(x) = (45x + 92x^2) mod 368 | Per spec |
| **P-25 Phase I** | Block | Min 6-bit (3-symbol) separation | ~18 bits |
| **DMR** | Arithmetic | (i × 181) mod 196 for BPTC(196,96) | Per block |
| **NXDN** | Proprietary | Integrated in AMBE+2 chip | Unknown |
| **D-STAR** | Minimal | Part of AMBE+ chip | Unknown |
| **YSF** | Proprietary | Integrated in AMBE+2 chip | Unknown |

### 7.6 Frame Structure

**OVP Frame (268 bytes transmitted):**
```
[24-bit Sync] [2144 bits FEC-encoded payload]
     ↓              ↓
  0x02B8DB    134 bytes → randomize → K=7 encode → interleave
```


**Timing**
Frame period is 40 ms (audio-driven from Opus codec). Frame reception time is ~39.6 ms at 54.2 kbps (must receive entire frame before decoding). Sync word transmission is 0.44 ms. FPGA Processing Latency at 61.44 MHz is encoder (conv. encode) timing of ~17.5 µs and a Viterbi decoder timing of ~1.15 ms. These are negligible compared to frame reception time

End-to-End Voice Latency is higher, with frame reception of ~40 ms (frame must be fully received), deinterleave + Viterbi + derandomize of 1-2 ms. The Opus codec algorithmic delay is 20-26.5 ms for a total of ~60-70 ms (antenna to speaker).

---

## 8. Key Differentiators of Opulent Voice

**Wideband Audio:** Opus at 16 kbps provides wideband audio versus narrowband AMBE/IMBE/Codec2. This is a categorical difference like FM broadcast vs. telephone rather than an incremental improvement. Direct MOS comparisons across bandwidths are not meaningful, but wideband audio is universally preferred for intelligibility and speaker recognition.

**Full Protocol Stack:** Native IP/UDP/RTP encapsulation enables direct interoperability with VoIP systems and standard networking tools. Other protocols require application-layer gateways for IP integration.

**Complete Openness:** Both protocol specification and vocoder are royalty-free and open source. M17 shares this characteristic, but other protocols rely on DVSI licensing. OPV has optimized synchronization and a flywheel approach on receive, with the number of frames to declare frame lock and the number of missed sync words to declare frame lock lost both being configurable.

**Target Application:** Designed for scenarios where bandwidth is available but link margins are challenging (satellite, weak signal). Not intended as a narrowband replacement for VHF simplex.

---

## 9. Trade-off Summary: OVP vs M17

Both OVP and M17 are fully open protocols with royalty-free vocoders. The key differences reflect different design priorities.

| Aspect | OVP | M17 |
|--------|-----|-----|
| **Optimized for** | Audio quality | Spectral efficiency |
| **Bandwidth** | ~80 kHz | 9 kHz |
| **Spectral efficiency** | 0.68 b/Hz | 1.07 b/Hz |
| **Vocoder quality** | Wideband (Opus) | Narrowband (Codec2) |
| **IP integration** | Native (RTP/UDP/IP) | Requires gateway |
| **Best use case** | Satellite, UHF+ | VHF/UHF repeaters |

Neither protocol is universally "better". They address different segments of the amateur radio problem space.

---

## 10. Future Testing

The following tests will provide additional benchmark data when completed.

- **BER Performance Curves:** Eb/N0 vs BER for each modulation scheme under AWGN and fading channels
- **Audio Quality Testing:** PESQ/POLQA objective metrics and MOS subjective testing on standardized speech samples
- **Acquisition Time:** Time to sync lock from cold start and during frame drops
- **Multipath Robustness:** Performance under Rayleigh and Rician fading profiles
- **Power Efficiency:** TX power consumption for equivalent link margin

---

## TODO: Items We're Working Hard to Add!

- [x] ~~FEC details: Specific RS parameters, code rates, interleaver polynomial coefficients~~
- [x] ~~Sync word PSLR analysis~~
- [x] ~~NXDN parameters~~
- [x] ~~FEC architecture comparison (protocol-layer vs integrated)~~
- [ ] COBS framing overhead breakdown (IP/UDP/RTP header sizes)
- [ ] Frame structure diagram
- [ ] Actual measured BER curves from LibreSDR testing
- [ ] Latency breakdown: codec + framing + transmission with additional detail after symbol lock functions are added
- [ ] Link budget comparison

---

## 11. Notes and Caveats

This comparison presents nominal specifications. Actual performance depends on implementation quality, channel conditions, and operating environment. Frame duration and sync patterns vary by frame type in most protocols. Spectral efficiency calculations use occupied bandwidth. Tegulatory channel spacing may differ.

Audio quality comparisons require controlled subjective testing (MOS) or objective metrics (PESQ/POLQA) on standardized speech samples. Such testing is beyond the scope of this specification comparison.

---

## References

- Thompson, M. (W5NYV), "Finding Optimal Synchronization Words for Digital Voice Protocols," QEX, 2026.
- Open Research Institute Opulent Voice Protocol: https://github.com/OpenResearchInstitute/
- Sync Word Analysis Notebook: https://github.com/OpenResearchInstitute/interlocutor/blob/main/OPV_sync_word_study.ipynb
- M17 Project Specification: https://spec.m17project.org/
- TIA-102 (P-25) Standards: https://www.tiaonline.org/
- ETSI TS 102 361 (DMR) Standards: https://www.etsi.org/
- NXDN Technical Specifications: https://www.nxdn-forum.com/
- JARL D-STAR Specification: https://www.jarl.org/
- DVSI AMBE Vocoder Documentation: https://www.dvsinc.com/
- Codec2 Project: https://www.rowetel.com/codec2.html
- Opus Codec: https://opus-codec.org/

---

*Document prepared by: Open Research Institute, Inc.*  
*License: CC BY-SA 4.0*  
*Contact: abraxas3d@gmail.com*
