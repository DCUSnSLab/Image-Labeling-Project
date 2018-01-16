"""
텐서플로 테스팅 프로그램
저자 : 안광은 (yooer10ms@cu.ac.kr)
버전 : 3.5.4

별거 없어요... 텐서플로 되는지 그냥 만들어본겁니다 ㅇㅅㅇ..

"""

import tensorflow as tf

HELLO = tf.constant("안녕하세요, 전 한국남자입니다 :)\n")

# 텐서플로 동작은 되는데 한국어는 바이너리에서 바로 깨지는군요... 절레절레...
with tf.Session() as sess:
    print(sess.run(HELLO)) 랩장바보 엘ㄹ레레ㅔ레레ㅔㄹ7
