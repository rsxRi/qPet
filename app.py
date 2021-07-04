# from util.Interaction import Interaction
# from util.Pet import Pet
from ui.ui_qPetMain import Ui_qPet
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class MainUi(Ui_qPet, QtWidgets.QMainWindow):
    def __init__(self, MainUi):
        super().__init__()

        self.setupUi(MainUi)

    def setupUi(self, MainUi):
        super().setupUi(MainUi)

        self.mainDisplay = MainDisplay(self.mainDisplay)
        self.mainDisplay.setFixedSize(400, 300)
        self.mainDisplay.show()
        # self.setCentralWidget(self.painterDisplay)
        # self.feedButton.clicked.connect(self.paintEvent)


class MainDisplay(QtWidgets.QWidget):
    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setPen(QtGui.QColor(200, 0, 0))
        painter.drawText(40, 30, "Text at fixed coordinates")
        painter.drawText(event.rect(), QtCore.Qt.AlignCenter, "Text centered in the drawing area")
        painter.end()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
