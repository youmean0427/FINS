import requests
import json

final_result = []
with open('movie_data.json', 'w', encoding='utf-8') as f:
    for i in range(1, 50):
        requestData = requests.get(f"https://api.themoviedb.org/3/movie/popular?api_key=8d2390a7f14da4093a0836c65dfb59a2&language=ko-KR&page={i}")
        jsonData = requestData.json()
        results=jsonData["results"]

        for k in results:
            id = k['id']
            data = requests.get(f"https://api.themoviedb.org/3/movie/{id}/videos?api_key=8d2390a7f14da4093a0836c65dfb59a2")
            vd = data.json()
            videoData = vd['results']
            if not videoData:
                video_path = ''
                continue

            if (videoData[0]['site'] == "YouTube"): # and (videoData[0]['type'] == 'Teaser'):
                # print('tmdb---------------')
                key = videoData[0]['key']
                video_path = f'https://www.youtube.com/watch?v={key}'
            elif(videoData[0]['site'] == "Vimeo"):
                key = videoData[0]['key']
                video_path = 'https://vimeo.com/{key}'
            else:
                # youtube teaser 영상이 없으면 youtube api로 영화 검색해서 첫번째 영상으로 처리
                # 하려했는데 youtube api 호출 횟수 초과로..
                video_path = ''
                
            if 'release_date' not in k:
                release_date = ''
            else:
                release_date = k['release_date']
            result = {
                'title' : k['title'],
                'overview':k['overview'],
                'popularity' : k['popularity'],
                'release_date' : release_date,
                'vote_average':k['vote_average'],
                'movie_key':id,
                'video_path' : video_path,
                'poster':k['poster_path'],
            }
            final_result.append(result)    
    json.dump(final_result, f, indent=2, ensure_ascii=False)
