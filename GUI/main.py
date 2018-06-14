# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
import sys
sys.path.append("/users/fuhongshuai/PycharmProjects/face_recognition/GUI")
import mainwindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = mainwindow.MainWindow()
    ui.show()
    sys.exit(app.exec_())



