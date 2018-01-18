"""
파이선 PyQt5 라이브러리 테스팅
저자 : 안광은 (yooer10ms@cu.ac.kr)
버전 : python 3.5.4, PyQt 5.9.0

GUI 라이브러리 제발 잘되라 ... ;ㅅ;
레퍼런스:
https://pythonspot.com/pyqt5/

"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget # 실행은 되는데 라이브러리를 못가져오네 ㅠㅠ....아 제발 ;;

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    
    sys.exit(app.exec_())