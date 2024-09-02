# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_v2.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1343, 831)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
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
        self.mainLabel.setStyleSheet(u"color: rgb(255, 255 255);	\n"
"font: 20pt \"Segoe UI\";\n"
"background-color: transparent;\n"
"font-size: 26px;")

        self.horizontalLayout_5.addWidget(self.mainLabel)

        self.mainPageButton = QPushButton(self.frame)
        self.mainPageButton.setObjectName(u"mainPageButton")

        self.horizontalLayout_5.addWidget(self.mainPageButton)

        self.statsPageButton = QPushButton(self.frame)
        self.statsPageButton.setObjectName(u"statsPageButton")

        self.horizontalLayout_5.addWidget(self.statsPageButton)

        self.scatter3dButton = QPushButton(self.frame)
        self.scatter3dButton.setObjectName(u"scatter3dButton")

        self.horizontalLayout_5.addWidget(self.scatter3dButton)

        self.scatter2dButton = QPushButton(self.frame)
        self.scatter2dButton.setObjectName(u"scatter2dButton")

        self.horizontalLayout_5.addWidget(self.scatter2dButton)

        self.marker2dButton = QPushButton(self.frame)
        self.marker2dButton.setObjectName(u"marker2dButton")

        self.horizontalLayout_5.addWidget(self.marker2dButton)


        self.horizontalLayout_4.addWidget(self.frame)


        self.horizontalLayout_3.addWidget(self.header)


        self.verticalLayout_8.addWidget(self.header_frame)

        self.body_stackedWidget = QStackedWidget(self.centralwidget)
        self.body_stackedWidget.setObjectName(u"body_stackedWidget")
        self.body_stackedWidget.setEnabled(True)
        self.body_stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.body_stackedWidgetPageMain = QWidget()
        self.body_stackedWidgetPageMain.setObjectName(u"body_stackedWidgetPageMain")
        self.horizontalLayout = QHBoxLayout(self.body_stackedWidgetPageMain)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.moving_frame = QFrame(self.body_stackedWidgetPageMain)
        self.moving_frame.setObjectName(u"moving_frame")
        self.moving_frame.setFrameShape(QFrame.Panel)

        self.horizontalLayout.addWidget(self.moving_frame)

        self.fixed_frame = QFrame(self.body_stackedWidgetPageMain)
        self.fixed_frame.setObjectName(u"fixed_frame")
        self.fixed_frame.setFocusPolicy(Qt.NoFocus)
        self.fixed_frame.setStyleSheet(u"")
        self.fixed_frame.setFrameShape(QFrame.Panel)
        self.fixed_frame.setFrameShadow(QFrame.Plain)
        self.fixed_frame.setLineWidth(1)
        self.fixed_frame.setMidLineWidth(0)

        self.horizontalLayout.addWidget(self.fixed_frame)

        self.info_layout = QFrame(self.body_stackedWidgetPageMain)
        self.info_layout.setObjectName(u"info_layout")
        self.info_layout.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_layout.sizePolicy().hasHeightForWidth())
        self.info_layout.setSizePolicy(sizePolicy)
        self.info_layout.setMaximumSize(QSize(300, 500))
        self.info_layout.setFrameShape(QFrame.NoFrame)
        self.info_layout.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.info_layout)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleEdit = QLineEdit(self.info_layout)
        self.titleEdit.setObjectName(u"titleEdit")
        self.titleEdit.setMinimumSize(QSize(0, 30))
        self.titleEdit.setMaximumSize(QSize(16777215, 30))
        self.titleEdit.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.titleEdit)

        self.label_4 = QLabel(self.info_layout)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.phantomTypeCombo = QComboBox(self.info_layout)
        self.phantomTypeCombo.setObjectName(u"phantomTypeCombo")
        self.phantomTypeCombo.setMinimumSize(QSize(0, 30))
        self.phantomTypeCombo.setMaximumSize(QSize(16777215, 30))
        self.phantomTypeCombo.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.phantomTypeCombo)

        self.infolabel1 = QLabel(self.info_layout)
        self.infolabel1.setObjectName(u"infolabel1")
        self.infolabel1.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.infolabel1)

        self.modelselector_frame = QFrame(self.info_layout)
        self.modelselector_frame.setObjectName(u"modelselector_frame")
        self.modelselector_frame.setMaximumSize(QSize(16777215, 30))
        self.modelselector_frame.setFrameShape(QFrame.NoFrame)
        self.modelselector_frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.modelselector_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.ctPageButton = QPushButton(self.modelselector_frame)
        self.ctPageButton.setObjectName(u"ctPageButton")
        self.ctPageButton.setCheckable(True)
        self.ctPageButton.setChecked(True)
        self.ctPageButton.setAutoDefault(False)
        self.ctPageButton.setFlat(False)

        self.horizontalLayout_7.addWidget(self.ctPageButton)

        self.geometryPageButton = QPushButton(self.modelselector_frame)
        self.geometryPageButton.setObjectName(u"geometryPageButton")
        self.geometryPageButton.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.geometryPageButton)


        self.verticalLayout.addWidget(self.modelselector_frame)

        self.movinginfo_frame = QFrame(self.info_layout)
        self.movinginfo_frame.setObjectName(u"movinginfo_frame")
        self.movinginfo_frame.setMaximumSize(QSize(16777215, 40))
        self.movinginfo_frame.setFrameShape(QFrame.NoFrame)
        self.movinginfo_frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.movinginfo_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.movinginfo_label = QLabel(self.movinginfo_frame)
        self.movinginfo_label.setObjectName(u"movinginfo_label")
        self.movinginfo_label.setMinimumSize(QSize(0, 30))
        self.movinginfo_label.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_6.addWidget(self.movinginfo_label)

        self.movingimgEdit = QLineEdit(self.movinginfo_frame)
        self.movingimgEdit.setObjectName(u"movingimgEdit")
        self.movingimgEdit.setEnabled(True)
        self.movingimgEdit.setMinimumSize(QSize(0, 30))
        self.movingimgEdit.setMaximumSize(QSize(250, 30))
        self.movingimgEdit.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.movingimgEdit)


        self.verticalLayout.addWidget(self.movinginfo_frame)

        self.fixed_stackedWidget = QStackedWidget(self.info_layout)
        self.fixed_stackedWidget.setObjectName(u"fixed_stackedWidget")
        self.fixed_stackedWidget.setEnabled(True)
        self.fixed_stackedWidget.setMinimumSize(QSize(300, 100))
        self.fixed_stackedWidget.setMaximumSize(QSize(300, 100))
        self.fixed_stackedWidget.setFrameShape(QFrame.NoFrame)
        self.fixed_stackedWidget.setFrameShadow(QFrame.Plain)
        self.ct_page = QWidget()
        self.ct_page.setObjectName(u"ct_page")
        self.verticalLayout_2 = QVBoxLayout(self.ct_page)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 10, 0)
        self.fixedinfo_frame = QFrame(self.ct_page)
        self.fixedinfo_frame.setObjectName(u"fixedinfo_frame")
        self.fixedinfo_frame.setMaximumSize(QSize(16777215, 40))
        self.fixedinfo_frame.setFrameShape(QFrame.NoFrame)
        self.fixedinfo_frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.fixedinfo_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fixedinfo_label = QLabel(self.fixedinfo_frame)
        self.fixedinfo_label.setObjectName(u"fixedinfo_label")
        self.fixedinfo_label.setMinimumSize(QSize(0, 30))
        self.fixedinfo_label.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_2.addWidget(self.fixedinfo_label)

        self.fixedimgEdit = QLineEdit(self.fixedinfo_frame)
        self.fixedimgEdit.setObjectName(u"fixedimgEdit")
        self.fixedimgEdit.setMinimumSize(QSize(0, 30))
        self.fixedimgEdit.setMaximumSize(QSize(250, 30))
        self.fixedimgEdit.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.fixedimgEdit)


        self.verticalLayout_2.addWidget(self.fixedinfo_frame)

        self.fixed_stackedWidget.addWidget(self.ct_page)
        self.geometry_page = QWidget()
        self.geometry_page.setObjectName(u"geometry_page")
        self.widget = QWidget(self.geometry_page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 281, 81))
        self.verticalLayout_9 = QVBoxLayout(self.widget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_9.addWidget(self.label_5)

        self.fixed_stackedWidget.addWidget(self.geometry_page)

        self.verticalLayout.addWidget(self.fixed_stackedWidget)

        self.controls_frame = QFrame(self.info_layout)
        self.controls_frame.setObjectName(u"controls_frame")
        self.controls_frame.setMinimumSize(QSize(0, 150))
        self.controls_frame.setMaximumSize(QSize(300, 100))
        self.controls_layout = QVBoxLayout(self.controls_frame)
        self.controls_layout.setObjectName(u"controls_layout")
        self.controls_layout.setContentsMargins(-1, 5, -1, 5)
        self.autoregistrationButton = QPushButton(self.controls_frame)
        self.autoregistrationButton.setObjectName(u"autoregistrationButton")
        self.autoregistrationButton.setMinimumSize(QSize(0, 30))
        self.autoregistrationButton.setMaximumSize(QSize(16777215, 30))
        self.autoregistrationButton.setStyleSheet(u"")

        self.controls_layout.addWidget(self.autoregistrationButton)

        self.manualregistrationButton = QPushButton(self.controls_frame)
        self.manualregistrationButton.setObjectName(u"manualregistrationButton")
        self.manualregistrationButton.setMinimumSize(QSize(0, 30))
        self.manualregistrationButton.setMaximumSize(QSize(16777215, 30))

        self.controls_layout.addWidget(self.manualregistrationButton)

        self.analyzeButton = QPushButton(self.controls_frame)
        self.analyzeButton.setObjectName(u"analyzeButton")
        self.analyzeButton.setMinimumSize(QSize(0, 30))
        self.analyzeButton.setMaximumSize(QSize(16777215, 30))
        self.analyzeButton.setStyleSheet(u"")

        self.controls_layout.addWidget(self.analyzeButton)

        self.statusLabel = QLabel(self.controls_frame)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setMinimumSize(QSize(280, 30))
        self.statusLabel.setMaximumSize(QSize(300, 30))
        self.statusLabel.setStyleSheet(u"")

        self.controls_layout.addWidget(self.statusLabel)


        self.verticalLayout.addWidget(self.controls_frame)


        self.horizontalLayout.addWidget(self.info_layout)

        self.body_stackedWidget.addWidget(self.body_stackedWidgetPageMain)
        self.body_stackedWidgetPageStats = QWidget()
        self.body_stackedWidgetPageStats.setObjectName(u"body_stackedWidgetPageStats")
        self.body_stackedWidgetPageStats.setMaximumSize(QSize(1470, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.body_stackedWidgetPageStats)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea = QScrollArea(self.body_stackedWidgetPageStats)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.stats_scrollAreaWidgetContents = QWidget()
        self.stats_scrollAreaWidgetContents.setObjectName(u"stats_scrollAreaWidgetContents")
        self.stats_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1306, 1196))
        self.verticalLayout_5 = QVBoxLayout(self.stats_scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.stats_scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_5.addWidget(self.label)

        self.stats_frame = QFrame(self.stats_scrollAreaWidgetContents)
        self.stats_frame.setObjectName(u"stats_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stats_frame.sizePolicy().hasHeightForWidth())
        self.stats_frame.setSizePolicy(sizePolicy1)
        self.stats_frame.setMinimumSize(QSize(0, 350))
        self.stats_frame.setMaximumSize(QSize(16777215, 1000))
        self.stats_frame.setFrameShape(QFrame.Box)
        self.stats_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.stats_frame)

        self.plots_frame = QFrame(self.stats_scrollAreaWidgetContents)
        self.plots_frame.setObjectName(u"plots_frame")
        self.plots_frame.setMinimumSize(QSize(0, 800))
        self.plots_frame.setFrameShape(QFrame.Box)
        self.plots_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.plots_frame)

        self.scrollArea.setWidget(self.stats_scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.body_stackedWidget.addWidget(self.body_stackedWidgetPageStats)
        self.body_stackedWidgetPage3d = QWidget()
        self.body_stackedWidgetPage3d.setObjectName(u"body_stackedWidgetPage3d")
        self.verticalLayout_4 = QVBoxLayout(self.body_stackedWidgetPage3d)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.body_stackedWidgetPage3d)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_4.addWidget(self.label_2)

        self.scatter3d_frame = QFrame(self.body_stackedWidgetPage3d)
        self.scatter3d_frame.setObjectName(u"scatter3d_frame")
        self.scatter3d_frame.setMaximumSize(QSize(16777215, 16777215))
        self.scatter3d_frame.setFrameShape(QFrame.Box)
        self.scatter3d_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.scatter3d_frame)

        self.body_stackedWidget.addWidget(self.body_stackedWidgetPage3d)
        self.body_stackedWidgetPage2d = QWidget()
        self.body_stackedWidgetPage2d.setObjectName(u"body_stackedWidgetPage2d")
        self.verticalLayout_6 = QVBoxLayout(self.body_stackedWidgetPage2d)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.body_stackedWidgetPage2d)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(450, 30))

        self.verticalLayout_6.addWidget(self.label_3)

        self.scatter2d_frame = QFrame(self.body_stackedWidgetPage2d)
        self.scatter2d_frame.setObjectName(u"scatter2d_frame")
        self.scatter2d_frame.setMinimumSize(QSize(700, 700))
        self.scatter2d_frame.setMaximumSize(QSize(700, 700))
        self.scatter2d_frame.setFrameShape(QFrame.Box)
        self.scatter2d_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.scatter2d_frame)

        self.body_stackedWidget.addWidget(self.body_stackedWidgetPage2d)
        self.body_stackedWidgetPageHeatmap2d = QWidget()
        self.body_stackedWidgetPageHeatmap2d.setObjectName(u"body_stackedWidgetPageHeatmap2d")
        self.verticalLayout_7 = QVBoxLayout(self.body_stackedWidgetPageHeatmap2d)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_heatmap2d = QLabel(self.body_stackedWidgetPageHeatmap2d)
        self.label_heatmap2d.setObjectName(u"label_heatmap2d")
        self.label_heatmap2d.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_7.addWidget(self.label_heatmap2d)

        self.marker2d_frame = QFrame(self.body_stackedWidgetPageHeatmap2d)
        self.marker2d_frame.setObjectName(u"marker2d_frame")
        self.marker2d_frame.setMinimumSize(QSize(700, 700))
        self.marker2d_frame.setMaximumSize(QSize(700, 700))
        self.marker2d_frame.setFrameShape(QFrame.StyledPanel)
        self.marker2d_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.marker2d_frame)

        self.body_stackedWidget.addWidget(self.body_stackedWidgetPageHeatmap2d)

        self.verticalLayout_8.addWidget(self.body_stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.body_stackedWidget.setCurrentIndex(0)
        self.ctPageButton.setDefault(False)
        self.fixed_stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MRIphantom", None))
        self.mainLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:26pt; font-weight:700;\">MRI</span><span style=\" font-size:26pt;\">phantom</span></p></body></html>", None))
        self.mainPageButton.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u044b\u0439 \u044d\u043a\u0440\u0430\u043d", None))
        self.statsPageButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u043e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u0439", None))
        self.scatter3dButton.setText(QCoreApplication.translate("MainWindow", u"3D \u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440", None))
        self.scatter2dButton.setText(QCoreApplication.translate("MainWindow", u"2D \u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440", None))
        self.marker2dButton.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u043a\u0435\u0440\u044b", None))
        self.titleEdit.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043c\u043e\u0434\u0435\u043b\u044c \u0444\u0430\u043d\u0442\u043e\u043c\u0430:", None))
        self.phantomTypeCombo.setCurrentText("")
        self.infolabel1.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0440\u0435\u0436\u0438\u043c \u0430\u043d\u0430\u043b\u0438\u0437\u0430:", None))
        self.ctPageButton.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0420\u0422 vs KT", None))
        self.geometryPageButton.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0420\u0422 vs \u043c\u043e\u0434\u0435\u043b\u044c", None))
        self.movinginfo_label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0420\u0422", None))
        self.movingimgEdit.setText("")
        self.fixedinfo_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0422", None))
        self.fixedimgEdit.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043e\u043c\u0435\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u043c\u043e\u0434\u0435\u043b\u044c \u0432 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0435", None))
        self.autoregistrationButton.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.manualregistrationButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0447\u043d\u0430\u044f \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.analyzeButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u043e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u044f", None))
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 (\u0441\u043d\u0430\u0447\u0430\u043b\u0430 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0440\u0430\u0441\u0447\u0435\u0442 \u043e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u0439)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"3D \u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 (\u0441\u043d\u0430\u0447\u0430\u043b\u0430 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0440\u0430\u0441\u0447\u0435\u0442 \u043e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u0439)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"2D \u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 (\u0441\u043d\u0430\u0447\u0430\u043b\u0430 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0440\u0430\u0441\u0447\u0435\u0442 \u043e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u0439)", None))
        self.label_heatmap2d.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u043a\u0435\u0440\u044b", None))
    # retranslateUi

