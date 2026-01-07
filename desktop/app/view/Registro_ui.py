# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Registro.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
from app import resources_rc

class Ui_Registro(object):
    def setupUi(self, Registro):
        if not Registro.objectName():
            Registro.setObjectName(u"Registro")
        Registro.resize(675, 543)
        self.contenedorInicial = QWidget(Registro)
        self.contenedorInicial.setObjectName(u"contenedorInicial")
        self.contenedorInicial.setGeometry(QRect(10, 10, 661, 521))
        self.contenedorInicial.setStyleSheet(u"#contenedorInicial {\n"
"  background-color: #00273d;\n"
"}")
        self.logo = QWidget(self.contenedorInicial)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(260, 20, 131, 131))
        self.btnLogo = QPushButton(self.logo)
        self.btnLogo.setObjectName(u"btnLogo")
        self.btnLogo.setGeometry(QRect(0, 0, 131, 131))
        icon = QIcon()
        icon.addFile(u":/assets/logo1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnLogo.setIcon(icon)
        self.btnLogo.setIconSize(QSize(131, 131))
        self.login = QWidget(self.contenedorInicial)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(150, 220, 381, 211))
        self.lblUser = QLabel(self.login)
        self.lblUser.setObjectName(u"lblUser")
        self.lblUser.setGeometry(QRect(10, 10, 81, 31))
        font = QFont()
        font.setPointSize(12)
        self.lblUser.setFont(font)
        self.lnUser = QLineEdit(self.login)
        self.lnUser.setObjectName(u"lnUser")
        self.lnUser.setGeometry(QRect(120, 10, 251, 31))
        self.lblCorreo = QLabel(self.login)
        self.lblCorreo.setObjectName(u"lblCorreo")
        self.lblCorreo.setGeometry(QRect(10, 60, 61, 21))
        self.lblCorreo.setFont(font)
        self.lnCorreo = QLineEdit(self.login)
        self.lnCorreo.setObjectName(u"lnCorreo")
        self.lnCorreo.setGeometry(QRect(120, 50, 251, 31))
        self.btnRegistrar = QPushButton(self.login)
        self.btnRegistrar.setObjectName(u"btnRegistrar")
        self.btnRegistrar.setGeometry(QRect(110, 150, 131, 41))
        self.btnRegistrar.setFont(font)
        self.lblContrasena = QLabel(self.login)
        self.lblContrasena.setObjectName(u"lblContrasena")
        self.lblContrasena.setGeometry(QRect(10, 100, 91, 21))
        self.lblContrasena.setFont(font)
        self.lnContrasena = QLineEdit(self.login)
        self.lnContrasena.setObjectName(u"lnContrasena")
        self.lnContrasena.setGeometry(QRect(120, 90, 251, 31))
        self.lblBienvenida = QLabel(self.contenedorInicial)
        self.lblBienvenida.setObjectName(u"lblBienvenida")
        self.lblBienvenida.setGeometry(QRect(220, 170, 211, 41))
        font1 = QFont()
        font1.setPointSize(25)
        self.lblBienvenida.setFont(font1)
        self.lblBienvenida.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(Registro)

        QMetaObject.connectSlotsByName(Registro)
    # setupUi

    def retranslateUi(self, Registro):
        Registro.setWindowTitle(QCoreApplication.translate("Registro", u"Form", None))
        self.btnLogo.setText("")
        self.lblUser.setText(QCoreApplication.translate("Registro", u"Nombre: ", None))
        self.lblCorreo.setText(QCoreApplication.translate("Registro", u"Correo: ", None))
        self.btnRegistrar.setText(QCoreApplication.translate("Registro", u"Registrate", None))
        self.lblContrasena.setText(QCoreApplication.translate("Registro", u"Contrase\u00f1a: ", None))
        self.lblBienvenida.setText(QCoreApplication.translate("Registro", u"\u00a1Bienvenid@!", None))
    # retranslateUi

