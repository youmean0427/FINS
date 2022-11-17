import pandas as pd
import json 

# def load_data():
#     df_all = pd.read_json(r'movie_data_test.json')
#     df_all.loc[:,
#         ['title', 'overview', 'popularity', 'release_date', 'vote_average',  'poster', 'movie_key', 'genres' ]
#     ]
#     return df_all
# df = load_data()
df = pd.read_json(r'movie_genre_test.json')
df.to_csv('movie_genre_test.csv', header=True, index=True, encoding='UTF-8')
