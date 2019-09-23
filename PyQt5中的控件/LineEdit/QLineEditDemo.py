'''文本输入框综合案例'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys

class QLineEditDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本输入框综合案例')

        formLayout = QFormLayout()

        #校验器
        edit1 = QLineEdit()
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(4)  # 最大长度
        edit1.setAlignment(Qt.AlignRight)  # 设置对齐方式
        edit1.setFont(QFont('Arial',13))  # 设置字体 字号

        edit2 = QLineEdit()
        edit2.setValidator(QDoubleValidator(-99.99,99.99,2))

        # 掩码

        edit3 = QLineEdit()
        edit3.setInputMask("000:000:00;_")

        # 回显模式
        edit4 = QLineEdit()
        edit4.setEchoMode(QLineEdit.Password)
        edit4.textChanged.connect(self.textChanged)  # 文本变化就会触发,会把当前文本传到槽函数

        # 只读
        edit5 = QLineEdit('欢迎阅读')
        edit5.setReadOnly(True)

        # 信号与槽
        edit6 = QLineEdit()
        edit6.editingFinished.connect(self.editFinished)  # 编辑文本结束（鼠标焦点跳到别处）就会触发

        formLayout.addRow('整数',edit1)
        formLayout.addRow('浮点数',edit2)
        formLayout.addRow('IP',edit3)
        formLayout.addRow('密码',edit4)
        formLayout.addRow('只读',edit5)
        formLayout.addRow('信号与槽',edit6)

        self.setLayout(formLayout)


    def editFinished(self):
        print('已完成输入')

    def textChanged(self,text):
        print('已输入字符:'+text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QLineEditDemo()
    main.show()
    sys.exit(app.exec_())