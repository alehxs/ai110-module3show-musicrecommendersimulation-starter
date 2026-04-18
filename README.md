# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

VibeFinder 1.0 scores every song in a 20-song catalog against a user's preferred genre, mood, and energy level, then returns the top matches with a plain-English explanation of why each song was picked. It is a content-based recommender with no user history or collaboration involved.

---

## How The System Works

Explain your design in plain language.
- Real-world recommendation systems are almost always a hybrid of content-based and collaboration filtering. 

  Content-based filterting recommends items by computing similarity between attributes and user preferences. The system learns what features a user likes, then finds similar items. No other users involved

  Collaborative Filtering recommends items by computing similarity between users based on their history. Then recommends items liked by similar users, that the user has not yet encountered.

Some prompts to answer:

- What features does each `Song` use in your system (For example: genre, mood, energy, tempo)
  - Each song has 
    - Categorical features (```genre```, ```mood```)
    - Continuous features with numerical values in [0,1] (```energy```, ```valence```, ```danceability```, ```acousticness```)
    - Continuous features on a raw scale (```tempo_bpm```, measured in beats per minute, ranging from 60–152)
- What information does your `UserProfile` store
  - My UserProfile stores 2 strings: favorite_genre and favorite_mood, a target_energy float, and a likes_acoustic bool

- How does your `Recommender` compute a score for each song
  - For each song, it adds up 3 weighted sub-scores. The max possible score is 5.0.
- How do you choose which songs to recommend
  - After every song is scored:
    - 1. Sort all the songs by score descending (highest match first)
    - 2. Take the top k (default: 5) from the sorted list.

### Algorithm Recipe

| Signal | Type | Points |
|---|---|---|
| Genre match | Binary | +2.0 if `song.genre == favorite_genre`, else 0 |
| Mood match | Binary | +1.0 if `song.mood == favorite_mood`, else 0 |
| Energy similarity | Continuous | `2.0 × (1.0 - abs(song.energy - target_energy))` → 0 to 2.0 |

**Max score: 5.0**

Energy was scaled to 0–2.0 (instead of 0–1.0) so it can meaningfully compete with the binary matches. Without this, a perfect genre+mood match with completely wrong energy (3.1 pts) would always beat a genre match with perfect energy (3.0 pts).

### Potential Biases

- **Genre over-dominance** — the +2.0 bonus means the right genre almost always wins, even if energy feels completely wrong. Similar genres (e.g. indie pop vs. pop) get zero credit.
- **Mood label coarseness** — mood is a coarse human-assigned tag; two "happy" songs can feel very different, and a song with a different label but matching energy might suit the user just as well.
- **No diversity** — the system always returns the closest matches, never exposing the user to anything outside their stated preferences.

```
songs.csv  →  load_songs()  →  [Song, Song, ...]
                                       ↓
UserProfile  ────────────────→  score(song, user)  [max 5.0]
                                       ↓
                              sort by score (desc)
                                       ↓
                              top k recommendations
```

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

**Weight shift:** Halved the genre weight (2.0 to 1.0) and doubled the energy weight (2.0 to 4.0). The Pop Fan list became more genre-diverse — a latin pop song broke into the top 3 that was not there before. The Hype Workout list barely changed because "edm" does not exist in the catalog at all, so weight adjustments had nothing to amplify.

**Adversarial profiles:** Tested 5 edge case profiles including a mood that does not exist in the catalog ("sad"), a genre that does not exist ("edm"), a contradictory preference (intense lofi), and a negative k value. The biggest finding was that the system never tells the user when their preference is missing — it just silently ranks by whatever signals do exist and returns confident-looking results anyway.

---

## Limitations and Risks

- The catalog only has 20 songs across 15 genres, so most genres have just one representative. Meaningful variety is basically impossible for most user types.
- The genre weight is so strong that users whose genre exists in the catalog always get genre-anchored results, while users whose genre is missing get something close to random.
- The system does not warn the user when their mood or genre preference has no match. It silently ignores missing preferences.
- Passing k=-1 returns 19 songs instead of raising an error, because Python list slicing does not treat negative values as invalid.

See [model_card.md](model_card.md) for a deeper breakdown.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Building this made it clear that a recommender does not need to be complex to feel like it is working. Three weighted signals and a sort is enough to produce results that look reasonable most of the time. The problem is that "looks reasonable" and "actually matched what the user wanted" are not the same thing, and a small system like this has no way to tell the difference.

The bias piece was more surprising. The genre weight was set to 2.0 to give it enough influence, but that decision quietly turned genre into the dominant factor in nearly every result. It was not intentional, but it means the system basically treats genre as the most important thing about a person's taste — which is not true for everyone. Real recommender systems make the same kind of hidden value decisions at a much larger scale, which is easy to miss when the results still feel plausible.


---
