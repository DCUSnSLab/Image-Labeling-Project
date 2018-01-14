"""
파이선 tkinter 라이브러리 테스팅
저자 : 안광은 (yooer10ms@cu.ac.kr)

으으으으으.... 이거 쓰기 싫어....근데 잘되 ㅠㅠ
레퍼런스:
http://pythonstudy.xyz/python/article/120-Tkinter-%EC%86%8C%EA%B0%9C

"""
from tkinter import *

root = Tk()
 
lbl = Label(root, text="이름")
lbl.pack()
 
txt = Entry(root)
txt.pack()
 
btn = Button(root, text="OK")
btn.pack()
 
root.mainloop()