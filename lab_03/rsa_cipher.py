import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_generate_keys.clicked.connect(self.call_api_gen_keys)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btn_sign.clicked.connect(self.call_api_sign)
        self.ui.btn_verify.clicked.connect(self.call_api_verify)

    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(data.get("message", "Keys generated"))
                msg.exec_()
            else:
                QMessageBox.warning(self, "Error", "Error while calling API generate keys")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Exception", str(e))

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/encrypt"
        payload = {"message": self.ui.textEdit.toPlainText(), "key_type": "public"}
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.textEdit_3.setText(data.get("encrypted_message", ""))
                QMessageBox.information(self, "Success", "Encrypted Successfully")
            else:
                QMessageBox.warning(self, "Error", "Error while calling API encrypt")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Exception", str(e))

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/decrypt"
        payload = {"ciphertext": self.ui.textEdit_3.toPlainText(), "key_type": "private"}
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.textEdit.setText(data.get("decrypted_message", ""))
                QMessageBox.information(self, "Success", "Decrypted Successfully")
            else:
                QMessageBox.warning(self, "Error", "Error while calling API decrypt")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Exception", str(e))

    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/rsa/sign"
        payload = {"message": self.ui.textEdit_2.toPlainText()}
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.textEdit_4.setText(data.get("signature", ""))
                QMessageBox.information(self, "Success", "Signed Successfully")
            else:
                QMessageBox.warning(self, "Error", "Error while calling API sign")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Exception", str(e))

    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/rsa/verify"
        payload = {
            "message": self.ui.textEdit_2.toPlainText(),
            "signature": self.ui.textEdit_4.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                if data.get("is_verified", False):
                    msg.setText("Verified Successfully")
                else:
                    msg.setText("Verification Failed")
                msg.exec_()
            else:
                QMessageBox.warning(self, "Error", "Error while calling API verify")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Exception", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
