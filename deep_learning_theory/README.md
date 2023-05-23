사전학습 : pre-training
미세조정 : fine-tuning




# 퍼셉트론(TLU(threshold logic unit) or LTU(linear threshold unit))
- 입력과 출력이 어떤 숫자이고 각각의 입력 연결은 가중치와 연관되어 있음


# 경사 하강 알고리즘(Gradient Descent Algorithm)
- Have some function $J(\theta_0,\theta_1)$
- Want $min_{\theta_0,\theta_1}J(\theta_0,\theta_1)$
- Outline
  - Start with some $\theta_0,\theta_1$
  - Keep changing $\theta_0,\theta_1$ to reduce $J(\theta_0,\theta_1)$ until we hopefully end up at a minimum
- 비용 함수 $J(\theta_0,\theta_1)$를 최소화 하는 $\theta$를 구하는 알고리즘으로 머신러닝에서 굉장히 폭넓게 쓰임
- 작동 원리
  - $\theta$에 대해 임의의 초기값 즉 시작점을 잡음
  - 그리고 J가 최소가 될 때까지 $\theta$값 갱신을 반복하여 최솟값에 도달했을 때 해당하는 $\theta$를 찾아냄
- Gradient descent algorithm 공식
  - repeat until convergence $\theta_j:=\theta_j-\alpha\frac{\partial}{\partial\theta_j}J(\theta_0,\theta_1)$ (for j=1 and i=0)
  - := : 대입 연산자
    - $\theta$값을 갱신한다는 의미
  - $\alpha$ 뒤에 곱해져 있는 것 : 비용 함수 J의 미분값
  - $\alpha$ : learning rate
    - 갱신되는 $\theta$ 값의 속도를 결정함
    - 아무리 미분값이 크더라도 $\alpha$가 작다면 갱신되는 속도가 느려짐
 - 경사하강 알고리즘 최종 목표 : 해당 공식으로 초기값 설정 후 반복적인 갱신을 통해 최종적인 minimum에 도달하는 것
 
 ### 미분 값
 - 미분 값 : 해당 지점에서의 기울기
   - 만약 $\alpha$가 일반적인 양수값이라면 $\theta(=w)$가 반복적으로 갱신되면서 최종적으로 최솟값에 도달함
   - $\theta$의 갱신은 기울기 하강과 기울기 상승 두가지로 나뉨
     - 미분 값 양수일 때 갱신 시 $\theta$는 감소
     - 미분 값 음수일 때 갱신 시 $\theta$는 증가

### Learning rate (학습 속도)
- Learning rate가 지나치게 작다면 : 최솟값에 도달하기 위해 굉장히 많은 연산이 요구됨
- Learning rate가 지나치게 크다면 : $\theta$가 반대쪽을 오가며 매우 큰 거리를 이동하게 되어 최솟값에서 점점 멀어지게 됨
- 적절한 Learning rate를 설정하는 것 매우 중요
- Learning rate는 속도에만 영향을 주는 것은 아님
  - Learning rate 없이 미분값으로만 갱신을 진행하게 되면 최솟값으로 도달하지 않고 제자리에서 진동할 수도 있기 때문에 Learning rate를 곱하여 갱신값에 변화를 주며 최솟값에 도달하게 해야함

### Batch Gradient Descent Algorithm
- 경사 하강 알고리즘은 Batch Gradient Descent Algorithm에 해당
- Batch는 total training set임
  - 갱신을 하는 매 단계마다 전체 Training set을 활용하였기 때문에 이런 이름이 붙게 됨
- 장단점
  - 장점
    - 전체 업데이트가 한 번에 이뤄지므로 계산의 횟수가 적음
    - 전체 데이터에 대해 미분값을 계산하여 갱신하므로 안정적으로 수렴해감
  - 단점
    - 한번의 갱신에 전체 Training set이 사용되므로 학습이 오래 걸림
    - 갱신 직전까지 전체 Training set의 오차를 가지고 있어야 하므로 상대적으로 많은 메모리가 요구됨
    - Local minimum에 빠지면 나오기가 어려움
 
