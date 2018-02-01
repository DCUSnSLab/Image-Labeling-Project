"""
파이선 커스텀 예외 처리 클래스
저자 : 안광은 (yooer10ms@cu.ac.kr)
버전 : python 3.5.4, opencv 3.4.0

프로그램 구동할때 사용할 커스텀 Exception 클래스

"""

class VariableInitError(Exception):
    def __init__(self, message = null):
        print ('변수 초기화 에러', message)
    pass