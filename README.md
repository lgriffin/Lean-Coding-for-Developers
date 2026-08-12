# Lean Coding for Developers

Source code listings for [*Lean Coding for Developers*](https://www.manning.com/), published by Manning.

## Repository structure

Each chapter has its own directory. Inside, every code listing from the book is stored as a standalone file named by its listing number:

```
chapter 1/
  1.1.md
chapter 2/
  2.1.py
  2.2.ts
  2.3.java
  …
chapter 7/
  7.1.py
  7.2.py
  …
```

### Naming convention

| Component | Format | Example |
|-----------|--------|---------|
| Directory | `chapter N` | `chapter 4` |
| File name | `{listing number}.{ext}` | `4.3.java` |
| Extension | Matches the language of the listing | `.py`, `.ts`, `.java`, `.tsx`, `.yaml`, `.sh`, `.md` |

The listing number (e.g. **4.3**) corresponds directly to **Listing 4.3** in the printed book. To find the code for any listing, open the matching chapter directory and file.

### File extensions

| Extension | Content type |
|-----------|-------------|
| `.py` | Python |
| `.ts` | TypeScript |
| `.tsx` | TypeScript / React (JSX) |
| `.java` | Java |
| `.yaml` | YAML (CI workflows, configs) |
| `.sh` | Shell / Bash |
| `.md` | Prose listings — checklists, logs, templates, standard-work documents, decision records |

Some listings in the book are not runnable code but structured documents (kaizen logs, friction logs, A3 reports, standard-work checklists). These are stored as Markdown (`.md`) files.

## Chapters

| # | Title | Listings |
|---|-------|----------|
| 1 | Why Lean, Why Now? | 1 |
| 2 | Value and Waste in Software | 7 |
| 3 | AI as a Partner and Problem | 6 |
| 4 | Writing Lean Code | 11 |
| 5 | Testing as Waste Prevention | 11 |
| 6 | Flow in Your Development Cycle | 1 |
| 7 | Taming Legacy Code | 10 |
| 8 | Root Cause Thinking for Developers | 5 |
| 9 | Measuring What Matters | 2 |
| 10 | Kaizen: Continuous Improvement | 5 |
| 11 | Architectures That Flow | 4 |
| 12 | Lean Operations and Production | 5 |
| 13 | Lean Team Culture | 5 |
| 14 | Personal Lean: Building Habits | 7 |
| 15 | Leading Lean Change | 2 |

## Usage

These listings are reference companions to the book. Each file contains the code or document exactly as it appears in the corresponding listing, ready to read, run, or adapt.

## License

All code in this repository accompanies *Lean Coding for Developers* and is provided for educational use.
