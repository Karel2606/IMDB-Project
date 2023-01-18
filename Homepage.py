import streamlit as st
import pandas as pd

# loading csv files from web scraped data of IMDB ( relativ path for windows)
actorsDf = pd.read_csv(".\\data\\top50Actors.csv")
moviesDf = pd.read_csv(".\\data\\moviesOfActors.csv")
actorsDf.index = actorsDf["Ranking"]

st.set_page_config(
    page_title="Top 50 Actors 📽️🍿",
    page_icon="📽️"
)
st.title("Top 50 Actors 📽️🍿")

topActor = pd.DataFrame()
topActors = actorsDf[["Ranking", "Actor Names"]]
actorRankingSelected = st.sidebar.selectbox("Select Actor for Details:", topActors)

# sidebar for master-detail view to select actor and get all movie details
st.sidebar.dataframe(topActors[["Ranking", "Actor Names"]])

moviesOfActorSelected = pd.DataFrame()
moviesOfActorSelected = moviesDf[moviesDf["Actor Ranking"] == actorRankingSelected]
actorSelected = actorsDf["Actor Names"].loc[actorRankingSelected]

st.header(f"{actorRankingSelected}. {actorSelected}")
# display mini bio section
st.subheader("Mini Bio 📝:")
st.caption(actorsDf["About"].loc[actorRankingSelected])

# diplay winnig Awards
awards = actorsDf["Winnig Awards"].loc[actorRankingSelected]
st.subheader(f"Winning Awards 🏆: {awards}")

# display Average Rating of all Movies
avgRating = moviesOfActorSelected["Rating"].mean()
avgRating = round(avgRating, 1)
st.subheader(f"Average Rating of all Movies ⭐: {avgRating}")
st.progress(avgRating/10)

# display Top 5 rated Movies
st.subheader("Top 5 Movies (sorted by IMDB-Rating)")
# rendering a dataframe as an interactive table (sorting on every column possible!)
st.dataframe(moviesOfActorSelected[["Title", "Year", "Genre", "Rating"]].sort_values("Rating", ascending=False).head(5))

# display all movies of selected actor
st.subheader(f"All Movies of {actorSelected} (sorted by popularity)")
st.dataframe(moviesOfActorSelected[["Title", "Year", "Genre", "Rating"]])