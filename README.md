# 🎬 Netflix Content-Based Recommendation System

## 📌 Project Overview
The Netflix Content-Based Recommendation System recommends movies and TV shows similar to a title selected by the user.

It uses content-based filtering techniques to identify similar titles based on genres and descriptions.

## 🎯 Objectives
- Recommend similar Netflix movies and TV shows.
- Help users discover content based on their interests.
- Provide a simple and interactive recommendation interface.

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- Streamlit

## 📂 Dataset
The project uses the Netflix Movies and TV Shows dataset containing information such as:
- Title
- Type
- Director
- Cast
- Release Year
- Genre
- Description

## ⚙️ How It Works
1. Load the Netflix dataset.
2. Combine genre and description information.
3. Convert text into numerical features using TF-IDF.
4. Calculate similarity between titles.
5. Recommend the five most similar titles.

## 🚀 Live Application
**Try the application here:**

https://netflix-content-recommender.streamlit.app/

## ▶️ Run Locally
Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run "app (1).py"
```

Make sure the Netflix dataset CSV file is in the same folder as the application.

## 📊 Project Result
The application successfully recommends five similar Netflix titles based on the selected title.

## 👩‍💻 Author
Harika Nakka

## 📌 Future Improvements
- Add user preference-based recommendations.
- Improve recommendation accuracy.
- Add filters for genre, release year, and content type.
- Develop a more personalized user experience.
