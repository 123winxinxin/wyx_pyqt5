'''定义输入掩码的字符
下表列出了输入掩码的占位符和字面字符，并说明其如何控制数据输入

A	ASCII字母字符是必须输入的（A-Z，a-z）
a	ASCII字母字符是允许输入的，但不是必须输入的
N	ASCII字母字符是必须输入的（A-Z，a-z，0-9）
n	ASCII字母字符是允许输入的，但不是必须输入的
X	任何字符都是必须输入
x	任何字符都是允许输入的，但不是必须输入的
9	ASCII数字字符是必须输入的（0-9）
0	ASCII数字字符是允许输入的，但不是必须输入的
D	ASCII数字字符是必须输入的（1-9）
d	ASCII数字字符是允许输入的，但不是必须的（1-9）
#	ASCII数字字符与加减字符是允许输入的，但不是必须的
H	十六进制格式字符是必须输入的（A-F，a-f，0-9）
h	十六进制格式字符允许输入，但不是必须的
B	二进制格式字符是必须输入的（0,1）
b	二进制格式字符是允许输入的，但不是必须的
>	所有字母字符都大写
<	所有字母字符都小写
！	关闭大小写转换
\	使用‘\’转义上面列出的字符
掩码由掩码字符与分隔符字符串组成，后面可以跟一个分号和空白字符，空白字符在编辑后会从文本删除的
掩码示例如下：

掩码	注意事项
000.000.000.000;_	ip地址，空白字符是‘_’
HH:HH:HH:HH:HH:HH;	MAC地址
0000-00-00	日期，空白字符是空格
>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#	许可证号，空白字符是‘_’，所有字母都转换为大写
'''


import sys
from PyQt5.QtWidgets import *

class QLineEditMask(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('使用掩码来限制文本输入框的字符')
        formLayout = QFormLayout()

        #初始化几个文本输入框
        ipLineEdit = QLineEdit()
        macLineEdit = QLineEdit()
        dateLineEdit = QLineEdit()
        licenseLineEdit = QLineEdit()

        # 设置掩码格式，分号后面是不输入时显示的字符
        ipLineEdit.setInputMask("000:000:000:000;_")
        macLineEdit.setInputMask(">HH-HH-HH-HH-HH-HH;_")
        dateLineEdit.setInputMask("0000/00/00")
        licenseLineEdit.setInputMask(">AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#")

        # 添加控件到布局
        formLayout.addRow('ip:',ipLineEdit)
        formLayout.addRow('mac地址:',macLineEdit)
        formLayout.addRow('date:',dateLineEdit)
        formLayout.addRow('license:',licenseLineEdit)

        self.setLayout(formLayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QLineEditMask()
    main.show()
    sys.exit(app.exec_())
