import sqlite3
from PyQt6.QtWidgets import QMainWindow, QMenu, QMessageBox
from Addbooks_ui import Ui_MainWindow

class AddWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnsave.clicked.connect(self.save_book)
        self.ui.btnclr.clicked.connect(self.clear_fields)
        self.ui.btnclose.clicked.connect(self.back_home)

    def save_book(self):
        bid = self.ui.txtBookId.text().strip()
        title = self.ui.txtTitle.text().strip()
        author = self.ui.txtAuthor.text().strip()
        category = self.ui.cmbCategory.currentText()
        publisher = self.ui.txtPublisher.text().strip()
        isbn = self.ui.txtISBN.text().strip()
        quantity = self.ui.spnQuantity.value()
        price = self.ui.spnPrice.value()

        if not title:
            QMessageBox.warning(self, "Validation", "Please enter book title")
            return

        try:
            conn = sqlite3.connect("library.db")
            cursor = conn.cursor()

            cursor.execute("""
            INSERT INTO Books
            (BID, Title, Author, Category, Publisher, ISBN, Quantity, Price)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (bid, title, author, category, publisher, isbn, quantity, price))

            conn.commit()
            conn.close()

            QMessageBox.information(
            self,
            "Success",
            "Book saved successfully"
            )

            self.clear_fields()

        except Exception as e:
            QMessageBox.critical(
            self,
            "Error",
            str(e)
        )
            
    def clear_fields(self):
        self.ui.txtBookId.clear()
        self.ui.txtTitle.clear()
        self.ui.txtAuthor.clear()
        self.ui.cmbCategory.setCurrentIndex(0)
        self.ui.txtPublisher.clear()
        self.ui.txtISBN.clear()
        self.ui.spnQuantity.setValue(0)
        self.ui.spnPrice.setValue(0)

    def back_home(self):
        from Home import HomeWindow
        self.back = HomeWindow()
        self.back.show()
        self.close()