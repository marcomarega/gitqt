import sys
from random import randrange
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget

from UI import Ui_Form


class Widget(QWidget, Ui_Form):
    def __init__(self):
        super(Widget, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.update)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        color = QColor(randrange(0, 256), randrange(0, 256), randrange(0, 256))
        qp.setPen(color)
        qp.setBrush(color)
        diameter = randrange(3, min(self.size().width(), self.size().height()) // 2)
        x_coord = randrange(0, self.size().width() - diameter)
        y_coord = randrange(0, self.size().height() - diameter)
        qp.drawEllipse(x_coord, y_coord, diameter, diameter)

        qp.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wid = Widget()
    wid.show()
    sys.exit(app.exec())
