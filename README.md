# 페어 프로젝트 영화 리뷰 📹

> Github 활용(Git - branch, merge)한 협업 프로젝트

<br/>

## **📅 프로젝트 기간**

- **2022.10.21**

<br/>

## **🧑‍💻 팀원**

<br/>

<a href="https://github.com/kkinter/pair_pjt_4/graphs/contributors">

| <img src="https://contrib.rocks/image?repo=kkinter/pair_pjt_4" /> |     |
| ----------------------------------------------------------------- | --- |
| 백엔드: 황성욱<br />프론트엔드: 조병진                            |     |

</a>

<br/>

## **사용 기술 💼**

<br/>

<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=ffffff"/> <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=ffffff"/>　<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=ffffff"/>　<img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=Git&logoColor=ffffff"/>　<img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=ffffff"/>

<br/>

---

## **목표 🎯**

- **CRUD** 기능 구현
- **Staticfiles** 활용 정적 파일(이미지, CSS, JS) 다루기
- **Django Auth** 활용 회원 관리 구현
- **Media** 활용 동적 파일 다루기
- **모델간 1:N 관계 매핑** 코드 작성 및 활용
- 클라이언트와 소통을 위한 **영화 리뷰 커뮤니티 서비스** 페이지 구현

<br/>

<details>
<summary>접기/펼치기</summary>

<br/>
### **추가++**
-TMDB API 를 통해, JSON 파일 생성 > `python manage.py loaddata sample.json' 모델에 fixture
-1:1 관계 (User - Profile) , N:M 관계 (User - Review.like_users) 모델 추가
-Q 객체를 사용한 검색 기능 추가

### **영화 관리**

> TMDB에서 가져온 영화 데이터를 바탕으로 **해당 영화의 리뷰를 작성**합니다.

1. **영화 목록 조회**
   - 영화 평점 출력

---

### **회원 관리**

> **로그인한 사용자만** 회원관리 및 프로필 관리를 할 수 있습니다.

1. **회원가입**
2. **로그인 및 로그아웃**
3. **회원정보 수정 및 삭제**
   - 비밀번호 변경
4. **프로필 사진 첨부**
   - (프로필 사진이 없다면) 대체 이미지 출력
5. **프로필 사진 수정 및 삭제**

---

### **리뷰 관리**

> **로그인한 사용자만** 리뷰 생성이 가능하고, **리뷰를 생성한 사용자만** 수정 및 삭제 버튼이 보이고 수정 및 삭제할 수 있습니다.

1. **리뷰 작성**
   - 이미지 추가 기능 구현
2. **리뷰 목록 조회**
   - 프로필 이미지 출력
   - 리뷰 이미지 출력
   - 업데이트 시간 출력
   - (댓글이 있다면) 댓글 수 출력
   - (좋아요가 있다면) 좋아요 수 출력
3. **리뷰 정보 조회**
   - 리뷰 수정 및 삭제
   - 댓글 작성 및 목록 조회
   - 댓글 삭제
   - 좋아요 기능 구현
4. **리뷰 수정 및 삭제**

---

### **댓글 관리**

> **로그인한 사용자만** 댓글을 생성 및 조회가 가능하고, **댓글을 생성한 사용자만** 삭제 버튼이 보이고 삭제할 수 있습니다.

1. **댓글 생성**
2. **댓글 목록 조회**
3. **댓글 삭제**

</details>

---

## **구현 영상**

<br/>

---

## **배운점 및 느낀점 💡**
