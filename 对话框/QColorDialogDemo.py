'''
QColoDialog可以打开一个颜色选择的对话框，getColor()方法可以选择颜色
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

class QColorDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QColorDialog示例')
        self.resize(300,100)

        layout = QVBoxLayout()
        self.btn1 = QPushButton('设置字体颜色')
        self.btn1.clicked.connect(self.getColor)
        self.label = QLabel('Hello，这是一个测试')

        self.btn2 = QPushButton('设置字体背景颜色')
        self.btn2.clicked.connect(self.getBGColor)


        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def getColor(self):
        color = QColorDialog.getColor()  # 获得选择的颜色
        p = QPalette()  # 初始化一个调色板
        # print(color.name()) # 选择的颜色的值（16进制）
        p.setColor(QPalette.WindowText,color) # 设置调色板，作用于窗口中的文本，颜色为color
        self.label.setPalette(p)  # 把字体颜色修改为选择的颜色

    def getBGColor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.Window,color) # 设置调色板，作用于窗口种的控件背景
        self.label.setAutoFillBackground(True)  # 打开标签背景色设置
        self.label.setPalette(p)


if __name__ =="__main__":
    app = QApplication(sys.argv)
    main = QColorDialogDemo()
    main.show()
    sys.exit(app.exec_())