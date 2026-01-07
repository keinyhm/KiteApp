from PySide6.QtWidgets import QWidget, QMessageBox
from app.view.LogIn_ui import Ui_LogIn
from app.services.auth_service import AuthService
from app.services.firestore_service import FirestoreService
from app.config import SETUP_FLAG_PATH
import app.resources_rc

API_KEY = "AIzaSyAky12H-k5PxXXaFnV6s9yj5eofTqNcJ54"
SERVICE_ACCOUNT = "credentials/serviceAccountKey.json"

auth = AuthService(API_KEY)
fs = FirestoreService(SERVICE_ACCOUNT)


class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LogIn()
        self.ui.setupUi(self)

        # Debug
        print("FLAG PATH:", SETUP_FLAG_PATH, "exists:", SETUP_FLAG_PATH.exists())

        self.ui.btnLogIn.clicked.connect(self.on_login_clicked)

        #  Mostrar/ocultar botón de crear admin según Firestore (NO según flag)
        try:
            hay_admin = fs.existe_admin()
        except Exception as e:
            hay_admin = False
            print("Error comprobando admin:", e)

        if hay_admin:
            self.ui.btnRegistro.hide()
            self.ui.label_2.hide()
        else:
            self.ui.btnRegistro.setText("Crear administrador (solo una vez)")
            self.ui.btnRegistro.clicked.connect(self.abrir_ventana_registro)

    def abrir_ventana_registro(self):
        from app.controller.registro import Registro
        self.ventanaRegistro = Registro(on_setup_completo=self.on_setup_complete)
        self.ventanaRegistro.show()
        self.close()

    def on_setup_complete(self):
        #  marca flag (opcional) y vuelve a login
        SETUP_FLAG_PATH.write_text("OK", encoding="utf-8")
        QMessageBox.information(self, "Listo", "Administrador creado. Ya puedes iniciar sesión.")

        # refrescar UI: ocultar registro ya que ahora hay admin
        try:
            if fs.existe_admin():
                self.ui.btnRegistro.hide()
                self.ui.label_2.hide()
        except Exception:
            pass

        self.show()

    def on_login_clicked(self):
        email = self.ui.lnCorreo.text().strip()
        password = self.ui.lnContrasena.text().strip()

        if not email or not password:
            QMessageBox.warning(self, "Error", "Introduce email y contraseña.")
            return

        try:
            # 1) Login en Firebase Auth
            session = auth.login(email, password)

            # 2) Perfil en Firestore
            perfil = fs.obtener_perfil_usuario(session["uid"])

            # Caso: NO hay perfil
            if not perfil:
                # Si NO hay admin → modo setup, manda a registro
                if not fs.existe_admin():
                    QMessageBox.information(self, "Setup", "No existe administrador. Vamos a crearlo.")
                    from app.controller.registro import Registro
                    self.reg = Registro(on_setup_completo=self.on_setup_complete)
                    self.reg.show()
                    self.close()
                    return

                # Si ya hay admin → usuario sin perfil
                QMessageBox.critical(
                    self,
                    "Error",
                    "Este usuario no tiene perfil. Pide al administrador que lo cree."
                )
                return

            #  Caso: SÍ hay perfil
            if perfil.get("esAdmin") is True:
                from app.controller.ventanaprincipal import VentanaPrincipal
                self.dashboard = VentanaPrincipal(session, perfil)
                self.dashboard.show()
                self.close()
            else:
                QMessageBox.warning(
                    self,
                    "Acceso denegado",
                    "Este usuario es TÉCNICO. El técnico usa la app móvil."
                )

        except ValueError as e:
            QMessageBox.critical(self, "Login fallido", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error inesperado: {e}")
