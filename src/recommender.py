import csv
from pathlib import Path
from typing import List, Dict, Tuple
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


# ---------------------------------------------------------------------------
# Scoring rules (energy is on a 0–1 scale, so thresholds are 0.10 / 0.20)
#   +2.0  genre matches favorite_genre
#   +1.0  mood  matches favorite_mood
#   +1.0  |energy - target| <= 0.10   ("within ±1" scaled to 0-1 range)
#   +0.5  |energy - target| <= 0.20   ("within ±2" scaled to 0-1 range)
# ---------------------------------------------------------------------------

def _compute_score(
    genre: str, mood: str, energy: float,
    target_genre: str, target_mood: str, target_energy: float,
) -> Tuple[float, str]:
    """Return (score, explanation) for a single song against user preferences."""
    score = 0.0
    reasons: List[str] = []

    if genre == target_genre:
        score += 2.0
        reasons.append(f"genre matches '{target_genre}'")

    if mood == target_mood:
        score += 1.0
        reasons.append(f"mood matches '{target_mood}'")

    energy_diff = abs(energy - target_energy)
    if energy_diff <= 0.10:
        score += 1.0
        reasons.append("energy is a close match")
    elif energy_diff <= 0.20:
        score += 0.5
        reasons.append("energy is a near match")

    explanation = (
        "Recommended because: " + ", ".join(reasons)
        if reasons
        else "No strong match, but included by ranking"
    )
    return score, explanation


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Return (score, reasons) reflecting how well a song matches user preferences."""
    score: float = 0.0
    reasons: List[str] = []

    # Categorical features
    if song["genre"] == user_prefs["favorite_genre"]:
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"] == user_prefs["favorite_mood"]:
        score += 1.5
        reasons.append("mood match (+1.5)")

    # Numerical features
    energy_score = max(0.0, 2.0 - abs(song["energy"] - user_prefs["target_energy"]))
    score += energy_score
    reasons.append(f"energy similarity (+{energy_score:.2f})")

    if "target_tempo_bpm" in user_prefs:
        tempo_score = max(0.0, 1.0 - abs(song["tempo_bpm"] - user_prefs["target_tempo_bpm"]) / 30.0)
        score += tempo_score
        reasons.append(f"tempo similarity (+{tempo_score:.2f})")

    return score, reasons


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top-k songs sorted by score (highest first)."""
        scored = [
            (
                _compute_score(
                    s.genre, s.mood, s.energy,
                    user.favorite_genre, user.favorite_mood, user.target_energy,
                )[0],
                s,
            )
            for s in self.songs
        ]
        scored.sort(key=lambda x: x[0], reverse=True)
        return [song for _, song in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Return a human-readable explanation for why a song was recommended."""
        _, explanation = _compute_score(
            song.genre, song.mood, song.energy,
            user.favorite_genre, user.favorite_mood, user.target_energy,
        )
        return explanation


def load_songs(csv_path: str) -> List[Dict]:
    """Parse a songs CSV file and return a list of dicts with typed numeric fields."""
    songs: List[Dict] = []
    with open(Path(csv_path), newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id":           int(row["id"]),
                "title":        row["title"],
                "artist":       row["artist"],
                "genre":        row["genre"],
                "mood":         row["mood"],
                "energy":       float(row["energy"]),
                "tempo_bpm":    int(row["tempo_bpm"]),
                "valence":      float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })
    return songs


def recommend_songs(
    user_prefs: Dict, songs: List[Dict], k: int = 5
) -> List[Tuple[Dict, float, List[str]]]:
    """Score all songs against user preferences and return the top-k ranked results."""
    # Score every song — list comprehension keeps this concise and readable
    scored = [
        (song, *score_song(user_prefs, song))  # unpacks (score, reasons) inline
        for song in songs
    ]

    # sorted() is preferred here: it returns a NEW list and leaves `scored` intact.
    # list.sort() would mutate `scored` in-place and return None — fine if you
    # don't need the unsorted version again, but sorted() is safer and clearer.
    ranked = sorted(scored, key=lambda x: x[1], reverse=True)

    # Slice to the top-k results
    return ranked[:k]
