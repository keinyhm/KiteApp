from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Qt
from app.view.VentanaPrincipal_ui import Ui_VentanaPrincipal
from app import resources_rc

class VentanaPrincipal(QMainWindow):
    def __init__(self, session: dict, perfil: dict):
        super().__init__()
        self.session = session
        self.perfil = perfil
        
        self.ui = Ui_VentanaPrincipal()
        self.ui.setupUi(self)
        #self.showMaximized()
        self.ui.btnCerrarSesion.clicked.connect(self.cerrar_sesion)

        self.setWindowTitle("Kite - Panel de Administración")

        nombre = self.perfil.get("nombre", "Administrador")
        self.statusBar().showMessage(f"Sesión iniciada como: {nombre} (ADMIN)")

        if self.perfil.get("esAdmin") is not True:
            QMessageBox.critical(self, "Acceso denegado", "Solo ADMIN puede acceder al panel.")
            self.close()
            return
        
    def closeEvent(self, event):
        # si quieres preguntar al cerrar:
        reply = QMessageBox.question(
            self,
            "Salir",
            "¿Quieres cerrar Kite?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def cerrar_sesion(self):
      reply = QMessageBox.question(
        self,
        "Cerrar sesión",
        "¿Seguro que quieres cerrar sesión?",
        QMessageBox.Yes | QMessageBox.No
      )

      if reply != QMessageBox.Yes:
        return

      # Limpiar sesión
      self.session.clear()

      # Volver a Login
      from app.controller.login import Login
      self.login = Login()
      self.login.show()

      # Cerrar ventana principal
      self.close()

