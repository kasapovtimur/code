# напиши здесь код для хранения текстовых инструкций для приложения
# напиши здесь код основного приложения и первого экран
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
class TextWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    def initUI(self):
        self.btn_next = QPushButton('txt_next',self)
        self.FIO = QLabel('FIO')
        self.FIOLINE = QLineEdit('FIO')
        self.LET = QLabel('LET')
        self.LETLINE = QLineEdit('LET')
        self.SPINA = QLabel('SPINA')
        self.SPINALINE = QLineEdit('SPINA')
        self.PRIS = QLabel('PRIS')
        self.PRISLINE = QLineEdit('PRIS')
        self.inistruction = QLabel('txt_instruction')
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.FIO, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.FIOLINE, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.LET, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.LETLINE, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.SPINA, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.SPINALINE, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.PRIS, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.PRISLINE, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.inistruction, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)
    def next_click(self):
        self.tw = TestWin()
        self.hide()
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    def set_appear(self):
        win_x,win_y = 200, 100
        win_width,win_height = 1000,600
        self.setWindowTitle('txt_title')
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
app = QApplication([])
mw = TextWin()
app.exec()    