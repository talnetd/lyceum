# Topic 5: Sustainability in Computing

> CM2045 · Topic 5 (Sustainability) · 5 lectures
> Source transcripts: `notes/transcripts/05-sustainability/` (local, gitignored)

## TL;DR
**Sustainability** = meeting present needs without compromising future generations' ability to meet theirs (Brundtland-style definition); we currently consume **1.7x** what Earth can regenerate per year (Global Footprint Network). Computing's footprint is large and hidden: making one **smartphone** uses **62 metals** and emits **~85 kg CO2** (10x the device's weight), the world threw out **53.6M tonnes of e-waste in 2019** (≈ 4,500 Eiffel Towers) and recycled only **17%**. The topic drills into four levers covered in [[sustainable-computing]] but goes deeper here: **green data centres** (cooling is up to **40%** of a centre's energy; fixes = liquid/free cooling, virtualisation, **waste-heat recovery**), **renewable energy** (tech uses **>200 TWh/yr** ≈ Sweden; giants buy via **PPAs** and **RECs**, chasing 100% renewable / carbon-free / carbon-negative pledges), **lifecycle assessment (LCA)** (four stages, extraction alone = **40%** of impact), and **e-waste / right-to-repair** (fighting **planned obsolescence**, building a **circular economy**). The recurring tension: clean tech and efficiency gains run up against rising device demand, the human cost of mining (**cobalt / child labour**), and intermittent renewables.

## 1. Why sustainability matters now ([[sustainability-definition]])

- **Definition:** meeting the needs of the present **without compromising future generations'** ability to meet their own needs.
- Current practices are **not** sustainable. Three drivers (likely exam fodder):

| Driver | Evidence / figure | Source |
|---|---|---|
| **Resource depletion** | Using **1.7x** the resources Earth regenerates per year | Global Footprint Network |
| **Climate change** | Catastrophic effects if warming exceeds **1.5°C** | IPCC |
| **Waste & pollution** | By **2050** there could be more plastic in the ocean than fish **by weight** | World Economic Forum |

- Stakes are not just environmental: unsustainable practice threatens **human health, economic stability, global security** (climate displacing communities, resource conflicts over water/energy).

## 2. The hidden footprint of devices ([[device-footprint]])

- Most people ignore the cost behind a phone/laptop: extracting **finite resources**, **toxic waste**, significant **CO2**.
- **One smartphone** = **62 different metals** (incl. gold + rare earths); manufacturing emits **~85 kg CO2** (Green Electronics Council, 2016 report), **>10x** the device's own weight.
- **Rare earth elements** (neodymium, tantalum, cobalt) are critical for magnets, speakers, batteries. Extraction is resource-intensive and damaging (pollution, soil degradation in China and the DRC).
- **Cobalt** (for lithium-ion batteries) carries a **human cost**: reports of **child labour** at extraction sites (DRC) (likely exam fodder, the ethics callback).

## 3. Energy-efficient (green) data centres ([[green-data-centres]])

Data centres are "the backbone of the digital world", running 24/7 to host sites, store data and run AI/cloud.

- Consume **~1% of the world's electricity**, and climbing with big data / AI / cloud.
- **Cooling can be up to 40%** of a centre's total energy use, so cooling is the prime efficiency target (likely exam fodder).

### Efficiency strategies (and their catch)
| Strategy | How it works | Catch / note |
|---|---|---|
| **Efficient cooling** | **Liquid cooling** or **free cooling** (naturally cool air/water) instead of traditional A/C | Depends on climate/location |
| **Server virtualisation** | Many VMs on one physical server, fewer servers needed | Consolidation limits |
| **Renewable energy** | Power servers from solar/wind/hydro | Intermittency (see §4) |
| **Waste-heat recovery** | Capture server heat and reuse it (heat buildings/pools) | Needs a nearby heat demand |

### Real-world examples (memorise these)
| Org | Innovation | Result |
|---|---|---|
| **NatWest Bank**, Exmouth, Devon | Pipes data-centre **waste heat** to a local community **swimming pool** | Heats pool *and* cools the centre more efficiently (heat moved from where it's unwanted to where it's wanted) |
| **Google** | **Machine-learning** to optimise cooling/energy | **~40%** less cooling energy in some centres; pledged **100% renewable** |
| **Microsoft** | **Project Natick** underwater data centres | Ocean provides natural cooling + offshore wind; proof-of-concept, **no longer active** |
| **Facebook (Meta)**, Luleå, **Sweden** | **Free air cooling** from cold climate | **100% renewable**, primarily **hydroelectric** |

