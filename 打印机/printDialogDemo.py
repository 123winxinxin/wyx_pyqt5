from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *
import sys

class PrinterDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.printer = QPrinter()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,500,400)
        self.setWindowTitle('打印对话框')

        self.edit = QTextEdit(self)
        self.edit.setGeometry(20,20,300,270)

        self.btn1 = QPushButton('open',self)
        self.btn1.move(350,20)
        self.btn1.clicked.connect(self.openFile)

        self.btn2 = QPushButton('settings',self)
        self.btn2.move(350,50)
        self.btn2.clicked.connect(self.showSettingsDialog)

        self.btn3 = QPushButton('print',self)
        self.btn3.move(350,80)
        self.btn3.clicked.connect(self.printerDialog)


    def openFile(self):# 打开文件
        fname = QFileDialog.getOpenFileName(self,'打开文本文件','./')
        if fname[0]:
            with open(fname[0],'r',encoding='utf-8',errors='ignore') as f:
                self.edit.setText(f.read())

    def showSettingsDialog(self): # 显示打印设置对话框
        printerSettingsDialog = QPageSetupDialog(self.printer,self)
        printerSettingsDialog.exec()

    def printerDialog(self): # 显示打印对话框
        printerDialog = QPrintDialog(self.printer,self)
        if QDialog.Accepted == printerDialog.exec():
            self.edit.print(self.printer)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=PrinterDialog()
    main.show()
    sys.exit(app.exec_())