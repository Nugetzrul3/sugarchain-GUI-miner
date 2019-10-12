# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):

    def __init__(self):
        super().__init__()

        self.setupUi(Form)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 300)
        Form.setMinimumSize(QtCore.QSize(600, 300))
        Form.setMaximumSize(QtCore.QSize(600, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 431, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 150, 66, 31))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 180, 71, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(0, 220, 61, 21))
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(0, 250, 71, 21))
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(70, 160, 211, 21))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 190, 211, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 220, 211, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(70, 250, 211, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(510, 0, 71, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(511, 16777215))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(450, 10, 47, 13))
        self.label_5.setOpenExternalLinks(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(450, 30, 31, 16))
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(450, 50, 47, 13))
        self.label_7.setOpenExternalLinks(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(450, 70, 141, 51))
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 270, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(290, 160, 61, 20))
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(350, 160, 20, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(380, 160, 111, 41))
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")

        self.pushButton_2.clicked.connect(self.cmd)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sugarchain GUI Solo Miner"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Welcome to the Sugarchain GUI Solo miner. </span><span style=\" font-weight:600; font-style:italic; color:#ff0000;\">Warning: This miner is only for YesPowerSugar, not for the use of other Yespower coins.</span></p><p><span style=\" font-weight:600; color:#000000;\">To start mining, make sure you have set your rpcuser and rpcpassowrd in your wallet configuration. If you haven\'t, check out these tutorials: </span><a href=\"https://forum.sugarchain.org/d/9-solo-mining-on-windows\"><span style=\" text-decoration: underline; color:#0000ff;\">Windows </span></a><a href=\"https://forum.sugarchain.org/d/9-solo-mining-on-windows\"><span style=\" text-decoration: underline; color:#000000;\">or </span></a><a href=\"https://forum.sugarchain.org/d/20-solo-mining-on-linux\"><span style=\" text-decoration: underline; color:#0000ff;\">Linux</span></a><a href=\"https://forum.sugarchain.org/d/20-solo-mining-on-linux\"><span style=\" text-decoration: underline; color:#000000;\">.</span></a></p><p><span style=\" font-weight:600;\">Once set, enter http://127.0.0.1 into the URL, enter your Sugarchain address, followed by your rpcuser and rpcpassword, and set the amount of threads you want to use. Then click \'Start\'</span></p><p><br/></p></body></html>"))
        self.label.setText(_translate("Form", "Solo/Pool URL:"))
        self.label_4.setText(_translate("Form", "Sugarchain Address:"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p align=\"center\">rpcuser:</p></body></html>"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p align=\"center\">rpcpassword:</p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><a href=\"https://sugarchain.org/\"><span style=\" text-decoration: underline; color:#0000ff;\">Website</span></a></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><a href=\"https://github.com/sugarchain-project\"><span style=\" text-decoration: underline; color:#0000ff;\">Github</span></a></p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><a href=\"https://discord.gg/5fvpTdk\"><span style=\" text-decoration: underline; color:#0000ff;\">Discord</span></a></p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" font-style:italic;\">\'One-CPU-One-Vote, The Worlds </span><span style=\" font-weight:600; font-style:italic;\">Fastest</span><span style=\" font-style:italic;\"> Proof Of Work Blockchain\'</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "Start"))
        self.label_11.setText(_translate("Form", "<html><head/><body><p>CPU Cores:</p></body></html>"))
        self.label_12.setText(_translate("Form", "<html><head/><body><p>(Dependent on how many threads your cpu has)</p></body></html>"))

    def cmd(self):
        command = ('start /D "cpuminer" cpuminer.exe -a yespower -o ' + self.lineEdit.text() + ':34229 ''-u ' + self.lineEdit_3.text() + ' -p ' + self.lineEdit_4.text() + ' --coinbase-addr=' + self.lineEdit_2.text() + ' -t' + self.lineEdit_5.text())
        os.system(command)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
