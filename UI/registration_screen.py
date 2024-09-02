# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registration_screen.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QFrame,
    QHBoxLayout, QLabel, QLayout, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_ManualRegistrationWindow(object):
    def setupUi(self, ManualRegistrationWindow):
        if not ManualRegistrationWindow.objectName():
            ManualRegistrationWindow.setObjectName(u"ManualRegistrationWindow")
        ManualRegistrationWindow.resize(949, 728)
        ManualRegistrationWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(ManualRegistrationWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMinimumSize(QSize(400, 0))
        self.header_frame.setMaximumSize(QSize(16777215, 80))
        self.header_frame.setStyleSheet(u"")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.header_frame)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 0))
        self.header.setStyleSheet(u"")
        self.header.setFrameShape(QFrame.NoFrame)
        self.header.setFrameShadow(QFrame.Raised)
        self.header.setLineWidth(0)
        self.horizontalLayout_4 = QHBoxLayout(self.header)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(0)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.mainLabel = QLabel(self.frame)
        self.mainLabel.setObjectName(u"mainLabel")
        self.mainLabel.setStyleSheet(u"color: rgb(0, 0, 0);	\n"
"font: 20pt \"Segoe UI\";\n"
"background-color: transparent;\n"
"font-size: 20px;")

        self.horizontalLayout_5.addWidget(self.mainLabel)


        self.horizontalLayout_4.addWidget(self.frame)


        self.horizontalLayout_3.addWidget(self.header)


        self.verticalLayout_8.addWidget(self.header_frame)

        self.body_frame = QFrame(self.centralwidget)
        self.body_frame.setObjectName(u"body_frame")
        self.body_frame.setEnabled(True)
        self.body_frame.setMaximumSize(QSize(16777215, 16777215))
        self.body_frame.setFrameShape(QFrame.NoFrame)
        self.body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.body_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.image_widget = QWidget(self.body_frame)
        self.image_widget.setObjectName(u"image_widget")
        self.verticalLayout_5 = QVBoxLayout(self.image_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.horizontalLayout.addWidget(self.image_widget)

        self.control_layout = QFrame(self.body_frame)
        self.control_layout.setObjectName(u"control_layout")
        self.control_layout.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.control_layout.sizePolicy().hasHeightForWidth())
        self.control_layout.setSizePolicy(sizePolicy)
        self.control_layout.setMaximumSize(QSize(300, 5000))
        self.control_layout.setFrameShape(QFrame.NoFrame)
        self.control_layout.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.control_layout)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.study_frame = QFrame(self.control_layout)
        self.study_frame.setObjectName(u"study_frame")
        self.study_frame.setEnabled(True)
        self.study_frame.setMinimumSize(QSize(300, 500))
        self.study_frame.setMaximumSize(QSize(300, 800))
        self.study_frame.setFrameShape(QFrame.NoFrame)
        self.study_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.study_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.flip_frame = QFrame(self.study_frame)
        self.flip_frame.setObjectName(u"flip_frame")
        self.flip_frame.setMinimumSize(QSize(0, 190))
        self.flip_frame.setFrameShape(QFrame.StyledPanel)
        self.flip_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.flip_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_flip_controls = QLabel(self.flip_frame)
        self.label_flip_controls.setObjectName(u"label_flip_controls")
        self.label_flip_controls.setMaximumSize(QSize(16777215, 30))
        self.label_flip_controls.setStyleSheet(u"")
        self.label_flip_controls.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_flip_controls)

        self.x_flip_frame = QFrame(self.flip_frame)
        self.x_flip_frame.setObjectName(u"x_flip_frame")
        self.x_flip_frame.setFrameShape(QFrame.StyledPanel)
        self.x_flip_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.x_flip_frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.flip_x_button = QPushButton(self.x_flip_frame)
        self.flip_x_button.setObjectName(u"flip_x_button")

        self.horizontalLayout_11.addWidget(self.flip_x_button)


        self.verticalLayout_6.addWidget(self.x_flip_frame)

        self.y_flip_frame = QFrame(self.flip_frame)
        self.y_flip_frame.setObjectName(u"y_flip_frame")
        self.y_flip_frame.setFrameShape(QFrame.StyledPanel)
        self.y_flip_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.y_flip_frame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.flip_y_button = QPushButton(self.y_flip_frame)
        self.flip_y_button.setObjectName(u"flip_y_button")

        self.horizontalLayout_12.addWidget(self.flip_y_button)


        self.verticalLayout_6.addWidget(self.y_flip_frame)

        self.z_flip_frame = QFrame(self.flip_frame)
        self.z_flip_frame.setObjectName(u"z_flip_frame")
        self.z_flip_frame.setFrameShape(QFrame.StyledPanel)
        self.z_flip_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.z_flip_frame)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.flip_z_button = QPushButton(self.z_flip_frame)
        self.flip_z_button.setObjectName(u"flip_z_button")

        self.horizontalLayout_13.addWidget(self.flip_z_button)


        self.verticalLayout_6.addWidget(self.z_flip_frame)


        self.verticalLayout_2.addWidget(self.flip_frame)

        self.shift_frame = QFrame(self.study_frame)
        self.shift_frame.setObjectName(u"shift_frame")
        self.shift_frame.setMinimumSize(QSize(0, 190))
        self.shift_frame.setFrameShape(QFrame.StyledPanel)
        self.shift_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.shift_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_shift_controls = QLabel(self.shift_frame)
        self.label_shift_controls.setObjectName(u"label_shift_controls")
        self.label_shift_controls.setMaximumSize(QSize(16777215, 30))
        self.label_shift_controls.setStyleSheet(u"")
        self.label_shift_controls.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_shift_controls)

        self.x_shift_frame = QFrame(self.shift_frame)
        self.x_shift_frame.setObjectName(u"x_shift_frame")
        self.x_shift_frame.setFrameShape(QFrame.StyledPanel)
        self.x_shift_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.x_shift_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.x_label = QLabel(self.x_shift_frame)
        self.x_label.setObjectName(u"x_label")
        self.x_label.setMaximumSize(QSize(85, 16777215))

        self.horizontalLayout_2.addWidget(self.x_label)

        self.x_slider = QDoubleSpinBox(self.x_shift_frame)
        self.x_slider.setObjectName(u"x_slider")
        self.x_slider.setMinimumSize(QSize(0, 25))
        self.x_slider.setMaximum(100.000000000000000)
        self.x_slider.setSingleStep(0.100000000000000)
        self.x_slider.setStepType(QAbstractSpinBox.DefaultStepType)

        self.horizontalLayout_2.addWidget(self.x_slider)


        self.verticalLayout_3.addWidget(self.x_shift_frame)

        self.y_shift_frame = QFrame(self.shift_frame)
        self.y_shift_frame.setObjectName(u"y_shift_frame")
        self.y_shift_frame.setFrameShape(QFrame.StyledPanel)
        self.y_shift_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.y_shift_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.y_label = QLabel(self.y_shift_frame)
        self.y_label.setObjectName(u"y_label")
        self.y_label.setMaximumSize(QSize(85, 16777215))

        self.horizontalLayout_6.addWidget(self.y_label)

        self.y_slider = QDoubleSpinBox(self.y_shift_frame)
        self.y_slider.setObjectName(u"y_slider")
        self.y_slider.setMinimumSize(QSize(0, 25))
        self.y_slider.setMaximum(100.000000000000000)
        self.y_slider.setSingleStep(0.100000000000000)

        self.horizontalLayout_6.addWidget(self.y_slider)


        self.verticalLayout_3.addWidget(self.y_shift_frame)

        self.z_shift_frame = QFrame(self.shift_frame)
        self.z_shift_frame.setObjectName(u"z_shift_frame")
        self.z_shift_frame.setFrameShape(QFrame.StyledPanel)
        self.z_shift_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.z_shift_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.z_label = QLabel(self.z_shift_frame)
        self.z_label.setObjectName(u"z_label")
        self.z_label.setMaximumSize(QSize(85, 16777215))

        self.horizontalLayout_7.addWidget(self.z_label)

        self.z_slider = QDoubleSpinBox(self.z_shift_frame)
        self.z_slider.setObjectName(u"z_slider")
        self.z_slider.setMinimumSize(QSize(0, 25))
        self.z_slider.setMaximum(100.000000000000000)
        self.z_slider.setSingleStep(0.100000000000000)

        self.horizontalLayout_7.addWidget(self.z_slider)


        self.verticalLayout_3.addWidget(self.z_shift_frame)


        self.verticalLayout_2.addWidget(self.shift_frame)

        self.rotation_frame = QFrame(self.study_frame)
        self.rotation_frame.setObjectName(u"rotation_frame")
        self.rotation_frame.setMinimumSize(QSize(0, 190))
        self.rotation_frame.setFrameShape(QFrame.StyledPanel)
        self.rotation_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.rotation_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_rotation_controls = QLabel(self.rotation_frame)
        self.label_rotation_controls.setObjectName(u"label_rotation_controls")
        self.label_rotation_controls.setMaximumSize(QSize(16777215, 30))
        self.label_rotation_controls.setStyleSheet(u"")
        self.label_rotation_controls.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_rotation_controls)

        self.z_rotation_frame = QFrame(self.rotation_frame)
        self.z_rotation_frame.setObjectName(u"z_rotation_frame")
        self.z_rotation_frame.setFrameShape(QFrame.StyledPanel)
        self.z_rotation_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.z_rotation_frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.z_rotation_label = QLabel(self.z_rotation_frame)
        self.z_rotation_label.setObjectName(u"z_rotation_label")
        self.z_rotation_label.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_8.addWidget(self.z_rotation_label)

        self.z_rotation_slider = QDoubleSpinBox(self.z_rotation_frame)
        self.z_rotation_slider.setObjectName(u"z_rotation_slider")
        self.z_rotation_slider.setMinimumSize(QSize(0, 25))
        self.z_rotation_slider.setMinimum(-180.000000000000000)
        self.z_rotation_slider.setMaximum(180.000000000000000)
        self.z_rotation_slider.setSingleStep(0.010000000000000)

        self.horizontalLayout_8.addWidget(self.z_rotation_slider)


        self.verticalLayout_4.addWidget(self.z_rotation_frame)

        self.y_rotation_frame = QFrame(self.rotation_frame)
        self.y_rotation_frame.setObjectName(u"y_rotation_frame")
        self.y_rotation_frame.setFrameShape(QFrame.StyledPanel)
        self.y_rotation_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.y_rotation_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.y_rotation_label = QLabel(self.y_rotation_frame)
        self.y_rotation_label.setObjectName(u"y_rotation_label")

        self.horizontalLayout_9.addWidget(self.y_rotation_label)

        self.y_rotation_slider = QDoubleSpinBox(self.y_rotation_frame)
        self.y_rotation_slider.setObjectName(u"y_rotation_slider")
        self.y_rotation_slider.setMinimumSize(QSize(0, 25))
        self.y_rotation_slider.setMinimum(-180.000000000000000)
        self.y_rotation_slider.setMaximum(180.000000000000000)
        self.y_rotation_slider.setSingleStep(0.010000000000000)
        self.y_rotation_slider.setValue(0.000000000000000)

        self.horizontalLayout_9.addWidget(self.y_rotation_slider)


        self.verticalLayout_4.addWidget(self.y_rotation_frame)

        self.x_rotation_frame = QFrame(self.rotation_frame)
        self.x_rotation_frame.setObjectName(u"x_rotation_frame")
        self.x_rotation_frame.setFrameShape(QFrame.StyledPanel)
        self.x_rotation_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.x_rotation_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.x_rotation_label = QLabel(self.x_rotation_frame)
        self.x_rotation_label.setObjectName(u"x_rotation_label")

        self.horizontalLayout_10.addWidget(self.x_rotation_label)

        self.x_rotation_slider = QDoubleSpinBox(self.x_rotation_frame)
        self.x_rotation_slider.setObjectName(u"x_rotation_slider")
        self.x_rotation_slider.setMinimumSize(QSize(0, 25))
        self.x_rotation_slider.setMinimum(-180.000000000000000)
        self.x_rotation_slider.setMaximum(180.000000000000000)
        self.x_rotation_slider.setSingleStep(0.010000000000000)

        self.horizontalLayout_10.addWidget(self.x_rotation_slider)


        self.verticalLayout_4.addWidget(self.x_rotation_frame)


        self.verticalLayout_2.addWidget(self.rotation_frame)

        self.saveButton = QPushButton(self.study_frame)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setMinimumSize(QSize(0, 34))
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setBold(False)
        self.saveButton.setFont(font)
        self.saveButton.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.saveButton)


        self.verticalLayout.addWidget(self.study_frame)


        self.horizontalLayout.addWidget(self.control_layout)

        self.control_layout.raise_()
        self.image_widget.raise_()

        self.verticalLayout_8.addWidget(self.body_frame)

        ManualRegistrationWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ManualRegistrationWindow)

        QMetaObject.connectSlotsByName(ManualRegistrationWindow)
    # setupUi

    def retranslateUi(self, ManualRegistrationWindow):
        ManualRegistrationWindow.setWindowTitle(QCoreApplication.translate("ManualRegistrationWindow", u"MRIphantom", None))
        self.mainLabel.setText(QCoreApplication.translate("ManualRegistrationWindow", u"<html><head/><body><p><span style=\" font-size:26pt;\">\u0420\u0443\u0447\u043d\u043e\u0435 \u0441\u043e\u0432\u043c\u0435\u0449\u0435\u043d\u0438\u0435</span></p></body></html>", None))
        self.label_flip_controls.setText(QCoreApplication.translate("ManualRegistrationWindow", u"<html><head/><body><p>\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043e\u0442\u0440\u0430\u0436\u0435\u043d\u0438\u0435\u043c \u041c\u0420\u0422</p></body></html>", None))
        self.flip_x_button.setText(QCoreApplication.translate("ManualRegistrationWindow", u"\u041e\u0442\u0440\u0430\u0437\u0438\u0442\u044c \u043f\u043e \u043e\u0441\u0438 X", None))
        self.flip_y_button.setText(QCoreApplication.translate("ManualRegistrationWindow", u"\u041e\u0442\u0440\u0430\u0437\u0438\u0442\u044c \u043f\u043e \u043e\u0441\u0438 Y", None))
        self.flip_z_button.setText(QCoreApplication.translate("ManualRegistrationWindow", u"\u041e\u0442\u0440\u0430\u0437\u0438\u0442\u044c \u043f\u043e \u043e\u0441\u0438 Z", None))
        self.label_shift_controls.setText(QCoreApplication.translate("ManualRegistrationWindow", u"<html><head/><body><p>\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0441\u0434\u0432\u0438\u0433\u043e\u043c \u041c\u0420\u0422</p></body></html>", None))
        self.x_label.setText(QCoreApplication.translate("ManualRegistrationWindow", u"\u043f\u043e \u043e\u0441\u0438 X, \u043c\u043c", None))
        self.y_label.setText(QCoreApplication.translate("ManualRegistrationWindow", u"\u043f\u043e \u043e\u0441\u0438 Y, \u043c\u043c", None))
        self.z_label.setText(QCoreApplication.translate("ManualRegistrationWindow", u"\u043f\u043e \u043e\u0441\u0438 Z, \u043c\u043c", None))
        self.label_rotation_controls.setText(QCoreApplication.translate("ManualRegistrationWindow", u"<html><head/><body><p>\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0432\u0440\u0430\u0449\u0435\u043d\u0438\u0435\u043c \u041c\u0420\u0422</p><p><br/></p></body></html>", None))
        self.z_rotation_label.setText(QCoreApplication.translate("ManualRegistrationWindow", u"\u0432\u043e\u043a\u0440\u0443\u0433 \u043e\u0441\u0438 Z, \u00b0", None))
        self.y_rotation_label.setText(QCoreApplication.translate("ManualRegistrationWindow", u"\u0432\u043e\u043a\u0440\u0443\u0433 \u043e\u0441\u0438 Y, \u00b0", None))
        self.x_rotation_label.setText(QCoreApplication.translate("ManualRegistrationWindow", u"\u0432\u043e\u043a\u0440\u0443\u0433 \u043e\u0441\u0438 X, \u00b0", None))
        self.saveButton.setText(QCoreApplication.translate("ManualRegistrationWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0441\u043e\u0432\u043c\u0435\u0449\u0435\u043d\u0438\u0435", None))
    # retranslateUi

