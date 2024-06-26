# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from instr import *
class FWin(QWidget):
    def __init__(self,exp):
        super().__init__()
        self.exp = exp
        self.initUI()
        self.set_appear()
        self.show()
    def results(self):
        if self.exp.LETLINE < 7:
            self.index = 0
            return "нет данных для такого возраста"
        self.index = (4 * (int(self.exp.SPINALINE) + int(self.exp.FINISH1) + int(self.exp.FINISH2)) - 200) / 10
        if self.exp.LETLINE == 7 or self.exp.LETLINE == 8:
            if self.index >= 21:
                return txt_res1
            elif self.index < 21 and self.index >= 17: 
                return txt_res2
            elif self.index < 17 and self.index >= 12:
                return txt_res3
            elif self.index < 12 and self.index >= 6.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.LETLINE == 9 or self.exp.LETLINE == 10:
            if self.index >= 19.5:
                return txt_res1
            elif self.index < 19.5 and self.index >= 15.5:
                return txt_res2
            elif self.index < 15.5 and self.index >= 10.5:
                return txt_res3
            elif self.index < 10.5 and self.index >= 5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.LETLINE == 11 or self.exp.LETLINE == 12:
            if self.index >= 18:
                return txt_res1
            elif self.index < 18 and self.index >= 14:
                return txt_res2
            elif self.index < 14 and self.index >= 9:
                return txt_res3
            elif self.index < 9 and self.index >= 3.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.LETLINE == 13 or self.exp.LETLINE == 14:
            if self.index >= 16.5:
                return txt_res1
            elif self.index < 16.5 and self.index >= 12.5:
                return txt_res2
            elif self.index < 12.5 and self.index >= 7.5:
                return txt_res3
            elif self.index < 7.5 and self.index >= 2:
                return txt_res4
            else:
                return txt_res5
        if self.exp.LETLINE >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index < 15 and self.index >= 11:
                return txt_res2
            elif self.index < 11 and self.index >= 6:
                return txt_res3
            elif self.index < 6 and self.index >= 0.5:
                return txt_res4
            else:
                return txt_res5
    def initUI(self):
        self.hello_text = QLabel(txt_workheart + self.results())
        self.inistruction = QLabel(txt_index + str(self.index))
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
