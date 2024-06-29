# Image Segmentation
- 입력 이미지에서 픽셀의 각 클래스를 구분하는 Task

# 1. 이미지 분할 아이디어
## 이미지 분할
- 바운딩 박스(Bounding box)로 검출된 물체들을 나타내는 객체검출(object detection)과는 다르게 이미지 분할(Image segmentation)은 픽셀의 분류 문제
- 목표 : 네트워크가 입력 이미지 안의 모든 픽셀을 지정된 개수의 클래스로 분류하는 것

## 이미지 분할의 종류
- Semantic Segmentation : 각 Pixel이 어떤 클래스인지 구분하는 문제
- Instance Segmentation : 더 나아가 같은 사물 안에서 서로 다른 객체(Instance)까지 구분하는 문제
- 이미지 분할 네트워크
  - 각 Pixel이 N개의 클래스 중 어떤 클래스에 속하는지를 나타낸 Segmentation map을 출력함
    - Segmentation map은 클래스의 개수와 동일하게 N개의 채널로 구성되어 있음
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/8425b975-f54b-4327-8260-47d2859b4bcb)

  - Segmentation map에 argmax를 통해서 1채널 이미지를 출력으로 내보냄
 ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/17a3b349-2084-40d4-90fc-c9fbf85ab203)


## 이미지 분할 네트워크의 기본 구조 : 인코더 & 디코더(Encoder & Decoder)
- 이미지 분할에 사용되는 많은 네트워크는 이미지의 사이즈를 줄이는 Encoder-Decoder로 구성되어 있음
- 이미지 분할의 핵심 아이디어
  - 입력 이미지의 W,H를 줄이고 채널 수를 늘려 피처의 개수를 증가시킨다
  - W,H를 입력이미지의 사이즈로 회복, 채널 수는 클래스의 사이로 맞춰 Segmentation map을 생성한다
- 이미지 W,H를 보존하면서 피처를 추출하면 좋겠으나 메모리 문제로 입력 이미지의 W,H를 유지하며 피처를 추출할 수가 없음
  - 위와 같이 네트워크를 구성하고 학습을 진행하면 Instance/Sementic별 픽셀이 분할되도록 네트워크의 가중치가 학습됨
  - 
# 2. 이미지 분할 모델 이해를 위한 사전 지식
## 1) Down-sampling
- 신호처리에서 말하는 용어 => sample의 개수를 줄이는 처리과정을 의미
  - 딥러닝에서는 인코딩할 때 data의 개수를 줄이는 처리 과정

### Pooling
- 특정한 규칙(Max, Average)에 의해서 Kernel 내에서 값을 만들어 내거나 추출하는 방법
- Max Pooling과 Average Pooling
  ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/10cb86bd-5b28-4cb0-a265-3c38d4bfe08c)

  - 해당 영역(kernel) 내에서 평균 혹은 최대값을 계산하여 요약된 데이터를 만들어냄
  - pooling의 방법으로 Downsampling을 하는 방법이 일반적임

### Dilated (Atrous) convolution
- Convolution도 Down sampling의 한 방법으로 사용할 수 있음
  - Pooling 계열과는 다르게 학습과정을 거침
  - 효과적으로 down samplin 할 수 있음
- 단점 : receptive field를 크게 하기가 어려움
  - receptive field : 출력 레이어의 뉴런 하나에 영향을 미치는 입력 뉴런들의 공간 크기
  - ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/387bfbc8-1add-4aea-9588-4bed145b09b7)
    - ex : 입력이 32x32x3인 경우 필터의 크기가 5x5x3 이면 receptive field는 5x5x3이 됨(필터의 크기와 같음)
  - receptive field를 크게 하면 trainable parameter가 무수히 늘어남
- Dilated Convolution : 위의 단점을 보완하기 위해 고안해낸 방법
  - Dilated convolution의 filter : 일반적인 convolution filter 사이에 빈 공간을 넣어서 구멍이 뚫려 있는 듯한 구조를 가짐
  - Sematic Segmentation에서 높은 성능을 내기 위해서 => CNN의 마지막 feature map에 존재하는 한 픽셀이 입력값에서 어느 크기의 영역에서 커버하는지를 결정하는 **receptive filed가 얼마나 큰지가 중요함**
  - Dilated Convolution을 수행하면 기존 convolution과 동일한 양의 파라미터와 계산량을 유지하면서도 receptive field는 커짐
  - Dilated Convolution을 시행할 때는 확장비율(dilation rate,r)를 지정하여 filter 사이에 빈 공간을 얼마나 둘지를 결정함
  - ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/5b4d7ff3-1b08-4306-9dd0-5c0eedee45c6)

