import sys
from PyQt5.QtWidgets    import QWidget, QLabel, QPushButton, QApplication, QGridLayout, QVBoxLayout
from PyQt5.QtGui        import QFont, QIcon, QPixmap
from PyQt5.QtMultimedia import QSound
from PyQt5.QtCore       import QCoreApplication, QSize, Qt


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):
        window   = QVBoxLayout()
        mainGrid = QGridLayout()
        self.setLayout(window)
        self.setWindowTitle('COOP SOUNDS')

        title = QLabel()
        title.setPixmap(QPixmap('title.png'))
        title.setAlignment(Qt.AlignCenter)

        title.setFont(QFont("Futura", 40, QFont.Bold))

        btn = QPushButton('X', self)
        btn.setShortcut('Space')
        btn.resize(30, 30)
        btn.move(10, 10)
        btn.clicked.connect(QCoreApplication.instance().quit)

        btn1 = QPushButton('OOOP', self)
        btn1.setShortcut('Left')
        temp = btn1.sizeHint()
        btn1.resize(temp)
        temp.setHeight(temp.width())
        btn1.setIcon(QIcon('airhorn.jpg'))
        btn1.setIconSize(temp)
        btn1.clicked.connect(self.Play)
        mainGrid.addWidget(btn1, 0, 0)

        btn2 = QPushButton('SOUP', self)
        btn2.setShortcut('Up')
        temp = btn2.sizeHint()
        btn2.resize(temp)
        temp.setHeight(temp.width())
        btn2.setIcon(QIcon('foghorn.jpg'))
        btn2.setIconSize(temp)
        btn2.clicked.connect(self.Play2)
        mainGrid.addWidget(btn2, 0, 1)

        btn3 = QPushButton('FOOP', self)
        btn3.setShortcut('Right')
        temp = btn3.sizeHint()
        btn3.resize(temp)
        temp.setHeight(temp.width())
        btn3.setIcon(QIcon('pirate.jpg'))
        btn3.setIconSize(temp)
        btn3.clicked.connect(self.Play3)
        mainGrid.addWidget(btn3, 1, 0)

        btn4 = QPushButton('GOOP', self)
        btn4.setShortcut('Down')
        temp = btn4.sizeHint()
        temp.setHeight(temp.width())
        btn4.setIcon(QIcon('yell.jpg'))
        btn4.setIconSize(temp)
        btn4.clicked.connect(self.Play4)
        mainGrid.addWidget(btn4, 1, 1)

        window.addWidget(title)
        window.addLayout(mainGrid)
        window.addWidget(btn)

        self.show()

        
    def Play(self):
        QSound.play("airhorn.wav")
        self.changeBackground()

    def Play2(self):
        QSound.play("foghorn.wav")
        self.changeBackground()

    def Play3(self):
        QSound.play("pirate.wav")
        self.changeBackground()

    def Play4(self):
        QSound.play("ahh.wav")
        self.changeBackground()

    def changeBackground(self):
        print 'try'


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())