# Image Captioning(이미지 캡셔닝)
- 이미지를 입력하면 해당 이미지를 잘 설명하는 문장을 생성해내는 Task
- 컴퓨터 비전과 NLP가 합쳐진 영역으로 NLP에 대한 지식도 필요한 Task

![image](https://github.com/JuHwna/thesis_summary/assets/49123169/9b2d42ad-13ef-4eaa-80ca-cff3a126f454)

# (1) 이미지 캡셔닝 아이디어
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/5fb513f3-155f-43bd-a1dc-e6563cb7afb5)

- text generation : 이미지가 주어졌을 때 이미지의 각 물체와 상황을 판단하고 설명하는 문장이 만들어지는 것
- image captioning
  - 이미지 내에 있는 객체에 대한 판단뿐만 아니라 객체들 간의 관계를 파악하고 자연어의 형태로 알맞게 표현하는 문제도 겸하고 있음
  - 컴퓨터 비전과 자연어처리의 종합적인 이해를 필요로 함
  - 이미지를 문장으로 바꾼 후 NLP 분야와 결합하여 다양하게 활용할 수 있고 비교적 용량이 큰 데이터인 이미지를 텍스트로 바꾸기 때문에 저장공간이 획기적으로 줄어들 수 있음

#### 이미지 캡셔닝 활용 사례
1. 이미지에 캡션을 추가해 검색의 효율성이 증가함
   - 기존에는 텍스트만으로 검색이 가능했지만 이미지를 텍스트화하여 가능하게 바꾸어 주었기 때문에 검색 효율이 더 좋아짐

2. 시각 장애인이나 저시력자들에게 도움을 줄 수 있음
   - 이미지를 텍스트화한 후 TTS(Text To Speak) 기술을 이용하여 음성으로 읽어주어 앞의 상황이나 그림에 대해 설명해줄 수 있음

3. 미술 치료 분야에서 치료사의 주관을 배제하고 이미지 캡셔닝을 이용하여 객관적으로 미술에 대한 설명을 함으로서 치료의 일관성을 부여할 수 있음


### 이미지 분할 네트워크의 기본 구조 : CNN & RNN
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/408dab24-710f-4bc5-a5b5-8e383abc83fc)

- 이미지 캡셔닝에 기본 네트워크는 이미지 특징을 추출하기 위한 CNN과 문장으로 나타내기 위한 RNN을 주로 사용함
   1. 입력 이미지를 CNN을 통과시켜 특징들을 추출함
   2. 추출한 특징들을 RNN에 대입하여 문장을 만들 수 있도록 이미지 데이터셋과 이미지에 대한 캡션들을 토대로 학습시킴

![image](https://github.com/JuHwna/thesis_summary/assets/49123169/93f33434-7e44-45ab-8ce5-dab65e0551c3)

- 사진과 같이 입력 이미지를 CNN을 이용해 특징을 추출하고 attention과 LSTM을 이용한 RNN 모델을 통과하여 각 특징에 맞는 단어들을 얻어내고 이미지를 설명하는 문장을 완성

### 이미지 캡셔닝 단계
- 예시 사진
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/80fc1cde-f0bd-4139-813d-c5638728d8ef)

#### 1. CNN을 이용한 특징 추출
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/ab2933c8-64ee-4065-97eb-fd46c0b65772)

- RGB 3채널의 인풋 데이터를 ResNet-101을 이용하여 특징을 추출함

#### 2. Attention Network를 이용하여 단어 생성
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/d4eb75e8-1571-4743-84c1-d9505d225b51)

- Attention Network를 통과하여 중요한 부분에 가중치를 두어 단어를 추출해 냄
- 가중치가 높은 부분을 이용해 사진을 한 문장으로 설명할 수 있는 물체, 행위 등을 추출해냄

#### 3. RNN을 이용하여 문장 완성
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/3c55314f-9f3a-4557-8c12-d96b153f4ba5)

- 가중치를 바탕으로 추출해낸 이미지의 주요 단어들을 RNN을 통해 조합하여 문장을 완성함
- 주요 단어들로 문장을 완성했기 때문에 배경과 같은 중요하지 않은 부분은 누락될 수 있지만 한 문장으로 간결하게 이미지를 설명해낼 수 있음

