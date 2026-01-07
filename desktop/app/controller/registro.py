from PySide6.QtWidgets import QWidget, QMessageBox
from app.view.Registro_ui import Ui_Registro
import app.resources_rc
from app.services.auth_service import AuthService
from app.services.firestore_service import FirestoreService

API_KEY = "AIzaSyAky12H-k5PxXXaFnV6s9yj5eofTqNcJ54"
SERVICE_ACCOUNT = "credentials/serviceAccountKey.json"

auth = AuthService(API_KEY)
fs = FirestoreService(SERVICE_ACCOUNT)

class Registro(QWidget):
    def __init__(self, on_setup_completo=None):
        super().__init__()
        self.on_setup_completo = on_setup_completo

        self.ui = Ui_Registro()
        self.ui.setupUi(self)

 #       self.ui.btnInicioSesion.setText("Crear administrador (finalizar setup)")
#        self.ui.btnInicioSesion.clicked.connect(self.crear_admin)

        self.ui.btnRegistrar.clicked.connect(self.crear_admin)

    def abrir_ventana_login(self):
        from app.controller.login import Login
        self.ventanaLogin = Login()
        self.ventanaLogin.show()
        self.close()

    def crear_admin(self):
        # TODO implementar Firebase Auth + Firestore.
        QMessageBox.information(self, "OK", "Admin creado.")

        #marcamos  la bandera
        if self.on_setup_completo:
            self.on_setup_completo()

        self.abrir_ventana_login()
   
    def crear_admin(self):
        # AJUSTA estos nombres según tu Registro_ui.py
        email = self.ui.lnCorreo.text().strip()
        password = self.ui.lnContrasena.text().strip()
        nombre = getattr(self.ui, "lnNombre", None)
        nombre = nombre.text().strip() if nombre else "Administrador"

        if not email or not password:
            QMessageBox.warning(self, "Error", "Introduce correo y contraseña.")
            return

        try:
            # 1) crear usuario en Firebase Auth
            result = auth.sign_up(email, password)
            uid = result["uid"]

            # 2) crear perfil en Firestore
            fs.crear_perfil_usuario(uid, {
                "nombre": nombre,
                "correo": email,
                "esAdmin": True,
                "activo": True
            })

            # 3) marcar bandera
            if self.on_setup_completo:
                self.on_setup_completo()

            QMessageBox.information(self, "OK", "Administrador creado correctamente. Ahora inicia sesión.")

            # 4) volver a Login
            from app.controller.login import Login
            self.login = Login()
            self.login.show()
            self.close()

        except ValueError as e:
            QMessageBox.critical(self, "Error", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error inesperado: {e}")