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
- 학습된 뉴럴넷을 재활용하는 방법


## 3. Under/Overfitting
