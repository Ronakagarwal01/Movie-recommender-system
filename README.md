# Movie Recommender System

A content-based movie recommendation system built with Streamlit and machine learning.

## Features

- Content-based movie recommendations using cosine similarity
- Beautiful Streamlit web interface
- Movie poster integration with TMDB API
- 5000+ movies from TMDB dataset

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Get TMDB API Key (Optional for posters)
1. Go to [TMDB](https://www.themoviedb.org/)
2. Create an account and get your API key
3. Replace `your_tmdb_api_key_here` in `app.py` with your actual API key

### 3. Run the Application
```bash
streamlit run app.py
```

## How it Works

1. **Data Processing**: The system processes movie data including genres, keywords, cast, crew, and overview
2. **Text Vectorization**: Uses CountVectorizer to convert text data into numerical vectors
3. **Similarity Calculation**: Uses cosine similarity to find similar movies
4. **Recommendations**: Recommends 5 most similar movies based on content similarity

## Files Description

- `app.py`: Main Streamlit application
- `Movie-recommender-system.ipynb`: Jupyter notebook with data processing and model training
- `movies_dict.pkl`: Pickled movie data
- `similarity.pkl`: Pickled similarity matrix
- `tmdb_5000_movies.csv`: Original movie dataset
- `tmdb_5000_credits.csv`: Movie credits dataset

## Usage

1. Select a movie from the dropdown
2. Click "Get Recommendations"
3. View 5 similar movies with posters (if API key is provided)

## Note

If you don't have a TMDB API key, the system will still work but won't display movie posters. 