
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from database import verify_user

from dasboard_window import DashboardWindow

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Login")
        self.setFixedSize(300, 200)


        self.layout = QVBoxLayout()

        self.user_label = QLabel("Username:", self)
        self.user_input = QLineEdit(self)


        self.password_label = QLabel("Password:", self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login", self)
        self.login_button.clicked.connect(self.handle_login)



        self.layout.addWidget(self.user_label)
        self.layout.addWidget(self.user_input)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.login_button)

        self.setLayout(self.layout)

        self.dashboard_window = None

    def handle_login(self):
        username = self.user_input.text()
        password = self.password_input.text()

        if not username or not password:
            QMessageBox.warning(self, "Error", "Please enter both username and password")
            return
        
        if verify_user(username, password):
            QMessageBox.information(self, "Success", "Login successfully!")
            self.open_dashboard(username)


        else:
            QMessageBox.warning(self, "Error", "Incorrect username or password")


    def open_dashboard(self, username):
        self.dashboard_window = DashboardWindow(username)
        self.dashboard_window.show()

        self.close()

