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
- 이미지 분류 방법
  - 1) 데이터 기반 방법(Data-Driven Approach)
    - 1-1. Nearest Neighbor Classifier
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
             
    - 1-2. K-Nearest Neighbor Classifier
      - NN을 보완하기 위해 K-nearest neighbor(KNN)를 활용할 수 있음
        - 예측 단계에서 인풋과 가까운 순으로 총 K개의 데이터의 레이블을 구한 후, 가장 빈번하게 나오는 레이블로 예측하는 방법
        - Voting 방법으로 볼 수 있음 -> 여러 개로부터 가장 빈번하게 나오는 것을 예측 결과로 하는 것
        - 학습 데이터셋에서 가장 가까운 하나의 이미지만을 찾는 것이 아니라 가장 가까운 k개의 이미지를 찾아서 테스트 이미지의 라벨에 투표하는 것
          - 직관적으로 k값이 커질수록 분류기는 이상점(outlier)에 더 강인하고 분류 경계가 부드러워지는 효과가 있음
          - 처음 보는 데이터(unseen data)에 대한 성능(generalization)이 높음
    - 1-3. Bayesian Classifier
      - 베이즈 정리를 이용하여 입력 데이터가 특정 카테고리에 속하는지 분류함
  - 2) 규칙 기반 방법(Rule-Driven Approach)
    - 정의 : 주어진 입력에 대해서 결과값을 도출하는 방법 => if-then 방식
      - 귀납적 사고 방식 : 예제에 대해 가설을 세우고 결과를 도출함
      - 규칙 기방 방법 종류 : Find-S 알고리즘, Version space/ Candidate 알고리즘
    - 규칙 기반 학습이 타당하기 위해서 필요한 가정
      1. 우리가 알아볼 세상에서는 관측 오차(observation errors)가 없음
      2. 일관성이 없는 관측 또한 존재하지 않음
      3. 어떤 확률론적 요소(stochastic element)도 존재하지 않음
      4. 우리가 관측하는 정보가 시스템에 있는 모든 정보
      - 완벽한 세계 : 위의 네 가지 가정을 만족하는 곳 -> 규칙 기반 학습은 완벽한 세계에서 타당할 수 ㅣㅇㅆ음
    - 2-1. Find-S 알고리즘
      - 정의 : 가장 구체적인 가설에서 시작하여 점점 General한 가설을 찾아내는 방법
      - 가장 중요한 점 : 예제 중 positive training example만 선별한다는 것
        - 특정 예제로부터 도출된 결과를 다른 예제들에 반복하여 적용하여 변경된 부분만 don't care condition으로 설정하고 최종적인 가설을 만들어냄
      - 단점 : 현실세계에서 사용하기에 한계가 존재함
        - 실제 세상에서는 고려해야할 부분이 많음
        - 최종적으로 하나의 일반화된 가설을 도출하기 때문에 가설의 집합이 존재하는 경우을 고려하지 않음
    - 2-2. Candidate Algorithm
      - 예제에 일치하는 모든 가설의 집합(version space)를 도출하는 알고리즘
        - 하나의 일반적인 가설을 도출하는 Find-S 알고리즘에서 발전된 형태
      - 구조
        - G : 매우 General한 가설에서 시작(negative 예제), S : 매우 Specific한 가설에서 시작(Positive 예제)
        - Version Space : 각자 조건을 더하거나 빼다보면 G와 S가 결국 만나게 되어 모든 가설의 집합이 됨
      - 단점
        - 어떤 가설이 정확한지 알 수 없어 현실 세계에서는 사용할 수 없음
  - 결론
    - 규칙 기반 학습보다는 **데이터 기반 학습**을 통해 인공지능을 학습시킴

## 2. 이미지 분류 모델들
- Image Classification 아키텍처를 모델에 사용된 Layer수로 구분함
- 1) LeNet, AlexNet, ZFNET(레이어 8개 이하)
  - LeNet-5
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