### Depthwise convolution
- 일반적인 convolution 연산 수행
  - 하나의 filter를 입력 영상의 모든 채널에 적용하고 그 출력물을 더하여 하나의 feature map을 출력함
  - 특정 채의 spatial feature를 추출하는 것이 불가능함
  - convolution layer가 깊어질수록 연산량이 증폭된다는 단점도 있음
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/a4fccb0d-3ca8-4317-9886-8b6db4697aa6)


- Depthwise convolution : 위의 단점을 해결하고자 제시된 것
  - 각 channel마다 spatial feature를 추출함 => 각 channel별 filter가 존재함
  - 해당 특징으로 input channel 수와 output channel 수가 같게 됨
  - depth-wise convolution은 한 번 통과하면 하나로 병합되지 않고 (R,G,B)가 각각 Feature map이 됨
    - 특정 채널만의 spatial feature를 추출하는 것이 가능해짐
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/f1384368-5976-4bca-91a7-1bac75a77fe6)

- 기존 Convolution과 Depthwise convolution 비교(파라미터와 연산량 측면)
  - W : input/output의 width
  - H : input/output의 height
  - C : input의 channel
  - K : kernel의 크기
  - M : output의 channel
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/21796b99-ea65-4c31-a555-156c47aa32e0)

### No. of Parameters
- 기존 Convolution
  - 하나의 filter가 가지는 parameter 크기 : K x K x C
  - 하나의 filter에서 나오는 output : output channel 중 하나에 해당하니 output을 M개의 channel로 만들어 주려면 이러한 filter의 개수가 총 M개가 있어야 함
  - 총 parameter 수 : K x K x C x M
- Depthwise convolution 시행 시
  - convolution filter가 가지는 parameter 크기 : K x K x C
  - 하나의 filter에서 나오는 output이 output channel 전체에 해당됨
  - 총 parameter 수 : K x K x C

### Computational Cost
- 기존 convolution와 Depthwise convolution 모두 output 크기 : H x W
- 하나의 OUTPUT : parameter 개수 x H x W 번 연산 해야됨

![image](https://github.com/JuHwna/thesis_summary/assets/49123169/4c177936-23e5-43e3-880a-99b591657cbe)

### Depthwise separable convolution
- Depthwise convolution 뒤에 1x1 convolution을 연결한 구조
- 기존 Convolution 필터가 Spatial dimension과 Channel dimension을 동시에 처리하던 것을 따로 분리시켜 각각 처리하는 방법
  - 두 축을 분리시켜 처리를 하더라도 최종 결과값은 두 축 모두를 처리함 => 기존 convolution이 수행하던 역할을 대체할 수 있음
- 장점 : 기존 Convolution에 비해 parameter의 수와 연산량이 훨씬 적음
  - 핵심 : 연산량이 높은 곳에서는 최대한 Feature Map을 적게 생성, 연산량이 낮은 곳에서 Feature Map의 숫자를 조절하는 것

![image](https://github.com/JuHwna/thesis_summary/assets/49123169/56a2df71-b498-4ac0-b676-3c8cc3767fff)

### No. of Parameters
- 기존 Convolution에서 하나의 filter가 가지는 총 parameter 수 : K x K x C x M
- Depthwise convolution을 시행하면 총 parameter 수 : K x K x C
- Depthwise seperable convolution : Depthwise convolution에 1x1xC 크기의 Convolution을 M개 연결한 것
  - 총 parameter 수 : K x K x C + 1 x 1 x C x M

### Computational Cost
- Depthwise seperable convolution
  - Output 크기 : H x w
  - 하나의 output : parameter 개수 x H x W 연산
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/b4ddd2b0-add9-4e09-af10-d24e1218cb2d)

- Atrous convolution, Depthwise separable convolution : sementic segmentation 모델 중 상위 성능을 보이는 Deep lab에서 공통적으로 사용하는 방법

## 2) Up-sampling
- Down sampling의 반대로 디코딩시 복원하기 위해서 data의 크기를 늘리는 처리 과정
- Upsampling의 방법 중 대표적인 것

### Unpooling
- Nearest Neighbor Unpooling : Maxpooling을 거꾸로 재현하여 주변 픽셀들을 동일한 값으로 채움
- Bed of NailsUnpooling : 0으로 채워주는 방식
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/0ba51ec6-ae1d-4aac-9a75-fe49207c60d7)

