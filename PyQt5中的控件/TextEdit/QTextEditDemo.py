'''
QTextEdit类是一个多行文本框控件，可以显示多行文本内容，当文本内容超出控件显示范围时，
可以显示水平个垂直滚动条，Qtextedit不仅可以用来显示文本还可以用来显示HTML文档

QTextEdit类中常用的方法
setPlainText()	设置多行文本框的内容
toPlainText()	返回多行文本框的文本内容
setHtml()	设置多行文本框的文本内容为HTML文档，HTML文档是描述网页的
toHtml()	返回多行文本框的HTML内容
clear()	清除多行文本框的内容

'''

from PyQt5.QtWidgets import *
import sys

class TextEditDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('TextEdit示例')

        self.resize(300,350)
        # 初始化水平布局
        layout = QVBoxLayout()

        # 初始化控件
        self.textEdit = QTextEdit()
        buttonText = QPushButton('显示文本')
        buttonHtml = QPushButton('显示HTML')
        buttonToText = QPushButton('获取文本')
        buttonToHtml = QPushButton('获取HTML')

        #绑定按钮的信号与槽函数
        buttonText.clicked.connect(self.onClick_buttonText)
        buttonToText.clicked.connect(self.onClick_buttonToText)
        buttonHtml.clicked.connect(self.onClick_buttonHtml)
        buttonToHtml.clicked.connect(self.onClick_buttonToHtml)

        #往布局中添加控件
        layout.addWidget(self.textEdit)
        layout.addWidget(buttonText)
        layout.addWidget(buttonToText)
        layout.addWidget(buttonHtml)
        layout.addWidget(buttonToHtml)

        #设置窗口布局
        self.setLayout(layout)

    def onClick_buttonText(self):
        self.textEdit.setPlainText('Hello World ! 欢迎使用PyQt5') # setPlainText() 设置TextEdit的文本

    def onClick_buttonHtml(self):
        self.textEdit.setHtml("<font color='red' size='5'>Hello World ! 欢迎使用PyQt5</font>")  #setHtml() 设置TextEdit的Html

    def onClick_buttonToText(self):
        print(self.textEdit.toPlainText()) # toPlainText() 获取TextEdit的文本

    def onClick_buttonToHtml(self):
        print(self.textEdit.toHtml()) # toHtml 获取TextEdit的Html

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = TextEditDemo()
    main.show()
    sys.exit(app.exec_())