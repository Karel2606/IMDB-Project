# IMDB Top 50 Actors Web-App with Streamlit

This is a Streamlit web application that displays an IMDb dataset in a Master-Detail-View format, 
with actor names in the master column and all of the movies of the actors in the details view.

## Requirements

- Python 3.x
- Streamlit (1.10 or higher)
- pandas
- plotly

## Setup

1. Clone or download the repository
2. In your Anaconda or code editor environment install requried packages running: 
    pip install streamlit
    pip install pandas
    pip install plotly

3. To test if setup works:
    streamlit hello

4. Run streamlit app localy in Browser (served at http://localhost:8501/):
    streamlit run Homepage.py 

## Usage

1. Select an actor from the sidebar
2. The app will display a dataframe of all the movies of the selected actor an other details about the actor
3. Second Page can be selected in the left upper corner to see charts

The relativ paths are in Windows format with "\\". When you run this on 
Linux or Mac-OS replace it with "/"