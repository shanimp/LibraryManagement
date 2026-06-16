# login.py
import sqlite3
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from mainwindow_ui import Ui_MainWindow
from Home import HomeWindow
from Signup import SignupDialog

class LoginWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnlogin.setVisible(True)
        self.ui.btnlogin.raise_()  # Bring to front

        # Debug: Check if button exists and is enabled
        print(f"Button exists: {hasattr(self.ui, 'btnlogin')}")
        print(f"Button enabled: {self.ui.btnlogin.isEnabled()}")
        print(f"Button visible: {self.ui.btnlogin.isVisible()}")

        # Try connecting to different signals
        self.ui.btnlogin.clicked.connect(self.login)
        self.ui.pushButton.clicked.connect(self.open_signup)
        # Also try pressed signal for debugging
        self.ui.btnlogin.pressed.connect(lambda: print("Button pressed!"))


    def login(self):
        print("Login function called!")  # This should print if clicked
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        if not username:
            QMessageBox.warning(
            self,
            "Validation",
            "Please enter username"
            )
            return

        if not password:
            QMessageBox.warning(
            self,
            "Validation",
            "Please enter password"
            )
            return
        
        try:
            conn = sqlite3.connect("library.db")
            cursor = conn.cursor()

            cursor.execute("""
                SELECT * FROM Users WHERE UserName = ? AND PWD = ?
            """, (username, password))

            user = cursor.fetchone()

            conn.close()

            if user:
                self.home = HomeWindow()
                self.home.show()
                self.close()

            else:
                QMessageBox.warning(
                self,
                "Login Failed",
                "Invalid username or password"
                )

        except Exception as e:
            QMessageBox.critical(
            self,
            "Error",
            str(e)
            )

    def open_signup(self):
        self.signup_window = SignupDialog()
        self.signup_window.show()
