# Image Classification(이미지 분류)
## 1. 이미지 분류 아이디어
- 이미지 분류 : 인공지능이 이미지를 분류해주는 것
  - 강아지 사진과 고양이 사진을 사람에게 보여주면 시각 이미지와 상식을 통해 사진을 구별해낼 수 있음
  - 컴퓨터가 이미지를 분류하는 방법
    - 이미지를 입력 받음 -> 컴퓨터는 미리 정해둔 카테고리가 존재함, 입력 사진이 어떤 카테고리에 속할지 결정을 해야함
    - 컴퓨터에게 이미지는 아주 큰 격자 모양의 숫자 집합으로 보임-> W*H*C (W: width, H: heigth, C: channel(RGB 그림의 경우 3))개의 픽셀 값으로 이루어짐
      - 이 숫자 집합으로 구별해내기 어려움
      - 같은 이미지를 보더라도 명암의 차이, 관점의 차이 등이 있을 수 있기 대문
      - 밑의 사항을 극복해야 함
        - 시점 변화(Viewpoint variation) : 이미지를 어느 방향에서 찍었는지에 따라 같은 대상도 다르게 보일 수 있음
        - 크기 변화(Scale variation) : 대상의 크기 변화에 따라 컴퓨터에 다른 이미지로 인식될 수 있음
        - 변형(Deformation) : 강체가 아닌 대상은 형태가 변형될 수 있음
        - 폐색(Occlusion) : 대상이 다른 물체에 의해 가려지거나 일부분만 보일 수 있음
        - 광원 조건(Illumination condition) : 조명을 받는지 유무와 그 정도에 따라 이미지가 다르게 보일 수 있음
        - 배경 클러터(Background clutter) : 대상이 배경에 섞여들어가 구분이 어려울 수 있음
        - 클래스 간 구별(Intra-class variation) : 대상이 속하는 레이블(클래스)의 범위가 너무 포괄적이어서 그 대상을 특정 짓지 못할 수 있음
### 이미지 분류 방법
#### 1) 데이터 기반 방법(Data-Driven Approach)
##### 1-1. Nearest Neighbor Classifier
- Nearest Neighbor(NN)
  - 컨볼루션 신경망 방법과는 아무 상관이 없고 실제 문제를 풀 때 자주 사용되지는 않지만 이미지 분류 문제에 대한 기본적인 접근 방법을 알 수 있도록 함
  - 예측 단계에서는 투입된 이미지와 가장 가까운 데이터의 레이블을 통해 예측하는 방법
  - 이미지와 이미지의 가까운 정도를 측정하는 지표
    - L1 distance
      - $$d1(I1,I2)=\sum(p|Ip1-Ip2)$$
    - L2 distance
      - $$d2(I1,I2)=\sqrt\sum(p(Ip1-Ip2)2)$$
    - 두 지표의 차이
      - L1과 L2는 p-norm 계열의 distance measure임
      - 두 지표의 큰 차이점 : L2 distance는 L1 distance를 사용하는 것보다 차이가 큰 것에 더 관대하지 않다는 것
        - L1이 아닌 L2 distance를 쓴다는 것은 여러 개의 dimension에서 적당한 차이를 보이는 것보다 하나의 dimension에서 큰 차이를 보이는 것에 더 페널티를 많이준다는 의미임
  - 단점
    - 단 하나의 label만 prediction에서 고려하기 때문에 안정성이 떨어지는 결과를 보여줌
    - 이상치(outlier)를 중심으로 섬과 같은 지역(decision boundary)가 생긴다는 것을 알 수 있음
      - 이상치에 민감하기 때문에 트레이닝 데이터에 국한된 규칙을 배울 가능성이 높음
         
##### 1-2. K-Nearest Neighbor Classifier
- NN을 보완하기 위해 K-nearest neighbor(KNN)를 활용할 수 있음
  - 예측 단계에서 인풋과 가까운 순으로 총 K개의 데이터의 레이블을 구한 후, 가장 빈번하게 나오는 레이블로 예측하는 방법
  - Voting 방법으로 볼 수 있음 -> 여러 개로부터 가장 빈번하게 나오는 것을 예측 결과로 하는 것
  - 학습 데이터셋에서 가장 가까운 하나의 이미지만을 찾는 것이 아니라 가장 가까운 k개의 이미지를 찾아서 테스트 이미지의 라벨에 투표하는 것
    - 직관적으로 k값이 커질수록 분류기는 이상점(outlier)에 더 강인하고 분류 경계가 부드러워지는 효과가 있음
    - 처음 보는 데이터(unseen data)에 대한 성능(generalization)이 높음
##### 1-3. Bayesian Classifier
- 베이즈 정리를 이용하여 입력 데이터가 특정 카테고리에 속하는지 분류함
  
#### 2) 규칙 기반 방법(Rule-Driven Approach)
- 정의 : 주어진 입력에 대해서 결과값을 도출하는 방법 => if-then 방식
  - 귀납적 사고 방식 : 예제에 대해 가설을 세우고 결과를 도출함
  - 규칙 기방 방법 종류 : Find-S 알고리즘, Version space/ Candidate 알고리즘
- 규칙 기반 학습이 타당하기 위해서 필요한 가정
  1. 우리가 알아볼 세상에서는 관측 오차(observation errors)가 없음
  2. 일관성이 없는 관측 또한 존재하지 않음
  3. 어떤 확률론적 요소(stochastic element)도 존재하지 않음
  4. 우리가 관측하는 정보가 시스템에 있는 모든 정보
  - 완벽한 세계 : 위의 네 가지 가정을 만족하는 곳 -> 규칙 기반 학습은 완벽한 세계에서 타당할 수 ㅣㅇㅆ음
