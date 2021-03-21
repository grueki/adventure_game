from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QDesktopWidget, QLabel
from PyQt5.QtGui import QIcon, QFont, QPainter, QColor, QMovie, QKeyEvent
import sys, random
from PyQt5.QtCore import Qt, QTimer
import sys, os, resources

clear = lambda: os.system('cls')
clear()
run = True

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

        self.player_img = QMovie("assets/playerleft.gif")
        self.player = QLabel(self)
        self.player.setMovie(self.player_img)
        self.player_img.start()

        self.player_xPos = 300
        self.player_yPos = 300
        self.player.setGeometry(self.player_xPos, self.player_yPos, 64, 64)

        ''' 'power up' item '''
        # self.power_up_img = QMovie("assets/power_up.gif")
        # self.power_up = QLabel(self)
        # self.power_up.setMovie(self.power_up_img)
        # self.power_up_img.start()
        #
        # self.power_up_xPos = 600
        # self.power_up_yPos = 300
        # self.power_up.setGeometry(self.power_up_xPos, self.power_up_yPos, 32, 32)

        self.show()

    def keyPressEvent(self, e):
        key = e.key()

        if not QKeyEvent.isAutoRepeat(e):
            if key == Qt.Key_Left:
                self.player_xPos -= 32
                self.player_img = QMovie("assets/playerleft.gif")
                self.player.setMovie(self.player_img)
                self.player_img.start()

            elif key == Qt.Key_Right:
                self.player_xPos += 32
                self.player_img = QMovie("assets/playerright.gif")
                self.player.setMovie(self.player_img)
                self.player_img.start()

            elif key == Qt.Key_Up:
                self.player_yPos -= 32
                self.player_img = QMovie("assets/playerback.gif")
                self.player.setMovie(self.player_img)
                self.player_img.start()

            elif key == Qt.Key_Down:
                self.player_yPos += 32
                self.player_img = QMovie("assets/playerfront.gif")
                self.player.setMovie(self.player_img)
                self.player_img.start()

            else:
                super(MyWindow, self).keyPressEvent(e)

        ''' for smiley face placeholder '''
        # if key == Qt.Key_Left:
        #     self.posX -= 20
        #     self.facing = 'left'

        # elif key == Qt.Key_Right:
        #     self.posX += 20
        #     self.facing = 'right'

        # elif key == Qt.Key_Up:
        #     self.posY -= 20
        #     self.facing = 'up'

        # elif key == Qt.Key_Down:
        #     self.posY += 20
        #     self.facing = 'down'

        # else:
        #     super(MyWindow, self).keyPressEvent(e)
        
        self.player.move(self.player_xPos, self.player_yPos)
        self.update()

    ''' center window on screen '''
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
    #         qp.drawRect(self.posX+15, self.posY+20, 4, 4)
    #         qp.drawRect(self.posX+30, self.posY+20, 4, 4)
    #         qp.drawRect(self.posX+15, self.posY+35, 19, 4)
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



while run:
    main()
