import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette,QPixmap
from PyQt5.QtCore import Qt
class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color=yellow>这是一个文本标签</font>")  # 可以使用html文本
        label1.setAutoFillBackground(True) # 填充背景
        palette = QPalette()
        palette.setColor(QPalette.Window,Qt.blue)  #  调色板 背景色蓝色
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)  # 居中对齐

        label2.setText("<a href='#'>欢迎使用pyqt</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap("../images/python.png")) # 把标签变为图片

        label4.setOpenExternalLinks(True)  # 如果为True  用浏览器打开链接，如为False 调用槽函数
        label4.setText("<a href='https://www.baidu.com'>百度</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip("这是一个链接")

        label2.linkHovered.connect(self.linkHovered)  #信号绑定槽函数
        label4.linkActivated.connect(self.linkActivated)

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        self.setLayout(vbox)

        self.setWindowTitle('QLabel演示')


    def linkHovered(self):
        print('当鼠标滑过label2时调用')

    def linkActivated(self):
        print('当鼠标点击label4时调用')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())
