# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project_design3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 356)
        Dialog.setStyleSheet("background-color: rgb(143,188,143);")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(25, 10, 351, 271))
        self.textBrowser.setStyleSheet("background-color:#C0DEC0;")
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 290, 151, 51))
        self.pushButton.setStyleSheet("#pushButton {\n"
"background-color:rgb(30, 185, 30);\n"
"border-style: outset;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: beige;\n"
"font: 22px;\n"
"\n"
"padding: 6px;\n"
"}\n"
"#pushButton:pressed {\n"
"background-color:rgb(50, 205, 50);\n"
"border-style: inset;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 290, 151, 51))
        self.pushButton_2.setStyleSheet("#pushButton_2 {\n"
"background-color:rgb(30, 185, 30);\n"
"border-style: outset;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: beige;\n"
"font: 22px;\n"
"\n"
"padding: 6px;\n"
"}\n"
"#pushButton_2:pressed {\n"
"background-color:rgb(50, 205, 50);\n"
"border-style: inset;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Добро пожаловать в локальную почту!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Выберите один из пунктов для создания учетной записи, если вы здесь впервые.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Или же войдите в ваш аккаунт. (Предупреждение: пароль изменить нельзя!) </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Приложение не требует открытие на весь экран и будет спокойно функционировать в режиме окна.</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Войти"))
        self.pushButton_2.setText(_translate("Dialog", "Регистрация"))
