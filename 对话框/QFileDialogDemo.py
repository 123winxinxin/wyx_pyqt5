'''
QFIleDialog是用于打开和保存文件的标准对话框。QFileDialog类继承自QDialog类
QFileDialog在打开文件时使用可文件过滤器，用于显示指定扩展名的文件，也可以设置使用QFileDialog打开文件时的起始目录和指定扩展名的文件

QFileDialog类中的常用方法
getOpenFileName()	返回用户所选择文件的名称，并打开该文件
                        第一个参数self：用于指定父组件
                        第二个参数是QFileDialog对话框的标题
                        第三个参数默认打开的目录，‘.’代表程序运行的目录，‘/’代表当前盘下的根目录(window.linux系统),
                                            需要注意的是不同路径的显示方式，比如window平台下的C盘“C:\”等
                        第四个参数是对话框中文件扩展名过滤器（fliter）,比如使用’Image files (.jpg .gif .png .jpeg)’表示只能显示扩展名为   .jpg,.gif等文件
getSaveFileName（）	使用用户选择的文件名保存文件
setFileMode（）	可以选择的文件类型，枚举常量是：
                        QFileDialog.AnyFile:任何文件
                        QFileDialog.ExistingFile:已存在的文件
                        QFileDialog.Directory:文件目录
                        QFileDialog.ExistingFiles:已经存在的多个文件
setFilter()	设置过滤器，只显示过滤器允许的文件类型

'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QFileDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文件对话框')

        layout = QVBoxLayout()

        self.imageBtn = QPushButton('加载一张图片')
        self.imageBtn.clicked.connect(self.loadImage)
        self.imageLabel = QLabel()

        self.textBtn = QPushButton('加载一个文本文件')
        self.textBtn.clicked.connect(self.loadText)
        self.textEdit = QTextEdit()

        layout.addWidget(self.imageBtn)
        layout.addWidget(self.imageLabel)
        layout.addWidget(self.textBtn)
        layout.addWidget(self.textEdit)

        self.setLayout(layout)

    def loadImage(self):
        # 从当前位置打开文件格式（*.jpg *.gif *.png *.jpeg）文件 返回路径
        fname, _ = QFileDialog.getOpenFileName(self,'打开图片','.','图片文件(*.jpg *.gif *.png *.jpeg)')
        self.imageLabel.setPixmap(QPixmap(fname)) # 设置标签为图片标签

    def loadText(self):
        dig = QFileDialog() # 实例化一个文件对话框
        dig.setFileMode(QFileDialog.AnyFile) # 设置模式为可以打开任何文件
        dig.setFilter(QDir.Files) # 文件过滤
        if dig.exec_(): # 如果文件对话框退出
            fnames = dig.selectedFiles()  #接受选中文件的路径，默认为列表
            with open(fnames[0],'r',encoding='utf-8') as f: #列表中的第一个元素即是文件路径，以只读的方式打开文件
                content = f.read()
                self.textEdit.setText(content)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QFileDialogDemo()
    main.show()
    sys.exit(app.exec_())