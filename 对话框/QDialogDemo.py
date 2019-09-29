'''
对话框：QDialog
为了更好的实现人机交互，比如window和linux等系统均会提供一系列的标准对话框来完成特定场景下的功能，
比如选择字号大小。字体颜色等，在PyQt5中定义了一系列的标准对话框类，让使用者能够方便快捷地通过各个
类完成字号大小，字体颜色以及文件的选择等.

QDialog类的子类主要包括：
消息对话框：QMessageBox
颜色选择对话框： QColorDialog
文件对话框： QFileDialog
字体选择对话框: QFontDialog
输入对话框:QInputDialog

QDialog类中的常用方法
setWindowTitle()	设置对话框标题
setWindowModality()	设置窗口模态，取值如下
                    Qt.NonModal：非模态，可以和程序的其他窗口进行交互
                    Qt.WindowModal:窗口模态，程序在未处理玩当前对话框时，将阻止和对话框的父窗口进行交互
                    Qt.ApplicationModal：应用程序模态，阻止和任何其他窗口进行交互

'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

class QDialogDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QDialog示例')
        self.resize(300,200)

        btn = QPushButton('打开一个窗口',self)
        btn.move(50,50)
        btn.clicked.connect(self.openDialog)

    def openDialog(self):
        dialog = QDialog()  #创建对话框
        dialog.resize(300,100) # 设置对话框大小
        btn = QPushButton('确定',dialog)  # 创建一个按钮在对话框
        btn.move(50,50)  # 移动按钮
        btn.clicked.connect(dialog.close)  # 点击按钮，关闭对话框  绑定了对话框的关闭方法
        dialog.setWindowTitle('对话框')  # 设置对话框标题
        dialog.setWindowModality(Qt.ApplicationModal)  # 设置对话框模式
        dialog.exec_()  # 显示对话框 让对话框进入循环

if __name__ =="__main__":
    app = QApplication(sys.argv)
    main = QDialogDemo()
    main.show()
    sys.exit(app.exec_())