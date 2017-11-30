#!/usr/bin/python3

import sys
from PyQt5.QtWidgets 	import QWidget, QApplication
from PyQt5.QtCore 	import QDateTime, Qt


def main():
    
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(500, 350)
    w.move(300, 300)
    w.setWindowTitle('Not so simple')
    w.show()
    
    sys.exit(app.exec_())

def time():
	now = QDateTime.currentDateTime()

	print("Local datetime: ", now.toString(Qt.ISODate))
	print("Universal datetime: ", now.toUTC().toString(Qt.ISODate))

	print("The offset from UTC is: {0} seconds".format(now.offsetFromUtc()))



if __name__ == '__main__':
	time()
	main()
