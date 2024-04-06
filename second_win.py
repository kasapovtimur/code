# напиши здесь код для хранения текстовых инструкций для приложения
# напиши здесь код основного приложения и первого экран
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from final_win import *
from instr import *
class TextWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    def initUI(self):
        self.btn_next = QPushButton('Отправить результаты',self)
        self.TIME = QLabel('00:00:15')
        self.FIO = QLabel('Введите Ф.И.О.:')
        self.FIOLINE = QLineEdit('Ф.И.О.')
        self.LET = QLabel('Полных лет:')
        self.LETLINE = QLineEdit('0')
        self.SPINA = QLabel('Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер.\nРезультат запишите в соответствующее поле.')
        self.okoloSPINA = QPushButton('Начать первый тест')
        self.SPINALINE = QLineEdit('0')
        self.PRIS = QLabel('Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания",\nчтобы запустить счётчик приседаний.')
        self.okoloPRIS = QPushButton('Начать делать приседания')
        self.MNOGO = QLabel('Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд.\nНажмите кнопку "Начать финальный тест", чтобы запустить таймер.\nЗелёным обозначены секунды, в течение которых необходимо \nпроводить измерения, черным - секунды без замера пульсаций. Результаты запишите в соответствующие поля.')
        self.FINISH = QPushButton('Начать финальный тест')
        self.FINISH1 = QLineEdit('0')
        self.FINISH2 = QLineEdit('0')
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.TIME, alignment = Qt.AlignRight)
        self.layout_line.addWidget(self.FIO, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.FIOLINE, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.LET, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.LETLINE, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.SPINA, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.okoloSPINA, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.SPINALINE, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.PRIS, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.okoloPRIS, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.MNOGO, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.FINISH, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.FINISH1, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.FINISH2, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)
    def next_click(self):
        self.tw = FWin()
        self.hide()
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    def set_appear(self):
        win_x,win_y = 200, 100
        win_width,win_height = 1000,600
        self.setWindowTitle('txt_title')
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
        
