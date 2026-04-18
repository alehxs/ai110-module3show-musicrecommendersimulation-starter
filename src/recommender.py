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

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        def score(song: Song) -> float:
            genre_pts = 2.0 if song.genre == user.favorite_genre else 0.0
            mood_pts = 1.0 if song.mood == user.favorite_mood else 0.0
            energy_pts = 2.0 * (1.0 - abs(song.energy - user.target_energy))
            return genre_pts + mood_pts + energy_pts

        return sorted(self.songs, key=score, reverse=True)[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

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

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    def score(song: Dict) -> float:
        genre_pts = 2.0 if song["genre"] == user_prefs["genre"] else 0.0
        mood_pts = 1.0 if song["mood"] == user_prefs["mood"] else 0.0
        energy_pts = 2.0 * (1.0 - abs(song["energy"] - user_prefs["energy"]))
        return genre_pts + mood_pts + energy_pts

    scored = [(song, score(song), "") for song in songs]
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:k]
