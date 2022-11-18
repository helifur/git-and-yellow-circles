import random
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget

from UI import Ui_Form

SIZE_SCREEN = [640, 490]


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag = False
        self.go_btn.clicked.connect(self.draw)
        self.coords = []
        self.setWindowTitle('Git и случайные окружности')

    def draw(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.size = random.randint(10, 150)
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)

            qp.setPen(QColor(*self.color))
            qp.setBrush(QColor(*self.color))
            self.x, self.y = random.randint(150, SIZE_SCREEN[0] - 150), random.randint(150, SIZE_SCREEN[1] - 150)
            qp.drawEllipse(self.x, self.y, self.size, self.size)

            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
