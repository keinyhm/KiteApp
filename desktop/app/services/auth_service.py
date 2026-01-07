import requests

class AuthService:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def login(self, email: str, password: str) -> dict:
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={self.api_key}"
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }

        r = requests.post(url, json=payload, timeout=15)
        data = r.json()

        if r.status_code != 200:
            msg = data.get("error", {}).get("message", "LOGIN_ERROR")
            raise ValueError(msg)

        return {
            "uid": data["localId"],
            "idToken": data["idToken"]
        }

    def sign_up(self, email: str, password: str) -> dict:
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={self.api_key}"
        payload = {"email": email, "password": password, "returnSecureToken": True}
        r = requests.post(url, json=payload, timeout=15)
        data = r.json()
        if r.status_code != 200:
            msg = data.get("error", {}).get("message", "SIGNUP_ERROR")
            raise ValueError(msg)
        return {"uid": data["localId"]}