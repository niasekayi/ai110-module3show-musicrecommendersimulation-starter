Project Summary

In this project, I built a simple music recommender system that suggests songs based on a user’s preferences. The system takes in features like genre, mood, and energy level, then scores each song to find the best matches.

This project helped me understand how recommender systems actually work behind the scenes, including how small design choices (like weights and features) can impact results in big ways.

How The System Works

The recommender compares a user’s preferences to song data and assigns a score to each song.

Song Features

Each song includes:

Genre (pop, rock, lofi, etc.)

Mood (happy, calm, energetic, etc.)

Energy (a value between 0 and 1)

(Optional) tempo or valence (used in experiments)

User Profile

Each user provides:

Favorite genre

Favorite mood

Target energy

Scoring Logic

Each song gets a score based on:

Genre match , adds points

Mood match , adds points

Energy difference. closer = higher score

Recommendation Process

Score all songs

Sort by score (highest first)

Return top 5 recommendations

System Evaluation

I tested the system using both normal and adversarial user profiles.

What Felt Accurate

For clear profiles like “High-Energy Pop,” results generally matched expectations.

Songs with matching genre and similar energy consistently ranked highest.

What Was Surprising

The same songs sometimes appeared across different profiles.

Genre often dominated the score, even when energy was a closer match.

Some recommendations looked correct but were actually fallback results (like when the genre didn’t exist in the dataset).

Key Insight

The system works best when user preferences are clear and realistic, but struggles when preferences conflict or fall outside the dataset.

Experiments You Tried

During development, I tested different changes to understand how the system behaves.

Adjusted Genre Weight (2.0 → 0.5)

Lowering the genre weight made the system rely more on energy.

 Results became more diverse but sometimes less relevant.

Added Features (Tempo / Valence)

Adding more features slightly improved personalization.

Helped differentiate similar songs, but impact was limited due to small dataset.

Different User Profiles

Tested:

High-energy users

Chill/lofi users

Intense rock users

 Worked well for clear preferences, struggled with conflicting ones.

Adversarial Testing

Tested edge cases like:

Case sensitivity (“Pop” vs “pop”)

Nonexistent genres

Conflicting preferences

Missing fields

 Revealed issues like:

Incorrect scoring

Ignored preferences

Runtime errors

Limitations and Risks

This system works for basic scenarios, but has several limitations:

Small Dataset
Limited variety leads to repeated recommendations.

No Understanding of Context
Only uses metadata, not lyrics or meaning.

Case Sensitivity Issues
Exact matching can break results.

No Input Validation
Missing or invalid inputs can cause crashes.

Bias in Scoring
Certain features (like genre) can dominate results.

No Feedback to Users
Users aren’t told when preferences can’t be satisfied.

Not Scalable
Would need major improvements for real-world use.

Reflection

This project showed me that recommender systems aren’t actually “smart”, they’re just applying rules to data. Small changes in weights or features can completely change the results, which makes them very sensitive to design choices.

It also made me realize how bias can show up easily. If the dataset is unbalanced or the scoring favors certain features, some users will get better recommendations than others. In real-world systems, this could affect what content people see and even shape their preferences over time.

