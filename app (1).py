
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

st.set_page_config(page_title="Netflix Recommender", page_icon="🎬")

@st.cache_resource
def load_model():
    df = pd.read_csv("netflix_titles.csv")
    df["content"] = (
        df["listed_in"].fillna("") + " " +
        df["description"].fillna("")
    )

    tfidf = TfidfVectorizer(stop_words="english")
    matrix = tfidf.fit_transform(df["content"])

    model = NearestNeighbors(metric="cosine", algorithm="brute")
    model.fit(matrix)

    return df, matrix, model

df, matrix, model = load_model()

st.title("🎬 Netflix Recommendation System")
st.write("Find Netflix titles similar to your favourites!")

title = st.selectbox("Choose a Netflix title:", sorted(df["title"].unique()))

if st.button("Recommend"):
    idx = df[df["title"] == title].index[0]
    distances, indices = model.kneighbors(matrix[idx], n_neighbors=6)

    st.subheader("Recommended Titles")

    for i in indices[0][1:]:
        st.write("🍿", df.iloc[i]["title"])
