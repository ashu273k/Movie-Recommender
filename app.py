import streamlit as st
import pickle
import requests
import os

# Get API key from environment variable or Streamlit secrets
TMDB_API_KEY = os.getenv('TMDB_API_KEY') or st.secrets.get("TMDB_API_KEY", "")

def fetch_poster(movie_id):
   response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}')
   data = response.json()
   if 'poster_path' in data and data['poster_path']:
       return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
   return "https://via.placeholder.com/500x750?text=No+Poster"

movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = movies_dict
movies_list = movies_dict['title'].values

def recommend(movie):
  movie_index = movies[movies['title'] == movie].index[0]
  distances = similarity[movie_index]
  movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
  
  recommend_movies = []
  recommend_movies_posters = []
  for i in movies_list:
    index = i[0]
    # fetch poster from API
    recommend_movies.append(movies.iloc[index].title)
    movie_id = movies.iloc[index].movie_id
    recommend_movies_posters.append(fetch_poster(movie_id))
  return recommend_movies, recommend_movies_posters
  
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')


# Define the list of options
available_options = movies_list

# Call st.selectbox() with the required 'options' argument
selected_movie_name = st.selectbox(
    "Which kind of movie you watch recently?", # The label for the selectbox
    available_options                     # The 'options' argument (a list/tuple)
)




if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
       st.text(names[0])
       st.image(posters[0])
       
    with col2:
       st.text(names[1])
       st.image(posters[1])
       
    with col3:
       st.text(names[2])
       st.image(posters[2])

    with col4:
       st.text(names[3])
       st.image(posters[3])
       
    with col5:
       st.text(names[4])
       st.image(posters[4])
       
