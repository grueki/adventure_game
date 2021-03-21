from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QDesktopWidget, QLabel
from PyQt5.QtGui import QIcon, QFont, QPainter, QColor, QPixmap
import sys, random
from PyQt5.QtCore import Qt, QBasicTimer

class MyWindow(QWidget):
    x = 0
    y = 0
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # QToolTip.setFont(QFont('SansSerif', 10))
        # self.setToolTip('Hi there! <b>bold</b>, <i>italics</i> and <u>underline</u>.')
        
        self.setFixedSize(1038, 700)
        self.center()
        
        self.setWindowTitle('adventure game')

        self.posX = 100
        self.posY = 100
        self.facing = 'left'

        self.im = QPixmap("./assets/playerleft_1.png")
        self.label = QLabel()
        self.label.setPixmap(self.im)
        self.grid = QGridLayout()
        self.grid.addWidget(self.label,1,1)
        self.setLayout(self.grid)

        self.show()

    def keyPressEvent(self, e):
        key = e.key()

        if key == Qt.Key_Left:
            self.posX -= 1
            self.facing = 'left'

        elif key == Qt.Key_Right:
            self.posX += 1
            self.facing = 'right'

        elif key == Qt.Key_Up:
            self.posY -= 1
            self.facing = 'up'

        elif key == Qt.Key_Down:
            self.posY += 1
            self.facing = 'down'

        else:
            super(MyWindow, self).keyPressEvent(e)
        
        self.update()
        

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    ''' draw placeholder smiley face player sprite '''
    # def paintEvent(self, e):
    #     qp = QPainter()
    #     qp.begin(self)

    #     qp.setBrush(QColor(255, 255, 0))
    #     qp.drawEllipse(self.posX, self.posY, 60, 60)

    #     qp.setBrush(QColor(0, 0, 0))

    #     if self.facing == 'left':
    #         # qp.drawRect(self.posX+15, self.posY+20, 4, 4)
    #         # qp.drawRect(self.posX+30, self.posY+20, 4, 4)
    #         # qp.drawRect(self.posX+15, self.posY+35, 19, 4)
    #     if self.facing == 'right':
    #         qp.drawRect(self.posX+25, self.posY+20, 4, 4)
    #         qp.drawRect(self.posX+40, self.posY+20, 4, 4)
    #         qp.drawRect(self.posX+25, self.posY+35, 19, 4)            
    #     if self.facing == 'up':
    #         qp.drawRect(self.posX+20, self.posY+10, 4, 4)
    #         qp.drawRect(self.posX+35, self.posY+10, 4, 4)
    #         qp.drawRect(self.posX+20, self.posY+25, 19, 4) 
    #     if self.facing == 'down':
    #         qp.drawRect(self.posX+20, self.posY+30, 4, 4)
    #         qp.drawRect(self.posX+35, self.posY+30, 4, 4)
    #         qp.drawRect(self.posX+20, self.posY+45, 19, 4)         
    #     qp.end()

    ''' close window popup '''
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


