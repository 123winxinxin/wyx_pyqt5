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