### 요약
1) Gradient descent algorithm은 비용함수(Cost Function)를 최소화하는 θ를 찾기 위한 알고리즘으로 기울기에 따라 θ를 반복적으로 갱신하면서 비용을 최소화시키는 θ에 도달한다.

2) Learning rate는 알고리즘의 학습 속도를 결정한다.

3) 경사 하강 알고리즘은 갱신 직전 값과 갱신 값이 같을 때 종료 된다.

### 단단한 머신러닝에서의 경사하강법
- 경사하강법 
  - 일종의 자주 사용되는 일차 최적화 방법
  - 무제약 최적화 문제에서 해를 구하는 가장 간단하고 전형적인 방법 중 하나
- 무제약 최적화 문제 $min_x f(x)$를 살펴보면, 여기서는 $f(x)$는 비분 가능한 연속 함수
  - 만약 하나의 수열 $x^0,x^1,x^2,...$을 만들어 다음을 만족한다면 국소 극소점에 수렴할 때까지 계속해서 해당 과정을 반복함
  - $f(x^{t+1}) < f(x^t), t=0,1,2,....$
  - 위의 식을 만족하고 싶다면 테일러 전개에 기반해 다음을 얻음
    - $f(x+ \triangle x) \cong f(x)+\triangle x^T\nabla f(x)$
    - 따라서 $f(x+ \triangle x) < f(x)$을 만족하려면 다음을 선택해야 함
      - $\triangle x = - \gamma \nabla f(x)$
      - 여기서 보폭 $\gamma$는 하나의 작은 상수 => 경사하강법


# Loss Surface
- 머신러닝 모델의 손실 함수가 그래프로 표현된 것
- 손실 함수 : 모델의 예측 결과와 실제 값 사이의 차이를 측정하고 모델을 최적화하는데 사용됨
  - 손실 함수의 그래프는 모델의 성능과 최적화 과정에 매우 중요한 역할을 함
- 특징
   1. 고차원 
      - 대부분의 머신러닝 모델은 매우 높은차원의 입력 공간에서 작동함
      - loss surface도 매우 높은 차원의 공간에 있는 함수로 볼 수 있음
   2. 비선형성
      - 많은 머신러닝 모델은 비선형 함수를 사용함
      - 이러한 모델의 손실 함수는 비선형적이며 loss surface는 매우 복잡한 형태를 가질 수 있음
   3. 지역 최소값
      - 일부 모델의 손실 함수는 지역 최솟값이 존재할 수 있음
      - 이러한 경우 모델은 최적의 해에 도달하지 못하고 지역 최소값에 빠질 수 있음
- 장단점
  - 장점
    - 모델을 최적화하는데 매우 중요한 정보를 제공함
      - 모델의 손실 함수를 시각화하면 모델이 수행하는 작업에 대한 이해를 높일 수 있으며 최적화 알고리즘의 성능을 개선할 수 있음
    - Overfitting과 Underfitting을 판단하는데 도움이 됨
      - Loss surface를 시각화하면 모델이 학습 데이터에 과적합되는지, 적절하게 일반화되는지 여부를 판단할 수 있음
  - 단점
    - 높은 차원의 함수이기 때문에 시각화하기 어려울 수 있음
      - 이를 해결하기 위해서는 차원 축소 기술을 사용하거나 일부 함수 값만 시각화해야 할 수도 있음
    - 일부 손실 함수는 지역 최솟값에 빠질 가능성이 있음
      - 모델의 최적화가 더 어려울 수 있음


# Attention


# Transformer
- 2017년 구글이 제안한 시퀀스-투-시퀀스 모델(sequence-to-sequence)
  - 최근 자연어 처리에서는 BERT나 GPT 같은 트랜스포머 기반 언어모델이 각광받고 있음 -> 성능이 좋기 때문

