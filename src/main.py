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

    profiles = [
        {"name": "Pop Fan",       "genre": "pop",  "mood": "happy", "energy": 0.55, "likes_acoustic": False, "target_tempo": 120},
        {"name": "Lofi Studier",  "genre": "lofi", "mood": "chill", "energy": 0.35, "likes_acoustic": True,  "target_tempo": 80},
        {"name": "Hype Workout",  "genre": "edm",  "mood": "hype",  "energy": 0.90, "likes_acoustic": False, "target_tempo": 140},
    ]

    for user_prefs in profiles:
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print(f"\n{'=' * 40}")
        print(f"Profile: {user_prefs['name']}")
        print("=" * 40)
        for i, rec in enumerate(recommendations, 1):
            song, score, explanation = rec
            print(f"\n{i}. {song['title']} — {song['artist']}")
            print(f"   Score  : {score:.2f}")
            print(f"   Because: {', '.join(explanation) or 'no matching preferences'}")


if __name__ == "__main__":
    main()
