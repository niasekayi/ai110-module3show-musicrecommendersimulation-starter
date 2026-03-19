"""
Command line runner for the Music Recommender Simulation.

Run with:
    python -m src.main
"""

from recommender import load_songs, recommend_songs


def print_recommendations(recommendations: list, profile_label: str) -> None:
    """Print a ranked list of song recommendations with scores and reasons."""

    # Header — describes which user profile generated these results
    print(f"\n{'=' * 52}")
    print(f"  Top Song Recommendations ({profile_label})")
    print(f"{'=' * 52}")

    for rank, (song, score, reasons) in enumerate(recommendations, start=1):
        # Rank + title + score on one line
        print(f"\n  #{rank}  {song['title']}  —  Score: {score:.2f}")
        print(f"       Artist: {song['artist']}  |  Genre: {song['genre']}  |  Mood: {song['mood']}")

        # Reasons printed as indented bullet points
        print("       Why matched:")
        for reason in reasons:
            print(f"         • {reason}")

    # Footer separator
    print(f"\n{'=' * 52}\n")


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded {len(songs)} songs.")

    # User profile — keys must match what score_song() expects
    user_prefs = {
        "favorite_genre": "Pop",
        "favorite_mood":  "Happy",
        "target_energy":  0.8,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    # Build a readable label from the profile for the header
    profile_label = f"{user_prefs['favorite_genre']} / {user_prefs['favorite_mood']} Profile"
    print_recommendations(recommendations, profile_label)


if __name__ == "__main__":
    main()