### Max Unpooling
- Unpooling 방식의 문제점
  - 2x2의 Matrix로 Max pooling된 data가 있다고 하면, 원래 사이즈인 4x4의 Matrix로 Unpooling하게 되면 원래 Max pooled된 값의 위치를 알 수 없음
- Max Unpooling : Unpooling 문제점 개선
  - Max pooling할 때의 선택된 값들의 위치를 기억해 원래 자료의 동일한 위치에 Max값을 위치시켜 Unpooling함
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/2163db6e-7178-4f30-82aa-043a10213edd)

### Bilinear Interpolation


### Deconvolution
- **convolution의 역연산으로 inversed matrix(역행렬)을 이용함**
- convolution 연산 수식 : $f*i = o$
  - f : filter(또는 kernel)
  - \* : convolution 연산
  - i : input
  - o : output
- Deconvolution : f,i,o 값을 모두 알고 있는 상황에서 f 역행렬 * o라는 연산을 통해 i를 알아내는 과정
  - 수식 : $inverse matrix of f*i = o$

### Transposed Convolution(Backward Strided Convolution)
- 기존에 알고 있는 f의 역행렬을 구하는 것 x
- **학습을 통해 새로운 f를 구함 => Deconvolution과 구별됨**
  - 수식 : $f`*i=o$
  - f` : 학습을 통해 만들어진 새로운 filter

- 이름에 "transposed(전치, 행과 열이 바뀜)"라는 단어가 붙은 이유를 이해하기 위한 설명
  - 일반적인 convolution의 계산 과정이 실제로는 어떻게 이루어지는지 확인 필요
    - 3x3 Kernel* 4x4 input = 2x2 output을 도출하기 위해 일반적인 convolution의 matrix 연산 수행 과정
       1. 3x3 kernel은 4x16 sparse matrix로 변환
       2. 4x4 input은 16x1 vector로 변환
       3. 4x1 output vector를 2x2 output으로 변환
    - ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/4ec8008b-74ab-4172-bc6e-fa88591c6a5b)
    - Transposed convolution 목표 : 3x3 kernel * 2x2 input = 4x4 output을 도출하는 것 => 연산 수행 과정
       1. 3x3 kernel은 16x4 sparse matrix로 변환
       2. 2x2 input은 4x1 vector로 변환
       3. 16x1 output vector를 4x4 output으로 변환
    - ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/c6624b7e-1940-440c-a767-8f1ceec02b50)
      - transposed convolution할 때 가중치 w의 위치가 transposed된 것을 볼 수 있음
        - 실제로는 위치도 전치되고 가중치의 값도 변함
      - input, output 값을 알고 있으므로 학습을 통해 최적의 가중치 값을 찾아가게 됨

### Transposed convolution의 구현
- keras에서 transposed convolution을 구현할 때 : Conv2DTranspose를 통해 구현하게 됨
- stride 값을 어떻게 하는지에 따라 output의 크기가 달라짐
  - 왜 이런 결과가 나오는지?
    - 파란색 feature map : 2x2 input
    - 초록색 feature map : 4x4 or 5x5 output
    - 일반적인 Convolution과 Transposed Convolution에서 stride의 의미가 반대
      - 일반적인 Convolution에서 stride 2 = 한 번에 두 칸씩 움직인다.
      - Transposed Convolution에서 stride 2 = 2칸 움직여야 다음 input 원소에 도달함
    - transposed Convolution에서 stride=1인 경우 아래 그림처럼 작동하여 최종 output 크기는 4x4
    - ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/0ae87b07-68b0-4e8a-b3ab-84346e2e5e27)
    - transposed Convolution에서 stride=2인 경우 아래 그림처럼 작동하여 최종 output 크기는 5x5
    - ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/d35a4edd-b009-4e2b-8b16-c9ada657fa82)

# 3. 이미지 분할 모델들
## 1) FCN
- 이미지 분류에서 우수한 성능을 보인 CNN 기반 모델(AlexNet, VGG16, GoogleNet)을 Semantic Segmentation Task를 수행할 수 있도록 변형시킨 모델
  - FCN 네트워크는 이미지 분류 문제를 먼저 트레이닝 시킨 후 모델을 튜닝해 학습하는 Transfer Learning으로 구현함
  - 이후 나온 Semantic Segmentation 방법은 대부분 FCN의 아이디어를 기반으로 했음

### 네트워크 핵심 아이디어
- 이미지 분류
  - 이미지 내의 모든 픽셀에서 Feature를 추출(Extraction)하고 추출한 Feature들을 분류기(Classifier)에 넣어 입력 이미지(Total)의 Class를 예측하는 구조