##### 2-1. Find-S 알고리즘
- 정의 : 가장 구체적인 가설에서 시작하여 점점 General한 가설을 찾아내는 방법
- 가장 중요한 점 : 예제 중 positive training example만 선별한다는 것
  - 특정 예제로부터 도출된 결과를 다른 예제들에 반복하여 적용하여 변경된 부분만 don't care condition으로 설정하고 최종적인 가설을 만들어냄
- 단점 : 현실세계에서 사용하기에 한계가 존재함
  - 실제 세상에서는 고려해야할 부분이 많음
  - 최종적으로 하나의 일반화된 가설을 도출하기 때문에 가설의 집합이 존재하는 경우을 고려하지 않음
##### 2-2. Candidate Algorithm
- 예제에 일치하는 모든 가설의 집합(version space)를 도출하는 알고리즘
  - 하나의 일반적인 가설을 도출하는 Find-S 알고리즘에서 발전된 형태
- 구조
  - G : 매우 General한 가설에서 시작(negative 예제), S : 매우 Specific한 가설에서 시작(Positive 예제)
  - Version Space : 각자 조건을 더하거나 빼다보면 G와 S가 결국 만나게 되어 모든 가설의 집합이 됨
- 단점
  - 어떤 가설이 정확한지 알 수 없어 현실 세계에서는 사용할 수 없음
#### 결론
  - 규칙 기반 학습보다는 **데이터 기반 학습**을 통해 인공지능을 학습시킴

## 2. 이미지 분류 모델들
- Image Classification 아키텍처를 모델에 사용된 Layer수로 구분함
### 1) LeNet, AlexNet, ZFNET(레이어 8개 이하)
#### LeNet-5
- CNN을 처음 개발한 Yann LeCun의 연구팀이 1998년에 제시한 단순한 CNN임
- 등장 배경
  - LeNet 이전의 패턴인식에서 이용되는 모델은 Hand-designed feature extractor로 특징을 추출하고 FC multi layer networks를 분류기로 이용했음
    - 해당 방법의 문제점 존재
      - Hand designed feature extractor는 관련있는 정보만 수집하고 모관한 정보는 제거함
        - feature extractor에 의해 추출된 정보만 가지고 classifier의 학습이 진행되므로 학습에 제한이 있었음
        - LeCun은 feature extractor 그 자체에서 학습이 이루어져야 한다고 생각함
      - 이미지를 FC로 전환해 학습하는 방식은 너무 많은 parameter를 포함함
      - 입력값의 Topology가 완전히 무시됨
        - 이미지는 기본적으로 2D 구조를 가지고 있는데 이는 공간적으로 매우 큰 상관관계가 있음
        - FC는 이미지를 일렬로 펼치기 때문에 이런 공간적인 관계를 완전히 무시하게 됨
  - 위의 문제의 해결점으로 CNN을 제시함
    - CNN은 classifier 뿐 아니라 feature를 추출하는 단계 역시 학습이 진행되고 Weight sharing과 local connectivity에 의해 파라미터 수를 줄일 수 있으며 이미지의 공간적인 Topology를 반영할 수 있음
- 구조
- ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/7f72aa34-260d-410c-adf3-a3639b2eb2ae)
  - 주목할 점
    - C3 layer -> 모든 S2 feature map이 C3의 feature map에 연결되지 않았음
    - C3의 feature map과 연결된 S2의 feature map의 생김새
    - ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/dbe25638-b657-467a-a5a2-123b204bc232)
      - 모든 feature map을 연결하지 않아 Connection을 줄일 수 있고 서로 다른 입력값을 취하도록 해서 C3의 각 feature map이 서로 다른 feature를 추출하기 위해 그렇게 했다고 설명함
- 특징
  - Filter size : 5 x 5
  - strid : 1
  - Pooling : 2x2 average pooling
  - Activation function:
    - 대부분의 unit이 sigmoid를 사용
    - F6에서는 tanh를 사용
    - 최종적인 output layer인 F7에서는 RBF(Euclidian Radia basis function unit)을 사용
  - loss function : MSE
#### AlexNet
- 2012년 Alex Krizhevsky, llya Sutskever,Geoffrey Hinton에 의해 제시된 CNN architecture로 기본적인 구조는 LeNet과 비슷하나 GPU 2대를 이용하여 빠른 연산이 가능해지면서 병렬적인 구조를 가지게 됨
- 특징
  - Activation function
    - 처음으로 ReLU 사용
    - ReLU 사용 시, 기존에 사용하던 Tanh, Sigmoid function에 비해 6배 빠르게 원하는 수준 이하의 error rate에 도달할 수 있음
  - Over-fitting 방지를 위해 도입한 방법
    1. Data Augmentation : 데이터셋 이미지를 좌우 반전을 시키거나(flip augmentation), 이미지를 잘라서(Crop augmentation) 데이터 수를 늘림. 또 RGB 값을 조정하여 (jittering) 데이터 수를 늘림
    2. Dropout rate: 0.5
    3. Norm layer 사용 : 원시적인 형태의 batch normalization, 지금은 쓰이지 않음
  - Batch size: 128
  - SGD momentum : 0.9
  - Learning rate : 1e-2, validation accuracy에 따라 manual하게 낮춤
  - L2 weigh decay : 5e-4
  - 7 CNN ensemble : error 18.2% -> 15.4%
#### ZFNet
- AlexNet에 이어 ILSVRC 2013에서 우수한 구조이며 역시 CNN 기반 모델
- CNN 모델의 고질적인 문제 : Black box
  - 특정 layer는 이미지의 어떤 부분을 검출하는지, 모델이 왜 잘 작동하는지 알 수 없다는 점
