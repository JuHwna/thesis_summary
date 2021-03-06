# 1. 전통적인 추천 시스템
## 1) 협업 필터링(Collaborative Filtering)
>위키백과
- 협업 필터링이란? : 많은 사용자들로부터 얻은 기호정보에 따라 사용자들의 관심사들을 자동적으로 예측하게 해주는 방법
  - 해당 접근법의 근본적인 가정
    - 사용자들의 과거의 경향이 미래에서도 그대로 유지될 것이라는 전제
  - 특징 : 특정 사용자의 정보에만 국한된 것이 아니라 많은 사용자들로부터 수집한 정보를 사용함
  - 고객들의 선호도와 관심 표현을 바탕으로 선호도, 관심에서 비슷한 패턴을 가진 고객들을 식별해 내는 기법
- 협업필터링의 방법론
  - 1) Memory based
    - 유사도를 기반으로 동작함
    - (1) user based
      - user 간의 유사도를 측정한 뒤 유사도가 높은 user들이 선호하는 상품을 추천한다.
        - 통계적 방법들을 이용하여 추천
      - 사용하는 유사도의 종류 : 코사인 유사도, 피어슨 유사도 등
        - 코사인 유사도 : cos(θ)= Α·Β/(||Α||·||Β||)
      - 해당 분석 방법에 필요한 데이터의 각 열들의 값 : 사용자 각각의 상품들의 점수
        |구분|상품A|상품B|....|
        |----|----|----|----|
        |A사용자||||
        |B사용자||||
        |C사용자||||
    - (2) item-based
      - item 간의 유사도를 계산함
      - user based와 마찬가지로 사용하는 유사도의 종류 비슷
      - 해당 분석 방법에 필요한 데이터의 각 열들의 값 : 사용자 평가점수
        |구분|A사용자|B사용자|....|
        |----|----|----|----|
        |상품A||||
        |상품B||||
        |상품C||||
   - 2) Model based
     - 머신러닝을 이용해 평점을 예측할 수 있는 모델을 만드는 방식
     - Memory-based 방식과의 차이점 
       - Memory-based : 평점을 가지지 않은 곳에 대해서는 효과를 가지지 못함
       - Model-based : 평점 정보가 없어도 특정 아이템에 대한 사용자의 평점을 모델을 통해 예측가능
     - 모델을 만드는데 사용되는 방법들
       - Matrix Factorization
         - Sparse한 데이터에서도 적용 가능
         - 평점 패턴으로부터 추론한 요인 벡터들을 통해 사용자와 아이템의 특성을 잡아냄
         - 사용자와 아이템 사이의 강한 연관성이 있다면 추천이 시행됨
         - 모델링 과정
           - 사용자와 아이템 모두를 차원 F의 결합 잠재요인 공간에 매핑시킴
             - 기존의 희소 행렬 형태의 사용자-아이템 평점 행렬∽ 밀집 행렬의 형태인 사용자-잠재요인 행렬 x 잠재요인 아이템 행렬
           - 해당 공간으로 생긴 두 벡터를 내적하면 사용자0아이템 사이의 상호작용을 반영하므로 아이템에 대한 사용자의 전반적인 관심으로 표현할 수 있음
             - 식 : τ<sup>^</sup><sub>ui</sub> = q<sup>T</sup><sub>i</sub>p<sub>u</sub>
           - SVD와 매우 유사
             - 하지만 추천 시스템에서는 결측값의 존재로 SVD를 직접적으로 사용하는 것은 불가능, 결측값을 채워 넣는 것도 효율적이지 못하고 데이터 왜곡 가능성 높음
           - 그래서 오직 관측된 평점만을 직접적으로 모델링함, 과적합을 방지하기 위해 규제항이 포함됨
               ![image](https://user-images.githubusercontent.com/49123169/117757680-7e8efc00-b25b-11eb-8c12-4e68b6962476.png)
