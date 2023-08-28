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
    - 좋은 생성 모델이라면 : density estimation을 목표로 한다면 개라는 이미지에 대해서는 높은 $p_{\theta}(x)$를, 그 외의 이미지에는 낮은 확률을 보일 수 있어야 함
  - Sampling : training에는 존재하지 않지만 training과 가장 비슷한 분포를 나타내는 model distribution으로 이미지를 만들어낼 수 있을까?
    - 좋은 생성 모델이라면 : Sampling을 목표로 한다면 학습된 데이터셋에는 없지만 확실히 강아지인 이미지를 만들어낼 수 있어야 함
  - Unsupervised representation learning : 특정 datapoint x에서 의미있는 feature representation을 학습할 수 있을까?
    - 좋은 생성 모델이라면 : representation learning을 목표로 한다면 개 품종과 같은 높은 수준의 feature를 찾아낼 수 있어야 할 것
- 생성 모델이 해결하고자 하는 문제들의 특성상 정량적인 evaluation은 non-trivial함
  - 일부 정량적인 지표가 있긴 하지만 특히 sample이나 representation learning의 경우, 만들어낸 이미지에 대한 찾아낸 feature에 대한 질적인 특징을 반영하지 못함
  - 생성모델의 정량적인 evaluation 방법을 개발하는 것은 매우 활발하게 연구가 진행되고 있는 영역
- 모든 생성 모델들이 모든 상황에서 효율적인 좋은 성능을 아직까지 보이지는 못함

### Discriptive vs Generative
#### 왜 Generative model이 필요한가?
##### Dataset의 증가
- generative model은 training set이 부족한 상황에서 더 training을 만들어내는데 사용될 수 있음
- Computer vision에서 사용되는 많은 구조들은 점점 더 많은 데이터셋을 요구하고 있음
  - vision transformer를 베이스로한 구조들은 기존의 CNN을 베이스로한 모델보다 훨씬 더 많은 양의 training을 필요로 함
  - 하지만 사람이 일일히 classification을 하면서 데이터셋을 만드는데에는 많은 시간과 노동력이 투입되며 현실적인 한계 역시 존재함
##### Style transfer & artwork
- Style transfer 또는 Image-to-image translation이라고 불리는 이 작업은 다양한 artwork에 응용될 수 있음
  - ex) 색이 없는 스케치에 realistic한 coloring을 해주는 모델
  - ex) 실제 사진을 베이스로 한 만화 그림체같이 이미지로 바꾸어주는데 응용
 
##### Super resolution
- 대표적인 super resolution 모델 중 하나인 SRGAN의 경우, 픽셀 단위 resolution도 더 고해상도로 transfer 할 수 있음

##### 생성 모델의 애플리케이션
- 예술적 스타일 이전 방법
  - 예술 스타일을 어떤 이미지 대상으로 옮기는 과정
    - 이미지의 예술적 스타일과 다른 이미지의 내용을 결합해 새로운 이미지를 만들 수 있음
- 동영상의 다음 프레임 예측
  - 생성 동영상 모델을 사용해 미래의 프레임을 예측할 수 있음
  - 이전 프레임의 얼굴을 보고 다른 각도에서의 얼굴 모습 데이터를 예측해낸 것
- 슈퍼 해상도 이미지
  - 작은 이미지에서 고해상도 이미지를 만드는 과정
  - 전통적으로 보간법은 더 큰 이미지를 만들기 위해 사용됐음
    - 그러나 보간법은 매끄러운 효과를 주기 때문에 고주파 세부 사항들을 놓치게 됨
- 이미지를 다른 이미지로 변환하기
  - 이미지는 특정 목적을 가진 다른 이미지를 생성하는데 사용될 수 있음
- 텍스트로 이미지 생성하기
  - 텍스트 설명을 가지고 이미지를 생성함
- 사진으로부터 3D 모델 생성
  - 2D 이미지로부터 3D 이미지를 생성함