- ZFNet은 feature map을 시각화하여 블랙박스를 들여다보고 모델의 성능을 개선하는 것을 목표로 고안됨
  - 위 그림과 같이 n-1번째 pooled maps이 "Convolution > ReLU activation > Max Pooling"을 통과하여 n번째 Pooled Maps을 생성하였다고 해보면 n번째 Pooled Maps에 해당 구조의 역과정을 수행하여 n-1번째 pooled maps을 복원해보고자 함
  1. Max unpooling
    - max pooling을 할 때 위치 정보를 같이 기억함
    - max pooling의 역과정을 수행할 때 max 값이 위치했던 영역에 max 값을 집어넣고 나머지 영역은 0으로 채움
  2. ReLU
    - ReLU를 통과하면 양수는 그대로 값이 보존되지만 음수 값은 모두 0으로 변경됨
    - 음수 값이 모두 소실되기 때문에 ReLU의 역과정은(양수->양수, 0->0)이 됨
  3. Transposed Convolution
    - Convolution의 역과정으로 Transposed Convolution을 시행함
- AlexNet의 각 layer를 시각화한 결과
  - Layer 1이나 2를 시각화한 결과, 이미지의 모서리, 경계, 색과 같은 low level feature를 잡아냄
  - Layer 3에서는 전반적인 패턴, 사물과 객체의 경계를 잡아내고 있음
  - Layer 5에서는 사물이나 개체의 전부를 보여주며 각각 다른 위치나 자세를 취하고 있는 모습을 잡아냄
 
- AlexNet을 수정하여 ZFNet으로
  - feature map을 시각화할 수 있으니 어떤 식으로 CNN 구조를 수정하면 성능이 좋아질지 어느 정도 예측할 수 있게 되었음
- 구조
  - AlexNet
    - Layer 1 : 11x11 Filter, Stride 4
    - Layer 2 : 5x5 Filter, Stride 1
  - ZFNet
    - Layer 1 : 7x7 Filter, Stride 2
    - Layer 2 : 3x3 Filter, Stride 2
### 2) VGG, GoogleNet(레이어 22개 이하)
- 두 논문 모두 논문 제목에서부터 본인들이 layer를 깊게 쌓았음을 강조
  - 더 네트워크를 깊게 만들었음은 이전 모델들과 핵심적인 차이점이자 좋은 성능을 내는 이유이기도 함
#### VGG-16/VGG-19
- VGGNet : 네트워크를 16~19층까지 쌓아 VGG를 기점으로 네트워크의 구조가 많이 깊어지게 됨
- 특징
  - 3X3의 보다 작은 필터를 사용함(VGG 이전에는 5X5를 주로 사용함)
    - 작은 필터가 주는 효과
      - 필터의 사이즈를 줄이면서보다 깊게 쌓았을 때 더 효율적인 receptive field를 가지게 됨
      - 더 넓은 필터를 쓰고 얇은 층을 쌓는 것이나 작은 필터를 쓰고 깊게 쌓는 것이나 receptive field가 같다는 의미
    - layer가 깊어지면서 다수의 activate function을 통과하므로 더 많은 non-linearity를 줄 수 있게 됨
    - 층 당 더 적은 수의 파라미터를 사용하게 됨
      - ex) 10×10 image에 7×7 filter 적용하여 4×4 feature map 생성 → parameter 개수: 49개
      - ex) 10×10 image에 3×3 filter 3번 적용하여 4×4 feature map 생성 → parameter 개수: 9개씩 3번 총 27개
  - padding을 이용해 이미지 사이즈를 유지하게 됨
    - padding이 주는 효과
      - 이전에는 Convolution 연산의 특징상 layer가 깊어지게 되면 가장자리 부분이 주는 영향력이 점점 줄어들게 되고 이미지 사이즈를 유지할 수 없었음
      - VGG부터는 padding을 도입하여서 Network가 깊어져도 이미지 사이즈를 유지할 수 있게 됨
#### GoogleNet(inception - v1)
- 22층의 구조임
- 특징
  - 22 layers
  - 효과적인 inception module
  - FC layer 없음(output layer에서만 한 번 나옴)
  - 오직 500만개의 파라미터 사용
- Inception module
  - Googlenet은 inception module이 여러차례 반복되는 형태로 이루어짐
  - inception module의 기본적인 아이디어 : 뭐가 optimal인지 모르지만 다해서 넣어보자, 그럼 optimal을 뽑아내도록 학습하겠지
  - 초창기
    - naive inception module : 1x1 convolution, 3x3 convolution, 5x5 convolution 그리고 3x3 max pooling 4가지를 병렬적으로 처리하고 output을 concat함
    - 이는 실제로는 잘 작동하지 않음 -> 여러가지 convolution 및 pooling의 output을 하나로 concat하는 것은 dimension을 상당히 늘릴 수 밖에 없었고 너무나도 비효율적이었음
  - 그 다음 단계
    - inception module 안에 1x1 convolution 층을 추가함
    - Convolution 연산은 연산량이 많으므로 Convolution 연산 전에 dimension을 줄여주고 max pooling은 Convolution에 비해 간단하니 연산 이후에 dimension을 줄여 모든 output을 concat함
    - 위의 방식을 통해 inception은 계산상의 어려움 없이 layer를 늘릴 수 있게 됨
    - 병렬적으로 수행된 연산들은 inception module을 나오면서 concat되어 다음 layer로 넘어감
- 1x1 Convolution의 역할
  - Network in Network(Lin et al)에서 소개된 개념
    - inception에서는 bottleneck layer라고도 부름
    - Dimension이 깊은 network에 대해 각 포인트마다 중요하다고 생각되는 정보를 뽑아내는 역할을 한다고 볼 수 있음
  - inception에서는 channel 수를 줄여 계산상에서의 이점을 보도록 도와주고 비선형성을 증가시켜 더 복잡한 함수도 approximation할 수 있도록 도와주는 역할을 함
