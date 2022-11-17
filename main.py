import sys
import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.draw)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        radius = random.randint(30, 500)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(10, 10, radius, radius)
        qp.end()

    def draw(self):
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())