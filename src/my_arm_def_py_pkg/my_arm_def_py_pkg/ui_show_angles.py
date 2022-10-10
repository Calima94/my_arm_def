# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show_angles.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 238)
        Form.setStyleSheet(u"background-color: rgb(32, 74, 135);")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 381, 211))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(64, 173, 191);")

        self.horizontalLayout.addWidget(self.label)

        self.elbow_angle_label = QLabel(self.widget)
        self.elbow_angle_label.setObjectName(u"elbow_angle_label")
        self.elbow_angle_label.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.elbow_angle_label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-color: rgb(64, 173, 191);")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.elbow_angle_to_reach_label = QLabel(self.widget)
        self.elbow_angle_to_reach_label.setObjectName(u"elbow_angle_to_reach_label")
        self.elbow_angle_to_reach_label.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.elbow_angle_to_reach_label)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"background-color: rgb(64, 173, 191);")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.shoulder_angle_label = QLabel(self.widget)
        self.shoulder_angle_label.setObjectName(u"shoulder_angle_label")
        self.shoulder_angle_label.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.shoulder_angle_label)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"background-color: rgb(64, 173, 191);")

        self.horizontalLayout_5.addWidget(self.label_10)

        self.shoulder_angle_to_reach_angle = QLabel(self.widget)
        self.shoulder_angle_to_reach_angle.setObjectName(u"shoulder_angle_to_reach_angle")
        self.shoulder_angle_to_reach_angle.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.shoulder_angle_to_reach_angle)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Elbow Angle</span></p></body></html>", None))
        self.elbow_angle_label.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Elbow Angle to reach</span></p></body></html>", None))
        self.elbow_angle_to_reach_label.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Shoulder Angle</span></p></body></html>", None))
        self.shoulder_angle_label.setText("")
        self.label_10.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Shoulder Angle to Reach</span></p></body></html>", None))
        self.shoulder_angle_to_reach_angle.setText("")
    # retranslateUi