## (1) 시퀀스-투-시퀀스
- 트랜스포머(transformer) : 기계번역(machince translation) 등 시퀀스-투-시퀀스 과제를 수행하기 위한 모델
  - 시퀀스 : 단어 같은 무언가의 나열을 의미함
  - 시퀀스-투-시퀀스 : 특정 속성을 지닌 시퀀스를 다른 속성의 시퀀스로 변환하는 작업
    - 소스와 타깃의 길이가 달라도 해당 과제를 수행하는 데 문제가 없어야 함
  - 기계 번역 : 어떤 언어(소스 언어, source language)의 단어 시퀀스를 다른 언어(대상 언어, target language)의 단어 시퀀스로 변환하는 과제

## (2) 인코더와 디코더
- 트랜스포머는 시퀀스-투-시퀀스 과제 수행에 특화된 모델
  - 임의의 시퀀스를 해당 시퀀스와 속성이 다른 시퀀스로 변환하는 작업이라면 꼭 기계 번역이 아니더라도 수행할 수 있음
- 시퀀스-투-시퀀스 과제를 수행하는 모델 : 인코더(encoder), 디코더(decoder)
  - 인코더
    - 소스 시퀀스의 정보를 압축해 디코더로 보내주는 역할을 담당함
    - 인코딩 : 인코더가 소스 시퀀스 정보를 압축하는 과정
  - 디코더
    - 인코더가 보내준 소스 시퀀스 과정을 받아서 타겟 시퀀스를 생성함
    - 디코딩 : 타겟 시퀀스를 생성하는 과정
- 트랜스포머 역시 인코더와 디코더 구조를 따름
  - 인코더의 입력 : 소스 시퀀스
  - 디코더의 입력 : 타겟 시퀀스의 일부

## (3) 모델 학습과 인퍼런스
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/9a534985-4d1e-4b10-86ff-88891342f17b)

- 인코더 입력 : 어제, 카페, 갔었어, 거기, 사람 많더라 같이 소스 시퀀스 전체
- 디코더 입력 : <s>
  - <s> : 타겟 시퀀스의 시작을 뜻하는 스페셜 토큰
- 인코더는 소스 시퀀스를 압축해 디코더로 보내고 디코더는 인코더에서 보내온 정보와 현재 디코더 입력을 모두 감안해 다음 토큰(I)을 맞힘
  
- 트랜스포머의 최종 출력(디코더 출력, Output Probabilities)
  - 타겟 언어의 어휘 수만큼의 차원으로 구성된 벡터
    - 해당 벡터의 특징 : element 값이 모두 확률이라는 점
    - ex : 타겟 언어의 어휘가 총 3만개라고 가정해보면 디코더 출력은 3만 차원의 벡터임
      - 이 벡터의 element 값 3만개는 각각은 확률이므로 0이상 1이하의 값을 가지며 모두 더하면 1이 됨
- 트랜스포머의 학습
  - 인코더와 디코더 입력이 주어졌을 때 정답에 해당되는 단어의 확률 값을 높이는 방식으로 수행됨
  - 모델은 이번 시점의 정답인 I에 해당하는 확률은 높이고 나머지 단어의 확률은 낮아지도록 모델 전체를 갱신함
  
  
  

# few-shot learning
- 이해 과정
  - meta learning : 구분하는 방법을 배우는 학습 시도
    - learn to learn 이라고도 표현
- few-shot learning
  - meta learning의 한 종류
  - 배우는 법을 배우려면 많은 데이터가 필요한데 few shot learning은 구분하려는 문제의 데이터는 training set에 없어도 된다.
  - few shot learning을 위해 필요한 것들 
     1. Training set : 구분하는 법을 배움
     2. Query image : 어떤 클래스에 속하느냐의 문제를 푸는 것이 아니라 어떤 클래스와 같은 클래스냐의 문제를 푼다고 생각하면 됨
     3. Support set : Query image가 Support set 중 어느 것과 같은 종류인지를 맞추는데 도움을 줌

