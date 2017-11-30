import sys
from PyQt5.QtWidgets    import QWidget, QLabel, QPushButton, QApplication, QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui        import QFont, QIcon, QPixmap
from PyQt5.QtMultimedia import QSound
from PyQt5.QtCore       import QCoreApplication, QSize, Qt


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):
        window   = QVBoxLayout()

        self.setLayout(window)
        self.setWindowTitle('COOP SOUNDS')
        self.initTitle(window)
        self.initSoundGrid(window)
        self.initOptions(window)

        self.show()

    def initTitle(self, window):
        titleImage  = QPixmap('dependencies/title.png')
        title       = QLabel()
        title.setPixmap(titleImage.scaledToWidth(800))
        title.setAlignment(Qt.AlignCenter)
        window.addWidget(title)


    def initSoundGrid(self, window):
        soundGrid   = QGridLayout()

        btn1    = QPushButton('OOOP', self)
        temp    = btn1.sizeHint()
        btn1.setShortcut('Left')
        btn1.resize(temp)
        temp.setHeight(temp.width())
        btn1.setIcon(QIcon('dependencies/airhorn.jpg'))
        btn1.setIconSize(temp)
        btn1.clicked.connect(self.Play)
        soundGrid.addWidget(btn1, 0, 0)

        btn2    = QPushButton('SOUP', self)
        temp    = btn2.sizeHint()
        btn2.setShortcut('Up')
        btn2.resize(temp)
        temp.setHeight(temp.width())
        btn2.setIcon(QIcon('dependencies/foghorn.jpg'))
        btn2.setIconSize(temp)
        btn2.clicked.connect(self.Play2)
        soundGrid.addWidget(btn2, 0, 1)

        btn3    = QPushButton('FOOP', self)
        temp    = btn3.sizeHint()
        btn3.setShortcut('Right')
        btn3.resize(temp)
        temp.setHeight(temp.width())
        btn3.setIcon(QIcon('dependencies/pirate.jpg'))
        btn3.setIconSize(temp)
        btn3.clicked.connect(self.Play3)
        soundGrid.addWidget(btn3, 1, 0)

        btn4    = QPushButton('GOOP', self)
        temp    = btn4.sizeHint()
        btn4.setShortcut('Down')
        temp.setHeight(temp.width())
        btn4.setIcon(QIcon('dependencies/yell.jpg'))
        btn4.setIconSize(temp)
        btn4.clicked.connect(self.Play4)
        soundGrid.addWidget(btn4, 1, 1)

        window.addLayout(soundGrid)

    def initOptions(self, window):
        optionsBox = QHBoxLayout()

        exitButton = QPushButton('X', self)
        exitButton.setShortcut('Space')
        exitButton.clicked.connect(QCoreApplication.instance().quit)

        optionsBox.addWidget(exitButton)
        window.addLayout(optionsBox)

    def Play(self):
        QSound.play("dependencies/airhorn.wav")
        self.changeBackground()

    def Play2(self):
        QSound.play("dependencies/foghorn.wav")
        self.changeBackground()

    def Play3(self):
        QSound.play("dependencies/pirate.wav")
        self.changeBackground()

    def Play4(self):
        QSound.play("dependencies/ahh.wav")
        self.changeBackground()

    def changeBackground(self):
        print 'try'


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())