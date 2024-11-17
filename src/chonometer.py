# -*- Mode: Python3; coding: utf-8; indent-tabs-mpythoode: nil; tab-width: 4 -*-

'''
    Simple time counter.
'''

import os
import sys
import time

from PySide6.QtCore    import Qt, QTimer
from PySide6.QtGui     import QFont, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout


class Window(QMainWindow):

    def __init__(self, title: str, width: int, height: int , minutes: int):
        """
        :param title: Title displayed in the window.
        :param width: Window width.
        :param height: Window height.
        :param minutes: Maximum limit in minutes to alert.
        """
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(0, 0, width, height)

        self.label = QLabel(self)
        self.label.setFixedSize(width, int(height * 0.90))
        
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self.seconds   = 0
        self.limit     = minutes * 60
        self.tolerance = 70 / 100

        self.button1 = QPushButton("Start")
        self.button1.setFont(QFont('Arial', 48))
        self.button1.setStyleSheet("background-color : blue; color : white;")
        self.button1.pressed.connect(self.restart)

        self.button2 = QPushButton()
        self.button2.setFixedHeight(10)
        self.button2.setStyleSheet("background-color : blue;")

        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        widget = QWidget(self)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def convert(self, seconds: int) -> str:
        minutes  = seconds // 60
        seconds -= minutes * 60
        return "{:02d} : {:02d}".format(minutes, seconds)

    def restart(self):
        self.seconds = 0
        self.button1.setText("-- : --")            

    def lineargradient(self, color1: QColor, color2: QColor, stop: float = 1):
        stop = 0.000 if stop < 0 else stop
        stop = 0.999 if stop >= 1 else stop        
        return "background: qlineargradient( x1:0 y1:0, x2:{stop} y2:0, stop:{stop} {color1}, stop:1 {color2});".format(
            color1=color1.name(), color2=color2.name(), stop=stop)

    def showTime(self):
        if self.button1.text() == "Start":
            return
        self.seconds += 1
        # Button 1
        color1 = QColor(0, 0, 0)
        color2 = QColor(0, 255, 0)
        if self.seconds > self.limit:
            if self.seconds % 2 == 0:    
                color1 = QColor(255, 0, 0)
        self.button1.setText(self.convert(self.seconds))
        self.button1.setStyleSheet("background-color : {color1}; color : {color2};".format(
            color1=color1.name(), color2=color2.name()))
        # Button 2
        color1 = QColor(54, 115, 50)
        color2 = QColor(255, 0, 0)
        self.button2.setStyleSheet(self.lineargradient(color2, color1, self.seconds / self.limit))

def run(minutes: int):
    if minutes < 0:
        minutes = 1
    app = QApplication()
    w = Window("Timer", 250, 100, minutes)
    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run(1) # test