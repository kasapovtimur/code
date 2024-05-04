from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from victorina4 import *
class VWin(QWidget):
    def __init__(self,exp):
        super().__init__()
        self.exp = exp
        self.initUI()
        self.set_appear()
        self.connects()
        self.show()
    def initUI(self):
        self.hello2 = QLabel('Второй вопрос')
        self.pravotvet = QLabel('Правильных ответо:'+str(self.exp))
        self.privet3 = QLabel('Что произошло в 1812 году?')
        self.vopros5 = QPushButton('Отечественная война')
        self.vopros6 = QPushButton('Открылась ппервая пятёрочка')
        self.vopros7 = QPushButton('Новый год')
        self.vopros8 = QPushButton('Дворцовый переворот')
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello2, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.pravotvet, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.privet3, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.vopros5, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.vopros6, alignment = Qt.AlignRight)
        self.layout_line.addWidget(self.vopros7, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.vopros8, alignment = Qt.AlignRight)
        self.setLayout(self.layout_line)
    def set_appear(self):
        win_x,win_y = 200, 100
        win_width,win_height = 1000,600
        self.setWindowTitle('hello2')
        self.resize(win_width,win_height)
        self.move(win_x,win_y)