- Inception의 Auxilary classifier
  - Auxilary classifier : 중간중간에 output을 내는 구조
  - GoogleNet에서 처음 도입한 방법
  - 중간중간에 Output을 먼저 만들고 이를 Back propagation시 반영해 Layer가 깊어짐에 따라 발생할 수 있는 Gradient vanishing/ explosion을 방지함
  - 초창기 모델인 GoogleNet(Inception-v1)의 경우, Auxilary classifier를 2개 씀
    - Inception-v2,v3부터는 Auxilary classifier를 1개 씀
    - Inception-v4부터는 Auxilary classifier를 아예 안 씀
      - Auxilary classifier를 사용하지 않는 이유
        - 문제가 존재
          - 초반 Layer에서 output을 내고 이걸 Backpropagation에 반영하면 당연하게도 초반 Layer에서 잘 classification을 잘 학습시킬 수 있는 방향이 어느정도 반영되어 학습이 진행될 것임.
          - 이에 따라 최종 Classification layer에서 optimal한 feature가 뽑히지 않는 문제가 있음


### 3)ResNet,ResNet의 확장(레이어 152개 이하)
- CNN을 연구하면서 20층 이상부터 성능이 낮아지는 현상인 Degradation 문제가 발생함
- ResNet은 Residual Learning이라는 개념을 통해 모델의 층이 깊어져도 학습이 잘 되도록 구현함
- 매주 깊은 네트워크의 문제점
  - plain convolutional neural network에서 layer를 무작정 늘렸을 때 성능이 오히려 떨어짐
    - Training에서도 Test에서도 성능이 좋지 않았기 때문에 overfitting 때문이 아님
    - Gradient vanishing/ explosing이 발생
    - 또는 Degradation Problem이 발생
      - layer가 어느정도 이상으로 깊어지면 오히려 성능이 안 좋아지는 현상
  - 해당 현상의 원인을 optimization이라고 추측해서
    - 새로운 Optimizer을 만들거나 깊어지더라도 쉽게 Optimization을 할 수 있는 새로운 architecture를 만들어 문제를 해결할 수 있음
  - 하지만 새로운 optimizer를 만든 것은 매우 어렵기 때문에 새로운 Network를 만드는데 집중
- Residual block
  - H(x)를 기존의 네트워크라고 할 때, H(x)를 복잡한 함수에 근사시키는 것보다 F(x)=H(x)-x일 때, H(x)=F(x)+x이고, F(x)+x를 근사시키는 것이 더 쉬울 것이라는 아이디어에서 출발함
  - F(x)의 정의 : Output에서 자기자신을 빼는 것 -> Residual learning이라는 이름을 갖게 됨
  - skip connection : x가 F(x)를 통과하고 나서 다시 x를 더해줌
  - ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/8e6bc87d-16b3-4459-9353-c9acbbd87102)
    - x : 입력값
    - F(x) : CNN Layer -> ReLU -> CNN Layer을 통과한 출력값
    - H(x) : CNN Layer -> ReLU -> CNN Layer -> ReLU를 통과한 출력값
  - 기존 신경망
    - H(x)가 정답값 y에 정확히 매핑이 되는 함수를 찾는 것을 목적으로 했음
    - 신경망은 학습을 하면서 H(x)-y의 값을 최소화시키면서 결국 H(x)=y가 되는 함수를 찾았음
    - 위 그림에서 H(x)는 Identitiy를 매핑해주는 함수이기 때문에 H(x)-x를 최소화하면서 H(x)=x가 되는 것을 목표로 함
      - H(x)-x=0
  - ResNet
    - H(x)-x=F(x)로 두어 F(x)를 최소화 시키려고 함
      - F(x)=0이라는 목표를 두고 학습을 진행함
    - 이렇게 학습을 진행하면 F(x)=0이라는 목표값이 주어지기 때문에 학습이 더 쉬워짐
    - **Skip Connection** : H(x)=F(x)+x가 되는데 이 때 입력값인 x를 사용하기 위해 쓰는 것
      - 입력값이 일정 층들을 건너뛰어 출력에 더할 수 있게 하는 역할을 함
    - 일반적인 CNN에서 나타나는 "main path"와 Skip Connection에 의해 연결되는 short cut을 가지게 됨
- Deeper bottleneck architecture
  - 50층 이상의 깊은 모델에서는 Inception에서와 마찬가지로, 연산상의 이점을 위해 bottleneck layer (1x1 convolution)을 이용했음
  - ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/f972a9fc-30b4-4c8a-992b-9243ee0c1594)
    - 기존의 Residual Block : 한 블록에 Convolution layer(3x3) 2개가 있는 구조
    - Bottleneck : 오른쪽 그림의 구조로 바뀜
      - 층이 하나가 더 생겼지만 Convolution Layer(1x1) 2개를 사용하기 때문에 파라미터 수가 감소하여 연산량이 줄어듬
      - layer가 많아짐에 따라 Activation Function이 증가하여 더 많은 non-linearity가 들어갔음
        - inputㅇㄹ 기존보다 다양하게 가공할 수 있게 됨
  - ResNet은 Skip Connection을 이용한 Shortcut과 Bottleneck 구조를 이용하여 더 깊게 층을 쌓을 수 있었음
- ResNet이 잘 되는 이유
  - Skip Connection을 통해 엄청나게 깊은 네트워크를 만들어주고 Optimal depth에서의 값을 바로 Output으로 보내버릴 수 있음
    - Main path에서 optimal depth 이후의 weight와 bias가 전부 0에 수렴하도록 학습된다면 optimal depth에서의 output이 바로 classification으로 넘어갈 수 있음
    - optimal depth 이후의 block은 모두 빈깡통임

