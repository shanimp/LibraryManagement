# home.py

from PyQt6.QtWidgets import QMainWindow, QMenu
from Home_ui import Ui_MainWindow


class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.menu = QMenu(self)

        logout_action = self.menu.addAction("Logout")
        logout_action.triggered.connect(self.logout)

        self.ui.btnprofile.setMenu(self.menu)
        self.ui.btnprofile.setPopupMode(self.ui.btnprofile.ToolButtonPopupMode.InstantPopup)

        self.ui.btnadd.clicked.connect(self.addBooks)
        self.ui.btnsearch.clicked.connect(self.searchBooks)

    def logout(self):
        from Login import LoginWindow
        self.login = LoginWindow()
        self.login.show()
        self.close()

    def addBooks(self):
        from Addbooks import AddWindow
        self.Addbooks = AddWindow()
        self.Addbooks.show()
        self.close()

    def searchBooks(self):
        from Searchbooks import SearchWindow
        self.Searchbooks = SearchWindow()
        self.Searchbooks.show()
        self.close()