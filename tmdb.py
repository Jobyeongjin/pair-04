import requests
from pprint import pprint
import os
from dotenv import load_dotenv
import json
import urllib.request

load_dotenv(verbose=True)
key = os.getenv('key')

def ranking():
    base = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
    'api_key': '1fbf55bcf78cb7b7e9b4e5832c889a5c',
    'language': 'ko-KR'
    }
    img_base = 'https://image.tmdb.org/t/p/w500'
  
    response = requests.get(base+path, params=params).json()
    
    data_list = []
    
    # data['title']= []
    # data['poster_path'] = []
    # data['id'] = []
    # data['vote_average'] = []
    # data['overview'] = []
    
    title = response.get('results')
    file_path = "./sample.json"
    for j in title:
        new_data = {"model": "movies.movie"}
        new_data['fields']  = {}
        new_data['fields']['id'] = j.get('id')
        new_data['fields']['title'] = j.get('title')
        new_data['fields']['poster_path'] = j.get('poster_path')
        new_data['fields']['vote_average'] = j.get('vote_average')
        new_data['fields']['overview'] = j.get('overview')
        data_list.append(new_data)
        # data['id'].append(j.get('id'))
        # data['title'].append(j.get('title'))
        # data['poster_path'].append(j.get('poster_path'))
        # data['vote_average'].append(j.get('vote_average'))
        # data['overview'].append(j.get('overview'))
        
        
        url = img_base + j.get('poster_path')
        print(url)
        urllib.request.urlretrieve(url, "static/images/" +str(j.get('id')) +".jpg")
    
    # with open('animations_data.json', 'w', encoding='UTF-8') as f:
	#     json.dump(new_list, f, ensure_ascii=False, indent=2)  # json 파일로 저장

    with open(file_path, 'w', encoding='UTF-8') as outfile:
        json.dump(data_list, outfile, indent=2, ensure_ascii=False)
    return data_list




pprint(ranking())
