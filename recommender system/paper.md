# 1. 논문 제목
- A Survey on Accuracy-oriented Neural Recommendation: From Collaborative Filtering to Information-rich Recommendation
  - 정확성 지향하는 뉴럴넷 추천 조사 : 협업 필터링에서 정보가 풍부한 추천까지

# 2. 저자
- Le Wu Member, Xiangnan He Member, Xiang Wang Member, Kun Zhang Member and Meng Wang, Fellow

# 3. 날짜
- 2021.12.27
  - 따끈따근한(?) 논문이긴 하면서도 아닐 수도 있음

# 4. 요약
- 컴퓨터 비전과 언어 이해(NLP)에서 딥러닝이 좋은 성공에 영향을 받은 추천의 연구는 뉴럴 네트워크 기반의 새로운 추천 모델을 발명하는 것으로 전환되어 왔다. 
- 최근에 우리는 뉴럴 추천 모델의 개발이 중요한 진전을 했다는 것을 목격했다. 일반화하고 뉴럴 네트워크의 강한 표현력 때문에 전통적인 추천 모델을 뛰어넘는다.
- 논문 조사에서 우리는 추천 시스템에서 작업하는 연구자와 실무자를 용이하게 하기 위해 이 분야를 요약하는 것을 목표로 정확성 목표를 가진 추천 모델링의 관점으로부터 뉴럴 추천 모델을 체계적인 리뷰를 한다.
- 특히 추천 모데링을 하는 동안 데이터의 사용을 기반으로 우리는 협업 필터링과 정보가 풍부한 추천으로 나눈다.
  - 협업 필터링 : 사용자와 아이템의 상호 작용 데이터를 주요 소스로 활용
  - 컨텐츠가 풍부한 추천(content based?) : 유저의 프로파일과 아이템 지식 그래프 같은 유저와 아이템과 관련된 사이드 정보를 추가적으로 활용한다.
  - 일시적이거나 순차적(시간적)인 추천 : 시간, 위치 및 과거 상호 작용과 같은 상호 작용과 관련된 상황 정보를 설명

# 5. 내용
## 1. 소개
- 정보 과부하는 인터넷의 확산 때문에 사람들의 일상 생활에서 증가하는 문제이다. 추천 시스템은 정보 과부하 문제를 완화하고, 원하는 정보를 찾는 사용자를 용이하게 하며, 서비스 제공업체의 트래픽과 수익을 증가시키는 효과적인 솔루션 역할을 한다.
- 추천 시스템은 넓은 범위의 어플리케이션에 사용되어 왔다. (어플리케이션 : 이커머스, 소셜 미디어 사이트, 뉴스 포탈, 앱 스토어, 디지털 책? 등등) 그것은 현대 정보 시스템에서 가장 보편적인 사용자 중심의 인공지능 애플리케이션 중 하나이다.
- 추천 연구는 1990년대로 거슬러 올라갈 수 있다. 초기 연구는 콘텐츠 기반과 협업 필터링 기반에 대한 많은 발견으로 개발되어왔다? 넷플릭스 챌린지에 의해 유명하게 된 MF 모델은 2008년부터 2016까지 많은 시간 동안 추천 모델 주류가 되었다.
- 그러나 선형 인수분해 모델의 선형 특성은 복잡한 사용자-아이템 상호작용과 같은 크고 복잡한 데이터를 다룰 때 덜 효율적이다. 아이템은 완전한 이해를 요구하는 복잡한 의미론을 포함할 수 있다.
- 2010년대 중반에 머신러닝에서 딥 뉴럴 네트워크의 부상은 스피치 인식, 컴퓨터 비전, NLP를 포함하여 여러 영역에서 혁명을 일으켰다. 딥러닝의 큰 성공은 특히 복잡한 패턴을 가진 큰 데이터에서 학습하는데 유리한 뉴럴 네트워크의 상당한 표현력(?)에서 비롯된다.
- 이것은 자연스럽게 추천 기술을 증진하기 위한 새로운 기회로 가져온다. 놀랍지도 않게 지난 세월 동안 추천 시스템에 대한 뉴럴 네트워크 접근법을 개발하는데 많은 연구가 있다. 이 연구에서 우리는 뉴럴 추천 모델을 언급한 뉴럴 네트워를 사용한 추천 모델에 대해 체계적인 리뷰를 제공하는데 목표를 둔다.
- 이것은 최근 추천 연구에서 번창한 주제이다. 최근에 많은 흥미로운 진전이 있었을뿐만 아니라 다음 세대 추천 시스템의 기술적인 기반이 될만큼 성장 가능성을 보여준다. 


