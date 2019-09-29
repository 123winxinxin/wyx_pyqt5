'''
QFontDialog控件是一个常用的字体选择对话框，可以让用户选择所显示文本的字号大小，样式和格式,
QFontDialog是QDialog控件对话框的一部分，使用QFontDialog类的静态方法getFont（）,
可以从字体选择对话框中选择文本的显示字号大小样式和格式
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

class QFontDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QFontDialog示例')
        self.resize(300,100)

        layout = QVBoxLayout()
        self.btn = QPushButton('请选择字体')
        self.btn.clicked.connect(self.getFont)
        self.label = QLabel('Hello，这是一个测试')

        layout.addWidget(self.btn)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def getFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.label.setFont(font)


if __name__ =="__main__":
    app = QApplication(sys.argv)
    main = QFontDialogDemo()
    main.show()
    sys.exit(app.exec_())