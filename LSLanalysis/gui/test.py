# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(855, 579)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(855, 579))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(99, 99, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 246))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 223, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 95, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 127, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 99, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 99, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 246))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 246))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 223, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 99, 99, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 99, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 246))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 223, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 95, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 127, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 99, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 99, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 246))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 246))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 223, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 99, 99, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 99, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 99, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 223, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 95, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 127, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 99, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 99, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 99, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 99, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 191, 241))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 99, 99, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.infoTable = QtWidgets.QTableWidget(self.centralwidget)
        self.infoTable.setMinimumSize(QtCore.QSize(355, 192))
        self.infoTable.setCornerButtonEnabled(True)
        self.infoTable.setRowCount(0)
        self.infoTable.setColumnCount(4)
        self.infoTable.setObjectName("infoTable")
        self.gridLayout_2.addWidget(self.infoTable, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 1, 2, 1)
        self.btn_loadBands = QtWidgets.QPushButton(self.centralwidget)
        self.btn_loadBands.setObjectName("btn_loadBands")
        self.gridLayout_2.addWidget(self.btn_loadBands, 2, 0, 1, 1)
        self.btn_loadStreams = QtWidgets.QPushButton(self.centralwidget)
        self.btn_loadStreams.setObjectName("btn_loadStreams")
        self.gridLayout_2.addWidget(self.btn_loadStreams, 5, 0, 1, 1)
        self.btn_fixParams = QtWidgets.QPushButton(self.centralwidget)
        self.btn_fixParams.setObjectName("btn_fixParams")
        self.gridLayout_2.addWidget(self.btn_fixParams, 8, 0, 1, 1)
        self.btn_unlock = QtWidgets.QPushButton(self.centralwidget)
        self.btn_unlock.setObjectName("btn_unlock")
        self.gridLayout_2.addWidget(self.btn_unlock, 9, 0, 1, 1)
        self.freqTable = QtWidgets.QTableWidget(self.centralwidget)
        self.freqTable.setMinimumSize(QtCore.QSize(355, 193))
        self.freqTable.setColumnCount(4)
        self.freqTable.setObjectName("freqTable")
        self.freqTable.setRowCount(0)
        self.gridLayout_2.addWidget(self.freqTable, 1, 0, 1, 1)
        self.params = QtWidgets.QGridLayout()
        self.params.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.params.setContentsMargins(0, -1, -1, -1)
        self.params.setSpacing(2)
        self.params.setObjectName("params")
        self.comboBox_conn = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_conn.setObjectName("comboBox_conn")
        self.comboBox_conn.addItem("")
        self.comboBox_conn.addItem("")
        self.comboBox_conn.addItem("")
        self.comboBox_conn.addItem("")
        self.comboBox_conn.addItem("")
        self.comboBox_conn.addItem("")
        self.params.addWidget(self.comboBox_conn, 3, 2, 1, 1)
        self.comboBox_input = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_input.setObjectName("comboBox_input")
        self.comboBox_input.addItem("")
        self.params.addWidget(self.comboBox_input, 1, 2, 1, 1)
        self.label_device = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.label_device.setFont(font)
        self.label_device.setObjectName("label_device")
        self.params.addWidget(self.label_device, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.params.addItem(spacerItem1, 7, 0, 1, 1)
        self.checkBox_wlag = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_wlag.setEnabled(False)
        self.checkBox_wlag.setObjectName("checkBox_wlag")
        self.params.addWidget(self.checkBox_wlag, 5, 2, 1, 1)
        self.label_oscIP = QtWidgets.QLabel(self.centralwidget)
        self.label_oscIP.setObjectName("label_oscIP")
        self.params.addWidget(self.label_oscIP, 8, 0, 1, 1)
        self.comboBox_chn = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_chn.setObjectName("comboBox_chn")
        self.comboBox_chn.addItem("")
        self.comboBox_chn.addItem("")
        self.params.addWidget(self.comboBox_chn, 2, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_wsize = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_wsize.setObjectName("lineEdit_wsize")
        self.horizontalLayout.addWidget(self.lineEdit_wsize)
        self.label_wlag = QtWidgets.QLabel(self.centralwidget)
        self.label_wlag.setObjectName("label_wlag")
        self.horizontalLayout.addWidget(self.label_wlag)
        self.lineEdit_wlag = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_wlag.setEnabled(False)
        self.lineEdit_wlag.setText("")
        self.lineEdit_wlag.setObjectName("lineEdit_wlag")
        self.horizontalLayout.addWidget(self.lineEdit_wlag)
        self.params.addLayout(self.horizontalLayout, 4, 2, 1, 1)
        self.lineEdit_oscCH = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_oscCH.setObjectName("lineEdit_oscCH")
        self.params.addWidget(self.lineEdit_oscCH, 9, 2, 1, 1)
        self.lineEdit_oscIP = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_oscIP.setStatusTip("")
        self.lineEdit_oscIP.setObjectName("lineEdit_oscIP")
        self.params.addWidget(self.lineEdit_oscIP, 8, 2, 1, 1)
        self.comboBox_device = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_device.setObjectName("comboBox_device")
        self.comboBox_device.addItem("")
        self.comboBox_device.addItem("")
        self.comboBox_device.addItem("")
        self.comboBox_device.addItem("")
        self.params.addWidget(self.comboBox_device, 0, 2, 1, 1)
        self.label_conn = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.label_conn.setFont(font)
        self.label_conn.setObjectName("label_conn")
        self.params.addWidget(self.label_conn, 3, 0, 1, 1)
        self.label_oscPort = QtWidgets.QLabel(self.centralwidget)
        self.label_oscPort.setObjectName("label_oscPort")
        self.params.addWidget(self.label_oscPort, 9, 0, 1, 1)
        self.label_wsize = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.label_wsize.setFont(font)
        self.label_wsize.setObjectName("label_wsize")
        self.params.addWidget(self.label_wsize, 4, 0, 1, 1)
        self.label_input = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_input.setFont(font)
        self.label_input.setObjectName("label_input")
        self.params.addWidget(self.label_input, 1, 0, 1, 1)
        self.label_chn = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_chn.setFont(font)
        self.label_chn.setObjectName("label_chn")
        self.params.addWidget(self.label_chn, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.params.addWidget(self.label_2, 6, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_normMin = QtWidgets.QLabel(self.centralwidget)
        self.label_normMin.setObjectName("label_normMin")
        self.horizontalLayout_2.addWidget(self.label_normMin)
        self.lineEdit_normMin = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_normMin.setObjectName("lineEdit_normMin")
        self.horizontalLayout_2.addWidget(self.lineEdit_normMin)
        self.label_normMax = QtWidgets.QLabel(self.centralwidget)
        self.label_normMax.setObjectName("label_normMax")
        self.horizontalLayout_2.addWidget(self.label_normMax)
        self.lineEdit_normMax = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_normMax.setObjectName("lineEdit_normMax")
        self.horizontalLayout_2.addWidget(self.lineEdit_normMax)
        self.params.addLayout(self.horizontalLayout_2, 6, 2, 1, 1)
        self.gridLayout_2.addLayout(self.params, 2, 2, 2, 1)
        self.param_check = QtWidgets.QLabel(self.centralwidget)
        self.param_check.setText("")
        self.param_check.setObjectName("param_check")
        self.gridLayout_2.addWidget(self.param_check, 7, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_osc = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_osc.setTristate(False)
        self.checkBox_osc.setObjectName("checkBox_osc")
        self.gridLayout.addWidget(self.checkBox_osc, 1, 0, 1, 1)
        self.btn_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop.setObjectName("btn_stop")
        self.gridLayout.addWidget(self.btn_stop, 2, 1, 1, 1)
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setObjectName("btn_start")
        self.gridLayout.addWidget(self.btn_start, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 6, 2, 3, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 855, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RhythmOfRelating"))
        self.btn_loadBands.setText(_translate("MainWindow", "1. set frequency bands"))
        self.btn_loadStreams.setText(_translate("MainWindow", "2. load LSL streams"))
        self.btn_fixParams.setText(_translate("MainWindow", "3. Lock parameters"))
        self.btn_unlock.setText(_translate("MainWindow", "unlock parameters"))
        self.comboBox_conn.setItemText(0, _translate("MainWindow", "Coherence"))
        self.comboBox_conn.setItemText(1, _translate("MainWindow", "Imaginary Coherence"))
        self.comboBox_conn.setItemText(2, _translate("MainWindow", "Envelope Correlation"))
        self.comboBox_conn.setItemText(3, _translate("MainWindow", "Power Correlation"))
        self.comboBox_conn.setItemText(4, _translate("MainWindow", "PLV"))
        self.comboBox_conn.setItemText(5, _translate("MainWindow", "CCorr"))
        self.comboBox_input.setItemText(0, _translate("MainWindow", "EEG"))
        self.label_device.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Device</span></p></body></html>"))
        self.checkBox_wlag.setText(_translate("MainWindow", "sending relative synchrony values based on *window lag* seconds ago."))
        self.label_oscIP.setText(_translate("MainWindow", "OSC IP address (optional)"))
        self.comboBox_chn.setItemText(0, _translate("MainWindow", "one-to-one (e.g. Fp1 is only correlated with Fp1 and so on.)"))
        self.comboBox_chn.setItemText(1, _translate("MainWindow", "all-to-all (e.g. each channel is correlated with all the other available channels in the selection.)"))
        self.lineEdit_wsize.setText(_translate("MainWindow", "3"))
        self.label_wlag.setText(_translate("MainWindow", "window lag (optional)"))
        self.lineEdit_oscCH.setText(_translate("MainWindow", "9000"))
        self.lineEdit_oscIP.setText(_translate("MainWindow", "10.0.0.24"))
        self.comboBox_device.setItemText(0, _translate("MainWindow", "MUSE"))
        self.comboBox_device.setItemText(1, _translate("MainWindow", "EMOTIV EPOC"))
        self.comboBox_device.setItemText(2, _translate("MainWindow", "EMOTIV EPOC+"))
        self.comboBox_device.setItemText(3, _translate("MainWindow", "Enobio"))
        self.label_conn.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Connectivity metric   </span></p></body></html>"))
        self.label_oscPort.setText(_translate("MainWindow", "OSC port (optional) "))
        self.label_wsize.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Window size </span></p></body></html>"))
        self.label_input.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Input type</span></p></body></html>"))
        self.label_chn.setText(_translate("MainWindow", "Connectivity type"))
        self.label_2.setText(_translate("MainWindow", "Normalization (MinMax)"))
        self.label_normMin.setText(_translate("MainWindow", "Min."))
        self.lineEdit_normMin.setText(_translate("MainWindow", "0"))
        self.label_normMax.setText(_translate("MainWindow", "Max."))
        self.lineEdit_normMax.setText(_translate("MainWindow", "1"))
        self.label.setText(_translate("MainWindow", "Welcome, specify your values and press on \'Start\'"))
        self.checkBox_osc.setText(_translate("MainWindow", "sending through OSC"))
        self.btn_stop.setText(_translate("MainWindow", "stop"))
        self.btn_start.setText(_translate("MainWindow", "4. start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())