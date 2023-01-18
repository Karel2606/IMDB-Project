import streamlit as st
import pandas as pd

# loading csv files from web scraped data of IMDB ( relativ path for windows)
actorsDf = pd.read_csv(".\\data\\top50Actors.csv")
moviesDf = pd.read_csv(".\\data\\moviesOfActors.csv")
actorsDf.index = actorsDf["Ranking"]
st.title("Top 50 Actors 📽️🍿")

topActor = pd.DataFrame()
topActors = actorsDf[["Ranking", "Actor Names"]]
actorRankingSelected = st.sidebar.selectbox("Select Actor for Details:", topActors)

st.sidebar.dataframe(topActors[["Ranking", "Actor Names"]])
# rendering a dataframe as an interactive table (sorting on every column possible!)
moviesOfActorSelected = pd.DataFrame()
moviesOfActorSelected = moviesDf[moviesDf["Actor Ranking"] == actorRankingSelected]
# display all movies of selected actor
actorSelected = actorsDf["Actor Names"].loc[actorRankingSelected]
st.subheader(f"All Movies of {actorSelected}")
st.dataframe(moviesOfActorSelected[["Title", "Year", "Genre", "Rating"]])