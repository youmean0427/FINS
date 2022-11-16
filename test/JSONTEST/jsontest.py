import requests
import json

final_result = []
with open('medi_genre.json', 'w', encoding='utf-8') as f:
    for i in range(1, 500):
        requestData = requests.get(f"https://api.themoviedb.org/3/movie/popular?api_key=8d2390a7f14da4093a0836c65dfb59a2&language=ko-KR&page={i}")
        jsonData = requestData.json()
        results=jsonData["results"]
        genreData = requests.get(f"https://api.themoviedb.org/3/genre/movie/list?api_key=8d2390a7f14da4093a0836c65dfb59a2&language=ko-KR")
        genres = genreData.json()
        for k in results:
            if 'release_date' not in k:
                print(k['title'])
                continue
            # g2 = []
            for g in k['genre_ids']:
                for gg in genres['genres']:
                    if gg['id'] == g:
                        g2 = {
                            'movie_id' : k['id'],
                            'genre_id' : gg['id'],
                        }
                        final_result.append(g2)    
            # g1. id genre_name
            # g2. id movie_id genre_id

    json.dump(final_result, f, indent=2, ensure_ascii=False)
