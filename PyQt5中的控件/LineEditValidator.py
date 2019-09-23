'''
校验器：限制文本输入框的输入，比如说只允许输入整型、浮点型、或者按照正则表达式等满足一定条件的字符串
流程：
1、初始化一个表单布局
2、往布局中添加控件
3、设置文本输入框提示信息
4、初始化各种校验器，设置范围、精度、正则表达式
5、校验器和文本输入框绑定
'''

from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp


class QLineEditValidator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        formLayout = QFormLayout() # 初始化布局

        # 初始化文本输入框
        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        reLineEdit = QLineEdit()

        # 往布局中添加控件
        formLayout.addRow("整型校验器",intLineEdit)
        formLayout.addRow("浮点型校验器",doubleLineEdit)
        formLayout.addRow("数字和字母校验器",reLineEdit)

        # 设置文本输入框的提示信息
        intLineEdit.setPlaceholderText("输入0-99的整数")
        doubleLineEdit.setPlaceholderText("输入-360到360的浮点数")
        reLineEdit.setPlaceholderText("输入数字或者字母")

        #初始化校验器
        intValidator = QIntValidator(self)
        intValidator.setRange(0,99) # 整数校验器

        doubleValidator = QDoubleValidator(self)
        doubleValidator.setRange(-360,360) # 浮点校验器  支持不太好
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)  # 使用标准格式
        doubleValidator.setDecimals(2)  # 设置精度为2

        reg = QRegExp("[a-zA-Z0-9]+$")  # 定义一个正则表达式
        reValidator = QRegExpValidator(self)
        reValidator.setRegExp(reg) #设置正则校验器的表达式

        # 绑定文本输入框和校验器
        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        reLineEdit.setValidator(reValidator)

        self.setLayout(formLayout)
        self.setWindowTitle('校验器')

if __name__ =="__main__":
    app = QApplication(sys.argv)
    lineEditValidator = QLineEditValidator()
    lineEditValidator.show()
    sys.exit(app.exec_())