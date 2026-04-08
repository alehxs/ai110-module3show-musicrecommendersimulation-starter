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

## Architecture

This is a Python simulation project with two parallel API styles in `src/recommender.py`:

1. **OOP style** — `Song` (dataclass), `UserProfile` (dataclass), `Recommender` class with `recommend(user, k)` and `explain_recommendation(user, song)` methods. Used by tests via `from src.recommender import ...`.

2. **Functional style** — `load_songs(csv_path)` and `recommend_songs(user_prefs, songs, k)`. Used by `src/main.py` via `from recommender import ...` (note: no `src.` prefix since main.py runs as a module under `src/`).

The song catalog lives in `data/songs.csv` with columns: `id, title, artist, genre, mood, energy, tempo_bpm, valence, danceability, acousticness`.

Most functions in `src/recommender.py` are stubs marked `# TODO` — the core task is implementing the scoring logic.
