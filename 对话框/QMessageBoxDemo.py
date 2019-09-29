'''
消息对话框：QMessageBox
QmessageBox是一种通用的弹出式对话框，用于显示消息，允许用户通过单击不同的标准按钮对消息进行反馈
QMessageBox类提供了许多常用的弹出式对话框
消息对话框，用来告诉用户关于提示信息
QMessageBox.information(self,'标题','消息对话框正文',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)

提问对话框，用来告诉用户关于提问消息
QMessageBox.question(self,'标题','提问框消息正文',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)

警告对话框，用来告诉用户关于不寻常的错误消息
QMessageBox.warning(self,'标题','警告框消息正文',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)

严重错误对话框，用来告诉用户关于严重的错误消息
QMessageBox.critical(self,'标题','严重错误对话框消息正文',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)

关于对话框
QMessageBox.about(self,'标题','关于对话框')

QMessageBox类中常用方法
information(QWdiget parent,title,text,buttons,defaultButton)	弹出消息对话框，各参数解释如下
                                                            parent：指定的父窗口控件
                                                            title：对话框标题
                                                            text：对话框文本
                                                            buttons：多个标准按钮，默认为ok按钮
                                                            defaultButton：默认选中的标准按钮，默认选中第一个标准按钮
question（QWidget parent,title,text,buttons,defaultButton）	弹出问答对话框（各参数解释如上）
warning（QWidget parent,title,text,buttons,defaultButton）	弹出警告对话框（各参数解释如上）
critical（QWidget parent,title,text,buttons,defaultButton）	弹出严重错误对话框（各参数解释如上）
about（QWidget parent,title,text）	弹出关于对话框（各参数解释如上）
setTitle()	设置标题
setText()	设置正文消息
setIcon()	设置弹出对话框的图片

QMessageBox的标准按钮类型如下
QMessage.Ok	同意操作
QMessage.Cancel	取消操作
QMessage.Yes	同意操作
QMessage.No	取消操作
QMessage.Abort	终止操作
QMessage.Retry	重试操作
QMessage.Ignore	忽略操作

'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

class QMessageBoxDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('消息对话框示例')
        self.resize(300,600)

        layout = QVBoxLayout()

        btn1 = QPushButton('关于对话框')
        btn1.clicked.connect(self.showDialog)

        btn2 = QPushButton('消息对话框')
        btn2.clicked.connect(self.showDialog)

        btn3 = QPushButton('警告对话框')
        btn3.clicked.connect(self.showDialog)

        btn4 = QPushButton('错误对话框')
        btn4.clicked.connect(self.showDialog)

        btn5 = QPushButton('提问对话框')
        btn5.clicked.connect(self.showDialog)

        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        layout.addWidget(btn5)

        self.setLayout(layout)

    def showDialog(self):
        text = self.sender().text()
        if text == '关于对话框':
            QMessageBox.about(self,'关于','这是一个关于对话框')
        elif text == '消息对话框':
            reply = QMessageBox.information(self,'消息','这是一个消息对话框',QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                print('Accept')
            else:
                print('Reject')
        elif text == '警告对话框':
            reply = QMessageBox.warning(self,'警告','这是一个警告对话框',QMessageBox.Retry | QMessageBox.Ignore,QMessageBox.Retry)
            if reply == QMessageBox.Retry:
                print('Retry')
            else:
                print('Ignore')
        elif text == '错误对话框':
            QMessageBox.critical(self,'错误','这是一个错误对话框',QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        elif text == '提问对话框':
            reply = QMessageBox.question(self,'提问','这是一个提问对话框',QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                print('Accept')
            else:
                print('Reject')

if __name__ =="__main__":
    app = QApplication(sys.argv)
    main = QMessageBoxDemo()
    main.show()
    sys.exit(app.exec_())