# 이미지 크롤링

## 관리자

이민영 (dud1547@cu.ac.kr)

## 개요
### 키워드를 이용하여 구글의 이미지를 자동으로 다운

## 개발 환경

> **운영체제**
> Window10Home

> **라이브러리**
>  [google-images-download](https://github.com/hardikvasa/google-images-download)

> **하드웨어**
> LG그램

## 사용법
1. 소스코드 clone (cmd 창에서)
~~~ 
1. 클론할 폴더로 이동
2. git clone http://github.com/hardikvasa/google-images-download.git
3. cd google-images-download
4. python setup.py install
~~~
2. 소스코드가 클론된 폴더 내에서 cmd 창을 통해 명령어 입력(아래는 기본으로 100장 다운 받는 명령어, 추가적인 Arguments 값은 확인해서 사용하시면 됩니다!)
~~~
googleimagesdownload -k "포트홀"
~~~
3. 소스코드를 클론한 폴더 내에 downloads 안에 키워드 이름으로 폴더가 생성되고 그 안에 이미지가 다운로드됨!