### 4) ResNet의 확장
#### Identity Mappings in Deep Residual Networks
- 해당 논문은 Residual이 왜 깊은 모델임에도 성능이 잘 나오는지를 설명 + 추가적인 아키텍처를 더하여 성능을 높임


#### Wide Residual Networks(WRN)
- residual network의 넓이를 증가시키고 깊이를 감소시킨 모델
  - 신경망의 넓이를 증가한다는 의미 : filter 수를 증가시킨다는 의미
  - residual block을 구성하는 convolution layer의 filter 수를 증가시켜서 신경망의 넓이를 증가시킴
- 등장 배경
  - Pre-Activation ResNet : Residual block 내의 활성화 함수의 순서(Conv-BN-ReLU-> BN-ReLU-Conv)를 바꿔서 초기 입력값이 최종 출력값에 도달하도록 함
  - 저자는 깊이와 활성화 함수의 순서를 제외하고 ResNet의 넓이에 따른 정확도 양상을 실험함
    - WRN
      - Residual blcok의 넓이를 증가시키는 것이 모델의 깊이를 증가시키는 것보다 효과적으로 성능을 향상시킬 수 있다고 함
      - 16 layer의 WRN은 1000-layer의 ResNet의 성능을 뛰어 넘는 결과를 보여줌
      - 학습 속도도 몇배는 빠름
- ResNet의 문제점
  - (1) circuit complexity theory
    - circuit complexity theory : 얇은 circuit는 깊은 circuit보다 더 많은 요소들을 필요로 한다는 이론
      - 깊은 신경망이 갖는 표현력을 얇은 신경망이 갖기 위해서는 엄청나게 넓은 신경망을 구성해야 된다고 생각해볼 수 있음
      - 넓은 신경망을 구성하는 것은 parameter 수도 증가한다는 것을 의미
    - ResNet은 이 이론을 접목시킴 -> bottleneck 구조를 제안함
      - 해당 구조는 모델을 얇게 해 parameter 수를 감소시켜 깊이를 증가시킴
      - residual block을 최대한 얇게 구성하여 모델의 깊이를 엄청나게 증가시킴
  - (2) Diminishing feature reuse
    - 순전파에서 발생하는 문제
      - 기울기 소실과 비슷한 문제
      - 입력과 가까운 계층이 학습한 특징이 최종 계층까지 도달하지 못하고 사라지는 문제
        - 많은 수의 가중치가 곱해져서 발생
    - 해결 방법
      - Stochastic Depth ResNet 논문 : 무작위로 residual block을 제거함
        - dropout의 일종
      - WRN : residual block에 dropout을 적용함
        - residual block 내에서 dropout은 convolutional layer 사이에 적용함
  - WRN의 해결방법
    - (1) 넓이를 증가시켜서 해결
    - (2) residual block 내에 있는 convolution layer 사이에 dropout을 적용
