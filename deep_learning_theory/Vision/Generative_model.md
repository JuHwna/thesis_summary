# Generative model(생성 모델)
## 1. 생성 모델 아이디어
### 생성 모델이란 무엇일까?
- 생성 모델
  - 정의 : 주어진 학습 데이터를 학습하고 학습 데이터의 분포를 따르는 유사 데이터를 생성하는 모델
    - 주어진 Training data와 같은 distribution을 가진 새로운 sample을 만들어내는 모델
  - 목적 : training set의 distribution을 배우는데 목적을 두고 있음
    - 데이터 각각을 label로 구분하지 않고 전체 데이터의 joint distribution을 학습함
    - 실제로 존재하는 것은 아니지만 마치 존재할 것 같은 특히 우리가 학습시켜준 데이터들 사이에 정말로 존재할 것 같은 데이터를 만들어내는 것
  - 이미지
    - 위의 그림에 나와 있는 P_model(x)와 P_data가 유사하도록 학습을 해줌
    - P_model : Generative model이 만들어낸 Generated Sample들의 분포
    - P_data : Training data, 즉 Real World의 데이터들의 분포
    - 두 가지의 대분류
      - Explicit Density Estimation : P_model을 확실하게 정의 (ex. VAE, Approximate Density)
      - Implicit Density : Model을 정의하지 않고 P_model에서 sample을 생성 (ex. GAN, Markov Chain)
  - 실제 세계의 데이터로부터 비슷한 Fake Data를 생성할 수 있음
    - Time-series data 등은 생성 모델에서 시뮬레이션이나 Planning에 사용 가능함
  - ex) 강아지 이미지를 만들애는 Generative model을 구축한다고 가정
    - model의 distribution이 실제 데이터, 즉 $$p_{data}$$와 가장 가깝도록 만드는 것
    - 녹색으로 표현된 model distribution, $p_{\theta}$와 $p_{data}$ 사이의 거리, d가 최소화되는 문제로 정의할 수 있음
- 생성 모델을 이용해 해결하는 문제
  - Density estimation : 주어진 datapoint x에 대해서 model에 의해 할당되는 확률 $p_{\theta}(x)$을 구할 수 있을까?
    - 좋은 생성 모델이라면 : density estimation을 목표로 한다면 개라는 이미지에 대해서는 높은 $p_{}$
  - Sampling : training에는 존재하지 않지만 training과 가장 비슷한 분포를 나타내는 model distribution으로 이미지를 만들어낼 수 있을까?
  - Unsupervised representation learning : 특정 datapoint x에서 의미있는 feature representation을 학습할 수 있을까?
    