#### 전체 구조
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/fde82fb4-b9c8-46b8-9061-10973ba3fd68)

### 이미지 캡셔닝 성공 예시
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/7e7e87d1-8837-4818-b8de-34b607d4c601)

- 물체와 상황을 정확히 인지한 경우 한 문장으로 이미지를 잘 설명하고 있는 것을 알 수 있음
- 어텐션을 이용하여 중요한 부분에 집중하여 사진의 특징을 정확하게 텍스트로 나타내어 주었음

### 이미지 캡셔닝 실패 예시
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/14517972-270c-44b6-9ec4-de7cee1fdb8b)

- 실패는 물체나 행위를 잘못 인지한 상황으로 어느 한 가지라도 잘못 추출하면 아예 다른 설명이 되어버릴 수 있기 때문에 상당한 정확성이 요구됨

## 1) 이미지 캡셔닝 데이터셋

# (2) 이미지 캡셔닝 모델 이해를 위한 사전지식
## 1) 워드 임베딩
#### 워드 임베딩(Word Embedding)
- 워드 임베딩 : 단어를 벡터로 표현하는 방법으로 단어를 밀집 표현으로 변환하는 것
  - 단어를 밀집 벡터(dense vecotr)의 형태로 표현하는 방법
- 임베딩 벡터 : 밀집 벡터를 워드 임베딩 과정을 통해 나온 결과
- 워드 임베딩 방법론 : LSA, Word2Vec, FastText, Glove 등
  - 케라스에서 제공하는 도구인 Embedding() : 앞서 언급한 방법들을 사용하지는 않지만 단어를 랜덤한 값을 가지는 밀집 벡터로 변환한 뒤에 인공 신경망의 가중치를 학습하는 것과 같은 방식으로 단어 벡터를 학습하는 방법을 사용함

### 1. 희소 표현(Sparse Representation)
- 희소 표현 : 단어를 표현할 때 모든 단어 개수로 벡터 차원을 설정하고 표현하고자 하는 인덱스 값만 1로 설정하고 나머지는 0으로 표현하는 원-핫 벡터로 표현하는 방법
  - ex) 고양이 = [ 0 0 0 0 1 0 0 0 0 ......]
- 희소 벡터의 문제점
  - 단어의 개수가 늘어나면 벡터의 차원이 한없이 커진다는 점
    - 단어 집합이 클수록 고차원의 벡터가 됨
    - 공간적 낭비를 불러일으킴
      - 희소 표현의 일종인 DTM과 같은 경우에도 특정 문서에 여러 단어가 다수 등장하였으나 다른 많은 문서에서는 해당 특정 문서에 등장했던 단어들이 전부 등장하지 않는다면 역시나 행렬의 많은 값이 0이 되면서 공간적 낭비를 일으킴
  - 원-핫 벡터는 단어의 의미를 담지 못함

### 2. 밀집 표현(Dense Representation)
- 밀집 표현 : 벡터의 차원을 단어 집합의 크기로 상정하지 않음
  - 사용자가 설정한 값으로 모든 단어의 벡터 표현의 차원을 맞춤
  - 이 과정에서 더 이상 0과 1만 가진 값이 아니라 실수값을 가지게 됨
- ex) 고양이 = [0.2 1.8 1.1 -2.1 ...........]
- 밀집 벡터 : 벡터의 차원이 조밀해졌다고 하여 붙여진 이름

## 2) Word2Vec
#### Word2Vec
- 단어 간 유사도를 반영할 수 있도록 단어의 의미를 벡터화할 수 있는 방법 중 대표적인 방법
- 두 가지 방식
  - CBOW(Continuous Bag of Words) : 주변에 있는 단어들을 가지고 중간에 있는 단어들을 예측하는 방법
  - Skip-Gram : 중간에 있는 단어로 주변 단어들을 예-측하는 방법
- 두 가지 방식 모두 메커니즘 자체는 거의 동일함


