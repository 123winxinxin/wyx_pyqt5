import sys
from PyQt5.QtWidgets import *

'''
QLineEdit
基本功能：输入单行文本
EchoMode(回显模式)
4种回显模式：
1、Normal 正常显示输入
2、NoEcho  不回显
3、Password 密码 回显黑点
4、PasswordEchoOnEdit  编辑时回显正常字符 过段时间后变成黑点
'''

class QLineEditEchoMode(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本输入框回显模式')
        formLayout = QFormLayout()
        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnEditLineEdit = QLineEdit()

        formLayout.addRow("Normal",normalLineEdit)
        formLayout.addRow("noEcho",noEchoLineEdit)
        formLayout.addRow("password",passwordLineEdit)
        formLayout.addRow("passwordEchoOnEdit",passwordEchoOnEditLineEdit)

        #placeholdertext 文本输入框的提示显示

        normalLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("noEcho")
        passwordLineEdit.setPlaceholderText('password')
        passwordEchoOnEditLineEdit.setPlaceholderText('passwordEchoOnEdit')


        #设置回显模式
        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.setLayout(formLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    echoMode = QLineEditEchoMode()
    echoMode.show()
    sys.exit(app.exec_())
