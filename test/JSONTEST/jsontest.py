# import requests
# import json

# API_URL = "https://api.themoviedb.org/3/movie/popular?api_key=8d2390a7f14da4093a0836c65dfb59a2&language=en-US&page=1"

# requestData = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=8d2390a7f14da4093a0836c65dfb59a2&language=en-US&page=1")

# jsonData = requestData.json()

# real_results=[]
# with open('output.json', 'w') as f:
#     for i in range(1, 20):
#         jsonData['page'] = i
#         results=jsonData["results"]
        
#         json.dump(real_results, f, indent=2)
    

import requests
import json

final_result = []
with open('TMDB_popular_movies.json', 'w', encoding='utf-8') as f:
    for i in range(1, 500):
        requestData = requests.get(f"https://api.themoviedb.org/3/movie/popular?api_key=8d2390a7f14da4093a0836c65dfb59a2&language=ko-KR&page={i}")
        jsonData = requestData.json()
        results=jsonData["results"]
        # print(results)
        for k in results:
            final_result.append(k)    
    json.dump(final_result, f, indent=2, ensure_ascii=False)
