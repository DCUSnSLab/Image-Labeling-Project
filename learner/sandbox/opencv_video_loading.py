"""
파이선 opencv 비디오 플레이 테스트
저자 : 안광은 (yooer10ms@cu.ac.kr)
버전 : 3.5.4

Visual Studio Code에서 실행 시 라이브러리 호출 문제로 Python:Terminal (integrated)로 실행하면 잘됨!

레퍼런스:

"""

import cv2

video = cv2.VideoCapture('../resources/videos/20170923_153612.mp4')

while(video.isOpened()):
    _, frame = video.read()
    cv2.imshow('test', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): # q 를 누르면 프로그램 종료~!
        break
video.release()
cv2.destroyAllWindows()


