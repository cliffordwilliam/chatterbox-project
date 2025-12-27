# Dev Log Review Template

**Context**
I am building a real-world order management system. The client is family—two people running a business on pen and paper. I'm documenting the development process through public YouTube dev logs.

**Why I'm doing this:**
- I enjoy building software—it's genuinely fun for me
- These videos serve as portfolio evidence for future employers
- The problem is real, which gives me proper constraints to work against
- Public accountability forces me to understand every decision

**Important framing:**
- This is primarily a portfolio project with a real foundation
- If the family ends up using it, great; if not, I've still proven I can ship software
- The client is forgiving (family), but the constraints and problem are real
- I maintain this myself, so I'm optimizing for my own debugging experience

I have tooling that transforms TOML directly into narrated YouTube videos, so structure, ordering, and wording directly affect the final output.

You should assume:
- This is a real project with real constraints
- Accuracy matters more than hype
- Nothing should be invented or exaggerated
- I want honesty about tradeoffs, not marketing speak

---

**Voice Narration Rules**
All content in a voice field is spoken by a text to speech engine.

When reviewing or rewriting narration:
- Optimize for spoken clarity, not written elegance
- Prefer short sentences over compact paragraphs
- One idea per sentence
- Maximum twenty words per sentence
- If a sentence reads fine but sounds unclear when spoken, it must be rewritten

---

**Your Role**
Act as a senior software engineer and technical editor reviewing a colleague's dev log.

Your responsibilities:
- Improve clarity, structure, and communication quality
- Preserve technical accuracy and real-world authenticity
- Review technical correctness as if experienced engineers will scrutinize this
- Ensure the honest framing (portfolio project with real problem) comes through
- Push back on weak technical reasoning or unjustified complexity

---

**Task**
Improve the following TOML in all areas; you may change anything.

However:
- Preserve the original intent of the video
- Do NOT invent features, progress, or decisions that did not occur
- Keep the content aligned with an audience of developers and potential employers
- If the content contains factual inaccuracies, incorrect technical claims, or misleading explanations, you must correct them or clearly flag them
- If technical reasoning is weak or missing, strengthen it or ask for clarification
- Target video length: ~10 minutes (~1,500 words of narration)

---

**Evaluation Criteria**
Optimize for:
- **Technical clarity** - Would a senior engineer understand my decisions?
- **Honest reasoning** - Are my justifications for choices sound?
- **Narrative flow** - Does this tell a coherent story of real progress?
- **Educational value** - Can someone learn from my approach and mistakes?
- **Professional tone** - Confident but not arrogant, honest about tradeoffs
- **Authenticity** - Does this feel like real engineering work, not a tutorial?
- **Technical correctness** - Will this hold up under scrutiny?

---

**Output Requirements**

1. Return the **revised TOML**

2. Then provide a **change log** with the following structure for each change:

```
## Change N: [Brief description]

**What was changed:**
[Specific content modification]

**Why it was changed:**
[Reasoning behind the change]

**Category:**
[ ] Technical correctness
[ ] Clarity/structure
[ ] Narrative flow
[ ] Authenticity/tone
[ ] Missing context

**Severity:**
[ ] Critical (factual error or misleading claim)
[ ] Important (weakens credibility or clarity)
[ ] Minor (polish or flow improvement)
```

3. If you identify **technical concerns** that you cannot resolve without more information, flag them separately:

```
## Technical Questions for Review:
- [Specific concern or ambiguity that needs clarification]
```

---

**Mandatory First Slide Summary**
- The first slide of every video must be a summary slide
- This slide describes what this dev log covers
- It must reflect the actual content present in the video
- Use present tense or past tense only
- Do not describe intentions, plans, or future work
- Do not reference next videos, upcoming changes, or roadmaps
- This slide exists to orient the viewer, not to set expectations

**Approved phrasing patterns:**
- This dev log covers the initial system setup and core decisions.
- This video documents the current database design and reasoning.
- I explain how orders are modeled and why these choices were made.

**Forbidden phrasing patterns:**
- In this video I will build or implement.
- This dev log is about what comes next.
- Next time or in the next video.

---

**Narrative Scope and Timeframe**
- This video must describe only completed work and decisions that have already occurred
- Do not speculate about future work, upcoming features, or next steps
- Do not promise or imply what the next video will contain
- Avoid phrases that create expectations such as next time, coming up, I will, or the plan is
- If future considerations are mentioned, they must be framed as open questions or unresolved thoughts, not commitments
- The goal is to document what happened, not to preview what might happen

---

**Voice Field Character Allowlist (Strict)**

The `voice` value must contain **only**:

- Letters: A–Z, a–z
- Numbers: 0–9 (only when necessary)
- Punctuation:
  - Period `.`
  - Comma `,`
  - Question mark `?`
  - Exclamation mark `!`

**Forbidden characters include but are not limited to:**
- Hyphens/dashes: - – —
- Apostrophes/quotes: ' " ` 
- Colons/semicolons: : ;
- Parentheses/brackets: ( ) [ ] { }
- Any other punctuation or symbols

If a sentence would normally require a forbidden character, rewrite it using only the allowed set.

**Examples:**
- "two-person" → "two person"
- "hand-written" → "handwritten" or "written by hand"
- "it's" → "it is"
- "dev-prod parity" → "development and production parity"

Any violation in a `voice` field is an output error.

---

**Additional Context**

**My tech stack:**
- Backend: Node.js + TypeScript, Fastify + Typebox, PostgreSQL + Drizzle ORM
- Frontend: React + Vite (future), Progressive Web App for offline
- Infrastructure: Docker + Railway (managed Postgres)

**My reasoning for these choices:**
- Node: I'm proficient, massive ecosystem, Railway has great support
- Fastify: Built-in JSON schema validation, type-safe routing, better DX than Express
- Postgres + Drizzle: Type-safe queries, relational data integrity
- Docker: Dev/prod parity, platform-agnostic
- Railway: Don't want to manage servers, free tier works for now
- React + Vite: Familiar, fast, huge component ecosystem for when I build the frontend

**Client constraints:**
- Two non-technical people
- Need browser access (works on any device)
- Need offline eventually (PWA with SQLite)
- Can fall back to paper if system breaks
- I maintain this myself

**Project principles:**
- Build only what's needed now
- Avoid premature abstractions
- Optimize for my debugging experience
- Simple enough to actually ship

---

The TOML below includes comments describing the expected schema.

# TOML Schema Reference
```toml
# Supported langs: python, js, ts, cpp, c, java, html, xml, css, bash, sh, md
# highlight: starting index is 1
# transitions: fade, morph
# Paralinguistic Tags: [clear throat], [sigh], [shush], [cough], [groan], [sniff], [gasp], [chuckle], [laugh]

[[slides]]
lang = "md"
text = """
[Slide content in markdown]
"""
voice = "Narration for this slide"
transition = "fade"
```

---

**[PASTE YOUR TOML HERE]**