## 1.1 기존 조사와의 차이점
- 추천 연구의 중요성과 인기를 고려할 때, 최근에 발표된 일부 연구도 검토했다. 여기서 우리는 이 연구의 필요성과 중요성을 강조하기 위해 이러한 연구와의 주요 차이점에 대해 간단히 논의한다.
- 기존 연구는 두 가지 중요한 파트로 구성된다. 
  - 첫 번째 파트
    - 협업 필터링(“Collaborative filtering beyond the user-item matrix: A survey of the state of the art and future challenges,”)
    - 크로스 도메인 추천(“Cross domain recommender systems: A systematic literature review,”)
    - 설명가능한 추천(“Tem: Treeenhanced embedding model for explainable recommendation,”)
    - 지식 그래프로 표시된 추천(“A survey on knowledge graph-based recommender systems,”)
    - 시퀀스 추천(“Deep learning for sequential recommendation: Algorithms, influential factors, and evaluations,”), (“Sequence-awarerecommender systems,”)
    - 세션 기반의 추천(“A survey on session-based recommender systems,”) 
  - 에서 부가 정보 활용과 같은 특정한 주제 또는 방향에 초점을 맞춘다. 
  - 다른 파트는 추천 방법을 요악한 딥러닝의 분류를 따른다.
    - 예를 들어 (“Deep learning based recommender system: A survey and new perspectives,”)는 MLP 기반, 오토인코더 기반, RNN 기반, 어텐션 기반(?) 등으로 추천 방법에 대한 논의를 정리했다.
    - 또한 비슷한 연구는 (“A review on deep learning for recommender systems: challenges and remedies,”), (“Recommendation system based on deep learning methods: a systematic review and new directions,”)로 발견할 수 있다. 
    - 이들의 연구는 주요하게 추천에서 다양한 딥러닝 방법을 사용하는 기술적인 다름을 비교한다.




- 존재하는 연구와 다른 우리의 연구는 정확성 목표를 가진 추천 모델의 관점에서 구성되고 협업필터링, 컨텐츠가 풍부한 방법, 일시적이거나 순차적(시간적)인 방법 같은 가장 일반적인 추천 시나리오를 다룸
- 해당 연구는 연구자들에게 딥러닝 기술이 효과가 있는 이유와 시기를 이해하는데 도움이 될 뿐만 아니라 특정한 추천 시나리에서 더 나은 솔루션을 설계하는데 용이할 것이다.

## 1.2 우리는 어떻게 연구자료를 모았는가?
- 우리의 연구는 정확성 목표를 가진 추천 모델 관점으로부터 모델 시스템을 검토하는데 초점이 맞추어져 있기 때문에 우리는 WWW, SIGIR, KDD, ICLR, AAAI, IJCAI, WSDM, RecSys와 같은 관련 상위 컨퍼런스와 TKDE, TKDD와 같은 상위 저널을 검색했다. 한편, 우리는 또한 최근 관련 연구를 찾기 위해 구글 스칼라를 검색했다. 이번 연구에서 만든 카테고리에 따라, 우리는 관련 연구를 검색하기 위해 협업필터링, 컨텐츠 추천 시스템, 사이드 정보, 그래프 뉴럴 네트워크, 신경망 추천 등과 같은 특정 단어를 사용했다.
- 그런 다음 검색된 연구를 기반으로 모든 논문을 가능한 한 완벽하게 포괄하도록 주제 구조를 신중하게 설계했다. 게다가 몇몇 중요한 연구를 놓치는 것을 피하기 위해, 우리는 또한 추천에서 전통적이고 유명한 연구를 다시 확인했다. 

