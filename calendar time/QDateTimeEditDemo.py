'''
QDateTimeEdit是一个允许用户编辑日期时间的控件，可以使用键盘上的上下键头按钮来增加或减少日期的时间值，
QDateTimeEdit通过setDisplayFormat（）函数来设置显示的日期时间格式

QDateTimeEdit类中常用方法
setDisplayFormat	设置日期的时间格式
                        yyyy：代表年份，用4为数表示
                        MM：代表月份，取值范围01-12
                        dd：代表日，取值范围01-31
                        HH：代表小时，取值范围00-23
                        mm：代表分钟，取值范围00-59
                        ss：代表秒，取值范围00-59
setMinimumDate()	设置控件的最小日期
setMaximumDate()	设置控件的最大日期
time()	返回编辑的时间
date()	返回编辑的日期

QDateTImeEdit类中常用的信号
    dateChanged	当日期改变时发射此信号
    dateTImeChanged	当日期时间改变时发射此信号
    timeChanged	当时间发生改变时发射此信号


'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyDateTime(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vlayout = QVBoxLayout()
        self.dateTimeEdit1 = QDateTimeEdit() # 实例化
        self.dateTimeEdit2 = QDateTimeEdit(QDateTime.currentDateTime()) #实例化 并给与一个初始值
        self.dateTimeEdit2.setMinimumDate(QDate.currentDate().addDays(-365)) # 设置最小日期为去年今天
        self.dateTimeEdit2.setMaximumDate(QDate.currentDate().addDays(365))  # 设置最大日期为明年今天

        self.dateTimeEdit2.setCalendarPopup(True) # 设置日历可以点开

        self.timeEdit = QDateTimeEdit(QTime.currentTime()) # 设置日期为当前日期
        self.dateEdit = QDateTimeEdit(QDate.currentDate()) # 设置时间为当前时间
        self.btn = QPushButton('获取选择的日期')
        self.btn.clicked.connect(self.getSelectedDateTime)

        self.dateTimeEdit1.setDisplayFormat('yyyy/MM/dd HH:mm:ss') # 设置显示格式
        self.dateTimeEdit2.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        self.dateEdit.setDisplayFormat('yyyy.MM.dd')
        self.timeEdit.setDisplayFormat('HH:mm:ss')

        self.dateTimeEdit1.dateTimeChanged.connect(self.onDateTimeChanged) # 日期时间改变时触发
        self.dateEdit.dateChanged.connect(self.onDateChanged)
        self.timeEdit.timeChanged.connect(self.onTimeChanged)


        vlayout.addWidget(self.dateTimeEdit1)
        vlayout.addWidget(self.dateTimeEdit2)
        vlayout.addWidget(self.dateEdit)
        vlayout.addWidget(self.timeEdit)
        vlayout.addWidget(self.btn)

        self.setLayout(vlayout)
        self.setWindowTitle('日期时间演示')
        self.resize(300,250)

    def onDateTimeChanged(self,dateTime):
        print('日期时间改变：',dateTime)

    def onDateChanged(self,date):
        print('日期改变',date)

    def onTimeChanged(self,time):
        print('时间改变',time)

    def getSelectedDateTime(self):
        dateTime = self.dateTimeEdit2.dateTime() #获取选择的日期时间
        print('选择的日期时间为',dateTime)
        print(self.dateTimeEdit2.maximumDate())
        print(self.dateTimeEdit2.minimumDate())
        print(self.dateTimeEdit2.maximumDateTime())
        print(self.dateTimeEdit2.minimumDateTime())

if __name__ =="__main__":
    app = QApplication(sys.argv)
    main = MyDateTime()
    main.show()
    sys.exit(app.exec_())