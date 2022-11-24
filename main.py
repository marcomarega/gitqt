import sys
import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        uic.loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.update)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        qp.setPen(QColor(200, 200, 0))
        qp.setBrush(QColor(200, 200, 0))
        diameter = random.randrange(3, min(self.size().width(), self.size().height()) // 2)
        x_coord = random.randrange(0, self.size().width() - diameter)
        y_coord = random.randrange(0, self.size().height() - diameter)
        qp.drawEllipse(x_coord, y_coord, diameter, diameter)

        qp.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wid = Widget()
    wid.show()
    sys.exit(app.exec())
