# напиши здесь код для хранения текстовых инструкций для приложения
from PyQt5.QtCore import Qt, QTimer , QTime , QLocale
from PyQt5.QtGui import QDoubleValidator,QIntValidator,QFont
# напиши здесь код основного приложения и первого экран
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from final_win import *
from instr import *
class HhghgWin():
    def __init__(self,FIOLINE,LETLINE,SPINALINE,FINISH1,FINISH2):
        self.FIOLINE = FIOLINE
        self.LETLINE = LETLINE
        self.SPINALINE = SPINALINE
        self.FINISH1 = FINISH1
        self.FINISH2 = FINISH2
class TextWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    def initUI(self):
        self.btn_next = QPushButton('Отправить результаты',self)
        self.text_timer = QLabel(txt_timer)
        self.text_timer.setFont(QFont("Times",20,QFont.Bold))
        self.loc = QLocale(QLocale.English,QLocale.UnitedStates)
        self.validator = QDoubleValidator()
        self.validator.setLocale(self.loc)
        self.text_timer = QLabel(txt_timer)
        self.text_timer.setFont(QFont("Times",20,QFont.Bold))
        self.loc = QLocale(QLocale.English,QLocale.UnitedStates)
        self.validator = QDoubleValidator()
        self.validator.setLocale(self.loc)
        self.text_timer = QLabel(txt_timer)
        self.text_timer.setFont(QFont("Times",20,QFont.Bold))
        self.loc = QLocale(QLocale.English,QLocale.UnitedStates)
        self.validator = QDoubleValidator()
        self.validator.setLocale(self.loc)
        self.FIO = QLabel('Введите Ф.И.О.:')
        self.FIOLINE = QLineEdit('Ф.И.О.')
        self.LET = QLabel('Полных лет:')
        self.LETLINE = QLineEdit('0')
        self.LETLINE.setValidator(self.validator)
        self.LETLINE.setValidator(QIntValidator(7,200))
        self.SPINA = QLabel('Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер.\nРезультат запишите в соответствующее поле.')
        self.okoloSPINA = QPushButton('Начать первый тест')
        self.SPINALINE = QLineEdit('0')
        self.SPINALINE.setValidator(self.validator)
        self.SPINALINE.setValidator(QIntValidator (7,200))
        self.PRIS = QLabel('Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания",\nчтобы запустить счётчик приседаний.')
        self.okoloPRIS = QPushButton('Начать делать приседания')
        self.MNOGO = QLabel('Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд.\nНажмите кнопку "Начать финальный тест", чтобы запустить таймер.\nЗелёным обозначены секунды, в течение которых необходимо \nпроводить измерения, черным - секунды без замера пульсаций. Результаты запишите в соответствующие поля.')
        self.FINISH = QPushButton('Начать финальный тест')
        self.FINISH1 = QLineEdit('0')
        self.FINISH1.setValidator(self.validator)
        self.FINISH1.setValidator(QIntValidator (7,200))
        self.FINISH2 = QLineEdit('0')
        self.FINISH2.setValidator(self.validator)
        self.FINISH2.setValidator(QIntValidator (7,200))
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.text_timer, alignment = Qt.AlignRight)
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
    def timer_test1(self):
        global time
        time = QTime(0,0,15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 20, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer_test2(self):
        global time
        time = QTime(0,0,45)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1000)
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 20, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer_test3(self):
        global time
        time = QTime(0,1,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss")[6:8]) >=45:
            self.text_timer.setStyleSheet("color: rgb(9, 219, 65)")
        elif int(time.toString("hh:mm:ss")[6:8]) <=15:
            self.text_timer.setStyleSheet("color: rgb(9, 219, 65)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0, 0, 0)")
        self.text_timer.setFont(QFont("Times", 20, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def next_click(self):
        self.ok=HhghgWin(self.FIOLINE.text,int(self.LETLINE.text()),self.SPINALINE.text,self.FINISH1.text,self.FINISH2.text)
        self.tw = FWin(self.ok)
        self.hide()
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        self.okoloSPINA.clicked.connect(self.timer_test1)
        self.okoloPRIS.clicked.connect(self.timer_test2)
        self.FINISH.clicked.connect(self.timer_test3)
    def set_appear(self):
        win_x,win_y = 200, 100
        win_width,win_height = 1000,600
        self.setWindowTitle('txt_title')
        self.resize(win_width,win_height)
        self.move(win_x,win_y)

