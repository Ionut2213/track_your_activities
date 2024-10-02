
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton


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


    def handle_login(self):
        username = self.user_input.text()
        password = self.password_input.text()

        print(f"Login attempt - Username: {username}, Password: {password}")

        self.accept()