### 1. CBOW(Continuous Bag of Words)
- CBOW의 기본 아아디어 : 주변 단어를 통해 주어진 단어를 예측하는 것
  - 총 단어가 C개라고 할 때 앞 뒤로 C/2개의 단어를 통해 주어진 단어를 예측하는 방법
- ex) "The fat cat sat on the mat" {"The", "fat", "cat", "on", "the", "mat"}으로부터 sat을 예측하는 것 => CBOW가 하는 일
  - 중심 단어(center word) : 예측해야하는 단어 sat
  - 주변 단어(context word) : 예측에 사용되는 단어들
  - 윈도우 : 중심 단어를 기준으로 앞 뒤로 몇 개의 단어를 볼지 선택하는 ㄴ범위
    - ex) 위 예문에서 중심 단어가 cat이고 window가 2라면 "The", "fat", "on", "the" 단어를 참고
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/9f110264-5793-4c42-9f7e-2bbc9e323ecc)

- 위 그림처럼 학습시킬 문장의 모든 단어들을 원-핫 인코딩 시켜줌
- 그 다음 window = m 으로 설정하고 하나의 Center 단어에 대해 주변 단어의 벡터를 Input으로 넣어줌
  - 수식 : $(x^{c-m},x^{c-m+1},...,x^{c-1},x^{c+1},...,x^{c+m-1},x{c+m}) \in IR^{|V|}$
- CBOW 방식의 파라미터 : Input layr -> Hidden layer로 가는 weights와 Hidden layer -> Output layer로 가는 weights
  - $W \in IR^{V \times N}, W` \in IR^{N \times V}$
- 워드 임베딩된 벡터 : CBOW 신경망을 학습시켜 나온 최적의 가중치
  - CBOW 모델은 맥락 단어로부터 타깃 단어를 예측하는 모델
  - CBOW 모델의 입력 : 맥락 단어의 원-핫 벡터
  - 출력 : 타깃 단어의 원-핫 벡터

![image](https://github.com/JuHwna/thesis_summary/assets/49123169/5135f151-1e05-4f0c-922e-acff4471f270)

- 위는 CBOW 신경망 모델의 개괄적인 모습
  - Window가 2일 때의 예이며 입력인 맥락 단어는 fat, cat, on, the이며 출력인 타깃 단어는 sat임


- 입출력 데이터가 모두 원-핫 벡터이며 지면 관계상 fat과 the는 생략되어 있음
  - 투사층(projection layer)의 크기 : M
    - 워드 임베딩 결과의 차원임
  - 입력층(input layer)에서의 가중치 행렬 W의 크기 : V x M
    - V : 단어의 개수
  - 출력층 W` 행렬의 크기 : M x V
  - W와 W`는 서로 다른 행렬임
- CBOW 신경망 모델은 입력 베터(맥락 단어)를 통해 출력 벡터(타깃 단어)를 맞추기 위해 계속해서 학습하며 이 가중치 행렬 W와 W`을 갱신함

![image](https://github.com/JuHwna/thesis_summary/assets/49123169/d370804d-fe97-4ca8-9988-2388802f1267)

- 입력층의 입력 벡터와 가중치 행렬 W가 곱해지는 과정
  - 위 그림에서 맥락 단어의 원-핫 벡터를 X라 표기했음
  - 예를 들어 x_cat(cat에 대한 원-핫 벡터)은 3번째 인덱스만 1이고 나머지는 다 0
  - 이와 가중치 행렬 W를 곱해주면 W의 3행에 해당되는 벡터가 도출됨
  - 그저 가중치 행렬 W에서 '입력 벡터에서 1이 포함된 인덱스'에 해당하는 행을 추출하는 작업일 뿐임
  - 원-핫 벡터 x에서 1의 값을 가지고 있는 인덱스를 i라 할 때, 가중치 행렬 W의 i번째 행을 가져오는 작업임

- 가중치 행렬 W가 결국 우리가 구하고자 하는 워드 임베딩 결과
  - 좋은 워드 임베딩 값을 구하기 위해서는 가중치 행렬 W를 잘 학습해야 함
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/6a71d293-64e6-4251-9847-23cc1bf89b62)

