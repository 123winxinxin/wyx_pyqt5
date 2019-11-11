'''
QlistView类用于展示数据，它的子类是QListWIdget。QListView是基于模型（Model）的，需要程序来建立模型，然后再保存数据
QListWidget是一个升级版本的QListView，它已经建立了一个数据储存模型（QListWidgetItem），直接调用addItem（）函数，就可以添加条目（Item）

QListView类中常用的方法如表
setModel()	用来设置View所关联的Model，可以使用Python原生的list作为数据源Model
selectedItem()	选中Model的条目
isSelected()	判断Model中的某条目是否被选中

QListView的常用信号
clicked	当单击某项时，信号被发射
doubleClicked	当双击某项时，信号被发射

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class ListViewDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('单列数据')
        self.resize(300,270)

        layout = QVBoxLayout()
        self.listView = QListView()
        self.listModel = QStringListModel()
        self.list = ['列表项1','列表项2','列表项3']
        self.listModel.setStringList(self.list)
        self.listView.setModel(self.listModel)
        self.label = QLabel('默认值')

        self.listView.clicked.connect(self.onClicked)
        # self.listView.doubleClicked.connect(self.onDoubleClicked)
        layout.addWidget(self.listView)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def onClicked(self,item):
        QMessageBox.information(self,'单列数据','你选择了' + self.list[item.row()])
    #
    # def onDoubleClicked(self,item):
    #     self.label.setText(self.list[item.row()])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ListViewDemo()
    main.show()
    sys.exit(app.exec_())