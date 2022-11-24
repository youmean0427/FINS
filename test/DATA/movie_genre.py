import requests
import json

genreData = [
  {
    "genre_id": 28,
    "genre_name": "액션"
  },
  {
    "genre_id": 12,
    "genre_name": "모험"
  },
  {
    "genre_id": 16,
    "genre_name": "애니메이션"
  },
  {
    "genre_id": 35,
    "genre_name": "코미디"
  },
  {
    "genre_id": 80,
    "genre_name": "범죄"
  },
  {
    "genre_id": 99,
    "genre_name": "다큐멘터리"
  },
  {
    "genre_id": 18,
    "genre_name": "드라마"
  },
  {
    "genre_id": 10751,
    "genre_name": "가족"
  },
  {
    "genre_id": 14,
    "genre_name": "판타지"
  },
  {
    "genre_id": 36,
    "genre_name": "역사"
  },
  {
    "genre_id": 27,
    "genre_name": "공포"
  },
  {
    "genre_id": 10402,
    "genre_name": "음악"
  },
  {
    "genre_id": 9648,
    "genre_name": "미스터리"
  },
  {
    "genre_id": 10749,
    "genre_name": "로맨스"
  },
  {
    "genre_id": 878,
    "genre_name": "SF"
  },
  {
    "genre_id": 10770,
    "genre_name": "TV 영화"
  },
  {
    "genre_id": 53,
    "genre_name": "스릴러"
  },
  {
    "genre_id": 10752,
    "genre_name": "전쟁"
  },
  {
    "genre_id": 37,
    "genre_name": "서부"
  }
]

final_result = []
with open('movie_genre_final.json', 'w', encoding='utf-8') as f:
    count = 0
    for i in range(1, 500):
        requestData = requests.get(f"https://api.themoviedb.org/3/movie/popular?api_key=8d2390a7f14da4093a0836c65dfb59a2&language=ko-KR&page={i}")
        jsonData = requestData.json()
        results=jsonData["results"]
        
        for k in range(len(results)):
            for g in results[k]['genre_ids']:
                for gg in range(len(genreData)):
                    if genreData[gg]['genre_id'] == g:
                        g2 = {
                            'movie_id' : count,
                            'genre_id' : gg,
                        }
                        final_result.append(g2)   
            count += 1
    json.dump(final_result, f, indent=2, ensure_ascii=False)
