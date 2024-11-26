import sys
from random import randint
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QPainter, QColor
from PyQt6 import QtCore, QtWidgets


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.resize(747, 600)
        MainWindow.setWindowTitle("MainWindow")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 430, 181, 81))
        self.pushButton.setText("PushButton")
        self.pushButton.clicked.connect(self.printshar)

        MainWindow.setCentralWidget(self.centralwidget)

    def printshar(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            size = randint(20, 200)
            qp.setPen(QColor(255, 255, 0))
            qp.drawEllipse(QtCore.QPointF(randint(100, 500), randint(200, 320)), size, size)
            qp.drawEllipse(QtCore.QPointF(randint(100, 500), randint(200, 280)), size, size)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())