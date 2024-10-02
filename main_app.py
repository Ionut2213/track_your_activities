from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt
import sys

from sign_up_window import SignUpWindow
from login_window import LoginWindow
from database import create_users_table

class FullScreenApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplicatie management task uri")
        self.showMaximized()
        self.setStyleSheet("background-color: green;")

        self.layout = QVBoxLayout()

        # Partea pentru butoanele signup/login
        button_layout = QHBoxLayout()
        self.login_button = QPushButton("Login", self)
        self.signup_button = QPushButton("Signup", self)
        self.login_button.setStyleSheet("background-color: white; color:black; font-size:18px;")
        self.signup_button.setStyleSheet("background-color: white; color:black; font-size:18px")
        
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(self.signup_button)
        button_layout.setAlignment(Qt.AlignTop | Qt.AlignRight)
        
        self.layout.addLayout(button_layout)

        self.layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        welcome_text = (
            "Welcome! If you want access to a platform where you can keep track of your daily activities "
            "along with many other useful features, then this application is perfect for you. "
            "Click the Sign Up button now and start exploring!"
        )

        self.central_label = QLabel(welcome_text, self)
        self.central_label.setStyleSheet("color: white; font-size:24px;")
        self.central_label.setWordWrap(True)

        self.central_label.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(self.central_label)
        self.layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.setLayout(self.layout)

        self.signup_button.clicked.connect(self.open_signup_window)

        self.login_button.clicked.connect(self.open_login_window)
    

    def open_signup_window(self):
        signup_window = SignUpWindow()
        signup_window.exec()

    def open_login_window(self):
        login_window = LoginWindow()
        login_window.exec()

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape:
            self.close()


if __name__ == "__main__":
    create_users_table()
    app = QApplication(sys.argv)
    window = FullScreenApp()
    window.show()
    sys.exit(app.exec())