- 이미지 분할
  - 이미지 분류에서 좀 더 나아가서 이미지(Total)의 Class 예측 X
  - 이미지를 이루는 모든 픽셀들의 Class를 예측하는 문제로 생각

- FCN
  - 기존 이미지 분류에서 쓰인 네트워크를 트레인된 상태에서(Pretrain)
  - Feature Extraction 레이어는 그대로 활용하여 Feature를 추출하고 FC 레이어를 버리고
  - 1x1 Conv 그리고 Up-sampling(Transpose Convolution)로 변경하여(Fine-Tuning) 픽셀 클래스 분류와 입력이미지와 같은 사이즈 회복을 하도록 네트워크가 구성됨

![image](https://github.com/JuHwna/thesis_summary/assets/49123169/83c61153-37eb-4736-9ab4-c5995d453071)

### 네트워크 구조
- FCN의 구조 : 4단계
   1. Convolution Layer를 통해 Feature 추출
   2. 1x1 Convolution Layer를 이용해 피처맵의 채널 수를 데이터셋 객체의 개수와 동일하게 변경
   3. Up-sampling : 낮은 해상도의 Heat Map을 Upsampling(=Transposed Convolution)한 뒤, 입력 이미지와 같은 크기의 Map 생성
   4. 최종 피처 맵과 라벨 피처맵의 차이를 이용하여 네트워크 학습

![image](https://github.com/JuHwna/thesis_summary/assets/49123169/0a5785cc-8b92-4b10-89cd-11726719a5fa)

![image](https://github.com/JuHwna/thesis_summary/assets/49123169/6efcda91-9a58-47fe-b933-f388a39c6a8f)

- 기본 FCN 네트워크 문제
  - VGG16에서 입력 이미지의 크기가 224x224인 경우 5개의 convolution block을 통과하면 Feature map의 크기 : 7x7이 됨
  - 기존 입력 이미지(크기 H x W)가 5개의 convolution block을 통과하면 H/32 x W/32 크기의 Feature map을 얻게 됨
  - Feature map의 한 픽셀 : 입력 이미지의 32x32 pixel를 대표하게 됨
    - 해당 Feature map은 낮은 해상도를 가짐 -> 입력 이미지의 위치 정보를 대략적으로만 가지고 있음
  - 문제는 3번 Up-sampling 과정에서 발생
    - 입력 이미지 위치 정보를 **대략적으로** 가지고 있는 feature map을 Up-sampling하여 얻은 segmentation map은 기존 입력 이미지와 비교했을 때 뭉뚱그려져 있고 디테일하지 못함
    - ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/a38f7a1b-bf0e-4eec-8639-50ea15a624a8)

### Up-sampling by Transposed convolution
- 뭉그러짐 문제를 해결하기 위해 먼저 드는 생각
  - Down-sampling을 하지 않아 feature map이 작아지지 않도록 하는 것
    - but, Down-sampling을 통해 feature map의 사이즈를 줄이는 과정이 없다면 **연산량이 급격히 늘어나 학습에 필요한 시간 및 비용이 너무 커지게 됨**
- Down-sampling은 필수, 이를 해결하기 위해 효과적인 Up-sampling을 위한 방법이 여러개 고안됨
  - 추가 필요
- FCN에서는 **Transposed convolution을 이용** => Up-sampling 진행

### Skip architecture
- 좀 더 디테일한 segmentation map을 얻기 위해 => Skip architecture라는 기법 제안
  - 최종 피처맵은 지역 정보를 '대략적으로' 유지하고 있어 이미지가 뭉개지는 것을 보완한 방법
- 핵심 아이디어 : 피처 추출 단계의 피처맵도 업샘플링에 포함하여 위치 정보 손실을 막자라는 것

### FCN 확장 모델
#### FCN-32s
- 5번의 convolution block을 통과해 1/32만큼 줄어든 5번 Feature map(5번 feature map 크기 : 7x7)
- 5번의 Feature map이 convolution layer를 통과하여 같은 크기의 6번 Feature map을 얻음
- 6번 Feature map을 한 번에 32배 upsampling(H/32 x W/32 크기를 HxW 크기로)

#### FCN-16s
- 4번의 convolution block을 통과해 1/16만큼 줄어든 4번 Feature map, 4번의 Feature map 크기는 14x14
- 4-1번 Feature map : 6번 Feature map을 2배 Upsampling(H/32 x W/32 크기를 H/16x W/16 크기로) 한 것과 4번 Feature map을 Sum함
- 새롭게 얻은 4-1번 Feature map을 한 번에 16배 upsampling(H/16 x W/16 크기를 HxW 크기로)

![image](https://github.com/JuHwna/thesis_summary/assets/49123169/8c9e95f5-47b6-4b8e-9208-c0caba818e4b)


#### FCN-8s
- FCN-16s과 유사한 Step이 추가됨
- 3-1번 Feature map : 4-1번 Feature map을 2배 upsampling(H/16 x W/16 크기를 H/8 x W/8 크기로) 한 것과 3번 Feature map을 Sum함
- 3-1번 Feature map을 한 번에 8배 upsampling(H/8 x W/8 크기를 HxW 크기로)

![image](https://github.com/JuHwna/thesis_summary/assets/49123169/0c4dd21e-522d-4734-af92-2275be3457ea)

- 결과 이미지 : 위치 정보가 더 잘 전달되어 FCN-32s => FCN-16s => FCN-8s 순서로 더 정교해졌음
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/5537207d-74e8-40fa-9f4a-79b00a09daab)

### 네트워크 트레이닝
- 데이터 셋 구성 : {입력 데이터 : 이미지, 라벨 데이터 : 픽셀이 속하는 클래스}
- 네트워크를 통해서 나온 출력값(Matrix) : 라벨 데이터와 같은 포맷으로 픽셀의 클래스를 값으로 갖는 피처 맵
- 손실함수 : 모든 픽셀의 크로스 앤트로피를 구하고 이를 모두 더하여 최종적으로 손실을 구함
  => 논문 : Multinomial logistic loss

### 네트워크 장단점 및 시사점
#### Skip architecture 아이디어
- Skip architecture 아이디어 : 최종적으로 나오는 피처에 local 정보를 추가
  - 파라미터의 큰 증가 없이 성능을 비약적으로 향상시켰음
  - 후속 연구에도 큰 영향을 미침

#### "이미지 분류" 네트워크를 "이미지 분할" 네트워크에 적용
- 서로 다른 Task의 네트워크를 활용하여 문제 해결
- 이미지 분류는 당시 엄청난 성능 향상이 이뤄진 상태
  - 이미지 분류 베이스 모델을 수정하여 이미지 분할에 적용시켜 큰 성능향상을 가져옴
- 이미지 분류 네트워크에서 추출하는 피쳐를 이미지 분할에 수정없이 사용가능하다는 점을 보여줌

#### FC 레이어를 삭제하여 이미지 분할을 구현 가능하도록 만들었음
- AlexNet, VGG 등 이미지 분류에 자주 쓰이는 FC 레이어를 이용하여 이미지 분할을 하는데 적합하지 않음
- 대표적인 이유
   1. FC layer(Fully connected layer)를 통과하고 나면 이미지의 위치 정보가 사라지기 때문
      - ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/2df71985-440e-49c6-8db6-cf4bd48e080f)
   2. FC layer는 고정된 크기의 input image만 받을 수 있기 때문
      - Dense layer에 가중치 개수가 고정되어 있기 때문에 바로 앞 레이어의 Feature map의 크기도 고정됨
      - 연쇄적으로 각 레이어의 Feature map 크기와 input image 크기 역시 고정됨
      - ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/04c46c7c-0f74-4f31-9c1a-9e78a772d22e)
   3. FC layer는 파라미터 개수를 너무 많이 필요로 함
      - FC 레이어를 이용하여 픽셀마다의 클래스를 예측하게 구성하게 하거나 혹은 Class Presence Heat Map을 만들려면 파라미터의 수가 너무 많이 증가함
      - ex) 4x4의 피처맵에서 2x2의 히트맵을 추출해낸다고 하면 FC 레이어는 4x4x4개의 weight가 필요함
        - 피처맵이 4x4보다 훨씬 크고 뒤이어지는 Up-sampling을 생각하면 어마어마한 컴퓨터 성능을 필요하게 됨
      - 해당 문제 해결을 위해 fully connected 레이어를 1x1 convolution 레이어로 바꿈
      - ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/fda661b3-1ae1-400f-974c-f7a6e5226baa)

