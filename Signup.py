import sqlite3
import re
from PyQt6.QtWidgets import QDialog, QMessageBox
from Signup_ui import Ui_Dialog

class SignupDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.btnsave.clicked.connect(self.save_user)
        self.ui.btnclose.clicked.connect(self.back_main)

    def validate_nic(self, nic): 
        nic = nic.strip().upper()

        # Old NIC format (9 digits + V/X)
        old_pattern = r'^\d{9}[VX]$'

        # New NIC format (12 digits)
        new_pattern = r'^\d{12}$'

        if re.match(old_pattern, nic):
            return True

        if re.match(new_pattern, nic):
            return True

        return False

    def save_user(self):
        name = self.ui.txtname.text().strip()
        nic = self.ui.txtnic.text().strip()
        username = self.ui.txtuser.text().strip()
        pwd = self.ui.txtpwd.text().strip()
        pwd2 = self.ui.txtpwd2.text().strip()

        if not name:
            QMessageBox.warning(self, "Validation", "Please enter name")
            return
        
        if not self.validate_nic(nic):
            QMessageBox.warning(
            self,
            "Validation Error",
            "Please enter a valid NIC number"
            )
            return
        
        if not username:
            QMessageBox.warning(self, "Validation", "Please enter username")
            return
        
        if not pwd:
            QMessageBox.warning(self, "Validation", "Please enter a password")
            return
        
        if pwd != pwd2:
            QMessageBox.warning(
            self,
            "Validation",
            "Passwords do not match"
            )
            return

        try:
            conn = sqlite3.connect("library.db")
            cursor = conn.cursor()

            cursor.execute("""
            INSERT INTO Users
            (Name, NIC, UserName, PWD)
            VALUES (?, ?, ?, ?)
            """, (name, nic, username, pwd))

            conn.commit()
            conn.close()

            QMessageBox.information(
            self,
            "Success",
            "User saved successfully"
            )
            self.close()
            

        except Exception as e:
            QMessageBox.critical(
            self,
            "Error",
            str(e)
        )
            
    def clear_fields(self):
        self.ui.txtname.clear()
        self.ui.txtnic.clear()
        self.ui.txtuser.clear()
        self.ui.txtpwd.clear()
        self.ui.txtpwd2.clear()

    def back_main(self):
        
        self.close()