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

## 2. Pretraining, Transfer Learning, Fine-Tuning
- 학습된 뉴럴넷을 재활용하는 방법


## 3. Under/Overfitting
