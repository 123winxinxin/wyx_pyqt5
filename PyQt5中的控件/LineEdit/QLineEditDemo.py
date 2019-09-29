'''文本输入框综合案例
QLineEdit类中常用的方法如下表
setAlignment()	按固定值方式对齐文本
                    Qt.AlignLeft：水平方向靠左对齐
                    Qt.AlignRight:水平方向靠右对齐
                    Qt.AlignCenter：水平方向居中对齐
                    Qt.AlignJustify：水平方向调整间距两端对齐
                    Qt.AlignTop：垂直方向靠上对齐
                    Qt.AlignBottom：垂直方向靠下对齐
                    Qt.AlignVCenter：垂直方向居中对齐
setEchoMode()	设置文本框的显示格式，允许输入的文本显示格式的值可以是：
                    QLineEdit.Normal：正常显示所输入的字符，此为默认选项
                    QLineEdit.NoEcho：不显示任何输入的字符，常用于密码类型的输入，且长度保密
                    QLineEdit.Password：显示与平台相关的密码掩饰字符，而不是实际输入的字符
                    QLineEdit.PasswordEchoOnEdit：在编辑时显示字符，负责显示密码类型的输入
setPlaceholderText()	设置文本框显示文字
setMaxLength()	设置文本框所允许输入的最大字符数
setReadOnly()	设置文本为只读
setText()	设置文本框的内容
text()	返回文本框的内容
setDragEnable()	设置文本框是否接受拖动
selectAll()	全选
setFocus()	得到焦点
setInputMask()	设置掩码
setValidator()	设置文本框的验证器（验证规则），将限制任意可能输入的文本，可用的校验器为
                QIntValidator:限制输入整数
                QDoubleValidator:限制输入浮点数
                QRegexpValidator:检查输入是否符合正则表达式

QLineEdit类中常用信号如下
selectionChanged	只要选择改变了，这个信号就会发射
textChanged	当修改文本内容时，这个信号就会发射
editingFinished	当编辑文本结束时，这个信号就会发射

'''

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