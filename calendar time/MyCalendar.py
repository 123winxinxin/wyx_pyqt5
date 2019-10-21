'''
QCalendar 是日历控件，提供基于月份的视图，允许通过鼠标或键盘选择日期，默认为当天日期。
QCalendar 类中的常用方法如下表
setDateRange()	设置日期范围供选择
setFirstDayOfWeek()	重新设置星期的第一天，默认为星期日。
setMinimumDate()	设置最大日期
setMaximumDate()	设置最小日期
setSelectedDate()	设置一个 QDate 对象，作为日期控件所选定的日期
maximumDate()	获取日历控件的最大日期
minimumDate()	获取日历控件的最小日期
selectedDate()	返回当前所选定的日期
setGridvisible()	设置日历控件是否显示网格

setFirstDayOfWeek() 的可选参数如下：
Qt.Monday	星期一
Qt.Tuesday	星期二
Qt.Wendnesday	星期三
Qt.Thursday	星期四
Qt.Friday	星期五
Qt.Saturday	星期六
Qt.Sunday	星期日

'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyCalendar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('日历演示')
        self.resize(500,400)
        self.cal = QCalendarWidget(self)

        self.cal.setMaximumDate(QDate(2088,1,1))
        self.cal.setMinimumDate(QDate(1988,1,1))

        self.cal.setGridVisible(True)
        self.move(40,20)

        self.label = QLabel(self)
        date = self.cal.selectedDate()
        self.label.setText(date.toString('yyyy-MM-dd dddd'))
        self.label.move(40,350)
        self.cal.clicked.connect(self.showDate)

    def showDate(self,date):
        # self.label.setText(date.toString('yyyy-MM-dd dddd'))
        self.label.setText(self.cal.selectedDate().toString('yyyy-MM-dd dddd'))


if __name__ =="__main__":
    app = QApplication(sys.argv)
    main = MyCalendar()
    main.show()
    sys.exit(app.exec_())