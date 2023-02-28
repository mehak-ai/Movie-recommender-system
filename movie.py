import streamlit as st
import pickle
import pandas as pd
import requests 

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=5bf271582f232c240d2a6ffc4461142d'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movieindex=movies[movies['title']==movie].index[0]
    distances=similarity[movieindex]
    movielist=sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:6]
    
    recc_movies=[]
    recc_movie_posters=[]
    for i in movielist:
        movie_id=movies.iloc[i[0]].movie_id
        #fetch poster from api
        recc_movies.append(movies.iloc[i[0]].title)
        recc_movie_posters.append(fetch_poster(movie_id))
    return recc_movies, recc_movie_posters

similarity= pickle.load(open(r'C:\Users\Dell\Desktop\python\simi.pkl','rb'))
movieslist= pickle.load(open(r'C:\Users\Dell\Desktop\python\moviesdict.pkl','rb'))
movies=pd.DataFrame(movieslist)
st.title('Movie Recommender System')
selectedmoviename = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values
) 

if st.button('Recommend'):
    names,posters=recommend(selectedmoviename)

    col1, col2, col3, col4, col5 = st.beta_columns(5)
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