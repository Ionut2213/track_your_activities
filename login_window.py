from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from database import verify_user

from dasboard_window import DashboardWindow



class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        
        layout = QVBoxLayout()

        self.username_input = QLineEdit(self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)


        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.username_input)

        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.password_input)

        login_button = QPushButton("Login", self)
        login_button.clicked.connect(self.handle_login)
        layout.addWidget(login_button)

        self.setLayout(layout)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if verify_user(username, password):
            print(f"Opening dashboard for user: {username}")
            self.accept()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")
