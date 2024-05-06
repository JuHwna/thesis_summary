# Image Segmentation
- 입력 이미지에서 픽셀의 각 클래스를 구분하는 Task

## 1. 이미지 분할 아이디어
### 이미지 분할
- 바운딩 박스(Bounding box)로 검출된 물체들을 나타내는 객체검출(object detection)과는 다르게 이미지 분할(Image segmentation)은 픽셀의 분류 문제
- 목표 : 네트워크가 입력 이미지 안의 모든 픽셀을 지정된 개수의 클래스로 분류하는 것

### 이미지 분할의 종류
- Semantic Segmentation : 각 Pixel이 어떤 클래스인지 구분하는 문제
- Instance Segmentation : 더 나아가 같은 사물 안에서 서로 다른 객체(Instance)까지 구분하는 문제
- 이미지 분할 네트워크
  - 각 Pixel이 N개의 클래스 중 어떤 클래스에 속하는지를 나타낸 Segmentation map을 출력함
    - Segmentation map은 클래스의 개수와 동일하게 N개의 채널로 구성되어 있음
![image](https://github.com/JuHwna/thesis_summary/assets/49123169/8425b975-f54b-4327-8260-47d2859b4bcb)

  - Segmentation map에 argmax를 통해서 1채널 이미지를 출력으로 내보냄
 ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/17a3b349-2084-40d4-90fc-c9fbf85ab203)


### 이미지 분할 네트워크의 기본 구조 : 인코더 & 디코더(Encoder & Decoder)
- 이미지 분할에 사용되는 많은 네트워크는 이미지의 사이즈를 줄이는 Encoder-Decoder로 구성되어 있음
- 이미지 분할의 핵심 아이디어
  - 입력 이미지의 W,H를 줄이고 채널 수를 늘려 피처의 개수를 증가시킨다
  - W,H를 입력이미지의 사이즈로 회복, 채널 수는 클래스의 사이로 맞춰 Segmentation map을 생성한다
- 이미지 W,H를 보존하면서 피처를 추출하면 좋겠으나 메모리 문제로 입력 이미지의 W,H를 유지하며 피처를 추출할 수가 없음
  - 위와 같이 네트워크를 구성하고 학습을 진행하면 Instance/Sementic별 픽셀이 분할되도록 네트워크의 가중치가 학습됨
## 2. 이미지 분할 모델 이해를 위한 사전 지식
### 1) Down-sampling
- 신호처리에서 말하는 용어 => sample의 개수를 줄이는 처리과정을 의미
  - 딥러닝에서는 인코딩할 때 data의 개수를 줄이는 처리 과정

#### Pooling
- 특정한 규칙(Max, Average)에 의해서 Kernel 내에서 값을 만들어 내거나 추출하는 방법
- Max Pooling과 Average Pooling
  ![image](https://github.com/JuHwna/thesis_summary/assets/49123169/10cb86bd-5b28-4cb0-a265-3c38d4bfe08c)

  - 해당 영역(kernel) 내에서 평균 혹은 최대값을 계산하여 요약된 데이터를 만들어냄
  - pooling의 방법으로 Downsampling을 하는 방법이 일반적임

#### Dilated (Atrous) convolution
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

#### Depthwise convolution
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

#### No. of Parameters