- WRN(Wide residual networks) 내용
  - ResNet은 깊이에 따라 두 가지 블록을 사용하여 모델을 정의
    - 얕은 모델인 ResNet-18, ResNet-34
      - Basic Block : 3x3 크기의 합성곱 연산을 2번 사용한 skip connection을 적용함
    - 더 깊은 모델(ResNet-50, ResNet-101 등)
      - BottleNeck Block : 연산량의 이점을 얻기 위해 1x1 합성곱을 적용하여 채널의 개수를 줄이고 3x3 합성곱을 적용한 뒤 다시 기존의 채널의 개수로 늘려주는 과정임
  - PreAct ResNet
    - Identity path의 중요성과 Activation function의 순서에 따른 성능 변화를 분석
    - 기존의 ResNet의 연산 순서였던 Conv-bn-relu -> bn-relu-conv로 순서로 변경하게 됨
      - 후자가 더 빠르게 학습되고 더 나은 결과를 가져옴
  - Residual Block의 표현력(representation power)을 늘리기 위해 선택할 수 있는 방법
    1) 블록별로 합성곱 계층을 더 추가하기
      - 연산량의 이점을 잃어버림 -> 선택x
    2) 각 합성곱 계층이 더 많은 특징 맵 채널을 만들 수 있게 하기
      - 고려 O
      - 채널의 개수 : 너비
    3) 합성곱 계층의 필터 크기를 증가하기
      - VGGNet에서 언급했다싶이 3x3 크기의 합성곱을 사용하는 것이 굉장히 효율적이기 때문에 고려대상이 아님x
      - 작은 필터가 성능이 좋음
  
  - (1) Residual Block
    - ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/86f0a106-47d9-4386-bcb7-feef13d22fb1)
    - (a) basic : 3x3 conv- BN(batch normalization) - ReLU - 3x3 conv - BN - ReLU 
    - (b) bottlenet : 1x1 conv(차원 축소) - BN - ReLU - 3x3 conv - BN - ReLU - 1x1 conv(차원 확대) - BN - ReLU
      - 해당 구조는 모델을 얇게 만들기 위해 사용하므로 WRN에서는 사용하지 않음
    - (c)와 (d) : WRN에서 정의한 새로운 블록 모양
      - 3X3 크기의 합성곱 계층이 (a)와 (b)에 비해 훨씬 넓은 것을 볼 수 있음
      - 깊이가 아닌 각 블록에서 3x3 크기의 합성곱 계층의 출력 특징맵의 채널 개수를 증가시키게 되면 깊은 모델이 아니더라도 성능을 향상시킬 수 있다고 주장
    - WRN에 추가된 파라미터
      - 깊이 l : 모델의 깊이
      - 너비 k : 기존의 Basic Block의 3x3 크기의 합성곱 계층의 출력 특징맵의 채널 개수에 곱하는 요소
        - k가 클수록 더욱 넓은 모델이 되는 것
  - (2) WRN architecture
    - ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/29fec7f0-9c10-4f1e-a078-26244ec73266)
  - (3) 새로운 기호 도입
      - $B(M)$ : residual block의 구조
      - M : 해당 블록에서 사용된 합성곱 계층의 필터 크기
        - $B(3,1)$ : 3x3 크기의 합성곱과 1x1 크기의 합성곱을 Residual Block에서 사용했음을 의미
      - 다양한 조합의 필터 크기에 대한 실험을 진행함
        - 실험하는 블록
          - (1) B(3,3) : Residual Block의 Basic Block
          - (2) B(3,1,3) : Residual Block의 Basic Block에서 가운데 1x1 합성곱 계층 추가
          - (3) B(1,3,1) : Residual Block의 BottleNeck Block
          - (4) B(1,3) : 1x1 합성곱 적용 후 3x3 합성곱 적용
          - (5) B(3,1) : 3x3 합성곱 적용 후 1x1 합성곱 적용
          - (6) B(3,1,1) : Network-In-Network 스타일의 구조
  - 실험의 결과
    - (1) Types of Convolutions in Residual Block
      - ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/0f565af7-d76e-4c1e-8e38-fca7c09030a0)
      - 깊이를 조절하면서 전체 파라미터의 개수를 맞추어 실험을 한 모습
      - 실험 결과 : WRN-28-2-B(3,3)이 WRN-22-2-B(3,1,3)에 비해서 아주 살짝 성능이 향상됨
    - (2) Number of Convolutions per Block
      - ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/3a4c8682-1991-4f49-a352-2a6a3bc82f18)
      - 블록별로 합성곱 계층의 개수를 다르게 하면서 실험을 진행함
      - 2개의 계층을 사용했을 때 최고의 성능이 나옴
    - (3) Width of Residual Blocks
      - ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/93e8cbf8-2488-44aa-b859-e5e278959e4a)
      - Widening Factor k와 Depth l에 대한 성능 변화를 측정
      - k=1이라면 기존의 ResNet과 동일한 구조
      - l=40으로 고정하고 성능을 비교해보면 k가 증가함에 따라 성능이 일관되게 향상되고 있음
        - 기존의 ResNet과 비교해보면 k가 증가함에 따라 성능이 향상되고 있음
      - k=10으로 고정 시, 깊어질수록 성능이 좋아짐
      - WRN-28-10 vs WRN-40-8
        - 깊이가 깊지 않음에도 Widening Factor K를 증가시킴으로써 충분히 좋은 성능을 낼 수 있음
    - (4) Comparison between Other Models
      - ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/b3a66a3a-8520-4e59-9349-5be606296b1a)
        - 해당 실험은 심층 신경망을 설계할 때 너비에 대한 중요도가 생각보다 높음을 의미
        - 깊이는 정규화 효과를 일으키고 너비는 과적합을 일으킨다는 이전의 주장에도 불구하고 ResNet-1001보다 몇 배 더 많은 매개변수를 가진 네트워크를 성공적으로 교육시킴
      - ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/4a72125b-0fff-461f-9d4f-3d11141a46f0)
        - ResNet과 WRN 사이의 에폭에 따른 손실함수 경향성을 비교하고 있음
        - 과적합을 막으려면 시험 손실함수와 훈련 손실함수의 차이가 적어야함
          - WRN은 ResNet보다 두 차이가 적기 때문에 과적합이 방지되고 있음
    - (5) Dropout in Residual Blocks
      - Dropout은 모델의 깊이가 상대적으로 깊을 때 더 높은 성능 향상을 얻을 수 있다는 것을 볼 수 있음
      - Droupout 그 자체로 얇은 네트워크와 넓은 네트워크에서의 효과적인 regularization 기술임
    - (6) ImageNet Classification
    - 실험 내용 요약
      - Widening은 다른 depth를 가지는 Residual Network 사이에서 일관적으로 성능을 향상함
      - 깊이와 너비 둘 다 증가시키는 것은 파라미터의 수가 너무 많아지거나 혹은 더 강력한 regularization이 요구될 때까지는 도움이 됨
      - 얇은 신경망과 동일한 수의 매개변수를 가진 넓은 신경망이 동일하거나 더 나은 성능을 낼 수 있기 때문에 Residual Network의 매우 깊은 깊이는 정규화 효과가 없는 것으로 보임. Wide Network는 얇은 네트워크보다 2배 이상의 많은 수의 매개변수를 사용하여 성공적으로 학습할 수 있음
    - (7) Computational efficiency
      - width를 증가시키는 것은 효과적으로 Computation을 균형 맞추는데 더욱 최적의 방식으로 도움을 주며, 얇은 네트워크보다 넓은 네트워크가 몇 배는 더 효율적임
      - ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/a64dd4a3-e493-4ede-ac7a-72054a10c0cd)
        - CIFAR에서 최고의 성능을 낸 WRN-28-10가 thin ResNet-1001보다 1.6배 더 빠름
        - wide WRN-40-4는 ResNet-1001와 거의 유사한 accuary를 가지지만 8배 더 빠름
  - Reference
    - https://everyday-image-processing.tistory.com/456
    - https://mldlcvmjw.tistory.com/297
    - https://cumulu-s.tistory.com/35
    - https://deep-learning-study.tistory.com/519
#### ResNeXt

#### Deep Networks with Stochastic Depth

#### SeNet

#### DenseNet






