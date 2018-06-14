# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDialog
import UI_camera_choose_gui

import sys
sys.path.append("/users/fuhongshuai/PycharmProjects/face_recognition/background")

import camera

class Dialog(QDialog,UI_camera_choose_gui.Ui_Dialog):
    def __init__(self,parent = None):
        QDialog.__init__(self,parent)
        self.setupUi(self)
        self.camera_num = 0

    def on_radioButton_clicked(self):
        self.camera_num = 0

    def on_radioButton_2_clicked(self):
        self.camera_num = 1

    def on_pushButton_clicked(self):
        camera.video_face_recognition(self.camera_num)

    def on_pushButton_2_clicked(self):
        self.close()

