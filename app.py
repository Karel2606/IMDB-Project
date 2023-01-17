import streamlit as st
import pandas as pd

# loading csv files from web scraped data of IMDB ( relativ path for windows)
actorsDf = pd.read_csv(".\\data\\top50Actors.csv")
moviesDf = pd.read_csv(".\\data\\moviesOfActors.csv")
actorsDf.index = actorsDf["Ranking"]
st.title("Top 50 Actors 📽️🍿")

topActors = actorsDf[["Ranking", "Actor Names"]].head(10)

st.dataframe(topActors)