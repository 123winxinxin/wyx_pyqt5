'''
MainWindow对象在底部保留有一个水平条，作为状态栏（QstatusBar），用于显示永久或临时的状态信息
addWidget()	在状态栏中添加给定的窗口小控件对象
addPermanentWidget()	在状态栏中永久添加给定的窗口小控件对象
showMessage()	在状态栏显示一条临时信息，指定时间间隔
clearMessage()	删除正在显示的临时信息
removeWidget()	从状态栏中移除指定的小控件

'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class StatusDemo(QMainWindow):
    def __init__(self,parent=None):
        super(StatusDemo, self).__init__(parent)

        #实例化菜单栏
        bar=self.menuBar()
        #添加父菜单
        file=bar.addMenu('File')
        #添加子菜单
        file.addAction('show')
        #当菜单对象被点击时，触发绑定的自定义的槽函数
        file.triggered[QAction].connect(self.processTrigger)

        #设置当行文本输入框为中间控件
        self.setCentralWidget(QTextEdit())

        #实例化状态栏
        self.statusBar=QStatusBar()

        self.setWindowTitle('QStatusBar例子')

        #设置状态栏，类似布局设置
        self.setStatusBar(self.statusBar)

    def processTrigger(self,q):

        if (q.text()=='show'):
            #设置状态栏的显示文本以及显示时间
            self.statusBar.showMessage(q.text()+'菜单选项被点击了',5000)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=StatusDemo()
    demo.show()
    sys.exit(app.exec_())
