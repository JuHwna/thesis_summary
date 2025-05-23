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
    - model의 distribution이 실제 데이터, 즉 $p_{data}$와 가장 가깝도록 만드는 것
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

## 2. 생성 모델을 위한 사전지식
### 1) 생성 모델의 역사
#### 초창기 생성 모델 아이디어
- Boltzman machine
  - 입력층 1개, 은닉층 1개 그리고 모든 node들을 잇는 edge로 구성되어 있음
  - RBM과는 다르게 같은 layer 안에서도 연결이 있는 모델임
  - 에너지 기반 모형
    - 볼츠만 머신의 결합확률 분포 : $P(x)=\frac{exp(-E(x))}{Z}$ => 에너지 함수를 통해 정의됨
    - E(x) : 하나의 에너지 함수
    - Z는 $\displaystyle\sum_{x}^{} P(x)$=1 이 되게 하는 (확률의 합이 1이 되게 하는) 분할 함수
    - 에너지 함수 : E(x) = $-x^{T} Ux-b^{T}x$
   

![image](https://github.com/JuHwna/thesis_summary/assets/49123169/0df28807-4861-4c02-a294-cbdbd6aad1a4)

#### RBM(Restricted Boltzman Machine, 1980)
- RBM : 입력층 1개와 은닉층 1개로 구성되어 있음
  - 모든 hidden layer의 노드들은 visible layer(입력층)와 연결되어 있고 그 역도 마찬가지임
  - 같은 layer 안에서는 연결이 되어 있지 않음(이를 bipartite graph라고 부름)
  - 해당 특성 때문에 제한된 볼츠만 머신이라고 불림
- Perceptron의 output은 결정론적인 것에 비해 RBN은 확률에 따라서 입력을 은닉층에 전달할지 전달하지 않을지 결정해 보냄


![image](https://github.com/JuHwna/thesis_summary/assets/49123169/ff891b99-7ca6-44eb-9ea8-5300a99a9e1d)

#### DBN(Deep belief network, 2006)
- DBN : 2006년에 제안되어 최초로 Deep한 network 구조를 훈현할 수 있었던 모델
  - 여러 개의 hidden layer를 가진 생성모델임
  - 기본적인 구조는 RBM을 stacking해서 깊게 쌓아올린 것
- Deep neural network를 학습할 때 사용하는 일반적인 것 : gradient descent
  - 오차를 토대로 output layer에서부터 chain rule을 이용해 input layer까지 교정해나가는 방법
  - 존재하는 문제점 : Gradient vanishing/ explosion
    - 심층 모델의 학습에서는 대부분 발생하는 문제
    - 당대에는 이 문제 해결이 불가능하다고 보고 네트워크를 깊게 쌓기보다는 kernel machine 등을 연구했었음
- DBN은 거꾸로 아래층에서 위로 올라가면서 pre-training을 하면서 모델을 깊게 쌓아올리는 방법을 씀
  - layer-wise pretraining이라고 부름
- 아래에서 위로 올라가기 위해 unsupervised learning의 개념이 나옴
  - DBN에서는 v(vision layer, input)만 알고 있다고 가정하고 이 입력이 어떤 h(hidden layer, 나아가서 y)의 값으로부터 만들어졌을까를 추론함
  - 이 과정을 한 번 풀어서 생각해보면 h와 w를 랜덤하게 초기화 했다고 해보면
    - 맨 처음 층에서 엉터리 h1와 w1가 있음
    - 엉터리 h라도 이걸 토대로 x(입력 데이터)를 추론할 수 있고 x로 h를 추론할 수 있음
    - 이 과정을 반복하면서 필터 w를 학습시킴
    - h1이 입력이고 x`이 출력일 때 x`이 최대한 x와 같은 값을 만들 수 있도록 함
    - 그리고 w1을 freeze 시키고 그 다음 단계에서 똑같은 작업을 진행함
  - 학습 과정을 정리해보면
  - 
