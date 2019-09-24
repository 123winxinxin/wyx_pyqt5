from PyQt5.QtWidgets import *
import sys

class QRadioButtonDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('单选框示例')
        self.resize(300,400)

        layout = QHBoxLayout()

        button1 = QRadioButton('Python')
        button1.setChecked(True)  # 默认选中
        button1.toggled.connect(self.buttonState)  # toggled 状态变化就会触发

        button2 = QRadioButton('Java')
        button2.toggled.connect(self.buttonState)

        button3 = QRadioButton('C++')
        button3.toggled.connect(self.buttonState)


        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)

        self.setLayout(layout)

    def buttonState(self):
        sender = self.sender()
        if sender.isChecked():  # 如果被选中
            print(sender.text()+'被选中了！')
        else:
            print(sender.text()+'被取消选中了！')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QRadioButtonDemo()
    main.show()
    sys.exit(app.exec_())