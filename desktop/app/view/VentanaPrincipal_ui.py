# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaPrincipal.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)
from app import resources_rc

class Ui_VentanaPrincipal(object):
    def setupUi(self, VentanaPrincipal):
        if not VentanaPrincipal.objectName():
            VentanaPrincipal.setObjectName(u"VentanaPrincipal")
        VentanaPrincipal.resize(1002, 700)
        self.centralwidget = QWidget(VentanaPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#menuPrincipal{\n"
"  background-color: #ffffff;\n"
"}\n"
"\n"
"#menuIzquierda{\n"
"   background-color: #00273d;\n"
"}")
        self.menuIzquierda = QWidget(self.centralwidget)
        self.menuIzquierda.setObjectName(u"menuIzquierda")
        self.menuIzquierda.setGeometry(QRect(10, 10, 261, 631))
        self.menuIzquierda.setStyleSheet(u"bg: #00273d\n"
"")
        self.logo = QWidget(self.menuIzquierda)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(80, 20, 91, 71))
        self.ll = QPushButton(self.logo)
        self.ll.setObjectName(u"ll")
        self.ll.setGeometry(QRect(10, 0, 71, 71))
        icon = QIcon()
        icon.addFile(u":/assets/logo1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ll.setIcon(icon)
        self.ll.setIconSize(QSize(101, 71))
        self.botones = QWidget(self.menuIzquierda)
        self.botones.setObjectName(u"botones")
        self.botones.setGeometry(QRect(30, 140, 220, 411))
        self.botones.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(self.botones)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnActivos = QPushButton(self.botones)
        self.btnActivos.setObjectName(u"btnActivos")

        self.verticalLayout.addWidget(self.btnActivos)

        self.btnUbicaciones = QPushButton(self.botones)
        self.btnUbicaciones.setObjectName(u"btnUbicaciones")

        self.verticalLayout.addWidget(self.btnUbicaciones)

        self.btnMovimientos = QPushButton(self.botones)
        self.btnMovimientos.setObjectName(u"btnMovimientos")

        self.verticalLayout.addWidget(self.btnMovimientos)

        self.btnUsuarios = QPushButton(self.botones)
        self.btnUsuarios.setObjectName(u"btnUsuarios")

        self.verticalLayout.addWidget(self.btnUsuarios)

        self.btnCerrarSesion = QPushButton(self.botones)
        self.btnCerrarSesion.setObjectName(u"btnCerrarSesion")

        self.verticalLayout.addWidget(self.btnCerrarSesion)

        self.menuPrincipal = QWidget(self.centralwidget)
        self.menuPrincipal.setObjectName(u"menuPrincipal")
        self.menuPrincipal.setGeometry(QRect(270, 10, 731, 631))
        self.encabezado = QWidget(self.menuPrincipal)
        self.encabezado.setObjectName(u"encabezado")
        self.encabezado.setGeometry(QRect(0, 0, 731, 91))
        self.widget = QWidget(self.encabezado)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 211, 81))
        self.contenedor = QWidget(self.menuPrincipal)
        self.contenedor.setObjectName(u"contenedor")
        self.contenedor.setGeometry(QRect(0, 90, 731, 541))
        VentanaPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(VentanaPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1002, 33))
        VentanaPrincipal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(VentanaPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        VentanaPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(VentanaPrincipal)

        QMetaObject.connectSlotsByName(VentanaPrincipal)
    # setupUi

    def retranslateUi(self, VentanaPrincipal):
        VentanaPrincipal.setWindowTitle(QCoreApplication.translate("VentanaPrincipal", u"MainWindow", None))
        self.ll.setText("")
        self.btnActivos.setText(QCoreApplication.translate("VentanaPrincipal", u"Activos", None))
        self.btnUbicaciones.setText(QCoreApplication.translate("VentanaPrincipal", u"Ubicaciones", None))
        self.btnMovimientos.setText(QCoreApplication.translate("VentanaPrincipal", u"Movimientos", None))
        self.btnUsuarios.setText(QCoreApplication.translate("VentanaPrincipal", u"Usuarios", None))
        self.btnCerrarSesion.setText(QCoreApplication.translate("VentanaPrincipal", u"cerrar sesi\u00f3n", None))
    # retranslateUi