## 2) SegNet
- 2016년에 공개된 모델
- 모델 목적 : 도로를 달리면서 촬영한 영상에 대해 pixel-wise semantic segmentation하기 위해 설계
- 자율 주행에 큰 역할을 한 모델
  - 도로와 보도가 일견 보기에는 비슷해보이지만 두 class간의 경계를 잘 구분하기 때문
- 기존의 sementic segmentation 모델의 문제
   1. 해상도가 매우 떨어짐
      - Max pooling, sub-sampling 연산을 수행할 시 : coarse(추상적인, 알맹이가 큰) feature map이 만들어지게 되는데 이런 feature map으로는 픽셀 단위로 정교하게 segmentation을 할 수 없음
      - FCN에서 이를 해결하기 위해 Skip architecture등 다양한 해결 방법을 시도 => 역시 정교하지 못했음
   2. 실시간으로 빠르게 segmentation 불 가능
      - 정확도가 높다고 하더라도 계산량이 많거나 parameter 수가 많으면 빠르게 segmentation을 할 수 없음
      - memory 및 inference time 측면에서 효율적으로 동작할 수 있어야 함
- 위의 문제를 해결하고자 등장한 모델 : SegNet
  - 특징 : Encoder - Decoder로 구성되어 있음
    - 해당 구조는 최근의 모델에서도 흔히 사용되고 있음
    - sementic segmentation 분야에 전체적으로 큰 영향을 끼친 구조로 볼 수 있음