> **Real-world correction (cite the source, not the lecture).** The lecture credits "**NatWest Bank**" for the Exmouth pool scheme, but that is wrong. The actual scheme is run by start-up **Deep Green**: a **washing-machine-sized** data centre heats **Exmouth Leisure Centre**'s pool, supplying **~60%** of its heating (pool kept **~30°C**). Deep Green installs the kit **free** and **refunds the electricity cost**; founder **Mark Bjornsgaard** developed it over 5 years, and **7** more England pools have signed up. Context: **65** UK pools have closed since 2019 partly on energy costs; one leisure centre faced a **£100,000** bill rise in 2023. Cambridge's **Dr Julian Allwood** notes data centres use less energy than previously reported. Source: Zoe Kleinman, *"Tiny data centre used to heat public swimming pool"*, BBC News, 14 Mar 2023 (`bbc.com/news/technology-64939558`). See [[waste-heat-recovery]].

- Future direction: AI-driven optimisation, more waste-heat reuse, alternative cooling, fully green-powered centres. Efficiency is "good for business" too (lower energy bills).

## 4. Renewable energy in tech ([[renewable-energy]])

- The tech industry uses **>200 TWh/yr** of electricity, ≈ a mid-sized country like **Sweden** (Bloomberg New Energy Finance).
- Drivers: environmental impact **plus** sustainability is **good for business** (investor pressure), and **wind/solar are now cheaper than fossil fuels** in many regions.

### Procurement mechanisms (key terms, likely exam fodder)
| Mechanism | What it is |
|---|---|
| **PPA** (Power Purchase Agreement) | Long-term contract to buy renewable energy at a **fixed price**; guarantees a market so providers invest in new capacity |
| **REC** (Renewable Energy Certificate) | Certificate purchased to **offset** energy drawn from non-renewable sources |

### Tech-giant pledges (note the precise wording, they differ)
| Company | Pledge | Detail |
|---|---|---|
| **Google** | **First** major company to hit **100% renewable** (2017) via **RECs**; aim **carbon-free by 2030** | Carbon-free = clean energy **every hour of every day**, *without relying on offsets* |
| **Microsoft** | **Carbon-negative by 2030**; by **2050** remove **all** carbon ever emitted since founding (**1975**) | Uses multiple **PPAs** with solar/wind + carbon-capture tech |
| **Amazon** | **100% renewable across all operations by 2025** (the **Climate Pledge**) | Virginia solar farm = **80 MW**; **AWS Clean Energy Accelerator**; **Bezos Earth Fund** = **$10bn** |
| **Facebook (Meta)** | PPA with a **300 MW** wind farm in **Texas** | |
| **Apple** | Solar projects generating **>1 GW** of clean energy globally | |

- **Cooling advances:** Google/Microsoft use **AI-driven algorithms** to cut energy by **~40%** via dynamic real-time adjustment; liquid cooling + submerged centres (Natick) reduce demand further.
- **Key challenge: intermittency.** Solar/wind aren't available 24/7, so tech needs **battery storage** and **grid balancing** to make renewables reliable (likely exam fodder).

## 5. Lifecycle assessment (LCA) of electronics ([[lifecycle-assessment]])

- **LCA** = method to evaluate a product's environmental impact across its **full lifespan**, creation through disposal (inspired by the **EPA**). Used to measure and reduce ecological damage (toxic e-waste, resource depletion, greenhouse gases).

