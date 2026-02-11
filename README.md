# Learning Resources

[![CI](https://github.com/organvm-ii-poiesis/learning-resources/actions/workflows/ci.yml/badge.svg)](https://github.com/organvm-ii-poiesis/learning-resources/actions/workflows/ci.yml)
[![Coverage](https://img.shields.io/badge/coverage-pending-lightgrey)](https://github.com/organvm-ii-poiesis/learning-resources)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/organvm-ii-poiesis/learning-resources/blob/main/LICENSE)
[![Organ II](https://img.shields.io/badge/Organ-II%20Poiesis-EC4899)](https://github.com/organvm-ii-poiesis)
[![Status](https://img.shields.io/badge/status-active-brightgreen)](https://github.com/organvm-ii-poiesis/learning-resources)
[![Markdown](https://img.shields.io/badge/lang-Markdown-informational)](https://github.com/organvm-ii-poiesis/learning-resources)


[![ORGAN-II: Poiesis](https://img.shields.io/badge/ORGAN--II-Poiesis-6a1b9a?style=flat-square)](https://github.com/organvm-ii-poiesis)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/status-active--development-yellow?style=flat-square)]()

> Tutorials, workshops, and educational materials for generative art, interactive performance, and creative coding -- structured as tiered learning paths from first sketch to exhibition-ready installation.

[Artistic Purpose](#artistic-purpose) | [Conceptual Approach](#conceptual-approach) | [Technical Overview](#technical-overview) | [Installation](#installation) | [Quick Start](#quick-start) | [Working Examples](#working-examples) | [Theory Implemented](#theory-implemented) | [Portfolio & Exhibition](#portfolio--exhibition) | [Related Work](#related-work) | [Contributing](#contributing) | [License & Author](#license--author)

---

## Artistic Purpose

There is a gap between the person who writes their first generative art sketch and the person who deploys a sensor-driven installation in a museum. It is not a gap of talent. It is a gap of curriculum. The tools exist -- Processing, p5.js, TouchDesigner, SuperCollider, Max/MSP, openFrameworks, Three.js -- and the documentation for each tool is adequate. But the path from "I can draw a circle that follows my mouse" to "I can build an interactive installation that responds to twelve depth cameras and drives a 40-channel sound system" is not documented anywhere as a coherent journey. You learn fragments from YouTube tutorials, forum posts, artist talks, and expensive MFA programs. The fragments do not add up to a curriculum.

Learning Resources is that curriculum. It is the educational layer of ORGAN-II (Poiesis), the art organ of the eight-organ creative-institutional system. Every tutorial, workshop module, and reference guide in this repository exists to move a learner along a deliberate path: from understanding why generative art matters (not just how it works), through the technical fundamentals of creative coding, to the practical realities of deploying interactive art in physical spaces with real audiences. The materials are designed for three contexts: university courses in new media art, museum and gallery workshop programs, and community coding events where participants may have programming experience but no art background (or art experience but no programming background).

The pedagogical philosophy is rooted in a specific claim: that creative coding is not a subset of software engineering with prettier output. It is a distinct practice with its own aesthetic priorities, its own relationship to error and surprise, its own criteria for what constitutes "working." A generative art sketch that produces unexpected results is not buggy -- it may be more interesting than what the artist intended. A real-time performance system that drops frames under load is not merely a technical failure -- it is an aesthetic failure that breaks the audience's immersion. These distinctions matter, and they are absent from conventional programming education. Learning Resources teaches them explicitly.

The repository integrates directly with [metasystem-master](https://github.com/organvm-ii-poiesis/metasystem-master) (the Omni-Dromenon Engine), using its performance-sdk and consensus algorithms as teaching examples throughout the intermediate and advanced tiers. Students who complete the full curriculum will have built components that could be deployed in a live Omni-Dromenon performance. This is not incidental -- it is the design. Education that ends in a portfolio piece is more valuable than education that ends in a certificate.

---

## Conceptual Approach

### Tiered Learning Paths

The curriculum is organized into three tiers, each with a distinct pedagogical goal and a distinct relationship to the tools:

**Tier 1: Foundations (Beginner)**
The learner has either programming experience or art experience, but not both in combination. Tier 1 bridges the gap. For programmers, it introduces aesthetic thinking: why randomness is not the same as generativity, why Perlin noise produces more interesting results than `Math.random()`, why color theory matters in algorithmic composition. For artists, it introduces computational thinking: variables as containers for aesthetic decisions, loops as repetition with variation, functions as reusable artistic gestures. Tier 1 uses p5.js exclusively -- it is the most accessible creative coding environment, runs in the browser, and has the largest community of beginners helping beginners.

**Tier 2: Practice (Intermediate)**
The learner can write a generative sketch from scratch. Tier 2 introduces real-time interaction, audio-visual synthesis, and multi-modal input. This is where the curriculum diverges from typical creative coding courses, which tend to focus on static or pre-rendered output. Tier 2 teaches the skills needed for live performance and interactive installation: WebSocket communication, OSC protocol, sensor integration, frame-rate management under load, spatial mapping, and audience input processing. The primary framework shifts to TypeScript with the metasystem-master performance-sdk, though modules also cover SuperCollider (audio synthesis), Three.js (3D environments), and TouchDesigner (visual patching for those who prefer node-based workflows).

**Tier 3: Deployment (Advanced)**
The learner can build interactive systems. Tier 3 teaches them to deploy those systems in physical spaces with real audiences. This is the tier that does not exist in any online course. It covers: hardware selection and procurement for installations (depth cameras, LIDAR units, projection mapping rigs, multi-channel audio interfaces), venue assessment and spatial calibration, failsafe protocols for public exhibitions (what happens when a sensor fails mid-show), audience flow design (how people move through an interactive space), documentation for gallery technicians who will maintain the installation after the artist leaves, and the grant-writing and exhibition-proposal skills needed to get the work shown in the first place. Tier 3 culminates in a capstone project: a fully documented installation proposal, complete with technical specifications, budget, timeline, and artist statement, ready to submit to a real venue or funding body.

### Pedagogy of Creative Error

Every module in the curriculum includes a section called "When Things Go Wrong (And Why That Might Be Good)." This is not a troubleshooting guide. It is a deliberate pedagogical intervention against the software engineering instinct to treat unexpected behavior as a bug. In creative coding, unexpected behavior is often the most valuable output. A particle system that collapses into a singularity because of a sign error in the gravity calculation may produce a visual effect more compelling than the intended behavior. A feedback loop in an audio synthesis patch that produces howling distortion may be the sound the piece needs.

The curriculum teaches students to distinguish between three categories of unexpected behavior: errors that break the system (must fix), errors that produce interesting output (investigate and potentially keep), and errors that reveal a deeper misunderstanding of the system's behavior (learning opportunity). This taxonomy is not taught in computer science programs, and it is the single most important skill for a creative coder to develop.

### Integration with the Eight-Organ System

Learning Resources does not exist in isolation. It is the educational layer of a larger system, and its curriculum reflects that architecture. Theory modules reference ORGAN-I (Theoria) concepts -- recursion as creative strategy, ontological layering, the relationship between formal systems and aesthetic experience. Deployment modules reference ORGAN-III (Ergon) tools -- the SaaS products and developer tools that support commercial applications of creative technology. The capstone project in Tier 3 includes a public-process component that feeds into ORGAN-V (Logos), teaching students to write about their work as part of making it.

This cross-organ integration is not marketing. It is a pedagogical position: that creative practice, theoretical understanding, commercial viability, and public articulation are not separate skills that happen to coexist in the same person. They are facets of a single practice, and a curriculum that separates them produces artists who can make things but cannot explain them, or theorists who can explain things but cannot make them, or entrepreneurs who can sell things but cannot make or explain them. Learning Resources teaches all four facets as an integrated whole.

---

## Technical Overview

### Repository Structure

```
learning-resources/
├── tier-1-foundations/
│   ├── 01-why-generative-art/
│   │   ├── lesson.md              # Conceptual introduction
│   │   ├── exercises/             # Hands-on p5.js sketches
│   │   └── references/           # Artist references, readings
│   ├── 02-computational-thinking/
│   ├── 03-color-and-composition/
│   ├── 04-randomness-and-noise/
│   ├── 05-repetition-and-variation/
│   ├── 06-interaction-basics/
│   ├── 07-time-and-animation/
│   └── 08-your-first-composition/
├── tier-2-practice/
│   ├── 01-real-time-systems/
│   ├── 02-websocket-communication/
│   ├── 03-osc-protocol/
│   ├── 04-sensor-integration/
│   ├── 05-audio-visual-synthesis/
│   ├── 06-consensus-algorithms/  # Uses metasystem-master examples
│   ├── 07-spatial-mapping/
│   └── 08-performance-optimization/
├── tier-3-deployment/
│   ├── 01-hardware-selection/
│   ├── 02-venue-assessment/
│   ├── 03-calibration-procedures/
│   ├── 04-failsafe-protocols/
│   ├── 05-audience-flow-design/
│   ├── 06-documentation-for-venues/
│   ├── 07-grant-writing/
│   └── 08-capstone-project/
├── workshop-kits/
│   ├── 2-hour-intro/             # Museum/gallery drop-in format
│   ├── weekend-intensive/        # Community coding event format
│   ├── semester-course/          # University 14-week syllabus
│   └── facilitator-guides/      # Train-the-trainer materials
├── shared-assets/
│   ├── starter-templates/        # Boilerplate for each tier
│   ├── datasets/                # Sample data for generative exercises
│   └── hardware-specs/          # Recommended equipment lists
├── scripts/
│   ├── setup-environment.sh      # One-command dev environment
│   ├── validate-exercises.py     # Check exercise completeness
│   └── generate-syllabus.py      # Build printable syllabi from modules
└── docs/
    ├── pedagogy.md               # Teaching philosophy
    ├── assessment-rubrics.md     # Grading criteria for university use
    └── accessibility.md         # Accessibility guidelines for workshops
```

### Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Tier 1 Sketches | p5.js 1.9+ | Browser-based creative coding |
| Tier 2 Systems | TypeScript, Node.js 18+ | Real-time interactive systems |
| Audio Synthesis | SuperCollider 3.13+ | Sound generation and processing |
| 3D Environments | Three.js r160+ | WebGL-based spatial experiences |
| Performance SDK | metasystem-master | Consensus algorithms, audience input |
| Documentation | MkDocs + Material theme | Structured lesson site generation |
| Exercise Validation | Python 3.11+ | Automated completeness checks |
| Environment Setup | Docker Compose | Reproducible dev environments |

### Module Format

Every module follows a consistent format designed for both self-paced learning and instructor-led delivery:

1. **Context** (500-800 words): Why this topic matters, with artist references and historical context
2. **Concept** (300-500 words): The core idea, explained without code
3. **Implementation** (variable): Step-by-step code with extensive inline commentary
4. **Exercises** (3-5 per module): Graduated difficulty, from guided to open-ended
5. **When Things Go Wrong**: Creative error taxonomy for this module's domain
6. **Portfolio Prompt**: A suggestion for turning the exercise output into a portfolio piece
7. **Further Reading**: Academic papers, artist interviews, related projects

---

## Installation

### Prerequisites

- Node.js >= 18.0.0
- pnpm >= 9.0.0
- Python 3.11+ (for validation scripts)
- Git

### Setup

```bash
# Clone the repository
git clone https://github.com/organvm-ii-poiesis/learning-resources.git
cd learning-resources

# Install dependencies
pnpm install

# Set up Python environment for validation scripts
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Verify installation
pnpm run verify
```

### Tier-Specific Setup

```bash
# Tier 1: No additional setup needed -- p5.js runs in browser
pnpm run serve:tier1   # Opens local server with all Tier 1 sketches

# Tier 2: Requires metasystem-master performance-sdk
pnpm run setup:tier2   # Installs SDK and configures local environment

# Tier 3: Requires Docker for hardware simulation
docker compose -f tier-3-deployment/docker-compose.yml up
```

---

## Quick Start

### 30-Minute First Sketch (Tier 1, Module 1)

```javascript
// exercises/01-first-composition.js
// A generative composition using Perlin noise flow fields

let particles = [];
const NUM_PARTICLES = 2000;
const NOISE_SCALE = 0.005;

function setup() {
  createCanvas(windowWidth, windowHeight);
  background(10, 10, 20);

  for (let i = 0; i < NUM_PARTICLES; i++) {
    particles.push({
      x: random(width),
      y: random(height),
      speed: random(0.5, 2.5),
      hue: random(180, 280),  // Purple-blue palette
    });
  }
  colorMode(HSB, 360, 100, 100, 100);
}

function draw() {
  // No background clear -- trails accumulate, creating history
  for (let p of particles) {
    let angle = noise(p.x * NOISE_SCALE, p.y * NOISE_SCALE) * TWO_PI * 2;

    p.x += cos(angle) * p.speed;
    p.y += sin(angle) * p.speed;

    // Wrap at edges
    if (p.x < 0) p.x = width;
    if (p.x > width) p.x = 0;
    if (p.y < 0) p.y = height;
    if (p.y > height) p.y = 0;

    stroke(p.hue, 60, 90, 5);
    strokeWeight(1);
    point(p.x, p.y);
  }
}
```

This sketch produces a flow field visualization where 2,000 particles trace paths through Perlin noise space. The trails accumulate because `background()` is never called in `draw()` -- each frame adds to the image rather than replacing it. Run it for thirty seconds and you have a unique generative composition. Run it for five minutes and the entire canvas fills with luminous thread-like structures. The hue range (180-280) produces cool blues and purples; change it to (0-60) for warm oranges and reds. This is your first aesthetic decision as a generative artist: the palette is not decoration, it is composition.

### Interactive Consensus Demo (Tier 2, Module 6)

```typescript
// exercises/06-consensus-visualization.ts
// Visualize how audience inputs converge through weighted consensus

import { ConsensusAggregator } from '@organvm/performance-sdk';
import { createCanvas } from './utils/canvas';

const aggregator = new ConsensusAggregator({
  spatialAlpha: 0.3,
  temporalBeta: 0.5,
  consensusGamma: 0.2,
  smoothingFactor: 0.15,
});

const canvas = createCanvas(800, 600);
const ctx = canvas.getContext('2d');

// Simulate 20 audience members with varying positions
const audience = Array.from({ length: 20 }, (_, i) => ({
  id: `participant-${i}`,
  position: { x: Math.random() * 10, y: Math.random() * 10 },
  distanceFromStage: Math.random() * 15 + 1,
}));

function simulateFrame() {
  // Each participant sends a mood value (0-1)
  for (const member of audience) {
    const input = {
      participantId: member.id,
      parameter: 'mood',
      value: Math.sin(Date.now() * 0.001 + member.position.x) * 0.5 + 0.5,
      spatialWeight: 1 / member.distanceFromStage,
      timestamp: Date.now(),
    };
    aggregator.addInput(input);
  }

  const consensus = aggregator.compute();

  // Visualize: consensus value maps to background color
  const hue = consensus.mood * 360;
  ctx.fillStyle = `hsl(${hue}, 70%, 15%)`;
  ctx.fillRect(0, 0, 800, 600);

  // Draw each participant's individual input as a dot
  for (const member of audience) {
    const x = (member.position.x / 10) * 800;
    const y = (member.position.y / 10) * 600;
    const memberHue = aggregator.getLastInput(member.id, 'mood') * 360;
    ctx.beginPath();
    ctx.arc(x, y, 5 + (1 / member.distanceFromStage) * 20, 0, Math.PI * 2);
    ctx.fillStyle = `hsl(${memberHue}, 80%, 60%)`;
    ctx.fill();
  }

  // Draw consensus indicator
  ctx.beginPath();
  ctx.arc(400, 300, 30, 0, Math.PI * 2);
  ctx.fillStyle = `hsl(${hue}, 90%, 70%)`;
  ctx.fill();
  ctx.strokeStyle = 'white';
  ctx.lineWidth = 2;
  ctx.stroke();

  requestAnimationFrame(simulateFrame);
}

simulateFrame();
```

This exercise makes the consensus algorithm visible. Twenty simulated audience members send continuously varying mood values. The aggregator computes a weighted consensus, and the visualization shows both individual inputs (small dots, sized by spatial weight) and the resulting consensus (large central dot). Students can adjust the three weighting parameters and watch how the consensus behavior changes: high `spatialAlpha` makes the dots near the "stage" dominate; high `temporalBeta` makes the consensus track rapid changes; high `consensusGamma` makes clusters of agreement amplify each other.

---

## Working Examples

### Workshop Kit: 2-Hour Museum Introduction

A complete facilitator package for running a drop-in generative art workshop at a museum or gallery:

| Time | Activity | Materials |
|------|----------|-----------|
| 0:00-0:15 | Welcome + context: "What is generative art?" | Slideshow of 10 artworks |
| 0:15-0:30 | Live coding demo: flow field from scratch | Projector + p5.js editor |
| 0:30-1:00 | Guided exercise: participants modify the demo | Laptops or tablets |
| 1:00-1:20 | Open exploration: "Make it yours" | Cheat sheet of parameters |
| 1:20-1:40 | Gallery walk: participants show their compositions | Screen sharing or printouts |
| 1:40-2:00 | Context: how this connects to interactive installation | metasystem-master demo video |

### Workshop Kit: 14-Week University Semester

A full syllabus for a university course in creative coding and interactive art:

| Week | Topic | Tier | Deliverable |
|------|-------|------|-------------|
| 1-2 | Generative fundamentals | 1 | Flow field composition |
| 3-4 | Color theory + algorithmic palette | 1 | Palette system |
| 5-6 | Interaction + real-time input | 1-2 | Interactive sketch |
| 7-8 | Audio-visual synthesis | 2 | Sound-reactive piece |
| 9-10 | Consensus + audience systems | 2 | Multi-user prototype |
| 11-12 | Hardware + spatial design | 3 | Installation proposal |
| 13 | Grant writing + artist statements | 3 | Exhibition application |
| 14 | Final presentations | All | Capstone portfolio |

---

## Theory Implemented

Learning Resources embeds theoretical frameworks from ORGAN-I (Theoria) into practical exercises:

### Recursion as Creative Strategy
Tier 1, Module 5 ("Repetition and Variation") teaches recursion not as a computer science concept but as an artistic one. Recursive structures appear throughout art history -- fractal branching in Islamic geometric patterns, self-similar forms in Romanesque architecture, nested narrative frames in Borges and Calvino. The module teaches students to use recursive functions to generate visual complexity, then asks them to identify recursive structures in non-computational art. The exercise is bidirectional: code illuminates art, and art illuminates code.

### Emergence and Authorship
Tier 2, Module 6 ("Consensus Algorithms") engages directly with the philosophical question of authorship in systems where behavior emerges from collective input. Who is the author of a performance shaped by 500 audience members, mediated by a consensus algorithm, interpreted by a performer? The module does not answer this question -- it teaches students to build systems that make the question unavoidable. This is the pedagogical strategy throughout: teach the tool, then reveal the question the tool opens.

### Feedback and Control Theory
Tier 2, Modules 3-4 ("OSC Protocol" and "Sensor Integration") introduce cybernetic feedback loops: systems where output feeds back as input, creating circular causality. Students build audio-reactive visual systems where the visual output influences the audio (through performer interpretation), which influences the visual output, creating an autopoietic loop. The theoretical reference is Norbert Wiener via second-order cybernetics (von Foerster, Maturana), but the teaching vehicle is a system the student builds and performs with.

### Situated Knowledge
Tier 3, Module 2 ("Venue Assessment") teaches Donna Haraway's concept of situated knowledge through the practical lens of site-specific installation. Every venue is different: the acoustics, the lighting, the foot traffic patterns, the electrical capacity, the institutional politics. An installation designed in the studio must be adapted to the venue, and that adaptation is not a compromise -- it is part of the artistic process. The module teaches students to conduct a venue assessment that is simultaneously technical (power requirements, network infrastructure, mounting points) and aesthetic (how does the space feel, what does it want, what does the institution expect).

---

## Portfolio & Exhibition

### For Grant Reviewers

Learning Resources demonstrates:

- **Curriculum design** at the intersection of art and technology, with tiered progression from beginner to exhibition-ready
- **Pedagogical innovation**: the creative error taxonomy and integrated cross-disciplinary teaching approach
- **Community impact**: workshop kits designed for museums, universities, and community organizations
- **Scalability**: modular format allows individual modules to be used independently or combined into multi-week courses
- **Open access**: MIT-licensed materials available to any institution or individual

### For Hiring Managers

This repository demonstrates expertise in:

- Technical writing that communicates complex systems to diverse audiences (artists, programmers, educators)
- Curriculum architecture: structuring a large body of knowledge into navigable, progressive learning paths
- Cross-disciplinary translation: making computer science concepts accessible to artists and artistic concepts accessible to programmers
- Full-stack creative technology: from p5.js sketches to multi-sensor installation deployment

### For Educators

All materials are designed for adaptation. The facilitator guides include timing variations (90-minute, 2-hour, half-day, full-day), audience profiles (artist-heavy, programmer-heavy, mixed), and equipment alternatives (laptop-only, with projector, with hardware kits). Assessment rubrics are provided for university contexts but can be removed for informal workshop settings.

---

## Related Work

Learning Resources builds on and extends the pedagogical traditions established by:

- **Processing Foundation** ([processing.org](https://processing.org)): Casey Reas and Ben Fry's Processing environment and its educational ecosystem established creative coding as a discipline. Learning Resources extends this tradition into real-time interactive systems and physical installation.
- **School for Poetic Computation** ([sfpc.study](https://sfpc.study)): Taeyoon Choi, Zach Lieberman, and collaborators created an intimate educational model that foregrounds poetry and politics alongside code. Learning Resources adopts SFPC's emphasis on "why" before "how" while providing a more structured curriculum framework.
- **The Coding Train** ([thecodingtrain.com](https://thecodingtrain.com)): Daniel Shiffman's video tutorials democratized creative coding education. Learning Resources provides the structured curriculum that complements Shiffman's exploratory approach.
- **MIT Media Lab's Lifelong Kindergarten** group: Mitchel Resnick's work on creative learning (Scratch, constructionism) informs the pedagogical philosophy of learning-by-making that underpins every module.
- **Algorithmic Art Assembly** ([algorithmicartassembly.com](https://algorithmicartassembly.com)): Community events that bring together algorithmic artists. Learning Resources provides the educational infrastructure for similar community gatherings.

### Cross-References Within the Eight-Organ System

| Repository | Organ | Relationship |
|-----------|-------|-------------|
| [metasystem-master](https://github.com/organvm-ii-poiesis/metasystem-master) | II | Performance SDK used in Tier 2-3 exercises |
| [example-interactive-installation](https://github.com/organvm-ii-poiesis/example-interactive-installation) | II | Reference implementation for Tier 3 capstone |
| [example-ai-collaboration](https://github.com/organvm-ii-poiesis/example-ai-collaboration) | II | AI-conductor methodology taught in Tier 2 |
| [recursive-engine](https://github.com/organvm-i-theoria/recursive-engine) | I | Theoretical foundations for recursion modules |
| [public-process](https://github.com/organvm-v-logos/public-process) | V | Public writing exercises in Tier 3 capstone |

---

## Contributing

### How to Contribute

```bash
# Fork and clone
git clone https://github.com/<your-fork>/learning-resources.git
cd learning-resources
pnpm install

# Create a feature branch
git checkout -b content/new-module-name

# Make changes
# Run validation
python scripts/validate-exercises.py

# Commit (conventional commits)
git commit -m "content(tier-2): add spatial audio mapping module"

# Push and open a PR
git push origin content/new-module-name
```

### Content Contributions Welcome

- **New modules**: Propose via issue first. Include: tier, topic, prerequisites, learning outcomes, estimated completion time.
- **Workshop kits**: Especially needed for non-English languages and specific institutional contexts (K-12, community centers, maker spaces).
- **Exercise translations**: Port exercises between frameworks (p5.js to Processing, TypeScript to Python, Three.js to Unity).
- **Accessibility improvements**: Screen reader compatibility, alternative input methods, colorblind-safe palettes in examples.
- **Facilitator reports**: If you run a workshop using these materials, share what worked and what did not. Real-world feedback is the most valuable contribution.

### Style Guide

- Lessons use second person ("you will build...") for exercises, first person plural ("we approach...") for conceptual sections.
- Code comments explain the artistic intent, not the syntax. "// Trails accumulate, creating visual history" not "// don't call background()".
- Every code example must run without modification. No pseudocode, no "exercise left to the reader."
- Artist references include medium, year, and why the reference is relevant -- not just a name drop.

---

## License & Author

**License:** [MIT](LICENSE)

**Author:** Anthony Padavano ([@4444J99](https://github.com/4444J99))

**Organization:** [organvm-ii-poiesis](https://github.com/organvm-ii-poiesis) (ORGAN-II: Poiesis)

**System:** [meta-organvm](https://github.com/meta-organvm) -- the eight-organ creative-institutional system coordinating ~80 repositories across theory, art, commerce, orchestration, public process, community, and marketing.

---

<sub>This README is a Gap-Fill Sprint portfolio document for the organvm system. It is written for grant reviewers, hiring managers, and educators who want to understand what Learning Resources offers, how it is structured, and how it fits within a larger creative-institutional architecture.</sub>