# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Run the app
python -m src.main

# Run tests
pytest

# Run a single test
pytest tests/test_recommender.py::test_recommend_returns_songs_sorted_by_score

# Install dependencies
pip install -r requirements.txt
```

## Project Status

**Phase 4 — Applied AI System (in progress)**

Extending the base music recommender (Phase 1) into a full applied AI system. The core scoring logic is complete and working. Current work adds Claude API integration on top of the existing recommender.

## Architecture

Two parallel API styles live in `src/recommender.py`:

1. **OOP style** — `Song` (dataclass), `UserProfile` (dataclass), `Recommender` class with `recommend(user, k)` and `explain_recommendation(user, song)` methods. Used by tests via `from src.recommender import ...`.

2. **Functional style** — `load_songs(csv_path)` and `recommend_songs(user_prefs, songs, k)`. Used by `src/main.py` via `from recommender import ...` (no `src.` prefix — main.py runs as a module under `src/`).

The song catalog lives in `data/songs.csv` with columns: `id, title, artist, genre, mood, energy, tempo_bpm, valence, danceability, acousticness`.

## Scoring Algorithm

Each song is scored against the user profile (max 5.0):

| Signal | Points |
|---|---|
| Genre match | +2.0 (binary) |
| Mood match | +1.0 (binary) |
| Energy similarity | `2.0 × (1 - abs(song.energy - target))` → 0–2.0 |

## Phase 4 Plan

Adding Claude API integration in layers:

1. **Natural language preference extraction** — user types freeform query, Claude parses it into `{genre, mood, energy}` JSON, existing scoring runs unchanged
2. **Claude-generated explanations** — rich natural language explanation per recommendation instead of raw score labels
3. **Output guardrails + retry** — validate Claude's JSON against expected schema, retry once on malformed output, warn when user preference has no catalog match
4. **Eval script** — `tests/test_eval.py` runs predefined NL queries, checks extracted preferences match expected values

## Key Files

```
src/
  main.py          # CLI runner — uses functional API
  recommender.py   # Core scoring logic (complete)
data/
  songs.csv        # 20-song catalog
tests/
  test_recommender.py  # Unit tests for OOP API
```
