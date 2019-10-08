'''
绘图API可以绘制
1、文本
2、各种图形（直线、点、椭圆、弧形、扇形、多边形）
3、图像

使用QPainter 类
过程：
1、实例化一个QPainter
2、painter.begin()
3、painter.drawText(...)
4、painter.end()
必须在paintEvent事件方法中绘制各种元素,paintEvent事件在创建窗口或窗口尺寸变化时调用。当窗口尺寸变化时，会重新绘制窗口

'''

import sys
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QPainter,QColor,QFont
from PyQt5.QtCore import Qt


class DrawText(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('绘制文本演示')
        self.resize(500,400)
        self.text = 'Hello,这是一个例子'

    def paintEvent(self, event):  # 绘制都要在这个事件中
        painter = QPainter()  # 实例化一个绘制的类
        painter.begin(self)  # 开始在目标设备上绘制，需要一个参数，告诉在哪里绘制
        print('开始绘制')
        painter.setPen(QColor(155,55,120))  # 设置画笔的颜色
        painter.setFont(QFont('Arial',20)) # 设置字体

        painter.drawText(event.rect(),Qt.AlignCenter,self.text)  # 显示给定坐标处的文字 event.rect()是指这个窗口，还可以设置对齐方式和文本

        painter.end()


if __name__ =="__main__":
    app = QApplication(sys.argv)
    main = DrawText()
    main.show()
    sys.exit(app.exec_())