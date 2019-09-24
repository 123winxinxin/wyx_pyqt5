from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class QPushButtonDemo(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QPushButton示例')
        self.resize(300,500)

        layout = QVBoxLayout()
        # 正常的按钮
        self.button1 = QPushButton()
        self.button1.setText('按钮1') # setText() 设置按钮文本
        self.button1.setCheckable(True) # 设置按钮有开关状态，按下不会自动起来
        # self.button1.toggle() # 开启按钮
        # self.button1.clicked.connect(self.whichButton)
        self.button1.clicked.connect(lambda:self.whichButton(self.button1)) # 把lambda表达式当作槽，触发后直接调用后面的方法，优点是可以传参
        self.button1.clicked.connect(self.buttonState)  #正常的绑定槽函数

        layout.addWidget(self.button1)
        # 在文本前加图标
        self.button2 = QPushButton('图片按钮')
        self.button2.setIcon(QIcon(QPixmap('../images/python.png'))) # 设置按钮图标
        self.button2.clicked.connect(lambda:self.whichButton(self.button2))

        layout.addWidget(self.button2)

        # 设置不可用按钮
        self.button3 = QPushButton('不可用的按钮')
        self.button3.setEnabled(False)
        layout.addWidget(self.button3)

        self.button4 = QPushButton('&MyButton') # 设置热键
        self.button4.setDefault(True)  # 设置默认按钮  窗口打开后不选择按钮 按回车时会点击默认按钮
        self.button4.clicked.connect(lambda:self.whichButton(self.button4))
        layout.addWidget(self.button4)

        self.setLayout(layout)

    # def whichButton(self):  # 多个信号共用一个槽函数
    #     sender = self.sender()  # 发出信号的对象
    #     print(sender.text()+'被单击')

    def whichButton(self,btn): # 多个信号共用一个槽函数
        print(btn.text()+'被单击')

    def buttonState(self):
        if self.button1.isChecked():  # 按钮按下时为真
            print('按钮1已被选中')
        else:
            print('按钮1未被选中')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QPushButtonDemo()
    main.show()
    sys.exit(app.exec_())