# Music Recommender — Data Flow

```mermaid
flowchart TD
    A["🎧 Input: User Preferences\ngenre · mood · target_energy"]

    A --> B["load_songs()\nParse songs.csv → List of Dicts"]

    B --> C["📋 Song List\n18 songs loaded into memory"]

    C --> D["🔁 Loop: For Each Song\n_compute_score(song, user_prefs)"]

    D --> E{"genre ==\nfavorite_genre?"}
    E -- "✅ Yes" --> F["+ 2.0 pts"]
    E -- "❌ No"  --> G["+ 0.0 pts"]

    F --> H{"mood ==\nfavorite_mood?"}
    G --> H

    H -- "✅ Yes" --> I["+ 1.0 pts"]
    H -- "❌ No"  --> J["+ 0.0 pts"]

    I --> K{"| energy − target |\n≤ 0.10?"}
    J --> K

    K -- "✅ Yes"  --> L["+ 1.0 pts\n(close match)"]
    K -- "❌ No"   --> M{"| energy − target |\n≤ 0.20?"}

    M -- "✅ Yes"  --> N["+ 0.5 pts\n(near match)"]
    M -- "❌ No"   --> O["+ 0.0 pts"]

    L --> P["Accumulate Score\nBuild Explanation String"]
    N --> P
    O --> P

    P --> Q{"More songs\nin list?"}
    Q -- "Yes" --> D
    Q -- "No"  --> R["Sort Descending\nby Score"]

    R --> S["Slice top K results"]

    S --> T["🏆 Output: Top-K Recommendations\n(song_dict, score, explanation)"]
```

## Score Breakdown Table

| Rule | Points |
|---|---|
| Genre matches `favorite_genre` | +2.0 |
| Mood matches `favorite_mood` | +1.0 |
| \|energy − target\| ≤ 0.10 | +1.0 |
| \|energy − target\| ≤ 0.20 | +0.5 |
| No match on any criterion | 0.0 |
| **Max possible score** | **4.0** |

## Trace Example

User prefs: `genre="pop"`, `mood="happy"`, `energy=0.8`

| Song | Genre | Mood | Energy | Score | Why |
|---|---|---|---|---|---|
| Sunrise City | pop ✅ | happy ✅ | 0.82 ✅ | **4.0** | all three match |
| Rooftop Lights | indie pop ❌ | happy ✅ | 0.76 ✅ | **2.0** | mood + energy near |
| Gym Hero | pop ✅ | intense ❌ | 0.93 ❌ | **2.0** | genre only |
| Block by Block | hip-hop ❌ | confident ❌ | 0.80 ✅ | **1.0** | energy close match |