## 4. Vision Transformer
- NLP 분야에서의 트랜스포머를 컴퓨터 비전에 적용한 네트워크
- CNN만 이용한 네트워크보다 좋은 성능을 보여주고 있음
### 요약
- 논문에서 제시한 ViT
  - Transformer의 Encoder부분(Self-Attention)을 그대로 응용함
  - 논문이 주는 강력한 메세지 : Vision Task에서 CNN을 이용하지 않고 충분한 퍼포먼스를 낼 수 있다는 점
  - 단점 : 충분한 데이터 셋으로 Pretrain하고 타켓 도메인에 Fine-tuning해야 성능을 제대로 발휘할 수 있다는 점
  - ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/c2d9310b-b47a-4b39-8c49-96eafc43a230)


### 네트워크 구조
#### 1) Image Patch 만들기
- 트랜스포머는 NLP 분야에서 출발한만큼 1D 임베딩들을 필요로 함
  - 그래서 이미지 패치를 만들어 1D 임베딩을 만들어 나감
  - EX) [300,300,3]의 이미지를 [100,100,3] 이미지 9개로 만들었음
#### 2-1) Patch Embedding 만들기
- 패치화된 각 이미지를 1차원으로 만듦(Linear Projection)
  - 앞서 하나의 패치가 [100,100,3]이었다면 각 픽셀들을 일렬로 이어 붙여서 [1,100x100x3]인 1차원으로 만듦
  - 식
    - $$x \in R^{H \times W \times C}$$ -> 원래 이미지 size
    - $$x_p \in R^{N \times (P^2 \times C)}$$ -> Flatten한 뒤, ViT에 입력 : 벡터로 처리하여 입력
    - $$N= \frac{HW}{P^2}$$
      - N : Transformer의 sequence 길이(패치 수)
      - P : 패치의 크기, 패치는 정사각형
      - where 원본 이미지 해상도 : (H,W), 각 이미지 패치 해상도 : (P,P)

#### 2-2) Class token 만들기
- BERT의 CLS token과 유사하게, 임베딩된 patch의 맨 앞에 하나의 학습 가능한 Class token을 추가했음
  - Class token : Transformer의 여러 encoder 층을 거쳐 최종 output으로 나왔을 때, 이미지에 대한 1차원 representation vector로써의 역할을 수행함
 
#### 2-3) Position Embedding
- 1차원으로 만든 벡터에 같은 차원의 Position Embedding을 더해줌
- Position Embedding
  - 오리지널 Transformer와 같이 임베딩에 순서 정보를 부여하기 위해서임
  - 하지만 이 부분은 Optional이라고 소개한 사이트도 있는 것으로 보아 꼭 필요한 알고리즘은 아닌 것 같음)
- 해당 과정을 마치면 전체 이미지는 [1,100x100x3] 차원의 embedding vector 10개로 정의되며 이후 Transformer의 Encoder로 들어가게 됨

#### 3-1) Layer Normalization
- 모든 이미지 임베딩을 채널 기준으로 Layer Normalization을 함

#### 3-2) Multi-Head Self Attention(MSA)
- Patch + Position Embedding을 이용하여 Self-Attention을 수행하기 위해 임베딩 1개당 1개씩의 q(쿼리), k(키), v(밸류)를 학습 가중치 W_q, W_k, W_v를 이용하여 구함
  - 만약 num_heads를 12이라고 하면 각 임배딩마다 [1,100x100x3/12] 차원의 q, k, v를 가지게 됨
- 이렇게 구한 q, k, v를 이용하여 Attention Value를 구하고 이것들을 차원방향으로 concat하여 Multi-head Attetion을 만듦
  
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/bde625f4-c9a2-46ac-a7a8-166f6312764e)


- 12번 self-attetion을 수행한다고 하면 image patch 한 개의 Attetion Value Matrix는 [1,100x100x3/12] 차원을 가짐
- num_heads 갯수인 12개 Attetion Value Matrix를 구하여 차원 방향으로 concat하면 한 개의 image patch당 [1100x100x3]개의 오리지널 임베딩의 차원을 회복함


#### 3-3) Residual Connection (잔차 연결)
- 2단계에서 구한 input 임베딩과 3-2단계에서 구한 multi-head attention을 더해 잔차 연결을 함
  - 차원 : [10,1,100x100x3]으로 동일

#### 4-1) Layer Normalization
- 3-3단계에서 잔차 연결한 Matrix를 3-1번과 동일하게 채널 기준으로 Normalization을 실시함

#### 4-2) Multi Layer Perceptron(MLP)
- 두 개의 Linear Layer로 구성되며 첫 번째 레이어에서 임베딩 사이즈를 확장하고 두 번째 레이어에서 원래의 임베딩 사이즈로 복원함
  
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/ee42ac97-d414-4671-9b10-0cab45f88e50)

#### 4-3) Residual Connection(잔차 연결)
- 4-2단계에서 구한 Matrix와 3-3단계의 Matrix를 더해 최종 output feature를 만듦
- 2번 input embedding이 3,4단계를 거쳐 최종 output feature를 만드는 과정을 수식으로 정리하면 아래와 같이 표현 가능

