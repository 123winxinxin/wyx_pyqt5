'''
QListWidget类是一个基于条目的接口，用于从列表中添加或删除条目，列表中的每个条目都是一个QListWidgetItem对象，QListWidget可以设置为多重选择
QListWidget类中常用的方法
addItem()	在列表中添加QListWidgetItem对象或字符串
addItems()	添加列表中的每个条目
insertItem()	在指定地索引处插入条目
clear()	删除列表的内容
setCurrentItem()	设置当前所选的条目
sortItems()	按升序重新排列条目

QLIstWidget类中常用的信号
currentItemChanged	当列表中的条目发生改变时发射此信号
itemClicked	当点击列表中的条目时发射此信号
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class ListWidgetDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QListWidget演示')

        self.resize(300,270)

        self.listWidget = QListWidget()
        self.listWidget.resize(300,120)
        self.listWidget.addItem('item1') # 增加条目
        self.listWidget.addItems(['item2','item3','item4']) # 增加多个条目
        self.listWidget.itemClicked.connect(self.onClicked)
        self.setCentralWidget(self.listWidget)

    def onClicked(self,item):
        QMessageBox.information(self,'QListWidget','您选择了：' + item.text())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ListWidgetDemo()
    main.show()
    sys.exit(app.exec_())