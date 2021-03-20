from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont, QPainter, QColor
import sys, random
from PyQt5.QtCore import Qt

class MyWindow(QWidget):
    x = 0
    y = 0
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # QToolTip.setFont(QFont('SansSerif', 10))
        # self.setToolTip('Hi there! <b>bold</b>, <i>italics</i> and <u>underline</u>.')
        
        self.resize(1000, 700)
        self.center()
        
        grid = QGridLayout()
        self.setLayout(grid)
        self.setWindowTitle('fuck you')

        self.posX = 100
        self.posY = 100

        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)

        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(self.posX, self.posY, 60, 60)

        qp.setBrush(QColor(0, 0, 0))
        qp.drawRect(self.posX+15, self.posY+20, 4, 4)
        qp.drawRect(self.posX+30, self.posY+20, 4, 4)
        qp.drawRect(self.posX+15, self.posY+35, 19, 4)
        
        qp.end()

    def keyPressEvent(self, e):
        key = e.key()

        if key == Qt.Key_Left:
            self.posX -= 60

        elif key == Qt.Key_Right:
            self.posX += 60

        elif key == Qt.Key_Up:
            self.posY -= 60

        elif key == Qt.Key_Down:
            self.posY += 60

        else:
            super(MyWindow, self).keyPressEvent(e)
        
        self.update()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    # def closeEvent(self, event):

    #     choice = QMessageBox.question(self, 'Quit', "Are you sure you want to quit? Your progress will not be saved!", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

    #     if choice == QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()

def main():

    app = QApplication(sys.argv) #Creates application object - necessary
    mW = MyWindow() #Base class of all UI in PyQt. This is the default constructor, aka a window
    sys.exit(app.exec_()) #When exited, ensures a clean exit and informs environment how application ended.


