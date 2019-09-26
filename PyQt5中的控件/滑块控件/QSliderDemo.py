'''
QSlider控件提供一个垂直或者水平的滑动条，滑动条是一个用于控制有界值典型的控件，它允许用户沿水平或者垂直方向在某一范围内移动滑块，并将滑块所在的位置转换为一个合法范围内的整数值，有时候这中方式比输入数字或者使用SpinBox（计数器·）更加自然，在槽函数中对滑块所在位置的处理相当于从整数之间的最小值和最高值进行取值

一个滑块条控件可以以垂直或者水平的方式显示，在构造函数中进行设置
self.sp=QSlider(Qt.Horizontal)
self.sp=Qslider(Qt.Vertical)

QSlider类中常用的方法如表所示
setMinimum()	设置滑动条控件的最小值
setMaximum()	设置滑动条控件的最大值
setSingleStep()	设置滑动条控件的步长
setValue()	设置滑动条控件的值
value()	获取滑动条控件的值
setTickInterval()	设置刻度间隔
setTickPosition()	设置刻度标记的位置，可以输入一个枚举值，这个枚举值指定刻度线想当与滑块和用户操作的位置，以下是可以输入的枚举值：
QSlider.NoTicks:不绘制任何刻度线
QSlider.TicksBothSides：在滑块的两侧绘制刻度线
QSlider.TicksAbove:在滑块的（水平）上方绘制刻度线
QSlider.TicksBelow:在滑块的（水平）下方绘制刻度线
QSlider.TicksLeft:在滑块的（垂直）左侧绘制刻度线
QSlider.TicksRight,在滑块的（垂直）右侧绘制刻度线

QSlider类中的常用信号
vlaueChanged	当滑块的值发生改变时发射此信号，此信号是最常用的
sliderPressed	当用户按下滑块时发射此信号
sliderMoved	当用户拖动滑块时发射此信号
slierReleased	当用户释放滑块时发射此信号

'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class QSliderDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('滑动条控件示例')
        self.resize(300,200)

        layout = QVBoxLayout()
        self.label = QLabel('Hello World!')
        self.label.setAlignment(Qt.AlignCenter)

        self.slider = QSlider(Qt.Horizontal)

        #设置初始值
        self.slider.setValue(12)

        #设置最大最小值
        self.slider.setMaximum(48)
        self.slider.setMinimum(8)

        #设置步长
        self.slider.setSingleStep(3)

        #设置刻度间隔
        self.slider.setTickInterval(6)

        #设置刻度位置
        self.slider.setTickPosition(QSlider.TicksBelow)

        self.slider.valueChanged.connect(self.valueChange)  # 值改变了就触发

        layout.addWidget(self.label)
        layout.addWidget(self.slider)

        self.setLayout(layout)

    def valueChange(self):
        print('当前值:',self.slider.value())
        size = self.slider.value()
        self.label.setFont(QFont('Arial',size))


if __name__ =="__main__":
    app = QApplication(sys.argv)
    main = QSliderDemo()
    main.show()
    sys.exit(app.exec_())