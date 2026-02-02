import streamlit as st
import pickle 
import pandas as pd
import requests

st.title("Movie Recommender System")

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=05edb51b0ce25038429cc73fc7fff38c'.format(movie_id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/original' + data['poster_path']
    
    

def recommended(movies):
    movie_index = movie[movie['title'] == movies].index[0]
    distance = similarity[movie_index]
    movies_list =  sorted((list(enumerate(distance))), reverse = True, key = lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_poster_path = []
    for i in movies_list:
        
        movie_id = movie.iloc[i[0]].movie_id
        recommended_movies.append(movie.iloc[i[0]].title)
        
        recommended_poster_path.append(fetch_poster(movie_id)) 
               
    return recommended_movies, recommended_poster_path
    
movies_dic = pickle.load(open('movie_pkl','rb'))
movie = pd.DataFrame(movies_dic)

similarity = pickle.load(open('similarity_pkl', 'rb'))



selected_movie_option = st.selectbox(
    'Enter your movie choice',
movie['title'].values
)

if st.button("Recommend"):
    names, posters = recommended(selected_movie_option)
    
    col1, col2, col3,col4 ,col5 = st.columns(5)

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

