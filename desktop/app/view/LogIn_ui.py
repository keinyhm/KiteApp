# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LogIn.ui'
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
import resources_rc

class Ui_LogIn(object):
    def setupUi(self, LogIn):
        if not LogIn.objectName():
            LogIn.setObjectName(u"LogIn")
        LogIn.resize(675, 543)
        self.contenedorInicial = QWidget(LogIn)
        self.contenedorInicial.setObjectName(u"contenedorInicial")
        self.contenedorInicial.setGeometry(QRect(10, 10, 661, 521))
        self.contenedorInicial.setStyleSheet(u"#contenedorInicial {\n"
"  background-color: #00273d;\n"
"}")
        self.logo = QWidget(self.contenedorInicial)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(280, 20, 131, 131))
        self.btnLogo = QPushButton(self.logo)
        self.btnLogo.setObjectName(u"btnLogo")
        self.btnLogo.setGeometry(QRect(0, 0, 131, 131))
        icon = QIcon()
        icon.addFile(u":/assets/logo1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnLogo.setIcon(icon)
        self.btnLogo.setIconSize(QSize(131, 131))
        self.login = QWidget(self.contenedorInicial)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(150, 220, 381, 171))
        self.lblCorreo = QLabel(self.login)
        self.lblCorreo.setObjectName(u"lblCorreo")
        self.lblCorreo.setGeometry(QRect(10, 20, 71, 21))
        font = QFont()
        font.setPointSize(12)
        self.lblCorreo.setFont(font)
        self.lnCorreo = QLineEdit(self.login)
        self.lnCorreo.setObjectName(u"lnCorreo")
        self.lnCorreo.setGeometry(QRect(130, 10, 241, 31))
        self.lblContrasena = QLabel(self.login)
        self.lblContrasena.setObjectName(u"lblContrasena")
        self.lblContrasena.setGeometry(QRect(10, 60, 121, 21))
        self.lblContrasena.setFont(font)
        self.lnContrasena = QLineEdit(self.login)
        self.lnContrasena.setObjectName(u"lnContrasena")
        self.lnContrasena.setGeometry(QRect(130, 50, 241, 31))
        font1 = QFont()
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.lnContrasena.setFont(font1)
        self.lnContrasena.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        self.lnContrasena.setEchoMode(QLineEdit.EchoMode.Password)
        self.btnLogIn = QPushButton(self.login)
        self.btnLogIn.setObjectName(u"btnLogIn")
        self.btnLogIn.setGeometry(QRect(130, 110, 131, 41))
        self.btnLogIn.setFont(font)
        self.lblBienvenida = QLabel(self.contenedorInicial)
        self.lblBienvenida.setObjectName(u"lblBienvenida")
        self.lblBienvenida.setGeometry(QRect(240, 170, 211, 41))
        font2 = QFont()
        font2.setPointSize(25)
        self.lblBienvenida.setFont(font2)
        self.lblBienvenida.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.contenedorInicial)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 410, 181, 31))
        self.label_2.setFont(font)
        self.btnRegistro = QPushButton(self.contenedorInicial)
        self.btnRegistro.setObjectName(u"btnRegistro")
        self.btnRegistro.setGeometry(QRect(340, 410, 271, 31))
        self.btnRegistro.setFont(font)

        self.retranslateUi(LogIn)

        QMetaObject.connectSlotsByName(LogIn)
    # setupUi

    def retranslateUi(self, LogIn):
        LogIn.setWindowTitle(QCoreApplication.translate("LogIn", u"Form", None))
        self.btnLogo.setText("")
        self.lblCorreo.setText(QCoreApplication.translate("LogIn", u"Correo:", None))
        self.lblContrasena.setText(QCoreApplication.translate("LogIn", u"Contrase\u00f1a: ", None))
        self.btnLogIn.setText(QCoreApplication.translate("LogIn", u"Acceder", None))
        self.lblBienvenida.setText(QCoreApplication.translate("LogIn", u"\u00a1Bienvenid@!", None))
        self.label_2.setText(QCoreApplication.translate("LogIn", u"\u00bfNo tienes una cuenta?", None))
        self.btnRegistro.setText(QCoreApplication.translate("LogIn", u"Registrate", None))
    # retranslateUi

