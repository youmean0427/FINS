import requests
import json

final_result = []
with open('TMDB_popular_movies.json', 'w', encoding='utf-8') as f:
    for i in range(1, 3):
        requestData = requests.get(f"https://api.themoviedb.org/3/movie/popular?api_key=8d2390a7f14da4093a0836c65dfb59a2&language=ko-KR&page={i}")
        jsonData = requestData.json()
        results=jsonData["results"]
        genreData = requests.get(f"https://api.themoviedb.org/3/genre/movie/list?api_key=8d2390a7f14da4093a0836c65dfb59a2&language=ko-KR")
        genres = genreData.json()
        print(len(genres['genres']))
        # print(results)
        for k in results:
            g_name = []
            for g in k['genre_ids']:
                for gg in genres['genres']:
                    if gg['id'] == g:
                        g_name.append(gg['name'])

            result = {
                'title' : k['title'],
                'overview':k['overview'],
                'popularity':k['popularity'],
                'release_date':k['release_date'],
                'vote_average':k['vote_average'],
                'movie_key':k['id'],
                'poster':k['poster_path'],
                'genres':g_name,
            }
            # print(result['genres'], type(result['genres']))
            final_result.append(result)    
        # print(final_result)
    json.dump(final_result, f, indent=2, ensure_ascii=False)
