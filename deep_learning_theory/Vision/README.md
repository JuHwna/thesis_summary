# 딥러닝 관련된 것들
## 1. Data Augmentation
(1)개요 : 데이터의 부족을 극복하고 Robust하게 만드는 것


(2)내용
- 딥러닝은 기본적으로 많은 데이터가 존재해야 학습이 잘됨
- 데이터의 수를 늘리는 것은 비용과 시간이 많이 필요함 + 어떤 경우에는 데이터 수집과 가공하는 것 조차 어려운 경우 존재
  - 1) 수집이 어려운 경우
    - 보안지역 감시 영상 데이터
    - 신체 주요 부위 혹은 개인 사생활 침해 데이터
  - 2) 가공이 어려운 경우
    - 의료, 법률 데이터와 같이 전문적인 지식이 필요한 경우
    - 평가자의 주관에 따라 판단 정도가 다를 경우(ex 인물 표정)
- Data Augmentation : 위의 문제를 해결하기 위해 기존의 데이터를 이용해 새롭게 데이터를 창조하는 기법
- **이미지 데이터의 Augmentation**
  - Data Augmentation의 방법에서 지켜야할 점 : Semantically Invariant Transformation
    - 데이터에서 중요한 부분을 보존하는 선에서 최대한 augmentation 하는 것이 좋다는 의미
  - 1) Basic image manipulation
    - Geometric Transformation
      - 기존 이미지를 Crop, Rotate, Contrast, Invert, Flip시켜 새로운 이미지를 만들어내는 방식
    - Color space Transformation
      - 기존 이미지의 RGB 값을 조정하여 새로운 이미지를 만들어내는 방식
    - Mixing images
      - 두 image를 0~1 사이의 \lambda 값을 통해 Weighted Linear Interpolation 해주는 기법
      - Label도 \lambda 값에 비례하여 지정함
    - Random Erasing
      - 이미지의 랜덤한 영역을 지워서 새로운 이미지를 만들어냄
    - Basic image manipulation 방법을 조합
      - CutMix
        - Mixing images와 Random Erasing 방법을 합친 방법
        - A image에서 box를 쳐서 지운 다음 그 빈 영역을 B image로부터 patch를 추출하여 집어넣음
        - Patch의 면적에 비례하여 Label도 섞어 지정함
      - PuzzleMix
        - cutmix를 개량한 방법
        - 두 이미지에서 중요한 feature는 보존하면서 섞도록 함
  - 2) Deep Learning Approach
    - Adversarial Training
      - Adversariel attack이란 DNN이 잘못된 결과를 산출하도록 의도적으로 조작시킨 입력값(adversarial example)을 생성하여 Training model에 제시하는 것을 말함
      - Adversarial Training : Adversarial example을 여러 개 제작하여 모델에 제시한 다음 어떤 상황에서 모델이 오분류를 일으키는지 확인하고 모델을 수정하여 전체적인 성능을 높이는 학습 방법
    - GAN Data augmentation
      - GAN(Generative Adversariel Networks) 모델을 이용해 기존 데이터와 유사한 샘플을 생성하여 데이터 수를 늘림
  - 3) Meta Learning
    - Autoaugmentation
      - 수많은 Data Augmentation 방법 중 해당 데이터셋에 적합한 기법을 제시하는 모델
      - ex) 구글 사례
        - 자주 사용되는 16가지 Data Augmentation 기법들 중 최적의 조합을 찾기 위해 PPO(Proximal Policy Optimization)로 학습하여 AutoAugmentation을 시행함
      - 계산량이 매우 많고 탐색 공간이 커 시간이 매우 오래 걸리고 사용할 수 있는 환경도 제한적임
        - 해당 문제 중 계산 속도를 개선하기 위한 여러 방법이 제시됨
        - Population Based Augmentation, Fast AutoAugment, Faster AutoAugment 등
    - RandAugmentation
      - 이전의 기법들이 적합한 Augmentation 기법을 찾는 모델이라면 해당 기법은 특정 모델을 찾는 것이 아님
      - batch마다 적용할 Augmentation 방법을 랜덤으로 추출하여 적용하는 기법
      - 성능은 다른 모델과 큰 차이가 없으나 코드가 단순하다는 장점이 있음

## 2. Pretraining, Transfer Learning, Fine-Tuning
(1)개요 : 학습된 뉴럴넷을 재활용하는 방법


(2)내용
- Transfer Learning의 필요성
  - 맨 밑바닥부터 학습시키는데 덩치가 큰 CNN일수록 엄청나게 많은 시간이 필요
    - (ex) MNIST와 같은 흑백 이미지를 인식하는 모델 : 최소 3개의 Convolution layer와 1개의 fully connected layer가 필요 + 학습시간은 1개의 cpu에서 1시간 정도 소요
    - (ex) CIFAR-10 등에서 사용되는 고해상도 컬러 이미지를 인식하는 모델 : 최소 5개의 Convolution layer와 2개의 fully connected layer가 필요 + 학습시간은 1개의 cpu에서는 수 백~수천 시간이 소요됨
  - Transfer Learning(전이 학습) : 이미 학습 되어 있는 CNN 모델, 즉 Pre-trained CNN을 가져와서 분석하고자 하는 데이터에 맞도록 Fine-tuning(미세 조정)하는 방법
    - 맨 밑바닥부터 학습 시키는 것에 비해 소요 시간이 획기적으로 줄어듬

- Transfer Learning은 왜 작동?
  - 딥러닝 모델의 중요한 성격 중 하나 : 초기 층은 **일반적인 특징**을 추출하도록 하는 학습이 이루어지는 반면에 모델의 마지막 층에 가까워질수록 특정 데이터셋 또는 특정 문제에서만 나타날 수 있는 **구체적인 특징**을 추출해내도록 하는 고도화된 학습이 이루어진다는 점
    - 초기 층은 다른 데이터셋의 이미지들을 학습할 때도 재사용될 수 있지만 마지막 층은 새로운 문제를 맞이할 때마다 새로 학습이 필요함

- Fine-tuning 시 고려할 점
  - 기존에 학습된 layer에 데이터를 추가로 학습시켜 파라미터를 업데이트해야 함
  - 주의할 점
    - pre-trained CNN이 학습한 데이터와 우리가 학습 시키고자 하는 데이터가 얼마나 유사한지, 데이터의 양은 얼마인지에 따라 Fine-tuning 시킬 영역 및 정도가 달라짐
    - 1) 새로 훈련할 데이터가 적지만, original 데이터와 유사할 경우
      - 데이터의 양이 적어, 전체 네트워크를 fine-tuning 하는 것은 over-fitting의 위험이 있기에 하지 않음
      - 
- 
## 3. Under/Overfitting
