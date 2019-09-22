import sys
from PyQt5.QtWidgets import *

class QLabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLabel伙伴控件')

        namelable = QLabel('&Name',self)
        nameLineEdit = QLineEdit(self)
        namelable.setBuddy(nameLineEdit)  # 设置伙伴控件

        passwordlable = QLabel('&Name',self)
        passwordLineEdit = QLineEdit(self)
        passwordlable.setBuddy(passwordLineEdit)  # 设置伙伴控件

        btnOK = QPushButton('OK')
        btnCancel = QPushButton('Cancel')

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(namelable,0,0)
        mainLayout.addWidget(nameLineEdit,0,1,1,2)

        mainLayout.addWidget(passwordlable,1,0)
        mainLayout.addWidget(passwordLineEdit,1,1,1,2)

        mainLayout.addWidget(btnOK,2,1)
        mainLayout.addWidget(btnCancel,2,2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    buddy = QLabelBuddy()
    buddy.show()
    sys.exit(app.exec_())
