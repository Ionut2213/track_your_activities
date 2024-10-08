
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy, QDialog
import sys
from PySide6.QtCore import Qt
from sign_up_window import SignUpWindow
from login_window import LoginWindow
from database import create_users_table
from dasboard_window import DashboardWindow

class FullScreenApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplicatie management task uri")
        self.showMaximized()
        self.setStyleSheet("background-color:blue;")

        self.layout = QVBoxLayout()

        button_layout = QHBoxLayout()
        self.login_button = QPushButton("Login", self)
        self.signup_button = QPushButton("Signup", self)
        self.login_button.setStyleSheet("background-color: white; color:black; font-size:18px;")
        self.signup_button.setStyleSheet("background-color: white; color:black; font-size:18px")
        
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(self.signup_button)
        button_layout.setAlignment(Qt.AlignTop | Qt.AlignRight)
        
        self.layout.addLayout(button_layout)

        welcome_text = "Welcome! If you want access to a platform where you can keep track of your daily activities, click the Sign Up button now and start exploring!"
        self.central_label = QLabel(welcome_text, self)
        self.central_label.setStyleSheet("color: white; font-size:24px;")
        self.central_label.setWordWrap(True)
        self.central_label.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(self.central_label)
        self.setLayout(self.layout)

        self.signup_button.clicked.connect(self.open_signup_window)
        self.login_button.clicked.connect(self.open_login_window)


    def open_signup_window(self):
        signup_window = SignUpWindow()
        signup_window.exec()

    def open_login_window(self):
        login_window = LoginWindow()
        if login_window.exec() == QDialog.Accepted:
            username = login_window.username_input.text()
            self.open_dashboard(username)

    def open_dashboard(self, username):
        self.dashboard_window = DashboardWindow(username)
        self.dashboard_window.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

if __name__ == "__main__":
    create_users_table()
    app = QApplication(sys.argv)
    window = FullScreenApp()
    window.show()
    sys.exit(app.exec())