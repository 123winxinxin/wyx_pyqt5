'''
QClipboard类提供了对系统剪切板的访问，可以在应用程序之间复制和粘贴数据，它的操作类似于QDrag类，，并使用类似的数据结构
QApplication类有一个静态方法clipboard（），它的返回值对剪切板对象的引用，任何类型的MimeData都可以从剪切板复制或粘贴

QClipboard类中的常用方法
clear()	清空剪切板的内容
setImage()	将QImage对象复制到剪切板中
setMimeData()	将MIME数据设置为剪切板
setPixmap()	从剪切板中复制Pixmap对象
setText()	从剪切板中复制文本
text()	从剪切板中检索文本
mimeData() 从剪切板中检索mimeData
pixmap() 从剪切板中检索图像

QClipboard类中的常用信号
dataChanged	当剪切板内容发生变化时，这个信号被发射

'''

import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ClipBoardDemo(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('剪切板示例')
        layout = QGridLayout()

        # 创建复制粘贴按钮，并添加快捷键
        textCopyBtn = QPushButton('&CopyText')
        textPasteBtn = QPushButton('Paste&Text')

        htmlCopyBtn = QPushButton('C&opyHtml')
        htmlPasteBtn = QPushButton('Paste&Html')

        imageCopybtn = QPushButton('Cop&yImage')
        imagePastebtn = QPushButton('Paste&Image')

        # 创建文本标签和图像标签，显示文本和图像
        self.testLabel = QLabel('默认文本')
        self.imageLabel = QLabel()

        # 设置栅格布局，并添加部件到相应的位置
        layout.addWidget(textCopyBtn,0,0)
        layout.addWidget(textPasteBtn,0,1)#设置主窗口的布局，自定义槽函数，设置标题
        layout.addWidget(htmlCopyBtn,0,2)
        layout.addWidget(htmlPasteBtn,1,0)
        layout.addWidget(imageCopybtn,1,1)
        layout.addWidget(imagePastebtn,1,2)
        layout.addWidget(self.testLabel,2,0,1,2)
        layout.addWidget(self.imageLabel,2,2)

        #定义按钮的槽函数
        textCopyBtn.clicked.connect(self.copyText)
        textPasteBtn.clicked.connect(self.pasteText)
        htmlCopyBtn.clicked.connect(self.copyHtml)
        htmlPasteBtn.clicked.connect(self.pasteHtml)
        imageCopybtn.clicked.connect(self.copyImage)
        imagePastebtn.clicked.connect(self.pasteImage)

        self.setLayout(layout)

    def copyText(self):
        # 实例化剪切板，设置剪切板的文本
        clipboard = QApplication.clipboard()
        clipboard.setText('Hello World')

    def pasteText(self):
        # 实例化剪切板，标签设置为剪切板的文本并显示
        clipboard = QApplication.clipboard()
        self.testLabel.setText(clipboard.text())

    def copyHtml(self):
        mimeData = QMimeData() # #实例化MimeData数据类型，设置类型Html的文本
        mimeData.setHtml("<font color=red>Bold and Red</font>")
        # 实例化剪切板，设置MimeData的初值文本
        clipboard = QApplication.clipboard()
        clipboard.setMimeDate(mimeData)

    def pasteHtml(self):
        # 实例化剪切板，，获取MimeData的数据，并设置为标签的文本值
        clipborad = QApplication.clipboard()
        mimeData = clipborad.mimeData()
        if mimeData.hasHtml():
            self.testLabel.setText(mimeData.html())

    def copyImage(self):
        # 实例化剪切板，设置剪切板加载的图像路径
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(QPixmap('./images/python.png'))

    def pasteImage(self):
        # 实例化剪切板，设置图像标签的图片加载，从剪切板获取图像路径
        clipboard = QApplication.clipboard()
        self.imageLabel.setPixmap(clipboard.pixmap())

if __name__ =="__main__":
    app = QApplication(sys.argv)
    main = ClipBoardDemo()
    main.show()
    sys.exit(app.exec_())