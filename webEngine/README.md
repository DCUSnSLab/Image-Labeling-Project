# 이미지 라벨링 UI

## 관리자

한정 (gkswjd9969@cu.ac.kr)

## 개요



## 개발 환경
>
> **운영체제**
>- Windows 10 Home x64
>
> **개발도구**
>- Visual Studio Code 1.19.2
>
> **라이브러리**
>- php 7.
>
> **하드웨어**
>- 노트북 : 삼성 노트북 9 Always 
>- CPU : Intel i5-7200U
>- M/M : 8GB
>---
> **운영체제(서버)**
>- Linux(Ubuntu-Server 16.04.3) x86_64
>
> **라이브러리(서버)**
>- apache 2.4.18
>- mySQL 14.14
>- php 7.0.22
>
> **하드웨어(서버)**
>- 노트북 : MSI CQ ~~
>- CPU : Intel i5-4210M
>- GPU : NVIDIA GeForce940Mp
>- M/M : 4GB

## 프로그램 구성
> **서버와의 연결**
>- Visual Studio Code
>   - [ ] ftp-sync 이용
>       | 명령어 | 기능 |
>       | --- | --- |
>       | remotePath | 업로드하려는 경로 설정 ( 기본 경로 "root" ) |
>       | host | FTP서버 hostname |
>       | username | FTP 접속 ID |
>       | password | FTP 접속 PW |
>       | port | FTP서버 연결 포트 설정 ( 기본 포트 "21" ) |
>       | protocol | FTP프로토콜 설정 ( ftp 또는 sft p) |
>       | uploadOnSave | 파일을 저장할 때마다 자동 업로드 ( 기본 값 "false " ) |
>       | passive | FTP 수동 모드 사용 여부 ( 기본 값 " false " ) |
>       | debug | 디버그 정보 표시 여부 ( 기본 값 " false " ) |
>       | privateKeyPath | SFTP 개인 키 경로 지정 ( 기본 값 " null " ) |
>       | passphrase | SFTP 개인 키와 함께 사용될 암호 지정 (기본 값 " null ") |
>       | ignore | 무시할 경로 설정 ( 기본 값 "./git, ./vscode, ./DS_Store ") |
>       | "generatedFiles": { </br> &emsp;"uploadOnSave": true, </br> &emsp;"path": "", [e.g.] "/build", </br> &emsp;"extensionsToInclude": [] e.g. [".js", ".styl"] </br>} | 이건 아직 잘 모르겠....따아ㅠ
>
>   - [ ] ftp-simple 이용
>       | 명령어 | 기능 |
>       | --- | --- |
>       | name | 설정 이름 |
>       | host | FTP 서버 주소 |
>       | port | FTP 서버 포트 |
>       | type | FTP 타입 ( ftp 또는 sftp ) |
>       | username | FTP 접속 ID |
>       | password | FTP 접속 PW |
>       | path | 연결할 경로 |
>       | autosave | 자동 저장 여부 ( true 또는 false ) |
>       | confirm | 확인 창 ( true 또는 false ) |
>
>- [x] 연구실 Git ( Yona ) 이용
>    - clone 주소 : http://gkswjd9969@203.250.34.153:9000/gkswjd9969/UI_test
>    - UI_Test ( branch : develop )
>       - Main.php
>---

### 디렉토리 구성
```
    ./Main.php                       # UI적용 php파일
    ./Other_Site_Features.md         # 다른 웹 사이트게임들 특징 정리
    ./README.md                      # 개발 가이드
```