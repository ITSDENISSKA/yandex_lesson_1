from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QGridLayout, QSizePolicy
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sys
from random import randint

from UI import Ui_MainWindow


class MyProgram(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.draw_circle)
        canvas = QPixmap(500, 400)
        canvas.fill(QColor("white"))
        self.lbl.setPixmap(canvas)

    def draw_circle(self):
        x, y = [randint(10, 500) for i in range(2)]
        w = h = randint(10, 100)
        painter = QPainter(self.lbl.pixmap())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        painter.setPen(pen)
        painter.drawEllipse(x, y, w, h)
        painter.end()
        self.update()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyProgram()
    w.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
