# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from instr import *
class FWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.show()
    def initUI(self):
        self.hello_text = QLabel('Индекс Руфье:')
        self.inistruction = QLabel('Работоспособность сердца:')
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.inistruction, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)
    def set_appear(self):
        win_x,win_y = 200, 100
        win_width,win_height = 1000,600
        self.setWindowTitle('txt_title')
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
