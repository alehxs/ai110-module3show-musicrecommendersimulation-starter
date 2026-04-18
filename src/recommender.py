from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

def _format_points(pts: float) -> str:
    """Format a score delta as a signed string, e.g. +2."""
    return f"+{pts:g}"

def _score_with_reasons(genre: str, mood: str, energy: float,
                        pref_genre: str, pref_mood: str, pref_energy: float
                        ) -> Tuple[float, List[str]]:
    """Return (total_score, reason_labels) for a song against user preferences."""
    components = [
        ("genre match",  2.0 if genre == pref_genre else 0.0),
        ("mood match",   1.0 if mood  == pref_mood  else 0.0),
        ("energy match", round(2.0 * (1.0 - abs(energy - pref_energy)), 2)),
    ]
    total   = sum(pts for _, pts in components)
    reasons = [f"{label} ({_format_points(pts)})" for label, pts in components if pts > 0]
    return total, reasons

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        return sorted(
            self.songs,
            key=lambda song: _score_with_reasons(
                song.genre, song.mood, song.energy,
                user.favorite_genre, user.favorite_mood, user.target_energy
            )[0],
            reverse=True,
        )[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        _, reasons = _score_with_reasons(
            song.genre, song.mood, song.energy,
            user.favorite_genre, user.favorite_mood, user.target_energy,
        )
        return ", ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    import csv

    int_fields = {"id", "tempo_bpm"}
    float_fields = {"energy", "valence", "danceability", "acousticness", "loudness", "instrumentalness", "speechiness"}

    songs = []
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            song = {k.strip(): v.strip() for k, v in row.items()}

            for field in int_fields:
                if field in song:
                    song[field] = int(song[field])

            for field in float_fields:
                if field in song:
                    song[field] = float(song[field])

            songs.append(song)
            
    return songs

def score_song(song: Dict, user_prefs: Dict) -> Tuple[float, List[str]]:
    """Score a single song dict against user preference dict."""
    return _score_with_reasons(
        song["genre"], song["mood"], song["energy"],
        user_prefs["genre"], user_prefs["mood"], user_prefs["energy"],
    )

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, List[str]]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    all_scored = [(song, *score_song(song, user_prefs)) for song in songs]
    return sorted(all_scored, key=lambda x: x[1], reverse=True)[:k]
