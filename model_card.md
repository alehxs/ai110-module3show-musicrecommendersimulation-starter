# Model Card: VibeFinder 1.0

## 1. Model Name

VibeFinder 1.0

---

## 2. Goal / Task

VibeFinder takes a user's preferred genre, mood, and energy level and returns the top songs from the catalog that best match those preferences. It also explains why each song was recommended in plain English.

---

## 3. Data Used

The catalog has 20 songs. Each song has a genre, mood, energy level (0 to 1), tempo, valence, danceability, and acousticness. There are 15 different genres but most of them only have one song. Pop has the most with 4 songs. The mood options in the dataset are happy, intense, moody, chill, and relaxed. A lot of moods people might actually want (like sad, angry, or melancholic) are not in the dataset at all.

---

## 4. Algorithm Summary

Each song gets a score based on three things:

- **Genre match:** If the song's genre matches what the user wants, it gets 2 points. If not, 0.
- **Mood match:** If the mood matches, it gets 1 point. If not, 0.
- **Energy match:** Songs closer in energy to the user's preference score higher. A perfect energy match gives 2 points, and the score drops gradually the further away it is.

The three scores are added together (max possible is 5.0) and the top results are returned.

---

## 5. Observed Behavior / Biases

Genre match is worth 2 points, which makes it the strongest signal by far. This means a song in the right genre with bad energy will often beat a song in the wrong genre with perfect energy and a mood match. That feels wrong for users who care more about mood than genre.

The bigger issue is that the system has no way to tell the user when their preference does not exist in the catalog. If someone asks for "sad" or "edm" songs, neither exists in the dataset. The system just skips those preferences and ranks by whatever does match, without any warning. The recommendations still look plausible on the surface, which makes it easy to miss that the system never actually found what was asked for.

---

## 6. Evaluation Process

Five adversarial profiles were tested to look for edge cases:

1. A user asking for a mood ("sad") that does not exist in the catalog. The system returned pop songs ranked by energy with no warning about the missing mood.
2. A contradictory profile (intense lofi) where the genre and mood don't usually go together. Results were scattered across genres.
3. A k=-1 input, which caused Python's slice behavior to return 19 songs instead of erroring.
4. A folk/relaxed/low-energy user. This one actually worked well because the catalog has a matching folk song with a relaxed mood.
5. A tie-breaking case with synthwave where two songs had the same score, to see how ordering was handled.

A weight-shift experiment was also run: genre weight was halved (2.0 to 1.0) and energy weight was doubled (2.0 to 4.0). The Pop Fan list became more diverse in genre, which felt more accurate. The Hype Workout list barely changed because neither the genre nor mood existed in the catalog regardless of weights.

---

## 7. Intended Use and Non-Intended Use

**Intended use:** This is a classroom simulation for learning how scoring-based recommenders work. It is good for exploring how weight choices affect results and how missing data creates silent failures.

**Not intended for:** Real music recommendations, any situation where users expect coverage of their full taste, or anything that needs to scale beyond a small catalog. It should not be used to make product decisions or as an example of a production-ready system.

---

## 8. Ideas for Improvement

1. Add a warning when the user's requested genre or mood does not exist in the catalog, instead of silently falling back.
2. Grow the catalog significantly. With only 1 song per genre for most genres, variety in results is basically impossible for most user types.
3. Validate that k is a positive integer before slicing, so bad inputs fail clearly instead of returning unexpected results.

---

## 9. Personal Reflection

The biggest thing I learned is how much a weight choice is actually a values decision. Setting genre to 2 points and mood to 1 point sounds like a neutral math choice, but it is really saying the system thinks genre matters twice as much as mood. Nobody wrote that rule intentionally but it shapes every result.

AI tools helped a lot with running experiments quickly and catching edge cases I would not have thought to test on my own, like the k=-1 slice bug. But I had to double-check the explanations because the output always looked reasonable even when the system was clearly not doing what I asked. That is the part that surprised me most: a simple algorithm can return confident-looking results even when it has completely ignored the user's actual preference.

If I kept working on this, the first thing I would do is add more songs so users who like less common genres actually get meaningful recommendations instead of a random energy-ranked list.
