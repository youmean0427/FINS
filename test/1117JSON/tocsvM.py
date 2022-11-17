import pandas as pd
import json 
# def load_data():
#     df_all = pd.read_json(r'movies_images.json')
#     df_all.loc[:,
#         ['image_path', 'movie_id_id']
#     ]
#     return df_all
# df = load_data()
df = pd.read_json(r'movie_images2.json')
df.to_csv('movie_images2.csv', header=True, index=True, encoding='UTF-8')
