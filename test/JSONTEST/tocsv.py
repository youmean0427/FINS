import pandas as pd
import json 

def load_data():
    df_all = pd.read_json(r'TMDB_popular_movies.json')
    df_all.loc[:,
        ['title', 'overview', 'popularity', 'release_date', 'vote_average',  'poster', 'movie_key' ]
    ]
    return df_all
df = load_data()
df.to_csv('out.csv', header=True, index=True, encoding='UTF-8')
