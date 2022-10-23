### 0. 라이브러리

```python
import request
import json
import urillib.request
```

### 1. BASE_URL

```python
def function():
    # 요청에 따라, 변경
    base = "<url>"
    path = ""
    params = {
    'key' : 'your_key',
    'language' : 'ko-kr'
    }
    # 저장 경로 변수로 선언
    file_path = "./sample.json"
    img_base = "https://image.tmdb.org/t/p/w<width>"
    # 요청을 json 형식으로 변수에 저장
    response = requests.get(base+path, params=params).json()
```

### 2. JSON 가공

```python
        movie_list = []
    movies = reponse.get('results')
    for movie in movies:
        new_data = {"models" : "<appname>:<modelname>"}
        new_data['fields'] = {}
        new_data['fields']['<dict_key>'] = movie.get('<dict_key>')
        .
        .
        movie_list.append(new_data)
        # 이미지를 저장하기 위해, poster_path 를 url에 담아줌
        url = img_base + movie.get('poster_path')
        # <dir> 경가 있다면,
        if os.path.isdir("<dir>"):
            # url을 , ./<dir> 경로에 movie의 id를 이름으로 저장
            urllib.request.urlretrieve(url, "<dir>" +str(movie.get('id')) +".jpg")
        # 폴더가 없다면, 만들고 이미지 저장
        else:
            os.makedirs("<dir>")
            urllib.request.urlretrieve(url, "<dir>" +str(movie.get('id'))
         +".jpg")
```

모델에서 정의한 필드를 for문으로 순회하며, movie_list에 담아줌

### 3. JSON 저장

```python
# for 문이 끝난 후 json 파일로 가공한 정보를 저
    with open(file_path, 'w', encoding='UTF-8') as outfile:
        json.dump(movie_list, outfile, indent=2, ensure_ascii=False)
    return movie_list
```




