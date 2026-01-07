import sys
from PySide6.QtWidgets import QApplication
from pathlib import Path
from PySide6.QtGui import QFontDatabase

from app.services.firestore_service import FirestoreService

SERVICE_ACCOUNT = "credentials/serviceAccountKey.json"
fs = FirestoreService(SERVICE_ACCOUNT)

def cargar_estilos(app: QApplication):
    qss_path = Path(__file__).parent / "app" / "styles" / "app.qss"
    if qss_path.exists():
        app.setStyleSheet(qss_path.read_text(encoding="utf-8"))


BASE_DIR = Path(__file__).resolve().parent  # /desktop
FONTS_DIR = BASE_DIR / "app" / "assets" / "fonts"


def load_font():
    QFontDatabase.addApplicationFont(str(FONTS_DIR / "Montserrat-Regular.ttf"))
    QFontDatabase.addApplicationFont(str(FONTS_DIR / "Montserrat-SemiBold.ttf"))
    QFontDatabase.addApplicationFont(str(FONTS_DIR / "Montserrat-Bold.ttf"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cargar_estilos(app)
    load_font()

    hay_admin = fs.existe_admin()
    print("¿HAY ADMIN EN FIRESTORE?:", hay_admin)

    if hay_admin:
        from app.controller.login import Login
        ventana = Login()
    else:
        from app.controller.registro import Registro
        ventana = Registro()  # setup admin

    ventana.show()
    sys.exit(app.exec())
