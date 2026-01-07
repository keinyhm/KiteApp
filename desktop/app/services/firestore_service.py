import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime, timezone


class FirestoreService:
    
    def __init__(self, service_account_path: str):
#        print("FIRESTORE PROJECT:", self.db.project)

        if not firebase_admin._apps:
            cred = credentials.Certificate(service_account_path)
            firebase_admin.initialize_app(cred)

        self.db = firestore.client()

    def obtener_perfil_usuario(self, uid: str):
        doc = self.db.collection("usuarios").document(uid).get()
        if not doc.exists:
            return None
        return doc.to_dict()

    def crear_perfil_usuario(self, uid: str, data: dict):
        data = dict(data)
        data["createdAt"] = datetime.now(timezone.utc).isoformat()
        self.db.collection("usuarios").document(uid).set(data)

    def existe_admin(self) -> bool:
        # Busca 1 documento donde esAdmin == True
        docs = (
            self.db.collection("usuarios")
            .where("esAdmin", "==", True)
            .limit(1)
            .stream()
        )
        return any(True for _ in docs)