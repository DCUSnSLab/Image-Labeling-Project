"""
텐서플로 기반 SegNet 구현
저자 : 안광은 (yooer10ms@cu.ac.kr)
버전 : python 3.5.4, tensorflow-gpu 1.4.0

저자 제공 SegNet 예제 모델이 Caffe 용이라니.. 게다가 다른 소스는 전부 Tensorflow 1.0용이라니 ㅠㅠ
하 슈밤... 그냥 내가 짠다.... 써글 ㅠㅠ 울고싶네 ㅠㅠ...

레퍼런스:
https://github.com/tkuanlun350/Tensorflow-SegNet
https://github.com/alexgkendall/SegNet-Tutorial
https://github.com/mathildor/TF-SegNet
https://github.com/andreaazzini/segnet.tf
https://github.com/arahusky/Tensorflow-Segmentation


"""

# Tensorflow 함수
import tensorflow as tf # 텐서플로 라이브러리 불러오기 
from tensorlfow.python.framework import ops # 연산작업 라이브러리
from tensorflow.python.framework import dtypes # 데이터 타입 라이브러리
from tensorflow.python.ops import gen_nn_ops

# 파이선 내장 함수
from datetime import datetime
from PIL import Image
from math import ceil
import os, sys
import numpy as np
import math
import time


