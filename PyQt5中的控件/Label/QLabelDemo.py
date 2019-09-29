'''
QLabel的作用：占位符、显示文本、显示图片、放置gif动画、超链接、提示标记
Qlabel常用方法
setAlignment()	按固定值方式对齐文本
                    Qt.AlignLeft：水平方向靠左对齐
                    Qt.AlignRight:水平方向靠右对齐
                    Qt.AlignCenter：水平方向居中对齐
                    Qt.AlignJustify：水平方向调整间距两端对齐
                    Qt.AlignTop：垂直方向靠上对齐
                    Qt.AlignBottom：垂直方向靠下对齐
                    Qt.AlignVCenter：垂直方向居中对齐
serIndent()	设置文本缩进值
setPixmap()	设置QLabel为一个Pixmap图片
text()	获得Qlabel的文本内容
setText()	设置Qlabel的文本内容
selectedText()	返回所选择的字符
setBuddy()	设置QLabel的助记符及buddy（伙伴），及使用Qlabel设置快捷键，
            会在快捷键后将焦点设置到其buddy上，这里用到了Qlabel的交互控件功能 ，
            此外，buddy可以是任何一个widget控件，使用setBuddy(QWidget*)设置，
            其Qlabel必须是文本内容，并且使用“&”符号设置了助记符
setWordWrap()	设置是否允许换行

Qlabel类中的常用信号
linkActiveted	当单击标签中的超链接，希望在新窗口打开这个超链接时，setOpenExternalLinks特性必须设置为True，即setOpenExternalLinks（True）
linkHovered	当鼠标指针滑过标签中嵌入的超链接时，需要用槽函数与这个信号进行绑定

'''

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
