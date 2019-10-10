'''
如果想把A拖拽到B，需要设置A.setDragEnabled()为True，另外设置B.setAcceptDrops()为True
另外 基于MIME类型的拖曳数据传输是基于QDrag类的，QMimeData对象将关联的数据与其对应的MIME类型相关联

MimeData类函数允许检测和使用方便的MIME类型
判断函数	    获取函数	     设置函数	           MIME类型
hasText()	text()	    setText()	       text/plain
hasHtml()	html()	    setHtml()	       text/html
hasUrls()	urls()	    setUrls()	       text/url-list
hasImage()	imageData()	setImageData	   image/*
hasColor()	colorData()	setColrDaata()	   application/x-color

常用的拖曳事件
DragEnterEvent	当执行一个拖曳控件操作，并且鼠标指针进入该控件时，这个事件将会被触发。
                    在这个事件中可以获得被操作的窗口控件，还可以有条件地接受或拒绝该拖曳操作
DragMoveEvent	在拖曳操作进行时会触发该事件
DragLeaveEvent	当执行一个拖曳操作，并且鼠标指针离开该控件时，这个事件被触发
DropEvent	当拖曳操作在其目标控件上被释放时，这个事件将被触发


'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyComboBox(QComboBox):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)  # 设置为可接收拖拽的控件

    def dragEnterEvent(self, e): #鼠标拖拽进入该控件时，事件触发
        if e.mimeData().hasText():  # 如果拖拽进来的数据是文本就接受，不是就忽略
            e.accept()
        else:
            e.ignore()

    def dropEvent(self,e): # 当拖曳操作在其目标控件上被释放时，这个事件将被触发
        self.addItem(e.mimeData().text()) # 把文本添加到下拉框的项目中


class DragDrop(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('拖拽示例')
        layout = QFormLayout()
        layout.addRow(QLabel('请把左侧的文本拖拽到右侧的下拉框中'))
        lineEdit = QLineEdit()
        lineEdit.setDragEnabled(True)  # 设置为可拖拽

        cb = MyComboBox()
        layout.addRow(lineEdit,cb)

        self.setLayout(layout)


if __name__ =="__main__":
    app = QApplication(sys.argv)
    main = DragDrop()
    main.show()
    sys.exit(app.exec_())