![image](https://github.com/JuHwna/thesis_summary/assets/49123169/02a1601e-f8da-4cb5-a724-e86e79847055)

#### 5) Multi Layer Perceptron (MLP) head

![image](https://github.com/JuHwna/thesis_summary/assets/49123169/257cdfed-82a9-47cb-b2e2-0bbdc9a861f4)

- Transformer의 output 출력단이라고 할 수 있으며 일반적인 CNN의 Image classifier와 동일함
- 특이한 것은 Class token만을 사용한다는 점
  - class token이 Transformer의 여러 encoder 층과 Layer Normalization을 거쳐 최종 output, y가 나왔을 때, 이 y가 이미지에 대한 1차원 representation vector로써의 역할을 수행하기 때문
- MLP의 경우, y를 Flatten한 후 단순 Linear Layer를 통과시켜 classification을 수행함


### ViT Training & Fine-Tuning
- large-scale dataset에 대해 ViT를 pre-train하고 downstream task에 대해 fine-tuning을 수행함
  - pre-trained Multi Layer Perceptron(MLP) head를 제거하고 0으로 초기화된 D×K feedforward layer를 추가함
  - D : 100×100×3
  - K : downstream class의 개수

## 5. CoAtNet(Convolution+Transformer)

### Background
- 2021년 6월, Google AI팀에서 EfficientNet-V2와 함께 발표
- ImageNet top 1 accuracy SOTA를 갈아치운 모델
- Convolution과 Attetion을 합친 방법을 제시

### ViT의 문제점
- JFT-300(3억개 정도)같은 엄청난 양의 데이터가 주어졌을 때 CNN보다 성능이 좋음
- 하지만 그보다 못한 데이터 양이면 일반적으로 vanilla ResNet(기본적인 ResNet)보다도 성능이 떨어짐
  - 이유 : CNN이 가지는 고유의 inductive bias보다 ViT가 가지는 inductive bias가 약하기 때문임
    - inductive bias : 지금까지 만나보지 못했던 이미지를 봤을 때 정확한 판단을 내리기 위해 사용하는 추가적인 가정
    - 
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/91067ad2-4d77-4f56-be57-1104be0b071d)

- CNN의 inductive bias : **Locality**
  - 모델의 설계 자체에 Vision task는 지역적인 정보에서 중요한게 많다는 가정이 깔려있는 것
    - 실제로 Vision task에서는 적절한 가정
    - CNN 특유의 generalization이 잘 된다는 특징 역시 이 가정을 기반으로 한 모델이기에 가능한 것
  - 단점 : Global한 정보를 잘 이용하지 못함
    - 이러한 단점을 보완하기 위해 receptive field를 넓히기 위해 층을 깊게 쌓는 식으로 진화해 왔음
- CNN의 Locality와 ViT의 Self-attention, Input-dependent weightning을 모두 이용할 수 있는 방법
  - 시도한 방법 : 어떻게 Convolution에 Self-attention의 특징을 추가할지, 어떻게 ViT에 Convolution의 특징을 추가할지를 고민하는 방향으로 진행되었음
  - 하지만 어떻게 넣느냐만큼이나 중요한 것이 각각의 특징을 얼마나 포함시켜 섞을지도 중요한 문제
  - 이를 고려하여 제시된 모델 : CoatNet

### Convolution과 Attention
- CNN과 transformer를 베이스로 한 architecture는 상술했듯 각각의 장단점이 있음
- Convolution과 Attention을 합치기 위해서 이 둘의 특징을 분석(CoatNet의 저자들은 둘 각각의 시스템적인 분석을 진행했음)
  - Convolution layer : 빠르게 수렴할 수 있고 특유의 inductive bias(Locality, parameter sharing) 덕택에 generalization을 잘함
    - translation equivariance
    - 논문에서는 주로 MobileNet의 MBConv block에 초점을 맞췄음
    - Attention의 FFN이 채널을 늘였다가 줄이는 Inverted Bottle neck이 MBConv와 유사하다고 판단
  - Attention은 CNN과 반대로 Global receptive field를 가지고 Input-dependent한 weight는 여러 spatial position들 사이의 관계성을 잘 포착할 수 있으며 CNN과 비교했을 때 Capacity가 높음 -> 더 큰 dataset에 적합함
 
- Computer vision의 문제를 해결하기 위해
  - Conv layer로부터 Translation Equivariance를,
  - Attention layer로부터는 Input-adaptive weighting과 Global receptive field라는 장점을 가져와야 한다고 생각해볼 수 있음

![image](https://github.com/JuHwna/thesis_summary/assets/49123169/ba2b4d61-8d0a-4428-8b92-964c972b696f)

- 저자들은 Attention에 Global static convolution kernel을 추가해서 시도했음
  - Softmax 후에 넣을지, 전에 넣을지 두 가지 경우로 나눌 수 있음
    - 이런 방법은 Relative Attetio이라고 정의했음
   
### 다양한 Block들을 어떻게 합칠 것인가?

- Attention의 실용성을 해치는 가장 큰 원인 : 토큰의 제곱으로 증가하는 연산량
- Attention을 기반으로 한 architecture들을 다양한 방법으로 Attention의 연산 방식을 바꿔 연산량을 줄이려는 시도를 했음
  - ViT의 경우 이미지를 패치로 잘라 토큰을 줄이는 전략을 취함
- CoatNet에서는 multi-stage layout을 이용해 ConvNet이 5개의 stage를 갖도록 구성했음
  - S0 : simple 2-layer convolution 적용
  - S1 : MBConv block과 Squeeze-excitation 적용
  - S2-S4 : Convolution이 Local pattern 처리에 유리하다는 가정에 입각하여 각 stage의 초반부에는 Convolution(MBConv)을 넣고 뒤쪽에는 Transformer stage를 넣었음
    - C를 Convolution, T를 transformer라고 했을 때
    - 구성 : C-C-C-C, C-C-C-T, C-C-T-T, C-T-T-T

### 모델 결정
- 저자들은 Convolution의 장점인 generalization과 Attention의 장점인 model Capacity의 관점에서 비교를 진행했음
  - Generalization : train과 validation score의 최소 gap
  - Capacity : Overfit 없이 학습할 수 있는 데이터셋의 크기
