"""
파이선 언어 샌드박스 코드
저자 : 안광은 (yooer10ms@cu.ac.kr)
버전 : python 3.5.4

자꾸 파이선 언어 잊어머거서 결국 기억하기 용도로 만들어야겠....;ㅂ;

"""

# 문자열(string) 합치기(concatenation) 테스트
# + 사용해서 합쳐보기
str_1 = 'testing'
str_2 = 'a concatenation'
print(str_1 + str_2) # 진짜 잘됨 ㅇㅅㅇ
# 중간에 고정 문자 끼워보기
print(str_1 + ' ' + str_2) # 제대로 잘됨 ㅇㄴㅇ~

# 반복문 사용하기~
for x in range(0, 5): # foreach 문 숫자 올라가는거 테스트해보기
    print(x)

# 조건문 해보기 
if 3 is 3:
    print('3은 3이죠 ...!')

# 파이선 초 단위 처리 시간 계산
## 레퍼런스: https://stackoverflow.com/questions/3638532/find-time-difference-in-seconds-as-an-integer-with-python

import time # 시간 라이브러리 호출
now = time.time() # 현재시간 저장
# 계산할 작업 내용~!
later = time.time() #처리 후 시간 저장
difference = int(later - now) # 시간차이 계산 
print(difference) # 시간 차이 출력

# 파이선 파일 사이즈 얻기 
import os # 시스템 라이브러리 호출
statinfo = os.stat('./Image-Labeling-project/learner/resources/images/sample_image.png') # 파일 경로 입력
print(statinfo)#  파일 정보 출력
print(statinfo.st_size) # 파일 사이즈 출력!

# 파이선 현재 파일 경로 얻기
import os # 시스템 라이브러리 호출
print(os.getcwd()) # 현재 파일 경로 출력!