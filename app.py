import streamlit as st
import pickle
import pandas as pd
import sklearn

def recommend(movie):
    movie_index= movies[movies['title']==movie].index[0] # marking index of the movie 
    distances = similarity[movie_index] 
    movies_list= sorted(list(enumerate(distances)), reverse = True, key= lambda x:x[1])[1:6]
    
    recommended_movies =[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append((movies.iloc[i[0]].title))
    
    return recommended_movies
    







movies_dict= pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

#Vectorisation
from sklearn.feature_extraction.text import CountVectorizer
count_vec= CountVectorizer(max_features = 5000, stop_words = 'english')
vectors = count_vec.fit_transform(movies['tags']).toarray()




#Similarity Matrix
from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(vectors)



st.title('Movie Recommendations')

selected_movie_name = st.selectbox(

    'What Kind of Movies Do You Watch?',
    movies['title'].values
    )

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)

    for i in recommendations:
        st.write(i)