- few shot learning의 다른 점
  - Supervised learning의 경우
    - Test image(Query image)의 클래스가 Training set에 존재
      - ex) training set에 강아지 사진 존재, test image가 강아지 존재
  - few shot learning
    - training set에 없는 클래스를 맞추는 문제
      - ex) training set에 토끼 사진 없음, test image가 토끼 사진
    - Support set의 클래스 개수와 샘플 수를 기준으로 k-way n-shot이라는 표현을 씀
      - k-way : Support set이 k개의 클래스로 이루어짐
        - Query image가 k개의 클래스 중 어떤 것과 같은 것인지 묻는 문제가 되므로 k가 클수록 모델의 정확도는 낮아짐
      - n-shot : 각 클래스가 가진 sample의 개수로 비교해볼 사진이 많으면 많을수록 어떤 클래스에 속하는지 알기 쉽기 때문에 n이 클수록 모델의 정확도는 높아지게 됨
        - n이 1이 되면 one-shot learning이라고 부르게 됨

  - Transfer learning과 다른 점
    - Transfer learning
      - vision 분야에서 다른 도메인으로 학습된 모델의 layer의 일부를 얼리고 일부를 다른 도메인의 이미지로 fine-tuning하는 과정
      - 이 때 새로운 도메인의 경우 많은 라벨링된 데이터가 있을 수도 있음
    - few shot learning
      - 꼭 일부를 얼리고 fine-tuning하는 것을 의미하지는 않으며 (fine-tuning을 안해도 상관 없음) 말 그래도 새로운 도메인이 few(적게) 있는 경우를 지칭함


