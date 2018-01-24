"""
파이선 opencv 이미지 압축 저장 테스트 코드
저자 : 안광은 (yooer10ms@cu.ac.kr)
버전 : python 3.5.4, opencv 3.4.0

레퍼런스:
http://answers.opencv.org/question/115/opencv-python-save-jpg-specifying-quality-gives-systemerror/
https://docs.opencv.org/master/d4/da8/group__imgcodecs.html#ga292d81be8d76901bff7988d18d2b42ac

"""

import cv2 # 오픈 쒸브잏 2!
import time # 시간 라이브러 호출
import os # 시스템 라이브러리 호출

#IMAGE_PATH_PNG = u'./Image-Labeling-project/learner/resources/images/sample_image.png'
IMAGE_PATH_PNG = u'C:/Users/yooer/Downloads/20170923_153612/example_25.png'
IMAGE_SAVE_PATH = u'C:/Users/yooer/Downloads/testing/'

# 사용된 기본 이미지 정보

image = cv2.imread(IMAGE_PATH_PNG) # 상대경로 먹힘 !!!. 상대경로따윈 더이상 믿지 않는다...! 원

# 했는데 변환에 시간이 얼마나 소요되는지 몰라서 대량 이미지 변환 시 걸리는 소요시간 예측을 위해 대략적으로 시도해보기 ㅇ!
# JPEG 압축
for x in [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
    before_start = time.time()
    cv2.imwrite(IMAGE_SAVE_PATH + 'example_25_'+ str(x)+ '.jpg',image, [int(cv2.IMWRITE_JPEG_QUALITY),x])
    print("JPEG 옵션 " + str(x) + "의 처리속도" + str(time.time()-before_start))
"""
실험에 사용된 이미지 정보
    example_25.png, 1920x1080, png(압축 알수 없음), 2.7MB

실험 결과
    공통 저장 옵션 : JPEG(YUV), 1920x1080
    옵션 0:  처리속도 0.03609418869018555, 41.2KB, 
    옵션 10: 처리속도 0.03709769248962402, 
    옵션 20: 처리속도 0.03910684585571289
    옵션 30: 처리속도 0.0381011962890625
    옵션 40: 처리속도 0.0411076545715332
    옵션 50: 처리속도 0.042112112045288086
    옵션 60: 처리속도 0.04311490058898926
    옵션 70: 처리속도 0.045119524002075195
    옵션 80: 처리속도 0.04812812805175781
    옵션 90: 처리속도 0.052138328552246094
    옵션 100: 처리속도 0.08522629737854004
    # example_25_100.jpg, 1920x1080, jpeg(), 1.2MB
"""

# PNG 압축
for x in range(0, 10):
    before_start = time.time()
    cv2.imwrite(IMAGE_SAVE_PATH + 'example_25_'+ str(x)+ '.png',image, [int(cv2.IMWRITE_PNG_COMPRESSION),x])
    print("PNG 옵션 " + str(x) + "의 처리속도" + str(time.time()-before_start))

"""
실험 결과
    공통 저장 옵션 : PNG, 1920x1080
    * 옵션 <번호>: 처리속도, 파일 크기
    옵션 0: 0.0691838264465332, 5.9MB
    옵션 1: 0.1594545841217041, 2.3MB
    옵션 2: 0.176469087600708. 2.3MB
    옵션 3: 0.268160343170166. 2.2MB
    옵션 4: 0.21557402610778809, 2.2MB
    옵션 5: 0.34892797470092773. 2.2MB
    옵션 6: 0.6005957126617432, 2.1MB
    옵션 7: 0.8352465629577637, 2.1MB
    옵션 8: 2.0955724716186523, 2.0MB
    옵션 9: 3.346895456314087, 2.0MB
"""