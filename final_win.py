from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QGroupBox, QRadioButton, QListWidget, QLineEdit
from instr import *



class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.show()
    def results(self):
        self.index = (4*(int(self.exp.t1)+int(self.exp.t2)+int(self.exp.t3))-200/10)
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index<15 and self.index>=11:
                return txt_res2
            elif self.index<11 and self.index>=6:
                return txt_res3
            elif self.index<6 and self.index>=0.5:
                return txt_res4
            elif self.index<=0.4:
                return txt_res5
        
        if self.exp.age==13 or self.exp.age==14:
            if self.index >= 16.5:
                return txt_res1
            elif self.index<16.5 and self.index>=12.5:
                return txt_res2
            elif self.index<12.5 and self.index>=7.5:
                return txt_res3
            elif self.index<7.5 and self.index>=2:
                return txt_res4
            elif self.index<=1.9:
                return txt_res5
        
        if self.exp.age==11 or self.exp.age==12:
            if self.index >= 18:
                return txt_res1
            elif self.index<18 and self.index>=14:
                return txt_res2
            elif self.index<14 and self.index>=9:
                return txt_res3
            elif self.index<9 and self.index>=3.5:
                return txt_res4
            elif self.index<=3.4:
                return txt_res5
        
        if self.exp.age==9 or self.exp.age==10:
            if self.index >= 19.5:
                return txt_res1
            elif self.index<19.5 and self.index>=15.5:
                return txt_res2
            elif self.index<15.5 and self.index>=10.5:
                return txt_res3
            elif self.index<10.5 and self.index>=5:
                return txt_res4
            elif self.index<=4.9:
                return txt_res5
        
        if self.exp.age==7 or self.exp.age==8:
            if self.index >= 21:
                return txt_res1
            elif self.index<21 and self.index>=17:
                return txt_res2
            elif self.index<17 and self.index>=12:
                return txt_res3
            elif self.index<12 and self.index>=6.5:
                return txt_res4
            elif self.index<=6.4:
                return txt_res5
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.line = QVBoxLayout()
        self.work_text = QLabel(txt_workheart + str(self.results()))
        self.index_text = QLabel(txt_index + str(self.index))
        self.line.addWidget(self.index_text, alignment= Qt. AlignCenter)
        self.line.addWidget(self.work_text, alignment= Qt. AlignCenter)
        self.setLayout(self.line)