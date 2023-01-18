import streamlit as st
import pandas as pd
from Homepage import actorsDf, moviesDf
import plotly.express as px

st.title("Charts of Movie and Actor Data 📊")

st.header("Top 10 Actors by winning Awards")
topActors = actorsDf.sort_values("Winnig Awards", ascending=False).head(10)
#awardsFig = topActors.plot.bar(x="Actor Names", y="Winnig Awards")
awardsFig = px.bar(x=topActors["Actor Names"], y=topActors["Winnig Awards"])
# set the labels
awardsFig.update_layout(title='Top 10 Actors by Number of Awards',
                  xaxis_title='Actor',
                  yaxis_title='Number of Awards')

st.plotly_chart(awardsFig)

st.header("Top 10 Years, where the most movies were released")
topYears = moviesDf.groupby(by=["Year"])["Title"].count()
topYears = topYears.sort_values(ascending=False).head(10)
yearsFig = px.bar(topYears)
yearsFig.update_layout(title='Top 10 Years number of released movies',
                  xaxis_title='Year',
                  yaxis_title='Movies released')

st.plotly_chart(yearsFig)