from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton

class SignUpWindow(QDialog):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Sign Up")
        self.setFixedSize(300, 200)


        self.layout = QVBoxLayout()


        self.user_label = QLabel("Username:", self)
        self.user_input = QLineEdit(self)



        self.password_label = QLabel("Password:", self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)


        self.signup_button = QPushButton("Sign Up", self)
        self.signup_button.clicked.connect(self.handle_signup)

        self.layout.addWidget(self.user_label)
        self.layout.addWidget(self.user_input)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.signup_button)


        self.setLayout(self.layout)

    def handle_signup(self):
        username = self.user_input.text()
        password = self.password_input.text()
        print(f"Username: {username}, Password: {password} " )

        self.accept()
