# 학습 모방기

## 관리자

안광은 (yooer10ms@cu.ac.kr)

## 개요

 Deep-Q Learning 및 Convolutional Neural Network을 사용한 사용자 라벨링 모방학습 시스템.

## 개발 환경

> **운영체제**
> Windows 10 Pro x86_64(64bit)
> **라이브러리**
> Tensorflow 1.4
> Opencv 3.4 for Python 3.5.x
> PyQt5 5.9
> Tkinter 8.6
> **하드웨어**
> CPU : Intel i7-7700
> GPU : NVidia GTX 1080Ti(11GB GDDR)
> M/M : 16GB

### 환경 구성

라이브러리와 언어 설치하는 방법입니다~ 없으면 실행 안되요! (자꾸 설치하던 방법 까먹어서 적어놔요 ;ㅂ;)

* **Python 3.5.4**

최신버전은 3.6.x이지만 Tensorflow가 아직 3.6버전으로 준비가 안되서 이걸로 설치해줍니다. 운영체제 버전 확인하고 설치해주세요~

[Python 다운로드 링크](https://www.python.org/downloads/release/python-354/)

* **pip**

다른 라이브러리를 편하게 설치하기 위해서 pip를 설치해줍니다

[pip 설치 방법 설명](https://pip.pypa.io/en/stable/installing/)

* **Tensorflow**

Nvidia GPU를 가지고 있는 경우 세심하게 읽어보면서 설치해주세요~!
(개인적으로 정말 삽질 많이 했다는...)

[Tensorflow 설치 방법 설명](https://www.tensorflow.org/install/install_windows)

* **OpenCV 3.4.0 contrib**

OpenCV 공식 사이트는 2.7 버전만 업데이트 해주어서... 빌드하기는 귀찮으니 CPU버전을 다운받아 줍니닷.! 사용하는 운영체제 버전 확인하고 설치해주세요~ Contrib 버전으로 설치해줍니다~!

[Python 3.5.4용 OpenCV 3.4.0 설치 스크립트](https://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv)

```bash
pip install <다운로드받은 스크립트>.whl
```

* **numpy**

opencv 및 tensorflow는 수식 표현 라이브러리인 numpy가 필수입니다아~ pip를 이용해 설치해주세요~

```bash
pip install numpy
```

## 프로그램 구성

### 디렉토리 구성

```None
./sandbox                                           # 테스트 코드 폴더
    ./resources                                     # 테스트용 파일들~!
        ./videos                                    # 비디오 파일들
            sample_video.mp4                        # 연습용 비디오 파일
        ./images                                    # 이미지 파일들
    opencv_image_loading.py                         # 이미지를 화면에 보여주기
    opencv_video_loading_using_threaing.py          # 멀티프로세스 사용 비디오 재생하기
    opencv_video_loading.py                         # 비디오 재생하기
    opencv_video_to_image_saver_using_threading.py  # 멀티프로세스 사용 비디오 재생 및 저장하기
    opencv_video_to_image_saver.py                  # 비디오 이미지로 저장하기
    pyqt5_testing.py                                # PyQt 5.9 라이브러리 GUI 테스트
    python_sandbox.py                               # 파이선 문법 자꾸 잊어먹어서;ㅂ;
    tensorflow_example.py                           # 텐서플로 예제 및 테스트 코드
    tkinter_testing.py                              # Tkinter 8.6 라이브러리 GUI 테스트
```