- 입력인 맥락 단어가 총 4개이므로 각 입력 원-핫 벡터와 가중치 행렬 W를 곱한 벡터 v가 4개 도출될 것임
  - 이 벡터들의 평균 벡터를 구해야 함
    - 구해진 모든 v벡터(v_fat, v_eat, v_on, v_the)를 더한 뒤 4로 나누어주면 됨
      - 값이 4인 이유 : 2 x (window size)
  - 평균 벡터 v의 크기 : M
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/6a8461b8-007a-4c9b-972d-190529b6818f)

- 위에서 구한 평균 벡터 v를 출력층 가중치 행렬 W`와 곱함
  - 곱해서 얻어진 Z벡터의 크기는 V(위의 평균 v와는 다른 값임)(저 위에 출력층에 적은 V 값임)
  - 벡터 z에 소프트맥스를 취해주면 확률 값에 해당하는 벡터 값이 구해짐
    - 소프트맥스를 취해주면 모든 원소의 합이 1인 상태로 바뀌기 때문에 확률을 나타내는 것
  - 소프트맥스를 취해준 벡터와 실제 타깃 단어의 원-핫 벡터의 손실 함수 : cross entropy 사용
    - 손실 함수로 cross-entropy를 사용한다는 것
      - CBOW 신경망을 통해 최종적으로 도출한 벡터가 타깃 벡터와 최대한 똑같아지게 하라는 뜻
      - 이런 식으로 학습을 반복하며 가중치 행렬 W와 W`를 갱신함
        - 학습이 잘 되면 W와 W`의 값은 거의 비슷하기 때문에 어떤 것을 워드 임베딩 행렬로 사용해도 됨
        - 때로는 W와 W`의 평균값을 사용함
- 학습을 진행할수록 맥락으로부터 타깃 단어를 잘 추측하는 방향으로 가중치 행렬 W가 갱신됨
  - 이렇게 해서 얻은 분산 표현 W에는 '단어의 의미'도 잘 녹아 있음

### 2. Skip-gram
- Skip-gram : 중심 단어에서 주변 단어를 예측함
- 앞서 언급한 예문에 대해서 동일하게 윈도우 크기가 2일 때, 데이터셋은 다음과 같이 구성됨

