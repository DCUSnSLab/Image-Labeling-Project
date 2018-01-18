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
while(VIDEO.isOpened()): # 비디오 플레이, 비디오 끝 만날 시 플레이 종료
    _, FRAME = VIDEO.read() # 비디오로부터 프레임 읽기
    cv2.imshow('test', FRAME) # 화면에 프레임 보여주기
    IMAGE_SAVE_FILE_NAME = IMAGE_SAVE_PATH+'20170923_153612_'+str(FRAME_COUNTER)+'.png' # 저장 이름, 경로에서 폴더가 없는 경우 파일이 저장되지 않음!
    print(IMAGE_SAVE_FILE_NAME) # 저장 경로 및 파일 저장 이름 콘솔에 출력
    cv2.imwrite(IMAGE_SAVE_FILE_NAME,FRAME) # 프레임 이미지로 저장, 기본이 png포맷인것 같음
    FRAME_COUNTER += 1 # 이미지 인덱스 번호 증가
    if cv2.waitKey(1) & 0xFF == ord('q'): # q 를 누르면 프로그램 종료~!
        break
VIDEO.release() # 비디오 종료
cv2.destroyAllWindows() # 화면 종료

