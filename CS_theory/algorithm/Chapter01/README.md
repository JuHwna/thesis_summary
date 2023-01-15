## 프로그래머스 코딩테스트 1주차

(1) 
- 1번 문제 : https://programmers.co.kr/learn/courses/30/lessons/42576
- 해설 강의
  - 크기 : 몇 명이 마라톤에 참여했냐?
  - n, nlogn 정도의 속도 알고리즘으로 풀어야 한다
  - 동명이인이 없다면 집합으로 바꾸어서 차집합으로 풀면 된다.
  - 이름이 주어지면 몇 번이나 배열에 등장했는지를 데이터를 저장할 수 있는 
    - 이름에 대해서 어떤 수를 기록하고 저장할 수 있는 구조 필요 -> 해쉬
  - 자료구조(와 알고리즘)의 선택
    - 만약 이름 대신 번호가 주어졌다면 
      - 선형 배열(linear array) - 여기서는 배열을 이용할 수 없음
      - 번호 말고 다른 것(예: 문자열)로 접근할 수 있는 좋은 자료 구조는 없나? -> 해쉬
  - 해쉬(Hash)
    - 해시 테이블 : 저장공간
    - 키 : 사람들의 이름  
    - 해쉬 : 이 키들이 어느 위치에 있는지 정해서 해쉬테이블 안에 저장하는 것
    - hash function : 키들이 서로 다른 칸에 저장되게 만드는 것
    - 해시 버킷 : 해쉬 테이블 내의 각각의 칸
    - ![image](https://user-images.githubusercontent.com/49123169/212478417-763733e3-6dbb-4a3d-8d75-865fe2b28282.png)
    - 충돌(collision) : 키들이 서로 같은 칸에 사상되는 경우
      - 해결 방법 : 같은 칸에다가 옆으로 해시 버킷을 만들어서 넣는 것
      - ![image](https://user-images.githubusercontent.com/49123169/212478491-22f79e8e-db83-42be-a458-50db2860c448.png)
      
    
- 2번 문제 : 벨 문제
    
(2) 1번 문제 : https://somjang.tistory.com/entry/Programmers-%ED%83%90%EC%9A%95%EB%B2%95Greedy-%EC%B2%B4%EC%9C%A1%EB%B3%B5-Python


(3) 
- 1번 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42746
- 2번 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/148653

(4)
- 1번 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42883
- 2번 문제 : 철학자
- ![image](https://user-images.githubusercontent.com/49123169/212348180-dba875f1-9801-4610-96a5-847a2f205eb7.png)
- ![image](https://user-images.githubusercontent.com/49123169/212348266-818d2e5a-3642-4433-9d34-6108219230e4.png)
- ![image](https://user-images.githubusercontent.com/49123169/212348319-b22323db-97cf-49b0-9b2b-bfc45df40a1c.png)
