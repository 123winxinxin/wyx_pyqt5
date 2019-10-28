'''
在QMainWindow对象的标题栏下方，水平的QMenuBar被保留显示QMenu对象
QMenuBar类提供了一个可以包含一个或多个QAction对象或 级联的QMenu对象，要创建一个弹出菜单，Pyqt提供了createPopupMenu（）函数，menuBar（）函数用于返回主窗口的QMenuBar对象：addMenu（）函数可以将菜单添加到菜单栏中，通过addAction()函数可以在菜单中进行添加操作

menuBar()	返回主窗口的QMenuBar对象
addMenu()	在菜单栏中添加一个新的QMenu对象
addAction()	向QMenu小控件中添加一个操作按钮，其中包含文本或图标
setEnabled()	将操作按钮设置为启用/禁用
addSeperator()	在菜单中添加一条分割线
clear()	删除菜单栏的内容
setShortcut()	将快捷键关联到操作按钮
setText()	设置菜单项的文本
setTitle()	设置QMenu小控件的标题
text()	返回与QACtion对象关联的文本
title()	返回QMenu小控件的标题
单击任何QAction按钮时，QMenu对象都会发射triggered信号
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        bar = self.menuBar()  #实例化主窗口的QMenuBar对象
        file = bar.addMenu('File')  #向菜单栏中添加新的QMenu对象，父菜单
        file.addAction('New')  #向QMenu小控件中添加按钮，子菜单

        # #定义响应小控件按钮，并设置快捷键关联到操作按钮，添加到父菜单下
        save = QAction('Save',self)
        save.setShortcut('Ctrl + S')
        file.addAction(save)
        # save.triggered.connect(self.save)  # 单击save 触发槽函数

        # 创建新的子菜单项，并添加孙菜单
        edit = file.addMenu('Edit')
        edit.addAction('Copy')
        edit.addAction('Paste')

        quit = QAction('Quit',self)
        file.addAction(quit)
        file.triggered[QAction].connect(self.process)  # 菜单发射triggered信号，将信号连接到槽函数processtrigger（）该函数接受信号的QAction对象

    def save(self,q):
        if q:
            print(self.sender().text())

    def process(self,q):
        print(q.text())


if __name__ =="__main__":
    app = QApplication(sys.argv)
    main = MyMenu()
    main.show()
    sys.exit(app.exec_())