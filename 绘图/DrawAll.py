'''
这一次我们来绘制各种图形
弧形 扇形 圆 多边形 图像
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DrawAll(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('绘制不同的图形')
        self.resize(500,800)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        #绘制弧形
        rect = QRect(10,40,160,160)  #定义一个矩形区域用于绘制
        painter.setPen(Qt.blue) # 用蓝色绘制
        painter.drawArc(rect,0,60 * 16)  # 参数含义  绘制区域 起始角度 终止角度  注意单位是alen 1个alen 等于1/16度

        #通过弧画圆
        painter.setPen(Qt.red)
        painter.drawArc(240,40,160,160,0,360 * 16)

        #绘制带弦的弧
        painter.setPen(Qt.darkYellow)
        painter.drawChord(10,240,160,160,20*16,90*16)

        # 绘制扇形
        painter.setPen(Qt.green)
        painter.drawPie(240,240,160,160,30*16,120*16)

        #绘制椭圆
        painter.setPen(Qt.black)
        painter.drawEllipse(10,400,160,120)  # 不需要指定角度  若宽和高相等 就是圆

        # 绘制六边形
        #先制定6个点坐标
        p1 = QPoint(315,400)
        p2 = QPoint(415,400)
        p3 = QPoint(500,475)
        p4 = QPoint(415,550)
        p5 = QPoint(315,550)
        p6 = QPoint(240,475)

        polygon = QPolygon([p1,p2,p3,p4,p5,p6])
        painter.drawPolygon(polygon)

        # 绘制图像
        image = QImage('./images/python.png')
        rect = QRect((self.width()-image.width()/3.0)/2,600,image.width()/3.0,image.height()/3.0)
        painter.drawImage(rect,image)
        painter.end()


if __name__ =="__main__":
    app = QApplication(sys.argv)
    main = DrawAll()
    main.show()
    sys.exit(app.exec_())