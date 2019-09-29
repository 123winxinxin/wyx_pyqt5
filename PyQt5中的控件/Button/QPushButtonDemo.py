'''
QAbstractButton类为抽象类，不能实例化，必须由其他的按钮类继承QAbstractButton类，来实现不同的功能和表现形式，
常见的按钮QPushButton，QToolButton，QRadioButton和QCheckBox这些按钮均继承自QAbstractButton类，
根据各自的使用场景通过图形显示出来

QAbstractButton提供的状态如下
isDown()	提示按钮是否已按下
isChecked()	提示按钮是否已经标记
isEnable()	提示按钮是否可以被用户点击
isCheckAble()	提示按钮是否为可标记的
setAutoRepeat()	设置按钮是否在用户长按时可以自动重复执行

QAbstractButton提供的信号如下
Pressed	当鼠标指针在按钮上并按下左键时触发该信号
Released	当鼠标左键被释放时触发该信号
Clicked	当鼠标左键被按下然后释放时，或者快捷键被释放时触发该信号
Toggled	当按钮的标记状态发生改变时触发该信号

QPUshButton类中的常用方法
setCheckable()	设置按钮是否已经被选中，如果设置True，则表示按钮将保持已点击和释放状态
toggle()	在按钮状态之间进行切换
setIcon()	设置按钮上的图标
setEnabled()	设置按钮是否可以使用，当设置为False时，按钮变成不可用状态，点击它不会发射信号
isChecked()	返回按钮的状态，返回值为True或者False
setDefault()	设置按钮的默认状态
setText()	设置按钮的显示文本
text()	返回按钮的显示文本

为QPushButton设置快捷键
通过按钮名字能为QPushButton设置快捷键，比如名字为‘&Download’的按键，它的快捷键是‘Alt+D’。
其规则是;想要实现快捷键为“Alt+D”，那么按钮的名字里有D这个字母，并且在D的前面加上“&”，
这个字母D一般是按钮名称的首字母，而且在按钮显示时。“&”不会显示出来，如果想显示，那么需要转义，核心代码如下
self.btn=QPushButton('&Download')
self.btn.setDefault(True)


'''



from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class QPushButtonDemo(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QPushButton示例')
        self.resize(300,500)

        layout = QVBoxLayout()
        # 正常的按钮
        self.button1 = QPushButton()
        self.button1.setText('按钮1') # setText() 设置按钮文本
        self.button1.setCheckable(True) # 设置按钮有开关状态，按下不会自动起来
        # self.button1.toggle() # 开启按钮
        # self.button1.clicked.connect(self.whichButton)
        self.button1.clicked.connect(lambda:self.whichButton(self.button1)) # 把lambda表达式当作槽，触发后直接调用后面的方法，优点是可以传参
        self.button1.clicked.connect(self.buttonState)  #正常的绑定槽函数

        layout.addWidget(self.button1)
        # 在文本前加图标
        self.button2 = QPushButton('图片按钮')
        self.button2.setIcon(QIcon(QPixmap('../images/python.png'))) # 设置按钮图标
        self.button2.clicked.connect(lambda:self.whichButton(self.button2))

        layout.addWidget(self.button2)

        # 设置不可用按钮
        self.button3 = QPushButton('不可用的按钮')
        self.button3.setEnabled(False)
        layout.addWidget(self.button3)

        self.button4 = QPushButton('&MyButton') # 设置热键
        self.button4.setDefault(True)  # 设置默认按钮  窗口打开后不选择按钮 按回车时会点击默认按钮
        self.button4.clicked.connect(lambda:self.whichButton(self.button4))
        layout.addWidget(self.button4)

        self.setLayout(layout)

    # def whichButton(self):  # 多个信号共用一个槽函数
    #     sender = self.sender()  # 发出信号的对象
    #     print(sender.text()+'被单击')

    def whichButton(self,btn): # 多个信号共用一个槽函数
        print(btn.text()+'被单击')

    def buttonState(self):
        if self.button1.isChecked():  # 按钮按下时为真
            print('按钮1已被选中')
        else:
            print('按钮1未被选中')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QPushButtonDemo()
    main.show()
    sys.exit(app.exec_())