### 학습 방법
- few shot learning의 기본 학습 방법 : 유사성을 학습하는 것
  - 두 개의 사진이 주어졌을 때 각 사진을 잘 분석해서 두 사진이 유사한지 다른지를 판단할 수 있다면 Query image가 주어졌을 때 Support set의 사진들과 비교하여 어떤 클래스에 속하는지 알아낼 수 있음.
    - Learn a similarity function : sim(x,x`)
    - Ideally, sim(x1,x2)=1, sim(x1,x3)=0, and sim(x2,x3)=0
  - 많은 training set을 통해 각 사진별로 중요한 특징들을 잘 추출해서 "같다"와 "다르다"를 학습해야 함
  - 이후에 Query 이미지에 대해 Support set의 이미지들과 유사성을 구하고 가장 유사한 이미지를 가진 class로 분류할 수 있게 됨
 
### Dataset 구성
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/027ebed6-1be3-437f-9c64-a7d0d291ed5d)

- 위의 그림과 같이 Positive set, Negative set으로 구성하여 학습이 진행됨
  - 이 때 feature extraction을 잘 학습할 수 있는 모델을 디장니해야하는데 일반적인 Conv-Relu-Pool 구조도 충분히 적합함
- 기초 Few shot learning에서는 **샴 네트워크(Siamese Network)** 사용
  - 같은 CNN 모델을 사용하여 hidden representation을 구한 뒤 이 차이를 이용하는 형식
  - 이후 Positive pair에 대해서 한 번, Negative pair에 대해서 한 번 번걸아가며 학습을 진행
  - Prediction에서는 위에서 설명한 것과 같이 Support set의 이미지의 representation과 Query image의 representation 간의 차이를 샴 네트워크를 이용해 트레이닝에서의 방법과 같이 계산하여 유사성을 구할 수 있게 됨


### Few-shot Learning의 대표적인 두 접근 방법
- Data-Driven Approach : Support Set으로 주어진 데이터에 Transformation을 적용하거나  GAN을 이용해 모델을 학습시킬 충분한 양의 데이터를 생성하는 방법
  - 장점 : 그 방법이 간단하고 직관적
  - 단점 : Support set의 데이터가 데이터의 모집단을 보장할 수 없는 한계
- Model-based Approach : 모델이 같은 클래스의 이미지와 서로 다른 클래스의 이미지를 구분할 수 있게 하도록 Feature vector 간의 Similarity를 학습하게 하거나 적은 양의 데이터에 모델이 Overfitting되지 않도록 Regularization 등을 도입하는 방법


### Model-based Approach
- Metric-based Approach :  Distance나 Similarity와 같은 Metric을 이용
- Graph Neural Network(GNN)를 활용하는 방법 등도 존재

### Metric-based Approach
- 이미지 간의 Similarity나 Distance를 학습해 Query Data가 주어졌을 때 가장 Similarity가 높은 Supoort Set의 클래스로 예측하는 방법
- 모델에 Similarity를 학습시키기 위해 이미 레이블링이 되어 있는 방대한 양의 데이터를 활용할 수 있음
  - Novel Class(Target Domain) : 실제로 풀어야할 문제에서 예측할 클래스
  - Base Class(Source Domain) : 실제 예측을 하기 전에 방대한 양으로 활용할 데이터의 클래스
    - 모델이 적은 양의 Novel Class 데이터를 잘 활용했는지 정당하게 평가하기 위해 Novel Class와 Base Class는 겹치지 않아야 함
- 해당 방법에서 풀어야할 문제
  - 방대한 양의 Base Class 데이터를 이용해 모델을 미리 학습해놨다가 Novel Class로 주어진 Support Set을 적절하게 활용해 Query Set에서 Novel Class를 예측하는 문제로 바뀜
- 방대한 양의 Base Class 데이터를 활용해 Novel Class에 적용하는 방법
   1. Transfer Learning
      - Base Class 데이터셋을 이용해 학습한 후, Novel Class와 Support Set에 재학습하는 방법
      - 일반적으로 사용되는 Fine-Tuning도 여기에 속함
   2. Meta-Learning
      - 최근에 각광 받고 있는 접근법
      - Novel Class에서 Support Sset을 이용하여 Query Set 예측하는 것과 같이, Base Class에서도 특정 클래스 샘플들을 뽑아 임의로 Support Set과 Query Set으로 구성해 가상의 Episode를 설정하여 학습을 진행함
      - 이렇게 함으로써 실제 모델을 평가할 Few-shot 세팅을 데이터가 충분히 많은 Base Class 데이터셋에서 실험해볼 수 있음
      - 이러한 방법을 Episodic Training으로 부름

- Episodic Training
  - 실제 풀어야할 문제를 Support Set과 Query Set으로 나누듯이, Base Class을 이용해 학습할 때도 특정 Class를 선별하여 Support set과 Query Set을 뽑음
    - 이렇게 묶인 하나의 작업을 하나의 Episode 또는 Task라고 부름
  - ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/0849c2a4-043d-4f90-a871-9524f6b431f6)
  - 구체적인 절차
     1. Base Class(Source Domain)에서 N-Way에 해당하는 클래스를 랜덤으로 뽑음
     2. 해당하는 클래스당 K-shot개의 이미지, 레이블 쌍을 가져와 Support Set을 지정하고 다시 해당하는 클래스로 이루어진 Query Set을 정함
     3. 주어진 Support Set을 이용하여 Query Set을 평가한 후, 계산된 Loss를 이용해 모델을 업데이트해줌
     4. 1~3의 과정을 충분히 반복해 모델이 학습된 뒤, Novel Class(Target Domain)의 Support Set을 활용해 Query Set에 테스트함
  - Learning-to-Learn이라고 하여 학습 자체를 학습하는 방법을 제안함
    - 그런데 Meta-learning 방식이 제대로 된 검증과 정당하고 철저한 비교 실험이 부족함
    - 그래서 간단한 fine-tuning 기반 방법을 이요해 더 나은 성능을 얻을 수 있다고 말하고 있음

### Learning Similariy for Few-Shot Learning
- Query Set이 주어질 때, 해당 이미지가 Support Set의 어떤 클래스에 해당하는지 예측하는 방법
  - 딥러닝 모델을 통해 각각의 이미지로부터 Feature Vector를 추출하여, 가장 차이가 작은 Feature Vector의 클래스로 할당하는 방법
- Similarity 기반 Few-shot Learning 방법
  - 위의 아이디어에 착안해 동일한 클래스의 Feature Vector 간에 Similarity가 1이 되도록 모델을 학습시킴
  - 같은 클래스의 Feature Vector간의 Similarity는 1이 되도록, 서로 다른 클래스라면 Similarity가 0이 되도록 Loss Function을 설정하여 모델을 학습시킬 수 있음
  - Feature Vector간의 Similarity 계산
    - Similarity-Metric을 이용하여 다음과 같이 모델 구성할 수 있음
    - ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/a63a1472-27c1-4e39-bd62-081c6f8a965c)
      - $hat{x}$ : Query Set의 이미지
      - $x_i$, $y_i$ : Support Set에 속하는 이미지와 레이블을 의미함
      - 함수 f와 g: 각각의 이미지에서 Feature Vector를 추출하는 Feature Extractor 또는 Embedding 모듈
      - a : Similarity 함수
      - 위의 수식은 각각의 이미지로부터 Feature Vector를 추출하고 이에 대한 Similarity를 전부 계산한 뒤 해당 Support Set의 레이블에 해당하는 점수만 남겨두었다고 이해할 수 있음
- 위와 같이 Similarity 기반으로 모델을 구성하여 Meta-laerning 방식을 적용하면 다음과 같은 절차를 따름
   1. Base Class(Source Domain)에서 Support Set, Query Set을 포함한 하나의 Episode 선정
   2. 각각의 이미지로부터 Feature Vector를 추출한 후, Support Set과 Query Set를 쌍으로 묶어 모든 경우의 수에 따라 Similarity 계산
   3. 이렇게 계산한 Matrix를 Support Set의 one-hot encoding Ground-Truth(GT)와 매칭시켜 각 레이블에 따른 점수를 계산함
   4. 최종적으로 계산한 점수와 Query Set의 GT를 비교하여 Loss 계산
   5. 1~4의 방식을 반복하여 모델을 학습한 후, Novel Class(Target Domain)에서 Support Set에 대한 Query Set의 Similarity를 계싼해 클래스를 예측함


# Federated Learning(연합 학습)
## 위키페디아
- 각각 고유한 데이터 세트를 사용하는 여러 개의 독립적인 세션을 통해 알고리즘을 교육하는 기계 학습 기술
- 데이터 샘플을 명시적으로 교환하지 않고 로컬 노드에 포함된 여러 로컬 데이터 세트에서 심층 신경망과 같은 기계 학습 알고리즘을 교육하는 것을 목표
- 일반적인 원칙은 모든 노드가 공유하는 전역 모델을 생성하기 위해 일부 빈도로 이러한 로컬 노드 간에 매개 변수 (예: 심층 신경망의 가중치 및 편향)를 교환하고 로컬 데이터 샘플에 대한 로컬 모델을 교육

## 찾아서 정리
- 데이터를 한 곳에 집적시키지 않고 분산된 형태에서 데이터 분석을 수행
- 다수의 로컬 클라이언트와 하나의 중앙서버가 협력하여 데이터가 탈중앙화된 상황에서 글로벌 모델을 학습하는 기술(로컬 클라이언트 : 사물 인터넷 기기, 스마트폰 등)
- 장점 
  - 데이터 프라이버시 향상(개인정보가 보호되어야 하는 상황에서 데이터 유출 없이 학습이 가능)
  - 커뮤니케이션 효율성(로컬 모델의 업데이트 정보만을 주고 받음)
- 구성
  - 완전 탈중앙 학습
    - 연합학습의 기본적인 아이디어 : 중앙 서버에서 로컬 업데이트를 받아 글로벌 모델을 수정하는 방법으로 진행됨
    - 문제 : 중앙 서버의 존재는 때때로 문제가 되기도 하는데 단일 서버 모델이기 때문에 단일 장애 지점 문제가 있고 항상 서비스 가능한 상태가 아니기 때문에 장기적으로 보면 문제가 발생할 수도 있음
      - 이 문제를 해결하기 위해 네트워크 커뮤니케이션 방식을 Peer-to-Peer Network 형태로 변경하는 방법 -> 완전 탈중앙 학습
      - 
