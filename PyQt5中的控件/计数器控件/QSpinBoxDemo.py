'''
QSPINBox是一个计数器控件，允许用户选择一个整数值通过单击向上向下或者按键盘上的上下键来增加减少当前显示的值，当然用户也可以输入值
在默认情况下，QSpinBox的取值范围是（0-99），每次改变的步长是1
QSpinBox类和QDoubleSpinbox类均派生自QAbstractSpinBox类，QSpinBox用于处理整数值，QDoubleSpinBox则用于处理浮点数值，
他们之间的区别就是处理数据的类型不同，其他功能基本相同，QDoubleSpinBox的默认精度是两位小数，但可以通过setDecimals（）来改变

QSpinBox类中的常用方法
方法	描述
setMinimum()	设置计数器的下界
setMaximum()	设置计数器的上界
setRange()	设置计数器的最大值，最小值，步长值
setValue()	设置计数器的当前值
Value()	返回计数器的当前值
setSingleStep()	设置计数器的步长值

每次值改变QSpinBox发出valueChanged()信号
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class QSpinBoxDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('计数器控件示例')
        self.resize(300,100)

        layout = QVBoxLayout()

        self.label = QLabel('当前值:')
        self.label.setAlignment(Qt.AlignCenter) # 居中显示

        self.sb = QSpinBox()

        #设置初始值
        self.sb.setValue(18)
        #设置范围
        self.sb.setRange(2,60)
        # 设置步长
        self.sb.setSingleStep(2)

        self.sb.valueChanged.connect(self.valueChange)

        layout.addWidget(self.label)
        layout.addWidget(self.sb)

        self.setLayout(layout)

    def valueChange(self):
        self.label.setText('当前值:'+str(self.sb.value()))


if __name__ =="__main__":
    app = QApplication(sys.argv)
    main = QSpinBoxDemo()
    main.show()
    sys.exit(app.exec_())
