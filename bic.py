from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGroupBox,
    QRadioButton,
    QPushButton,
    QLineEdit,
    QLabel)
from PyQt5 import QtGui
import pywinstyles

stfb = """
    QPushButton {
        color:white;
        border-color: white;
        border-radius: 5px;
        border-width:1px;
        padding:10 px;
        border-style: outset;
        font-weight: 600;
        font-size: 30px;
    }
    QPushButton:hover {
        color:white;
        border: 1px solid white;
        font-weight: 700;
        
    }
    QPushButton:focus {
        color:gray;
        border: 1px solid gray;
        border-color: gray;
    }
    """



app = QApplication([])
window = QWidget()
window.setWindowTitle('Перевод')

window.setStyleSheet("background:black;")
layout = QVBoxLayout()
lable = QLabel("")
window.setWindowIcon(QtGui.QIcon('негр.jpg'))
pywinstyles.apply_style(window, 'dark')
layout3 = QVBoxLayout()
layout4 = QHBoxLayout()
layout2 = QHBoxLayout()
layout5 = QVBoxLayout()
t11 = 0
t12 = 0
def rub(t11):
    t11 = int(t1.text())
    res = t11 / 100
    lable.setText(str(res))
    lable.setStyleSheet("color: white;font-size:32px;")
def dol(t12):
    t12= int(t2.text())
    res2 = t12 * 100
    lable.setText(str(res2))
    lable.setStyleSheet("color: white;font-size:32px;")



t1 = QLineEdit()
layout.addWidget(t1)
t1.setPlaceholderText('Введите рубли')
t1.setStyleSheet('color:white;border-color: white;border-radius: 5px;border-width:1px;padding:10 px;border-style: outset;font-weight: 600;font-size: 30px;')

t2 = QLineEdit()
layout.addWidget(t2)
t2.setPlaceholderText('Введите  долары')
t2.setStyleSheet('color:white;border-color: white;border-radius: 5px;border-width:1px;padding:10 px;border-style: outset;font-weight: 600;font-size: 30px;')

t3 = QPushButton("перевести в доллары")
layout3.addWidget(t3)
t3.setStyleSheet(stfb)
t3.clicked.connect(lambda: rub(t11))

t4 = QPushButton("перевести в рубли")
layout3.addWidget(t4)
t4.setStyleSheet(stfb)
t4.clicked.connect(lambda: dol(t12))










layout4.addWidget(lable)

layout2.addLayout(layout)
layout2.addLayout(layout3)

layout5.addLayout(layout2)
layout5.addLayout(layout4)
window.setLayout(layout5)

window.show()
window.resize(700,200)
app.exec_()