## 1.3 본 연구의 범위 및 구성
- 이 연구는 두 가지 주요한 파트로 구성된다. 섹션 2부터 4까지 기존 방법들을 검토하고 섹션 5는 미래의 방향과 열린 이슈에 대해서 토론한다. 각 섹션을 설명하기 전에 먼저 문제 공식을 제공한다.
- 추천 도메인과 시나리오에 상관없이 우리는 추천 학습 문제를 다음과 같이 추상화할 수 있다. -> y<sup>^</sup><sub>u,i,c</sub> = f(D<sub>u</sub>,D<sub>i</sub>,D<sub>c</sub>)
- 유저 u, 아이템 i, 컨텍스트 c를 각각 설명하기 위한 데이터 Du, Di, C가 주어졌을 때 유저 u가 컨텍스트 c에서 항목 i를 선호할 가능성을 추정하기 위해 예측 함수 f를 학습한다. 그렇게 함으로써, 우리는 통합 프레임워크가 뉴럴 추천 모델을 요약할 수 있도록 허락한다.
  - 섹션 2는 개인화된 추천을 기초로 형성하고 추천에서 가장 많이 연구된 주제인 협업 필터링 모델을 검토한다. 협업 필터링 모델은 컨텍스트 데이터 D<sub>c</sub>를 무시하고 단지  D<sub>u</sub>과 D<sub>i</sub>에서 ID나 상호 작용 이력을 사용하는 것으로 불 수 있다.
  - 섹션 3은 유저의 프로파일, 사회 네트워크, 아이템 속성, 지식 그래프와 같은 추천에서 유저와 아이템의 사이드 정보를 통합한 모델을 검토한다. 우리는 그것들을 D<sub>u</sub>와 D<sub>i</sub>에 사이드 정보를 통합함으로써 자연스럽게 협업필터링을 확장하는 콘텐츠 풍부 모델로 표현하지만 컨텍스트 데이터 D<sub>c</sub>도 무시된다.
  - 섹션 4는 컨텍스트 정보를 사용하는 모델을 검토한다. 컨텍스트 데이터는 각 유저-아이템 상호작용과 관련되었지만 시간, 위치, 과거 상호작용 시퀀스와 같은 유저 컨텐트(내용) 또는 아이템 컨텐트(내용)에 속하지 않는다. 컨텍스트 인식 모델은 유저관련 데이터 D<sub>u</sub>와 아이템 관련 데이터 D<sub>i</sub> 외에도 켄텍스트 데이터 D<sub>c</sub> 기반으로 예측을 진행한다. 페이지 제한 때문에 우리는 가장 일반적인 컨텍스트 데이터 중 하나인 일시적인 컨텐트에 초점을 맞춘다.

