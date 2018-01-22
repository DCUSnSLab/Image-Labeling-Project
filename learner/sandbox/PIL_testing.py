"""
파이선 PIL 라이브러리 테스팅
저자 : 안광은 (yooer10ms@cu.ac.kr)
버전 : python 3.5.4, PyQt 5.9.0

PIL 라이브러리 테스팅! 

PIL을 사용하기 위해서 Pillow 패키지를 설치해야됨~
pip install Pillow

레퍼런스:
http://pythonstudy.xyz/python/article/406-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%B2%98%EB%A6%AC
http://effbot.org/imagingbook/introduction.htm


"""

from PIL import Image

# 데스크탑용
# TODO: 와 진짜 상대경로 안먹히는 이유를 1도 모르겠다 ;ㅁ;....... 제발 ㅠㅠ
IMAGE_PATH_IN_PNG = u'C:/Users/yooer/Documents/GitHub/Image-Labeling-project/learner/resources/images/sample_image.png'
IMAGE_PATH_IN_JPEG = u'C:/Users/yooer/Documents/GitHub/Image-Labeling-project/learner/resources/images/sample_image.jpg'

# 이미지 불러오기
IM_PNG = Image.open(IMAGE_PATH_IN_PNG)
IM_JPEG = Image.open(IMAGE_PATH_IN_JPEG)

# 이미지 보여주기!, 이거 운영체제에 설치된 프로그램으로 보여주네 ;;; 좀 당황했다 ㅋㅋㅋㅋ
IM_PNG.show()
IM_JPEG.show()

