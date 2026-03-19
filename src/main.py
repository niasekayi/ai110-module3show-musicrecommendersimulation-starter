"""
Command line runner for the Music Recommender Simulation.

Run with:
    python -m src.main
"""

from recommender import load_songs, recommend_songs


# ---------------------------------------------------------------------------
# User profiles — each dict represents a listener's taste preferences.
# Keys must match what score_song() reads.
# ---------------------------------------------------------------------------
PROFILES = [
    {
        "name":           "High-Energy Pop",
        "favorite_genre": "pop",
        "favorite_mood":  "happy",
        "target_energy":  0.90,
        "target_tempo_bpm": 128,
    },
    {
        "name":           "Chill Lofi",
        "favorite_genre": "lofi",
        "favorite_mood":  "chill",
        "target_energy":  0.35,
        "target_tempo_bpm": 75,
    },
    {
        "name":           "Deep Intense Rock",
        "favorite_genre": "rock",
        "favorite_mood":  "intense",
        "target_energy":  0.92,
        "target_tempo_bpm": 150,
    },
]


def print_recommendations(recommendations: list, profile_name: str) -> None:
    """Print a ranked list of song recommendations with scores and reasons."""
    width = 56

    # Profile header block
    print(f"\n{'#' * width}")
    print(f"  PROFILE: {profile_name}")
    print(f"{'#' * width}")

    for rank, (song, score, reasons) in enumerate(recommendations, start=1):
        # Rank line: number, title, score
        print(f"\n  #{rank}  {song['title']}  —  Score: {score:.2f}")
        print(f"  {'─' * (width - 4)}")
        print(f"     Artist : {song['artist']}")
        print(f"     Genre  : {song['genre']}   |   Mood: {song['mood']}")
        print(f"     Energy : {song['energy']}  |   BPM:  {song['tempo_bpm']}")

        # Match reasons as bullet points
        print(f"     Why matched:")
        for reason in reasons:
            print(f"       • {reason}")

    print(f"\n{'─' * width}\n")


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"\nLoaded {len(songs)} songs from dataset.")
    print(f"Running recommendations for {len(PROFILES)} profiles...\n")

    # Loop through each profile, score all songs, print top 5
    for profile in PROFILES:
        # Separate the display name before passing prefs to recommender
        name = profile["name"]
        prefs = {k: v for k, v in profile.items() if k != "name"}

        recommendations = recommend_songs(prefs, songs, k=5)
        print_recommendations(recommendations, name)


if __name__ == "__main__":
    main()
