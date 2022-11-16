import pandas as pd
import json 

def load_data():
    df_all = pd.read_json(r'TMDB_popular_movies.json')
    # for i in range(len(df_all)):
    #     result ={'title':df_all[i]['title']}
    # print(df_all [0])
    df_all.loc[:,
        ['title', 'overview', 'popularity', 'release_date', 'vote_average', 'poster_path', 'id' ]
    ]
    print(type(df_all)) 
    return df_all

df = load_data()
# print(df)
# df = pd.read_json(r'TMDB_popular_movies.json')
# df.to_csv('out3.csv', header=True, index=True, encoding='UTF-8')