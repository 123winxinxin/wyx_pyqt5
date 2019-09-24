from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

class QCheckBoxDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('复选框示例')
        self.resize(300,400)

        layout = QHBoxLayout()

        self.cb1 = QCheckBox('选择项1')
        self.cb1.setChecked(True)
        self.cb1.stateChanged.connect(lambda: self.checkBoxState(self.cb1)) # stateChanged状态变化就会触发

        self.cb2 = QCheckBox('选择项2')
        self.cb2.stateChanged.connect(lambda: self.checkBoxState(self.cb2))

        self.cb3 = QCheckBox('选择项3')
        self.cb3.setTristate(True) # 让这个复选框有3种状态可选
        self.cb3.setCheckState(Qt.PartiallyChecked)  # 设置这个复选框为中间状态
        self.cb3.stateChanged.connect(lambda: self.checkBoxState(self.cb3))



        layout.addWidget(self.cb1)
        layout.addWidget(self.cb2)
        layout.addWidget(self.cb3)

        self.setLayout(layout)

    def checkBoxState(self,cb):
        print('复选框1选中状态为'+str(self.cb1.isChecked())+',state为'+str(self.cb1.checkState()))
        print('复选框2选中状态为'+str(self.cb2.isChecked())+',state为'+str(self.cb2.checkState()))
        print('复选框3选中状态为'+str(self.cb3.isChecked())+',state为'+str(self.cb3.checkState()))
        print()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QCheckBoxDemo()
    main.show()
    sys.exit(app.exec_())