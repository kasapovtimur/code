from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from victorina2 import *
class FWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.connects()
        self.show()
    def initUI(self):
        self.hello = QLabel('Викторина')
        self.privet = QLabel('Добро пожалывать')
        self.Nachalo = QPushButton('Начать',self)
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.privet, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.Nachalo, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)
    def next_click(self):
        self.tw =TWin()
        self.hide()
    def connects(self):
        self.Nachalo.clicked.connect(self.next_click)
    def set_appear(self):
        win_x,win_y = 200, 100
        win_width,win_height = 1000,600
        self.setWindowTitle('Викторина')
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
app = QApplication([])
mw = FWin()
app.exec()   