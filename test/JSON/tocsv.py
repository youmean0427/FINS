import pandas as pd
import json 

# def load_data():
#     df_all = pd.read_json(r'movie_data_test.json')
#     df_all.loc[:,
#         ['title', 'overview', 'popularity', 'release_date', 'vote_average',  'poster', 'movie_key', 'genres' ]
#     ]
#     return df_all
# df = load_data()

# .json 데이터 입력
df = pd.read_json(r'movie_image_final.json')

# csv 파일이름 똑같이 하자! (movie_test.csv)
df.to_csv('movie_image_final.csv', header=True, index=True, encoding='UTF-8')
