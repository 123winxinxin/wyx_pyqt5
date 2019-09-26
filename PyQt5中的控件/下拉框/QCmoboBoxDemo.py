'''
QComboBox是一个集按钮和下拉选项于一体的控件，也称做下拉列表框

QComboBox类中的常用方法如表
addItem()	添加一个下拉选项
addItems()	从列表中添加下拉选项
Clear()	删除下拉选项集合中的所有选项
count()	返回下拉选项集合中的数目
currentText()	返回选中选项的文本
itemText(i)	获取索引为i的item的选项文本
currentIndex()	返回选中项的索引
setItemText(int index,text)	改变序列号为index的文本

QComboBox类中的常用信号
Activated	当用户选中一个下拉选项时发射该信号
currentIndexChanged	当下拉选项的索引发生改变时发射该信号
highlighted	当选中一个已经选中的下拉选项时，发射该信号
'''

import sys
from PyQt5.QtWidgets import *


class QCmoboBoxDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('下拉列表示例')
        self.resize(300,100)

        layout = QVBoxLayout()

        self.label = QLabel('请选择语言')
        self.cb = QComboBox()
        self.cb.addItem('Python') # 添加条目
        self.cb.addItem('Java')
        self.cb.addItems(['C++','Ruby','Go'])  # 一次加多个条目

        self.cb.currentIndexChanged.connect(self.selectionChange)  # 选择变化就会触发

        layout.addWidget(self.label)
        layout.addWidget(self.cb)
        self.setLayout(layout)

    def selectionChange(self,i):
        self.label.setText(self.cb.currentText())  # 标签设置为当前选择的文本 currentText()：返回选中选项的文本
        self.label.adjustSize()  # 调整标签尺寸

        print('所有选项为:')
        for count in range(self.cb.count()): # count()  下拉有几个条目
            print('item' + str(count)+'='+self.cb.itemText(count)) # itemText(i) 获取索引为i的item的选项文本
        print('current index',i,'selection changed',self.cb.currentText())


if __name__ =="__main__":
    app = QApplication(sys.argv)
    main = QCmoboBoxDemo()
    main.show()
    sys.exit(app.exec_())