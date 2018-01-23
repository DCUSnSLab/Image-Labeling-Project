"""
파이선 opencv 비디오 플레이 테스트
저자 : 안광은 (yooer10ms@cu.ac.kr)
버전 : python 3.5.4, opencv 3.4.0

Visual Studio Code에서 실행 시 라이브러리 호출 문제로 Python:Terminal (integrated)로 실행하면 잘됨!

레퍼런스:

"""

import cv2

VIDEO = cv2.VideoCapture('../resources/videos/20170923_153612.mp4') # 파일 불러오기 ~, 스크립트 파일이 있는 것을 기준으로 불러왔음!!!

while(VIDEO.isOpened()):
    _, FRAME = VIDEO.read() # 프레임 이미지 읽기 
    cv2.imshow('test', FRAME) # 화면 창으로 보여주기
    if cv2.waitKey(1) & 0xFF == ord('q'): # q 를 누르면 프로그램 종료~!
        break
VIDEO.release() # 파일 락 해제
cv2.destroyAllWindows() # 화면 창 부숴버려어엌!


