"""
텐서플로 기반 SegNet 구현
저자 : 안광은 (yooer10ms@cu.ac.kr)
버전 : python 3.5.4, tensorflow-gpu 1.4.0

저자 제공 SegNet 예제 모델이 Caffe 용이라니.. 게다가 다른 소스는 전부 Tensorflow 1.0용이라니 ㅠㅠ
하 슈밤... 그냥 내가 짠다.... 써글 ㅠㅠ 울고싶네 ㅠㅠ...

레퍼런스:
https://github.com/mathildor/TF-SegNet
https://github.com/mshunshin/SegNetCMR

"""

# Tensorflow 함수
import tensorflow as tf # 텐서플로 라이브러리 불러오기 

# 파이선 내장 함수
from datetime import datetime # 날짜 시간 함수
from PIL import Image # Pillow 이미지 라이브러리
from math import ceil # 수학 라이브러리 반올림 함수
import os, sys # 운영체제 및 시스템 라이브러리
import numpy as np # 과학 계산용 라이브러리
import math # 수학 라이브러리 ~ 근데 어째 위에 반올림 함수 부르는데 쓰인듯 한데 왜 따로 또 불럿지..?
import time # 시간 라이브러리