![image](https://github.com/JuHwna/thesis_summary/assets/49123169/45669b45-4f1b-453c-bbe1-9694b55dacf7)

- 신경망을 도식화해보면 다음과 같음

![image](https://github.com/JuHwna/thesis_summary/assets/49123169/32e3ff78-6bc5-4747-b5d3-788fd669ca43)

- 중심 단어에 대해서 주변 단어를 예측하므로 투사층에서 벡터들의 평균을 구하는 과정은 없음
- 성능 비교 : 전반적으로 Skip-gram이 CBOW보다 성능이 좋다고 알려져 있음

# (3) 이미지 캡셔닝 모델들
## 1) Show and Tell
### 네트워크 핵심 아이디어
- 2015년 구글에서 공개한 "Show and Tell: A Neural Image Caption Generator"에서 공개한 NIC모델임
  - 이미지 캡셔닝 아이디어(이미지 캡셔닝의 문제를 기계번역으로 생각하겠다)의 시작이 된 논문임
- 이미지의 임베딩을 추출하는 CNNs 네트워크로는 GoogleNet을 이용하였고 문장을 생성하는 RNNs 네트워크로는 Seq2Seq을 이용하였음

- 이미지 캡셔닝 네트워크 : NLP분야와 큰 연관관계가 있음
- 해당 논문은 단순한 네트워크에 대한 설명 뿐만이 아니라 이미지 캡셔닝에서 생각봐야할 주제를 다루고 있음
  - 평가방법(Metric)에 대한 한계, 그럼에도 저자들이 설명하기 위해 이용한 여러 Metric
    - 적절한 Metric이 없어 숫자로 정확한 성능을 표현하지는 못하나 여러 불완전한 Metric으로 측정해보았을 때 이전 네트워크들에 비해서 매우 큰 발전을 보여준 논문

### 네트워크 구조
![image](https://github.com/user-attachments/assets/a7022d09-e3d7-447c-a9dd-5e95be0c93e0)

- 네트워크 : 이미지 분류에 사용된 GoogleNet과 기계번역(Machine Translation)의 Seq2Seq 모델을 이어서 붙인 모습

#### CNN 인코더(GoogleNet)
- 이미지 분류에 사용된 GoogleNet을 거의 그대로 이용
  - 과적합 방지하기 위해서 ImageNet 데이터셋을 이용하여 Pretrain함
  - 마지막 FC layer를 추가하여 워드 임배딩과 같은 차원(2048->512)으로 맞추기 위해 사용하고 그 외의 네트워크 앞 부분 Weight들은 동일
- 추출된 피처들은 기존 Seq2Seq네트워크의 Context Vector와 동일한 개념으로 이용됨

#### RNN 디코더(Seq2Seq)
- 기존 Seq2Seq2의 인코더 부분을 그대로 이용
- 이미지 임베딩과 차원을 맞추어 Label 원핫벡터를 워드임베딩 이후 512 차원이 되도록 정의해 모델을 구현했음

### 네트워크 트레이닝
#### 손실함수(Loss function)
- 가중치를 업데이트하기 위한 손실함수
  - $\theta^{*} = argmax_{\theta}\displaystyle\sum_{(I,S)}logp(S|I;\theta)$
  - 기계번역에서는 많이 쓰는 손실함수
  - 이미지가 주어졌을 때 각 스텝에서 예측한 워드임베딩과 짝지어진 label의 워드임베딩(S,embedding word)과의 분포 차이의 합을 이용
- 코드에서는 위 식에다 -1을 곱하여 유사도가 높을수록 손실값이 감소하도록 하여 훈련함
- 손실함수를 이용하여 업데이트 되는 가중치들
  - (1) CNN의 최상단 레이어, (2) 워드임베딩 벡터, (3) LSTM의 파라미터 (CNN인코더의 파라미터 : Pretrain됨)

#### 데이터셋(Dataset)
![image](https://github.com/user-attachments/assets/5a153cff-4bb8-42e2-b3b8-49e1807b0897)

- Pascal VOC2008, Flickr8k, Flickr30k, MSCOCO, SBU data를 사용했음
  - SBU를 제외하고는 모두 5개의 correct sentence 라벨이 있음
  - SBU 데이터는 Flickr라는 사이트에 이미지를 올릴 때 같이 올린 이미지 설명으로 학습 시 일종의 noise로 작동함
    - 인터넷에서 사진을 올리면서 아무렇게 끼적거린 설명이라서
  - 나머지 4개의 data set으로 학습을 하고 Pascal 데이터는 test를 위해서만 사용
 
#### 인퍼런스(inference)
- 네트워크 트레이닝과 관련된 부분은 아니지만 실제 모델 활용 시에 예측 문장의 후보들을 구하는 **BeamSearch** 기법을 사용했음
- Seq2Seq에서는 step당 문장의 각 단어들을 예측하는데 각 step에서의 최고의 예측이 종합적으로는 최고가 아닐 수 있기 때문
  - 문장 2개 예시
    - ①[나는, 버스를, 탔습니다] ②[나는, 버스는. 그것은]
    - 두 문장에서 분명 첫번째 문장의 단어가 더 자연스럽고 잘 설명했음
    - but, 각 step에서 가장 최고 확률의 워드를 택하면 두번째 문장과 같이 예측될 수 있음
- BeamSearch(빔서치) : 각 step에서 20개의 후보군을 뽑아서 여러 경우의 수를 만들어 최종적으로는 가장 좋은 시퀀스를 선택하는 방법

### 네트워크 평가
#### 모델 평가의 어려움에 대해서

![image](https://github.com/user-attachments/assets/8ccbbe93-0674-4a51-9788-58d544af9c87)

- 위 사진의 GT(Ground Truth) 캡셔닝은 무엇일까?
  - 사람 3명이 길을 걷는다.
  - 사람들이 차도 옆을 걸어간다
  - 남자가 나무로 된 길을 건너간다.
- 이미지 캡셔닝 Task에서는 이미지 분류와는 어떻게 보면 Ground Truth라는 것이 없음

- 이 때문에 image captioning은 현재까지는 사람의 주관적인 평가 방법 외에는 100% 성능을 평가할 방법이 부족함
  - 저자들은 다양한 관점에서 여러 가지 평가 척도(BLEU, METEOR, Cider, recall@k...)를 이용하여 모델의 성능을 보여줌

#### Generation Result
- BLEU, METEOR, CIDER라는 자동, 정량적 지표로 평가한 결과 높은 성능을 보임을 알 수 있음
- 아래 Table 1,2에서 Human은 5개의 correct sentence label 중 하나를 선택해 나머지 4개와 비교하여 도출한 값임

![image](https://github.com/user-attachments/assets/731b933a-d8df-427e-a89a-24dd914aaddb)


#### Generation Divsersity Discussion
- 모델이 생성하는 caption 중 학습 데이터에 포함되지 않은 새로운 caption이 만들어질 확률은 얼마나 될지?
  - 저자들은 모델이 생성한 새로운 caption의 예시를 제시함
- 각 input image에 대해 BLEU Score가 가장 좋은 caption을 뽑아보면 약 80%는 기존 학습 데이터에 포함되어 있던 문장들이었음
- 다만 BLEU Score가 높은 순으로 15개의 caption을 뽑아보면 약 50% 정도는 새로운 문장이었다고 함

#### Human Evalution
- 사람을 이용해 NIC를 포함한 다양한 ML모델에서 생성된 Caption을 평가하도록 해봄
- 모델들에서 생성한 Caption에서 랭킹을 매겨 평가한 결과는 다음과 같음

![image](https://github.com/user-attachments/assets/6bfbf4c9-7f92-45ac-9154-90f3c939e838)

- R@1은 No.1으로 꼽힌 캡션의 개수
- 다른 모델과 대비해서는 아주 큰 성능차이를 ㅗ임

- Flickr-8k: GT(Ground truth)와 비교했을 때 NIC(Neural Image Caption)의 성능이 현저히 떨어지는 것을 볼 수 있음
  - NIC 성능의 한계를 보여주는 자료임
  - 자동&정량적 평가지표인 BLEU의 한계를 보여주는 것
    - BLEU-4에서는 사람이 만든 캡셔닝보다 NIC에서 만들어진 캡션의 점수가 오히려 더 높았음



### 네트워크의 장단점 및 한계점
- Show and Tell 논문의 시사점 : CNN 네트워크를 이용하여 뽑아낸 Feature를 NLP분야의 Context Vector로 이용가능 하다는 큰 아이디어를 준 논문

## 2) Show, Attend and Tell
- 이전 논문인 Show and Tell의 단점
  - CNN의 FC layer를 통과한 context vector를 이용하여 image captioning을 진행하므로 항상 같은 context vector를 참고하여 캡셔닝을 생성하게 됨
  - FC layer를 통과하면서 기존 이미지에서 공간 정보를 잃어버려 이미지의 어느 부분을 보고 캡셔닝을 생성했는지 네트워크 분석이 불가능함
- 위의 단점을 보완하여 저자들이 발표한 Show, Attention and Tell(2016) 논문에서는
  - 이미지에서 추출된 피쳐(Extract Feature)들을 한 개의 고정된 벡터(Context Vector)로 만들지 않고 어텐션 메커니즘을 이용하여 1개의 워드 예측하는 스텝마다 다른 분포의 벡터들을 생성하여 디코더의 입력으로 이용하도록 네트워크를 구성했음
  - 더 나아가 어텐션을 메커니즘을 2가지 방법(Soft/Hard)로 적용하여 각각의 성능 및 분석 결과를 보여줌

### 네트워크 구조
- 논문 전체에서 네트워크의 전체 구조가 나타난 Figure는 딱 한개임
- 이전 Show and Tell 논문과 비슷하게 네트워크의 구조가 혁신적이고 독창적인 구조를 만들어냈다기보다 기계 번역에서 존재했던 네트워크와 기법들을 잘 연결시켜서 이미지 캡션 문제를 풀었다고 봄

![image](https://github.com/user-attachments/assets/0951ac2f-8704-4545-b504-dfe1e5c7af90)

- Figure 1에서 1,2,4번에 해당하는 내용은 Show and Tell과 동일함
  - 3번 순서인 RNN with attention이 가장 생소할 것임
 
#### 어텐션 메커니즘(Attention mechanism)
- 논문에서는 CNNs를 이용하여 생성된 피처맵(Feature map)을 어텐션을 이용하여 매 스텝마다 RNNs에 입력함
- 과거 Show and Tell 논문에서도 피처 벡터를 매 스텝마다 입력으로 사용했음
  - 과적합(Overfit)이 발생하여 해당 과정을 삭제했다고 저자가 말함
- 매번 주어지는 이미지의 정보를 항상 동일한 피처 벡터가 아니라 매번 다른 가중치를 고려한 어텐션 메커니즘을 이용한 피처 벡터라면 결과는 달라짐
![image](https://github.com/user-attachments/assets/db4401c8-aaec-40db-9a33-cde829226dcb)

- 위의 그림을 이용하여 설명
  - (1) 피처맵(3x3x128)을 LSTM셀에 넣어 첫번째 워드 임베딩을 가장 잘 유추해낼 수 있는 어텐션 분포를 구함
    - 에텐션 분포 : 피처맵과 같은 차원(3X3)이나 채널 수는 1로 구해짐
    - 이렇게 구한 어텐션 분포1을 피처맵의 각 채널과 곱하여 1X128 차원의 Weighted 피처 벡터를 만듦
  - (2) 첫 번째 워드 임베딩(문장의 시작을 알려주는 워드임베딩)과 같이 LSTM 셀로 넣어줌
    - LSTM은 2개의 Matrix를 출력하게 되는데 예측 워드와 다음 워드의 에텐션 분포임
    - 이렇게 각 스텝마다 다음 워드를 예측하기 위한 서로 다른 에텐션 분포를 생성함
  - LSTM셀의 입장에서는 **이전 워드와 예측할 워드의 정보가 담겨져있는 Context Vector를 입력받게 되는 것**
    - 위와 같은 어텐션 메커니즘(Soft attention)을 보완하여 추가적으로 Hard 어텐션 메커니즘을 적용함

### RNN with Attetion(Visual Attention)
- Attention에 대한 개념
  - 다른 곳에서 개념

- Show, Attention and Tell 논문에 나온 Visual Attention에 대한 설명
  - 기존 Show and Tell 논문에서 LSTM으로 입력되는 context vector는 CNN의 FC layer를 통과한 Vector였음
  - Show, attend and tell 논문에서는 CNN의 Feature Map(L x D)을 LSTM에 제시함
    - 논문에서는 CNN 모델로 VGG 16을 사용했고 14x14x256 크기의 Feature map을 사용했음
    - 14x14은 flatten 시켜서 196x256 크기의 feature map를 LSTM에 제시함

- Feature map을 이용하여 어떻게 Attention Value를 만들어냈는지?
  - LxD 크기의 Feature map을 0번째 Hidden cell h0에 넣어 첫 번째 attention value a1(Lx1)을 구함
  - 첫 번째 attention value와 Feature map을 곱하여 하나의 Weighted feature z1를 만듦
  - 이렇게 구해진 Weighted feature z1과 First word(y1)를 1번째 Hidden cell h1의 input으로 사용함

- 1번째 Hidden cell h1의 output으로는 2가지가 나옴
  - 하나는 0번째 Hidden cell h0의 output과 같은 attention value a2가 나옴
  - 다른 하나는 prediction word의 원핫 벡터 distribution인 d1이 나옴
  - 이와 같은 재귀적으로 반복하여 이미지에 대한 캡셔닝을 구할 수 있음
- 해당 논문에서는 attetion value a를 구하는 방식을 두 가지로 제시하고 있음
  - 각각 : soft attetion, hard attention이라고 부름

### Soft attetion의 수식적 이해
- Soft attetion은 우리가 흔히 쓰는 attention 개념
  - 미분 가능한 형태이므로 Back Propagation을 통해 학습을 진행함
- Hard Attetion은 미분 불가능한 형태로 학습을 위해 강화 학습을 사용함
  - 이해하기 어렵고 많이 쓰이는 방법이 아니기에 설명 생랼

