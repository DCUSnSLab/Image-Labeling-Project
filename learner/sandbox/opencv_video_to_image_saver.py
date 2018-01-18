"""
파이선 opencv 비디오 프레임 저장 
저자 : 안광은 (yooer10ms@cu.ac.kr)
버전 : python 3.5.4, opencv 3.4.0

Visual Studio Code에서 실행 시 라이브러리 호출 문제로 Python:Terminal (integrated)로 실행하면 잘됨!

레퍼런스:
https://stackoverflow.com/questions/20425724/pythonopencv-cv2-imwrite


"""

import cv2

VIDEO_FILE_PATH = '../resources/videos/20170923_153612.mp4' # 비디오 파일 경로
IMAGE_SAVE_PATH = '../resources/images/20170923_153612/' # 이미지 저장 폴더 경로

VIDEO = cv2.VideoCapture('../resources/videos/20170923_153612.mp4')

FRAME_COUNTER = 0
while(VIDEO.isOpened()):
    _, FRAME = VIDEO.read()
    cv2.imshow('test', FRAME)
    IMAGE_SAVE_FILE_NAME = IMAGE_SAVE_PATH+'20170923_153612_'+str(FRAME_COUNTER)+'.png'
    print(IMAGE_SAVE_FILE_NAME)
    cv2.imwrite(IMAGE_SAVE_FILE_NAME,FRAME)
    FRAME_COUNTER += 1
    if cv2.waitKey(1) & 0xFF == ord('q'): # q 를 누르면 프로그램 종료~!
        break
VIDEO.release()
cv2.destroyAllWindows()