![image](https://user-images.githubusercontent.com/49123169/217449653-462339a2-2b68-4fc3-8e86-a2691f1755ba.png)

- 위의 그림은 추천 모델링에 사용되는 전형적인 데이터와 세 가지 모델 타입을 보여준다. 서로 다른 추천 시나리오를 위해 다른 모델이 설계된다는 점은 주목할 필요가 있다. 그럼에도 불구하고, 많은 케이스에서 우리는 모델의 구성 요소를 또 다른 시나리오에 적합하게(최소한 기술적으로 실행 가능한) 조정할 수 있다.
- 예를 들어 많은 협업 필터링 모델은 먼저 유저와 아이템 representation가 얻고 그 다음 예측 함수가 주어진 유저와 아이템 representation를 학습하도록 설계된다. 그것들의 컨텐츠를 풍부하게 만들기 위해선 우리는 간단하게 컨텐트 모델링의 representation 학습 요소를 증진시키는 것이 필요하다.
- 또 다른 예는 우리가 contextual information를 유저 데이터의 일부로 취급할 수 있다. 즉, D<sub>u</sub>를 대체하기 위해 D<sub>u,c</sub>를 구성하여 내용이 풍부한 모델을 또한 contextaware이 되도록 조정할 수 있다.
- 비록 이 조정된 모델들은 공식적으로 제안되거나 발표되지 않을 수 있지만 해당 모델들은 큰 노력 없이 얻을 수 있으며 실제 애플리케이션에서 탐색할 가치가 있다. 이러한 설계 유연성은 서로 다른 계층이 서로 다른 목표를 위해 설계되는 뉴럴 추천 모델의 계층별 아키텍처에 기인할 수 있다.
- 편의를 위해, 우리는 또한 관련된 뉴럴 추천 모델을 추천 모델링 1의 분류법으로 요약한다. (모델링 1: https://github.com/ImcRS/AWS-recommendation-papers) 우리는 이 연구가 실무자들이 그들의 목적에 맞는 모델을 이해하고 더 나은 모델을 설계하는데 도움이 되는 명확한 로드맵을 제공하기를 희망한다.

## 2. 협업 필터링 모델
- 협업필터링 개념은 타겟 고객의 행동을 예측하기 위해 모든 고객의 협업 행동을 활용한다는 생각에서 비롯되었다. 초기 접근법은 메모리 기반한 모델로서 고객(유저 베이스 CF) 또는 아이템(아이템 베이스 CF)의 행동 유사성을 직접 계산한다.
- 나중에, MF(행렬인수분해) 기반 모델은 고객 아이템 상호 작용 행렬을 인코딩하는 잠재 공간(latent space)을 집합적으로 찾음으로써 널리 퍼진다.
  - Y. Koren, R. Bell, and C. Volinsky, “Matrix factorization techniques for recommender systems,” Computer, no. 8, pp. 30–37, 2009.
  - S. Rendle, C. Freudenthaler, Z. Gantner, and L. Schmidt-Thieme, “Bpr: Bayesian personalized ranking from implicit feedback,” in UAI, 2009, pp. 452–461.
- 뉴럴 네트워크의 표현적이고 복잡한 모델링 능력을 고려할 때, 뉴럴 협업 필터링의 현재 솔루션은 두 가지 범주로 요약될 수 있다.
  - 사용자 및 아이템의 표현 모델링
  - 표현이 주어진 사용자-아이템 상호 작용 모델링

### 2.1 표현 학습
- CF에서 U는 유저, V는 아이템을 나타내고 R∈IR<sup>M×N</sup> 는 유저와 아이템의 상호 행동 행렬입니다. 일반적인 목표는 유저 임베딩 행렬 P와 아이템 임베딩 행렬 Q를 학습하는 것이며 여기서 p<sub>u</sub>, q<sub>i</sub>는 각각 유저 u와 아이템 i의 표현 파라미터로 나타남
- 실제, 대규모 아이템 데이터에 비해 각 유저들의 행동은 제한적이기 때문에 정확한 유저 및 아이템 임베딩 학습을 위한 유저-아이템 상호작용 행동의 희소성이 CF의 핵심 과제임. 다른 종류의 표현 학습 모델은 입력 데이터가 주어진 표현 모델링 기법에 따라 달라짐
- 우리는 이 섹션에서 세 가지 분류로 나눈다.
  - history behavior aggregation enhanced models : 히스토리 동작 집계 강화 모델?
  - autoencoder based models : 오토인코더 기반 모델
  - graph learning approaches : 그래프 학습 접근법
- 설명을 쉽게 하기 위해 표1에 일반적인 표현 학습 모델을 나열함
- 표1 : CF의 표현 학습 접근법 요약

|Category|Modeling Summarization|Models|
|--------|----------------------|------|
|Classical Matrix Factorization|User UID(Free Embed), Item IID(Free Embed)|BPR, MF et al.|
||User Interacted items(Free Embed+Heuristic Agg), Item IID(Free Embed)|FISM,PMLAM,pQCF,FAWMF|
||User Interacted items+UID(Free Embed+Heuristic Agg), Item IID(Free Embed)|SVD++|
|History Attention|User Interacted items(Free Embed+Heuristic Agg), Item IID(Free Embed)|NAIS|
||User Interacted items+UID(Free Embed+Heuristic Agg), Item IID(Free Embed)|ACF|
|Autoencoder Models|Item Interacted Items (Non-linear Encoder)|AutoRec, CDAE, Mult-VAE et al.|
||User Interacted Items (Non-linear Encoder), Item Interacted users (Non-linear Encoder)|REAP, CE-VNCF,SW-DAE|
|Graph Learning|User UID+Graph(GNN), Item IID+Graph(GNN)|GC-MC, NGCF, SpectralCF, NIA-GCN, BGCF, DGCF et al|
||User UID+Graph(Simplified GNN), Item IID+Graph(Simplified GNN)|LR-GCCF, LightGCN, DHCF et al|

#### 2.1.1. 히스토리 행동 관심도 집계 모델
- 원 핫 유저 id(UID)와 원핫 아이템 id(IID)를 입력으로 사용하여 전통적인 잠재 요인 모델은 각 UID u와 IID i를 p<sub>u</sub>와 q<sub>i</sub>의 자유 임베딩 벡터와 연결한다. 자유 임베딩으로 유저를 모델링하는 대신에 연구자는 더 나은 유저 표현 모델링을 위해 유저의 과거 행동을 차용할 것을 제안했음
- 예를 들어 FISM(Factored Item Similarity Model)은 상호작용된 아이템 임베딩을 유저 표현 벡터로 풀링하고 SVD++는 최종 유저 표현으로 상호작용 히스토리 임베딩(즉, FISM 유저 표현)과 함께 UID 임베딩 p<sub>u</sub>를 추가함. 이 모델들은 간단한 선형 행렬 분해에 의존했으며 상호작용 히스토리 집계에 휴리스틱 또는 동일한 가중치를 사용했다.
- 그러나 다른 히스터리적(기록) 아이템들이 유저의 선호도를 모델링하는데 다르게 기여해야 한다. 그러므로 몇몇 연구자들은 뉴럴 주의 메커니즘을 히스토리(기록) 표현 학습에 통합함.
- 하나의 대표적인 연구는 유저 인식 협업 필터링 -> ACF(Attentive Collaborative Filtering)으로, 각 상호작용된 아이템에 유저 인식 가중치를 부여하여 유저 표현에 대한 중요성을 나타냄. $\hat{r}$
- 