### The four stages
| Stage | What happens | Environmental impact |
|---|---|---|
| **1. Raw material extraction** | Mining copper, gold, lithium, rare earths for boards/batteries | **~40% of a device's total impact** (EPA); cobalt mining = child labour + harm in DRC (likely exam fodder) |
| **2. Manufacturing & assembly** | Raw materials become devices | Energy-intensive; **~85 kg CO2 per smartphone** (Green Electronics Council); **toxic chemicals** in chips/displays/batteries |
| **3. Use phase** | Energy consumed while devices operate | Per-device small, but **billions** add up; **data centres ≈ 1%** of world electricity (IEA), rising as cloud grows |
| **4. End-of-life disposal** | Devices discarded as **e-waste** | **53.6M tonnes/yr**, only **~17% recycled** (Global E-Waste Monitor); lead/mercury/cadmium leach into soil & water |

- **Solution emphasis: circular economy** (recycle/reuse components to shrink the end-of-life footprint).
- **Apple LCA case study:** **100% recycled aluminium** in some products; the **Daisy** disassembly robot recovers cobalt/aluminium/gold; **2020** efforts diverted **>48,000 tonnes** of e-waste from landfill via **closed-loop recycling** (likely exam fodder).

### Strategies to reduce LCA impact
- **Design for longevity** (last longer, easier to repair).
- **Energy efficiency** (manufacturers and consumers prioritise efficient devices).
- **Recycling & e-waste management** (better programmes, encourage returns).
- **Sustainable materials** (alternatives to rare earths, less extraction).

## 6. E-waste, planned obsolescence and right-to-repair ([[e-waste]], [[right-to-repair]])

Inspired by Gay Gordon-Byrne's TED talk *"You Deserve the Right to Repair Your Stuff."*

- **Scale:** **53.6M tonnes** of e-waste in **2019** and rising; only **17%** properly recycled, the rest goes to landfill (often in developing countries), leaching **lead, mercury, cadmium**.
- **Lost value:** 2019 e-waste held **$57bn** of recoverable precious metals (gold, silver), mostly lost to poor recycling (UN University).
- **Short lifespans:** average **smartphone ≈ 2 years**, laptops not much longer.
- **Planned obsolescence** = designing products with a **deliberately limited lifespan** to force upgrades: slowing old phones via updates, **non-replaceable batteries**, making repair hard (likely exam fodder).

### Pushback and fixes (with trade-offs)
| Approach | Example | Catch |
|---|---|---|
| **Right-to-repair** | EU + **California** legislation; consumers/third parties repair without voiding warranty | Manufacturers resist; uneven by region |
| **Recycling robots** | Apple's **Daisy** disassembles iPhones | Addresses only the disposal end |
| **Carbon-neutral / negative hardware** | **Google** carbon-neutral hardware by **2030**; **Microsoft** carbon-negative by **2030**, **circular computing** | Pledges, not yet fully realised |
| **Modular / sustainable design** | **Fairphone** modular phones, responsibly sourced + recycled parts | Niche; mainstream demand for new devices keeps rising |
| **Sustainable materials** | Biodegradable plastics, recycled metals, plant-based materials | Cost / supply scale |

- **Shared responsibility:** company initiatives only solve **part** of the problem; **consumer behaviour** (recycle, **repair**, extend life, use **take-back schemes**) and **government policy** are equally critical.

## Related concepts
- [[sustainable-computing]], the Topic 3 §6 overview (energy/water/e-waste trade-offs); this note is the deep dive
- [[sustainability-definition]], present-vs-future needs; 1.7x overshoot, 1.5°C, plastic-by-2050
- [[green-data-centres]], cooling = 40%, liquid/free cooling, virtualisation, waste-heat, TODO
- [[waste-heat-recovery]], Deep Green heats Exmouth pool (BBC, 14 Mar 2023, `bbc.com/news/technology-64939558`); lecture's "NatWest" attribution is wrong, TODO
- [[renewable-energy]], PPAs vs RECs, 100%/carbon-free/carbon-negative pledges, intermittency, TODO
- [[lifecycle-assessment]], the four LCA stages; extraction = 40% of impact, TODO
- [[e-waste]], 53.6M tonnes, 17% recycled, toxic leaching, TODO
- [[right-to-repair]], planned obsolescence vs repair laws (EU/California), Fairphone, TODO
- [[green-ai]], smaller models / ML for cooling efficiency (~40%), TODO
- [[circular-economy]], recycle/reuse/closed-loop (Apple Daisy, Dell), TODO
- [[ethics-vs-law]], the cobalt/child-labour and digital-divide ethics callback from Topic 3
