from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from victorina3 import *
class TWin(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.set_appear()
        self.show()
        self.connects()
    def initUI(self):
        self.hello1 = QLabel('Первый вопрос')
        self.privet2 = QLabel('Что произошло в 1812 году?')
        self.vopros1 = QPushButton('Отечественная война')
        self.vopros2 = QPushButton('Открылась первая пятёрочка')
        self.vopros3 = QPushButton('Новый год')
        self.vopros4 = QPushButton('Дворцовый переворот')
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello1, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.privet2, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.vopros1, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.vopros2, alignment = Qt.AlignRight)
        self.layout_line.addWidget(self.vopros3, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.vopros4, alignment = Qt.AlignRight)
        self.setLayout(self.layout_line)
    def next_click(self):
        self.tw =SWin(0)
        self.hide()
    def next_click_win(self):
        self.tw =SWin(1)        
        self.hide()
    def connects(self):
        self.vopros1.clicked.connect(self.next_click)
        self.vopros2.clicked.connect(self.next_click)
        self.vopros3.clicked.connect(self.next_click)
        self.vopros4.clicked.connect(self.next_click)    
    def set_appear(self):
        win_x,win_y = 200, 100
        win_width,win_height = 1000,600
        self.setWindowTitle('hello1')
        self.resize(win_width,win_height)
        self.move(win_x,win_y)