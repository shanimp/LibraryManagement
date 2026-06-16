import sqlite3
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QAbstractItemView
from Searchbooks_ui import Ui_MainWindow

class SearchWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_books()

        self.ui.tablebooks.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )

        self.ui.btnsearch.clicked.connect(self.search_books)
        self.ui.btnclear.clicked.connect(self.clear_table)
        self.ui.btnback.clicked.connect(self.back_home)


    def load_books(self):
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT BID, Title, Author,
                    Category, Publisher, ISBN, Quantity, Price, AddedDate
                    FROM Books
        """)

        rows = cursor.fetchall()

        self.ui.tablebooks.setRowCount(len(rows))

        for row_num, row_data in enumerate(rows):
            for col_num, data in enumerate(row_data):
                self.ui.tablebooks.setItem(
                    row_num,
                    col_num,
                    QTableWidgetItem(str(data))
                )

        conn.close()
        

    def search_books(self):
        keyword = self.ui.txtsearch.text().strip()

        try:
            conn = sqlite3.connect("library.db")
            cursor = conn.cursor()

            if self.ui.radioTitle.isChecked():
                cursor.execute("""
                    SELECT BID, Title, Author,
                    Category, Publisher, ISBN, Quantity, Price, AddedDate
                    FROM Books
                    WHERE Title LIKE ?
                    """, (f"%{keyword}%",))

            elif self.ui.radioAuthor.isChecked():
                cursor.execute("""
                    SELECT BID, Title, Author,
                    Category, Publisher, ISBN, Quantity, Price, AddedDate
                    FROM Books
                    WHERE Author LIKE ?
                """, (f"%{keyword}%",))

            else:
                QMessageBox.warning(
                    self,
                    "Search",
                    "Please select Title or Author"
                )
                return

            rows = cursor.fetchall()
            conn.close()

            self.ui.tablebooks.setRowCount(len(rows))

            for row_num, row_data in enumerate(rows):
                for col_num, value in enumerate(row_data):
                    self.ui.tablebooks.setItem(
                    row_num,
                    col_num,
                    QTableWidgetItem(str(value))
                    )

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def clear_table(self):
        self.ui.tablebooks.setRowCount(0)
        self.ui.txtsearch.clear()

    def back_home(self):
        from Home import HomeWindow
        self.back = HomeWindow()
        self.back.show()
        self.close()