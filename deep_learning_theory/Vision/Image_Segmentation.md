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
-
