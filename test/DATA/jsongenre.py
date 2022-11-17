import requests
import json

final_result = []
with open('TMDB_genere.json', 'w', encoding='utf-8') as f:
    genreData = requests.get(f"https://api.themoviedb.org/3/genre/movie/list?api_key=8d2390a7f14da4093a0836c65dfb59a2&language=ko-KR")
    genres = genreData.json()
    for g in genres['genres']:
        result = {
            'genre_id' : g['id'],
            'genre_name' : g['name']
        }
        final_result.append(result)
        # g1. id genre_name
            # final_result.append(result)    
    json.dump(final_result, f, indent=2, ensure_ascii=False)
