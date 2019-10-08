'''
这一次我们将用QPen这个类来绘制不同的线
第一步，实例化一个QPen对象
pen = QPen(Qt.red,3,SolidLine)  第一个参数是画笔的颜色；第二个参数是画笔的粗细；第三个是画笔类型，默认是实线
第二步，把画笔应用到绘制的对象中
painter.setPen(pen)
第三步，绘制线
drawLine(int x1,int y1,int x2,int y2)	绘制一条指定了端点坐标的线，绘制从（x1,y1）到（x2,y2）的直线并且设置当前地画笔位置为（x2,y2）

后面需要修改画笔类型可以用
pen.setStyle(Qt.DotLine)
painter.setPen(pen)
这样来设置画笔类型
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class DrawMultiLine(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('绘制不同的直线')
        self.resize(500,600)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        pen = QPen(Qt.green,2,Qt.SolidLine)  # 实例化一个画笔，并设置画笔颜色、粗细、线的类型
        painter.setPen(pen)  # 把画笔应用到绘制中
        painter.drawLine(50,40,400,40)  # 画一条线段  4个坐标是线段起始点和最终点坐标

        pen.setStyle(Qt.DashLine) # 有一些像素分割的线  宽的虚线
        painter.setPen(pen)  # 改变画笔后，需要重新应用到绘制中
        painter.drawLine(50,140,400,140)

        pen.setStyle(Qt.DotLine) # 有一些像素分割的线  虚线
        painter.setPen(pen)
        painter.drawLine(50,240,400,240)

        pen.setStyle(Qt.DashDotLine) # 轮流交替的点和短线
        painter.setPen(pen)
        painter.drawLine(50,340,400,340)

        pen.setStyle(Qt.DashDotDotLine) # 轮流交替的点和短线 一条短线，两个点
        painter.setPen(pen)
        painter.drawLine(50,440,400,440)

        #自定义线
        pen.setStyle(Qt.CustomDashLine) # 轮流交替的点和短线 一条短线，两个点
        pen.setDashPattern([1,4,5,8])  #4个参数分别表示 第一个线的长度 间隔 第二个线的长度 间隔   然后轮流交替
        painter.setPen(pen)
        painter.drawLine(50,540,400,540)

        painter.end()


if __name__ =="__main__":
    app = QApplication(sys.argv)
    main = DrawMultiLine()
    main.show()
    sys.exit(app.exec_())