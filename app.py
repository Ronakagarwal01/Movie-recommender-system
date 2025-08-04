import streamlit as st
import pickle
import pandas as pd
import requests

# TMDB API configuration
TMDB_API_KEY = "your_tmdb_api_key_here"  # You'll need to get this from TMDB
TMDB_BASE_URL = "https://api.themoviedb.org/3"

def fetch_poster(movie_id):
    """Fetch movie poster from TMDB API"""
    try:
        url = f"{TMDB_BASE_URL}/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
        response = requests.get(url)
        data = response.json()
        
        if 'poster_path' in data and data['poster_path']:
            poster_path = data['poster_path']
            full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
            return full_path
        else:
            return None
    except:
        return None

def recommend(movie):
    """Recommend movies based on similarity"""
    try:
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies = []
        recommended_posters = []
        
        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movies.append(movies.iloc[i[0]].title)
            # Fetch poster from API
            poster = fetch_poster(movie_id)
            recommended_posters.append(poster)
            
        return recommended_movies, recommended_posters
    except IndexError:
        st.error("Movie not found in database!")
        return [], []
    except Exception as e:
        st.error(f"Error occurred: {str(e)}")
        return [], []

# Load the data
try:
    movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open('similarity.pkl', 'rb'))
except FileNotFoundError as e:
    st.error(f"Required data files not found: {e}")
    st.stop()

# Streamlit UI
st.title('🎬 Movie Recommender System')
st.markdown("---")

# Movie selection
selected_movie_name = st.selectbox(
    'Select a movie you like:',
    movies['title'].values
)

# Recommend button
if st.button('🎯 Get Recommendations'):
    with st.spinner('Finding similar movies...'):
        recommendations, posters = recommend(selected_movie_name)
    
    if recommendations:
        st.success(f"Here are 5 movies similar to '{selected_movie_name}':")
        st.markdown("---")
        
        # Display recommendations in columns
        cols = st.columns(5)
        for i, (movie, poster) in enumerate(zip(recommendations, posters)):
            with cols[i]:
                if poster:
                    st.image(poster, width=120, caption=movie)
                else:
                    st.write("📽️")
                st.write(f"**{movie}**")
    else:
        st.warning("No recommendations found. Please try another movie.")

# Footer
st.markdown("---")
st.markdown("*Built with Streamlit and TMDB API*")