### 네트워크 구조
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/a6bc532b-002c-41f4-994d-fab554c8f245)

#### 1) Encoder Network
- VGG16의 구조에서 FC layer를 뺀 13개의 layer를 사용 => 연산량 줄임
  - 일반적으로 encoder-decoder network에서 encoder로 CNN 이용 시 : FC layer를 뺐음
  - classification을 할 것이 아니라면 FC가 중요한 역할을 하지도 않음 => 계산량이 너무 많이 들기 때문

#### 2) Decoder Network
- Decoder network는 각 encoder network에 대응하여 존재(mirrored)
  - Encoder의 pooling layer : Up-sampling layer로 대체
  - Up-sampling layer 뒤에는 Conv + batch norm + ReLU가 연결됨
- Coarse feature map이 생기는 이유 : pooling 및 convolution 연산 때문에 feature map의 정보가 소실되기 때문
  - Decoder에서 up-sampling을 할 때 Encoder의 feature map 정보를 decoder로 전달할 수 있다면 소실된 정보를 다시 찾는 것이니 pixel 단위로 정교하게 segmentation을 할 수 있을 것

- Encoder의 feature map 정보를 decoder로 전달하는 가장 정확한 방법
  - 전체 feature map을 저장해 두었다가 Up-sampling할 때 모두 Decoder로 전달하는 것
  - 단점 : 해당 방식을 수행하기 위해서 많은 메모리가 필요함
- SegNet에서는 max-pooling indices(위치 정보)만을 저장해두었다 이후 Max Unpooling을 진행함
  - 해당 방법은 accuracy는 아주 조금 감소, memory는 크게 아낄 수 있음

![image](https://github.com/JuHwna/thesis_summary/assets/49123169/d17d8464-26a7-45bd-a307-9ed2bc8a5959)

- Max Unpooling 방식으로 Up-sampling을 하면 장점
   1. FCN에서는 Transposed convolution으로 unsampling을 진행했음
     - SegNet은 Transposed convolution을 사용하지 x => 학습 파라미터가 없어 전체 parameter 개수를 줄일 수 있음
   2. 전체 모델은 end-to-end 학습이 가능함
   3. 다른 encoder-decoder 형식에 응용될 수 있고 변형도 가능함

#### 3) Softmax classifier
- Decoder의 output은 K-class softmax classifier로 들어가 최종적으로는 각 픽셀마다의 독립적인 확률값으로 계산됨
- 위 결과에서 각 픽셀별로 가장 확률이 높은 class만을 출력하여 최종 segmentation이 됨

### SegNet의 성능
- SegNet의 성능을 다른 architecture(FCN, DeepLab-LargeFOV, DeconvNet 등)와 비교한 결과를 제시하고 있음
- SegNet의 성능을 2가지 scene segmentation benchmark에서 평가했음
   1. Cam Vid dataset - road scene segmentation
   2. SUN RGB-D dataset - indoo scene segmentation
- 정량적 평가 척도로 총 4가지 metric을 사용했음
   1. Global accuracy(G) : 데이터셋 전체의 픽셀 수에서 올바르게 분류된 픽셀의 수
   2. Class average accuracy(C) : 각 클래스마다 accuracy를 계산한 뒤, 평균낸 것
   3. mloU
   4. Boundary F1 Score(BF) : 2\*precision\*recall/(recall+precision)

#### Cam Vid dataset
- SegNet, DeconvNet이 가장 좋은 성능을 보임
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/95b403e0-27c3-4234-a6a7-111be6180b86)

#### SUN RGB-D dataset
- SegNet은 다른 모델들과 비교해서 G,C,mloU, BF 모두에서 우수한 성능을 보임

