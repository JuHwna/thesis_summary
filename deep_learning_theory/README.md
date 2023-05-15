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
