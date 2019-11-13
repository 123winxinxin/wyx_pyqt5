'''
QTableWidget是Qt程序中常用的显示数据表格的控件，类似于c#中的DataGrid。QTableWidget是QTableView的子类，它使用标准的数据模型，并且其单元数据是通过QTableWidgetItem对象来实现的，使用QTableWidget时就需要QTableWidgetItem。
用来表示表格中的一个单元格，整个表格就是用各个单元格构建起来的

QTableWidget类中的常用方法
setROwCount(int row)	设置QTableWidget表格控件的行数
setColumnCount(int col)	设置QTableWidget表格控件的列数
setHorizontalHeaderLabels()	设置QTableWidget表格控件的水平标签
setVerticalHeaderLabels()	设置QTableWidget表格控件的垂直标签
setItem(int ,int ,QTableWidgetItem)	在QTableWidget表格控件的每个选项的单元控件内添加控件
horizontalHeader()	获得QTableWidget表格控件的表格头，以便执行隐藏
rowCount()	获得QTableWidget表格控件的行数
columnCount()	获得QTableWidget表格控件的列数
setEditTriggers(EditTriggers triggers)	设置表格是否可以编辑，设置表格的枚举值
                QAbstractItemView.NoEditTriggers	不能对表格内容进行修改
                QAbstractItemView.CurrentChanged	1	任何时候都能对单元格进行修改
                QAbstractItemView.DoubleClicked	2	双击单元格
                QAbstractItemView.SelectedClicked	4	单击已经选中的内容
                QAbstractItemView.EditKeyPressed	8	当修改键按下时修改单元格
                QAbstractItemView.AnyKeyPressed	16	按任意键修改单元格
                QAbstractItemView.AllEditTriggers	31	包括以上所有条件

setSelectionBehavior	设置表格的选择行为
            QAbstractItemView.SelectItems  0	选中单个单元格
            QAbstractItemView.SelectRows	1	选中一行
            QAbstractItemView.SelectColumns	2	选中一列

setTextAlignment()	设置单元格内文本的对齐方式
        Qt.AlignLeft	将单元格内的内容沿单元格的左边缘对齐
        Qt.AlignRight	将单元格内的内容沿单元格的右边缘对齐
        Qt.AlignHCenter	在可用空间中，居中显示在水平方向上
        Qt.AlignJustify	将文本在可用空间内对齐，默认从左到右
        Qt.AlignTop	与顶部对齐
        Qt.AlignBottom	与底部对齐
        Qt.AlignVCenter	在可用空间中，居中显示在垂直方向上
        Qt.AlignBaseline	与基线对齐
如果要设置水平和垂直方向对齐方式，比如在表格空间内上下，左右居中对齐，那么只要使用Qt,AlignHCenter和Qt,AlignVCenter即可

setSpan(int row,int column,int rowSpanCount,int columnSpanCount)合并单元格，要改变单元格的第row行，
                                                                column列，要合并rowSpancount行数和columnSpanCount列数
                                                                row：要改变的行数
                                                                column：要改变的列数
                                                                rowSpanCount：需要合并的行数
                                                                columnSpanCount：需要合并的列数
setShowGrid()	在默认情况下表格的显示是有网格的，可以设置True或False用于是否显示，默认True
setColumnWidth(int column,int width)	设置单元格行的宽度
setRowHeight(int row,int height)	设置单元格列的高度


'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class TableWidgetDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTableWidget演示')

        self.resize(430,270)
        layout = QHBoxLayout()
        self.tableWidget = QTableWidget(4,3)
        # TableWidget = QTableWidget()
        # TableWidget.setRowCount(4)
        # TableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['姓名','性别', '得分'])

        # 设置垂直方向的表头标签
        # TableWidget.setVerticalHeaderLabels(['行1', '行2', '行3', '行4'])

        #  设置水平方向表格为自适应的伸缩模式
        # TableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        nameItem = QTableWidgetItem('小明')
        self.tableWidget.setItem(0,0,nameItem)

        # ageItem = QTableWidgetItem('男')
        # self.tableWidget.setItem(0,1, ageItem)
        #
        # scoreItem = QTableWidgetItem('86')
        # self.tableWidget.setItem(0,2, scoreItem)

        layout.addWidget(self.tableWidget)

        #禁止编辑
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        #整行选择
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        #调整行和列边框
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

        #表格头的显示与隐藏
        # self.tableWidget.horizontalHeader().setVisible(False)
        # self.tableWidget.verticalHeader().setVisible(False)

        # 在单元格内放置控件
        comBox = QComboBox()
        comBox.addItems(['男','女'])
        comBox.addItem('未知')
        comBox.setStyleSheet('QComboBox{margin:3px}')  # QSS 设置Qt样式 此处为设置所有下拉框的样式为 距单元格边距3px
        self.tableWidget.setCellWidget(0,1,comBox)  # 将控件放置到单元格中

        modifyBtn=QPushButton('修改')
        modifyBtn.setDown(True)  # 设置为按下状态
        modifyBtn.setStyleSheet('QPushButton{margin:3px}')
        self.tableWidget.setCellWidget(0,2,modifyBtn)


        self.setLayout(layout)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TableWidgetDemo()
    main.show()
    sys.exit(app.exec_())