![image](https://github.com/JuHwna/thesis_summary/assets/49123169/9746372a-ab47-420f-986c-2bd5ce60a789)

## 3) U-NET
- ISBI cell tracking challenge 2015 대회에서 등장한 모델
  - ISBI cell tracking challenge 2015 대회에서 사용된 데이터 셋의 특성
    - Dataset : Transmitted light microscopy images(Phase contrast and DIC)
    - Transmitted light microscopy images : 투과 광선 현미경 검사
    - Phase contrast : 위상차 현미경
    - DIC(Differential interference contrast microscope) = 차등간섭대비 현미경
    - Input size : 512x512 pixel, 30개
- U-NET은 매우 적은 수의 학습 데이터로도 정확한 이미지 세그멘테이션 성능을 보임
  - 해당 대회에서 우승

### 네트워크 핵심 아이디어

![image](https://github.com/JuHwna/thesis_summary/assets/49123169/7bd83bd0-3224-4402-aafb-e06681d076f2)

- U-Net 네트워크 : 네트워크 모양이 U
- U-Net 네트워크의 핵심 아이디어(3가지)
   1. 인코더(Contract path)의 피처맵을 디코더 피처맵에 Concat하여 위치 정보전달
   2. 데이터셋의 전처리, 변형(deformation)을 이용하여 데이터 수 증가
   3. 테두리(border line)를 더 잘 분할하기 위해 Weight를 추가한 손실함수(Loss function)

### 네트워크 구조
- 일반적으로 Semantic Segmentation 모델
  - Down=sampling을 통해 크기가 줄어들었다가 다시 Up-sampling을 통해 크기가 늘어나는 구조를 취함
- U-NET도 비슷하지만 이를 다르게 부르고 있음
   1. Contracting Path : 점진적으로 넓은 범위의 이미지 픽셀을 보며 의미정보(Context Information)을 추출
   2. Bottle Neck : 수축 경로에서 확장 경로로 전환되는 전환 구간
   3. Expanding Path : 의미 정보를 픽셀 위치정보와 결합(Localization)하여 각 픽셀마다 어떤 객체 속하는지를 구분

![image](https://github.com/JuHwna/thesis_summary/assets/49123169/f5a916b5-a3d3-49bf-acb2-b5bbfe50b433)
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/e8782878-f410-4b2a-b0df-b392cfa41b22)

### Skip Architecture
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/5411dcbc-5ac0-4bbb-a506-b3cb98a1f6ca)

- U-Net에서도 FCN과 비슷하게 Skip Architecture를 활용
  - 다른 점 : 동일한 level에서 나온 Feature map을 더한다는 점
- Contracting Path의 Feature map이 Expanding Path의 Feature map보다 큼
  - Contracting Path에서 여러 번의 패딩이 없는 3x3 Convolution Layer를 지나면서 Feature map의 크기가 줄어들기 때문
  - Contracting Path의 Feature map의 테두리 부분을 자른 후 크기를 동일하게 맞추어 둔 feature map을 합쳐 줌

### 네트워크 특징
- 총 23-Layers Fully Convolutional Network 구조
- 최종 출력인 Segmentation map의 크기 : Input Image 크기보다 작음
  - Convolution 연산에서 패딩을 사용하지 않았기 때문
- https://medium.com/@msmapark2/u-net-%EB%85%BC%EB%AC%B8-%EB%A6%AC%EB%B7%B0-u-net-convolutional-networks-for-biomedical-image-segmentation-456d6901b28a

### 입력 이미지(Input image)에 적용한 기법들
- 일반적인 딥러닝 모델과 UNet과의 차이점 : 탐색 방식
  - 일반적인 딥러닝 모델
    - sliding window가 전체 이미지 위로 조금씩 이동하여 해당 영역을 각각의 DNN에 제시함
    - 단점 : 이미 사용한 영역의 일부를 다음 순서에서도 다시 훓어보기 때문에 계산량이 많아짐
      - Input image 크기가 클수록 모델의 속도도 확연이 저하됨

  - UNET의 경우 : patch 탐색 방식 사용
    - 이미지를 격자 모양으로 자름
      - 중첩되는 부분이 존재X
      - 속도 면에 있어 훨씬 나은 성능을 보임 => 이미 훓어본 영역은 깔끔하게 넘기고 다음 patch부터 탐색을 시작
        
- 해당 대회의 이미지 특징
   1. 의료 데이터이며 크기가 천차만별이고 사이즈나 해상도가 큼
   2. 부족한 데이터의 숫자
  
- 위의 문제를 해결하기 위해 논문의 저자는 두 가지 가정을 세움
   1. 일단 작게 자르고 부족한 크기의 이미지는 테두리에 좌우대칭 패딩(Padding) 진행
      - 테두리를 좌우대칭을 하는 것이 0으로 채워넣는 제로패딩보다 실제 삭제되지 않은 모습에 더 가까울 것
   2. Cell들은 유사한 형상이므로 기초적인 변형들(deformation)을 주어도 실제로 있을법한 데이터가 될 것
  
- 위의 두 가지 가정을 이용하여 두 가지 기법 사용 : Overlap-tile strategy & Mirroring Extrapolation, Data Augmentation
  - 위의 기법들은 데이터 전처리와 변형과 관련됨
 
#### ① Overlap-tile strategy & Mirroring Extrapolation 데이터 전처리
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/36cd6930-c36b-45e4-a555-fe5fd3cb2dec)

