import pandas as pd
import json 

df = pd.read_json(r'medi_genre.json')
df.to_csv('medi_genre.csv', header=True, index=True, encoding='UTF-8')
