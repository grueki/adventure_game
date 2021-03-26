from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QDesktopWidget, QLabel, QMessageBox
from PyQt5.QtGui import QIcon, QFont, QPainter, QColor, QMovie, QKeyEvent
import sys, random
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QPoint, QEasingCurve
import sys, os, resources

clear = lambda: os.system('cls')
clear()
run = True

class MyWindow(QWidget):
    ''' TODO: DYNAMIC RESIZING; SquareHeight VARIABLE -> FUNCTION '''
    squareHeight = 64

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # QToolTip.setFont(QFont('SansSerif', 10))
        # self.setToolTip('Hi there! <b>bold</b>, <i>italics</i> and <u>underline</u>.')
        
        # map_features{1:'assets/tree.gif'}
        self.map_data = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],\
                         [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],\
                         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],\
                         [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1],\
                         [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],\
                         [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],\
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0],\
                         [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],\
                         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],\
                         [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],\
                         [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0],\
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],\
                         [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],\
                         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],\
                         [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1],\
                         [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],\
                         [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],\
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0]]
        
        row_num = 0
        col_num = 0

        for row in self.map_data:
            col_num = 0
            for column in row:
                if self.map_data[row_num][col_num] == 1:
                    self.tree_img = QMovie("assets/tree.gif")
                    self.tree = QLabel(self)
                    self.tree.setMovie(self.tree_img)
                    self.tree_img.start()
                    self.tree_xPos = col_num
                    self.tree_yPos = row_num
                    self.tree.setGeometry(self.tree_xPos*self.squareHeight, self.tree_yPos*self.squareHeight, self.squareHeight, self.squareHeight)
                col_num += 1
            row_num += 1

        self.worldHeight = row_num
        self.worldWidth = col_num

        self.setFixedSize(17*self.squareHeight, 11*self.squareHeight)
        self.center()
        
        self.setStyleSheet("background-color: #b58465;")
        self.setWindowTitle('adventure game')
        self.setWindowIcon(QIcon('icon.png'))

        self.last_move = 'left'
        self.player_img = QMovie("assets/playerleft.gif")
        self.player = QLabel(self)
        self.player.setMovie(self.player_img)
        self.player_img.start()

        self.player_xPos = 8
        self.player_yPos = 5
        self.player.setGeometry(self.player_xPos*self.squareHeight, self.player_yPos*self.squareHeight, self.squareHeight, self.squareHeight)

        ''' 'power up' item (archive) '''
        # self.power_up_img = QMovie("assets/power_up.gif")
        # self.power_up = QLabel(self)
        # self.power_up.setMovie(self.power_up_img)
        # self.power_up_img.start()
        
        # self.power_up_xPos = 5
        # self.power_up_yPos = 8
        # self.power_up.setGeometry(self.power_up_xPos*self.squareHeight, self.power_up_yPos*self.squareHeight, self.squareHeight, self.squareHeight)

        self.show()

    def keyPressEvent(self, e):
        key = e.key()

        #if not QKeyEvent.isAutoRepeat(e): # Prevents auto-pressing by holding down a key
        if key == Qt.Key_Left:
            if self.last_move == 'left' and self.player_xPos-1 >= 0 and self.map_data[self.player_yPos][self.player_xPos-1] == 0:
                self.player_xPos -= 1

            ''' Changes sprite to face relevant direction '''
            self.player_img = QMovie("assets/playerleft.gif")
            self.player.setMovie(self.player_img)
            self.player_img.start()
            self.last_move = 'left'


        elif key == Qt.Key_Right:
            if self.last_move == 'right' and self.player_xPos+1 < self.worldWidth and self.map_data[self.player_yPos][self.player_xPos+1] == 0:
                self.player_xPos += 1

            self.player_img = QMovie("assets/playerright.gif")
            self.player.setMovie(self.player_img)
            self.player_img.start()
            self.last_move = 'right'


        elif key == Qt.Key_Up:
            if self.last_move == 'up' and self.player_yPos-1 >= 0 and self.map_data[self.player_yPos-1][self.player_xPos] == 0:
                self.player_yPos -= 1

            self.player_img = QMovie("assets/playerback.gif")
            self.player.setMovie(self.player_img)
            self.player_img.start()
            self.last_move = 'up'


        elif key == Qt.Key_Down:
            if self.last_move == 'down' and self.player_yPos+1 < self.worldHeight and self.map_data[self.player_yPos+1][self.player_xPos] == 0:
                self.player_yPos += 1

            self.player_img = QMovie("assets/playerfront.gif")
            self.player.setMovie(self.player_img)
            self.player_img.start()
            self.last_move = 'down'

        else:
            ''' handles and ignores all other key presses; prevents crashing '''
            super(MyWindow, self).keyPressEvent(e)
        
        self.anim = QPropertyAnimation(self.player, b"pos")
        self.anim.setEasingCurve(QEasingCurve.InOutQuad)
        self.anim.setEndValue(QPoint(self.player_xPos*self.squareHeight, self.player_yPos*self.squareHeight))
        self.anim.setDuration(200)
        self.anim.start()

        # self.player.move(self.player_xPos*self.squareHeight, self.player_yPos*self.squareHeight)
        self.update()


    ''' center window on screen '''
    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    ''' close window popup '''
    def closeEvent(self, event):

        choice = QMessageBox.question(self, 'Quit', "Are you sure you want to quit? Your progress will not be saved!", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if choice == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

# class LevelWorld(QWidget, level_num):


def main():

    app = QApplication(sys.argv) #Creates application object - necessary
    mW = MyWindow() #Base class of all UI in PyQt. This is the default constructor, aka a window
    sys.exit(app.exec_()) #When exited, ensures a clean exit and informs environment how application ended.



while run:
    main()