- UNE의 구조를 보면 388x388 크기의 Segmentation map을 얻기 위해 572x572 크기의 input image가 필요
  - 위 그림에서 파란색 patch를 input image로 제시하면 노란색 영역의 Segmentation map이 출력됨
  - 이미지 크기가 줄어들어 나오는 이유 : UNET에서 padding 없이 Convolution 연산을 반복적으로 수행했기 때문
- 위의 missing data 문제를 해결하기 위해 사용한 것 : mirroring extrapolation임
  - 파란색 박스의 빈 공간을 노란색 영역이 거울에 반사된 형태로 채우는 방식
- 해당 영역을 zero pixel로 채울 수 있었음
  - mirroring extrapolation을 하면서 data augmentation의 효과를 줄 수 있음
  - 좌우 대칭을 해도 큰 영향이 없는 세포 등의 의학 데이터에서는 zero padding보다 나은 방법
 
#### ② Data Augmentation
- Sementic segmentation은 pixel 별로 class labeling 해주어야 해서 학습 데이터가 적은 편
  - 해당 대회의 데이터 수 : 30개
- UNET 저자들이 논문에서 언급한 data augmentation 방식 : 4가지
  - Shift, Rotation, Gray value, Elastic Deformation
  - Elastic Deformation : pixel이 랜덤하게 다른 방향으로 뒤틀리도록 변형하는 방식
    - 현실 세계에 있을 법하게 변형되게 만드는 것
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/e8c6e7a4-d87f-4808-9b8f-80b58b9e1e80)


### 네트워크 트레이닝
- 손실함수를 픽셀마다의 구한 에너지 펑션의 총합으로 구현함
- 픽셀의 예측값에 SoftMax를 구하고 이 구한 값에 크로스 엔트로피를 함
- 특이하게 크로스 엔트로피에 픽셀 고유의 Weight를 곱함으로써 픽셀의 loss값을 계산함
  - ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/bef029b8-b42d-47d2-8bfb-0467c3828bcd)
  - 픽셀 고유의 Weight는 노드와 연결된 Weight를 의미하는 것이 아님
    - 경계선 라인에 더 강한 학습을 시키기 위해 가우시안 분포를 가정하고 경계선 픽셀에 더 큰 loss를 주었음
      - 모든 픽셀마다 각자의 weight를 가지고 있고 만약 픽셀이 경계선 픽셀일 경우 더 큰 손실값을 가지게 됨
      - 학습 전에 경계선과 경계선 아닌 픽셀들의 weight를 모두 구했고 이것을 weight map으로 구현하여 개발 시 사용함

### 네트워크 장점/단점/한계점
- U-NET 네트워크 시사점
  - FCN에서 나온 아이디어인 Skip architecture를 더욱 확장해서 사용한 모습을 보여줌
  - 개발된 화자분리(Speech Separation) 등의 Segment를 하는 네트워크 : U-NET의 형상과 매우 유사함
- 한계점
  - 특정 데이터에 한정된 기법

## 4) DeepLab V3+
- DeepLab v1~ v3+ architecture : 구글에서 제시한 모델
  - 2015년부터 현재에 이르기까지 계속해서 업데이트를 하고 있는 모델
- DeepLab시리즈의 발전 : 앞선 모델들을 계승하면서 조금씩 추가되는 항목이 생김
  - DeepLab V1 : Atrous convolution을 처음 적용
  - DeepLab V2 : multi-scale context를 적용하기 위한 Atrous spatial pyramid pooling(ASPP) 제안
  - DeepLab V3 : 기존 ResNe 구조에 Atrous convolution을 활용
  - DeepLab V3+ : Depthwise separable convolution과 Atrous convolution을 결합한 Atrous separable convolution을 제안

### 사용하고 있는 개념
#### Atrous convolution

dd
