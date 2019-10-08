import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class DrawPoint(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('在窗口上绘制一条正弦曲线')
        self.resize(500,300)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        painter.setPen(Qt.blue)
        size = self.size()

        for i in range(1000):
            x = 100*(-1 + 2.0*i/1000) + size.width()/2.0  # x的范围是-100到100 并且分成1000等分，由于坐标原点时窗口中心，所以加上宽度的一半
            y = -50* math.sin((x-size.width()/2.0) * math.pi/50) + size.height()/2.0  # y的范围是-50到50  x*pi/50 正好范围是-2pi到2pi
            painter.drawPoint(x,y)

        painter.end()


if __name__ =="__main__":
    app = QApplication(sys.argv)
    main = DrawPoint()
    main.show()
    sys.exit(app.exec_())