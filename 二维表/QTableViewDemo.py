'''在通常情况下，一个应用需要和一批数据进行交互，然后以表格的形式输出这些信息，这时就需要用到QTableView类了，
在QTableView中可以使用自定义的数据模型来显示内容，通过setModel来绑定数据源
QTableWidget继承自QTableView，主要区别是QTableView可以使用自定义的数据模型来显示内容（先通setModel来绑定数据源），
而QTableWidget自能使用标准的数据模型，并且其单元格数据是通过QTableWidgetItem对象实现的，通常QTableWidget就能够满足我们的要求
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class MyTable(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('显示二维表')
        self.resize(500,300)
        layout = QVBoxLayout()
        self.model = QStandardItemModel(4,3)  #设置数据结构
        self.model.setHorizontalHeaderLabels(['id','name','age']) # 设置字段名

        self.tableView = QTableView() # 实例化表格视图
        self.tableView.setModel(self.model) #绑定数据源

        # 水平方向标签拓展剩下的窗口部分，填满表格
        # self.tableView.horizontalHeader().setStretchLastSection(True)
        # 水平方向，表格大小拓展到适当的尺寸
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        item11 = QStandardItem('10')
        item12 = QStandardItem('雷神')
        item13 = QStandardItem('2000')

        item31 = QStandardItem('30')
        item32 = QStandardItem('死亡女神')
        item33 = QStandardItem('3000')

        self.model.setItem(0,0,item11) # 设置对应单元格的数据
        self.model.setItem(0,1,item12)
        self.model.setItem(0,2,item13)

        self.model.appendRow([item31,item32,item33]) # 继续添加一行数据

        layout.addWidget(self.tableView)
        self.setLayout(layout)



if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=MyTable()
    main.show()
    sys.exit(app.exec_())