'''
QToolBar控件是由文本按钮，图标或其他小控件按钮组成的可移动面板，通常位于菜单栏下方
addAction()	添加具有文本或图标的工具按钮
addSeperator()	分组显示工具按钮
addWidget()	添加工具栏中按钮以外的控件
addToolBar()	使用QMainWindow类的方法添加一个新的工具栏
setMovable()	工具变得可移动
setOrientation()	工具栏的方向可以设置为Qt.Horizontal或Qt.certical
每当单击工具栏中的按钮时，都将发射actionTriggered信号，另外，这个信号将关联的QAction对象的引用发到连接的槽函数上
'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class ToolBarDemo(QMainWindow):
    def __init__(self,parent=None):
        super(ToolBarDemo, self).__init__(parent)
        #设置标题与初始大小
        self.setWindowTitle('toolbar例子')
        self.resize(300,200)

        #垂直布局
        layout = QVBoxLayout()

        #在工具栏区域添加文件工具栏
        tb = self.addToolBar('File')
        #添加图形按钮
        new = QAction(QIcon('images\\new.png'),'new',self)
        tb.addAction(new)
        open = QAction(QIcon('images\open.png'),'open',self)
        tb.addAction(open)
        save = QAction(QIcon('images\save.png'),'save',self)
        tb.addAction(save)

        tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon) # 文本在图标下方
        #图形对象点击触发自定义槽函数
        tb.actionTriggered[QAction].connect(self.toolbtnpressed)

        self.setLayout(layout)

    def toolbtnpressed(self,a):
        #输出，点击地图性按钮
        print('pressed tool button is ',a.text())

if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=ToolBarDemo()
    demo.show()
    sys.exit(app.exec_())
