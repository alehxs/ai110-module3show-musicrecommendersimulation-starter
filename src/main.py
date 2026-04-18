"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

import os
from recommender import load_songs, recommend_songs

_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main() -> None:
    songs = load_songs(os.path.join(_PROJECT_ROOT, "data", "songs.csv"))
    print(f"Loaded songs: {len(songs)}")

    # Taste profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.55, "likes_acoustic": False, "target_tempo": 120}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop Recommendations")
    print("=" * 40)
    for i, rec in enumerate(recommendations, 1):
        song, score, explanation = rec
        print(f"\n{i}. {song['title']} — {song['artist']}")
        print(f"   Score  : {score:.2f}")
        print(f"   Because: {', '.join(explanation) or 'no matching preferences'}")


if __name__ == "__main__":
    main()
