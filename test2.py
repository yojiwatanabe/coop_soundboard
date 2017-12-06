"""
COOP SOUNDS
Yoji Watanabe - Fall 2017

test2.py - Coop Sounds Implementation

Working on:
- Changing background color between sounds
"""



# -*- coding: utf-8 -*-

import sys, math, os, random, glob
from os                 import system
from PyQt5.QtWidgets    import QWidget, QLabel, QPushButton, QApplication, QGridLayout, QVBoxLayout, QHBoxLayout, QInputDialog, QLineEdit
from PyQt5.QtGui        import QFont, QIcon, QPixmap
from PyQt5.QtMultimedia import QSound
from PyQt5.QtCore       import QCoreApplication, QSize, Qt
from PyQt5.QtCore       import QCoreApplication, QSize, Qt


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        window = QVBoxLayout()
        self.setLayout(window)
        self.setWindowTitle('COOP SOUNDS')

        self.initTitle(window)
        self.initSoundGrid(window)

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

        btn1.clicked.connect(lambda: self.changeBackground(btn1))
        btn2.clicked.connect(lambda: self.changeBackground(btn2))
        btn3.clicked.connect(lambda: self.changeBackground(btn3))
        btn4.clicked.connect(lambda: self.changeBackground(btn4))

        btn1.setStyleSheet('background-color:#FFFFFF;color:#000000;')
        btn2.setStyleSheet('background-color:#FFFFFF;color:#000000;')
        btn3.setStyleSheet('background-color:#FFFFFF;color:#000000;')
        btn4.setStyleSheet('background-color:#FFFFFF;color:#000000;')


        window.addLayout(soundGrid)
        self.initOptions(window, soundGrid)

    def initOptions(self, window, soundGrid):
        optionsBox = QHBoxLayout()

        exitButton          = QPushButton('X', self)
        exitButton.setShortcut('Space')
        exitButton.clicked.connect(QCoreApplication.instance().quit)
        
        backingOptions = QHBoxLayout()
        backing = QSound("dependencies/backing.wav")
        startBackingTrack   = QPushButton('Play', self)
        startBackingTrack.setShortcut('a')
        startBackingTrack.clicked.connect(lambda: self.playBacking(backing))
        backingOptions.addWidget(startBackingTrack)

        stopBackingTrack   = QPushButton('Stop', self)
        stopBackingTrack.setShortcut('a')
        stopBackingTrack.clicked.connect(lambda: self.stopBacking(backing))
        backingOptions.addWidget(stopBackingTrack)

        addButtonButton = QPushButton('+', self)
        addButtonButton.setShortcut('+')
        addButtonButton.clicked.connect(lambda: self.addButton(soundGrid))

        optionsBox.addWidget(exitButton)
        optionsBox.addWidget(addButtonButton)
        optionsBox.addLayout(backingOptions)
        window.addLayout(optionsBox)

    def Play(self):
        QSound.play("dependencies/airhorn.wav")

    def Play2(self):
        QSound.play("dependencies/foghorn.wav")

    def Play3(self):
        QSound.play("dependencies/pirate.wav")

    def Play4(self):
        QSound.play("dependencies/ahh.wav")

    def playCustom(self, text):
        os.system("say " + text)
        pass

        # Add a new button to the soundboard
    def addButton(self, soundGrid):
        text, okPressed = QInputDialog.getText(self, "Get text","Word:", QLineEdit.Normal, "")
        newButton       = QPushButton(text)
        temp            = newButton.sizeHint()
        temp.setHeight(temp.width())
        newButton.setIconSize(temp)
        newButton.clicked.connect(lambda: self.playCustom(text))
        newButton.clicked.connect(lambda: self.changeBackground(newButton))
        newButton.setStyleSheet('background-color:#FFFFFF;color:#000000;')
        soundGrid.addWidget(newButton)
        self.setRandomPic(newButton)

        # Change color of background each time 
    def changeBackground(self, button):
        r = lambda: random.randint(0,255)
        randColor = '#%02X%02X%02X' % (r(),r(),r())
        button.setStyleSheet('background-color:' + randColor +';color:#000000;')

    def playBacking(self, backing):
        backing.play()

    def stopBacking(self, backing):
        backing.stop()

    def setRandomPic(self, button):
        files = glob.glob("customImages/*.jpg")
        filename = files[int(math.floor(random.random() * len(files)))]
        button.setIcon(QIcon(filename))
        temp            = button.sizeHint()
        temp.setHeight(temp.width())
        button.setIconSize(temp)

    # def stopBacking(self, *QSound):
        # QSound.stop("dependencies/backing.wav")
        # QSound.stop()


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())