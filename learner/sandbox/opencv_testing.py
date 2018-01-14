"""
파이선 opencv 라이브러리 테스팅
저자 : 안광은 (yooer10ms@cu.ac.kr)
버전 : 3.5.4

Visual Studio Code에서 실행 시 라이브러리 호출 문제로 Python:Terminal (integrated)로 실행하면 잘됨!

레퍼런스:

"""

# 되긴 되는데 왜 코드 완성이 자동으로 안되는지 모르겟다.... 하.....진심 이거 
# 코딩할때 완전 불편해지는 심각한 문제인데.... 아오 ㅠㅠㅠ
import cv2

image = cv2.imread('../../mdRes/code_template.png') # 상대경로 먹힘 !!! 

cv2.imshow('test', image)
cv2.waitKey(0)
