1. Model Name

VibeMatch 1.0

2. Intended Use

This recommender system suggests songs based on a user’s preferred genre, mood, and energy level. It returns the top 5 songs from a small dataset that best match those preferences.

The system assumes that users have clear preferences, such as one main genre and mood. It is designed for classroom exploration and learning, not for real-world use.

3. How the Model Works

The model compares user preferences to song features and assigns a score to each song.

Each song includes a genre, mood, energy value, and tempo.

The user provides a favorite genre, favorite mood, and a target energy level.

The system adds points when the genre matches and when the mood matches. It also calculates how close the song’s energy is to the user’s target and includes tempo similarity as an additional factor.

All of these values are combined into a final score, and the songs are ranked from highest to lowest.

I also added tempo into the scoring and adjusted the weights to make the recommendations more balanced.

4. Data

The dataset contains 18 songs stored in songs.csv.

It includes genres such as pop, rock, lofi, edm, indie pop, and ambient. It also includes moods like happy, chill, intense, and melancholic.

The dataset is small and does not represent all types of music, so it reflects a limited range of musical taste.

5. Strengths

The system works well when user preferences are clear and consistent.

For example, the High-Energy Pop and Chill Lofi profiles produced results that felt accurate and intuitive.

The scoring system does a good job combining multiple features, especially energy and tempo. It is also easy to understand why a song was recommended because the output clearly explains each part of the score.

6. Limitations and Bias

The system has several limitations.

The dataset is small, which means recommendations can repeat and lack variety. It relies on exact matching, which can cause issues with capitalization or formatting.

Some genres may appear more often than others, which can bias the results. The system also struggles when user preferences conflict, such as high energy with a calm mood.

There is no input validation, so missing or incorrect values can cause errors. Because of these issues, some users may get better recommendations than others depending on how well their preferences match the dataset.

7. Evaluation

I tested the system using multiple profiles, including High-Energy Pop, Chill Lofi, and Deep Intense Rock.

The results were mostly accurate when the preferences aligned well with the dataset. Songs that matched both genre and mood with similar energy consistently ranked highest.

One thing I noticed was that some songs appeared across multiple profiles, especially when their energy and tempo were close to the target. This shows that the system sometimes prioritizes numerical similarity over genre differences.

Overall, the system works well for simple cases but is sensitive to how user preferences are defined.

8. Future Work

If I had more time, I would improve the system by adding input validation and normalizing text inputs so things like capitalization do not affect results.

I would also expand the dataset with more songs and include additional features such as lyrics or artist similarity. Improving diversity in recommendations and adding feedback when preferences cannot be satisfied would also make the system more realistic.

9. Personal Reflection

This project helped me understand how recommender systems actually work and how they turn data into decisions. Even simple systems can produce realistic results, but they are very sensitive to how they are designed.

What surprised me most was how often the same songs appeared across different profiles. It showed me that the system is not truly understanding music, it is just matching patterns in the data.

This changed how I think about real music apps, because now I understand that recommendations depend heavily on the dataset and scoring rules, which can introduce bias or limit what users see.