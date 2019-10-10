'''
QBrush(画刷)是一个基本的图形对象，用于填充如矩形，椭圆形，多边形等形状，QBrush有三种类型，预定义，过渡，和纹理图案
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class FillRect(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('用画刷填充区域')
        self.resize(500,800)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        brush = QBrush(Qt.SolidPattern)
        painter.setBrush(brush)
        painter.drawRect(10,40,120,100)

        brush = QBrush(Qt.Dense1Pattern)
        painter.setBrush(brush)
        painter.drawRect(150,40,120,100)

        brush = QBrush(Qt.Dense2Pattern)
        painter.setBrush(brush)
        painter.drawRect(300,40,120,100)

        brush = QBrush(Qt.Dense3Pattern)
        painter.setBrush(brush)
        painter.drawRect(10,160,120,100)

        brush = QBrush(Qt.Dense4Pattern)
        painter.setBrush(brush)
        painter.drawRect(150,160,120,100)

        brush = QBrush(Qt.DiagCrossPattern)
        painter.setBrush(brush)
        painter.drawEllipse(300,160,120,120)

        brush = QBrush(Qt.BDiagPattern)
        painter.setBrush(brush)
        painter.drawEllipse(10,300,160,120)

        brush = QBrush(Qt.HorPattern)
        painter.setBrush(brush)
        painter.drawEllipse(200,300,120,120)

        brush = QBrush(Qt.VerPattern)
        painter.setBrush(brush)
        painter.drawEllipse(350,300,120,120)

        brush = QBrush(Qt.Dense5Pattern)
        painter.setBrush(brush)
        painter.drawRect(10,500,120,100)

        brush = QBrush(Qt.Dense6Pattern)
        painter.setBrush(brush)
        painter.drawRect(150,500,120,100)

        brush = QBrush(Qt.Dense7Pattern)
        painter.setBrush(brush)
        painter.drawRect(300,500,120,100)



        painter.end()

if __name__ =="__main__":
    app = QApplication(sys.argv)
    main = FillRect()
    main.show()
    sys.exit(app.exec_())