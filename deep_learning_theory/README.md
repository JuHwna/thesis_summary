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
