'''
QInputDialog控件是一个标准对话框，有一个文本框和两个按钮（ok和cancel）组成，当用户单击ok或enter键后，
在父窗口可以收集通过QInputDialog控件输入的信息，QInputDialog控件是QDialog标准对话框的一部分
在QInpuTDialog控件中可以输入数字，字符串或列表中的选项，标签用于提示必要的信息

QInputDialog类中常用的方法
getint()	从控件中获得标准整数输入
getDouble()	从控件中获得标准浮点数输入
getText()	从控件中获得标准字符串的输入
getItem()	从控件中获得列表里的选项输入

'''


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

class QInputDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QInputDialog示例')

        layout = QFormLayout()
        btn1 = QPushButton('获得列表种的选项')
        btn1.clicked.connect(self.getItem)

        btn2 = QPushButton('获得文本')
        btn2.clicked.connect(self.getText)

        btn3 = QPushButton('获得整数')
        btn3.clicked.connect(self.getInt)

        btn4 = QPushButton('获得小数')
        btn4.clicked.connect(self.getDouble)

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit3 = QLineEdit()
        self.lineEdit4 = QLineEdit()

        layout.addRow(btn1,self.lineEdit1)
        layout.addRow(btn2,self.lineEdit2)
        layout.addRow(btn3,self.lineEdit3)
        layout.addRow(btn4,self.lineEdit4)

        self.setLayout(layout)

    def getItem(self):
        items = ('C','C++','Python','Java','Ruby')
        item, ok = QInputDialog.getItem(self,'请选择编程语言','语言列表',items)
        if ok and item:
            self.lineEdit1.setText(item)

    def getText(self):
        text, ok = QInputDialog.getText(self,'文本输入','请输入姓名')
        if ok and text:
            self.lineEdit2.setText(text)

    def getInt(self):
        num, ok = QInputDialog.getInt(self,'数字输入','请输入数字')
        if ok:
            self.lineEdit3.setText(str(num))

    def getDouble(self):
        db, ok = QInputDialog.getDouble(self,'浮点数输入','请输入浮点数')
        if ok :
            self.lineEdit4.setText(str(db))


if __name__ =="__main__":
    app = QApplication(sys.argv)
    main = QInputDialogDemo()
    main.show()
    sys.exit(app.exec_())