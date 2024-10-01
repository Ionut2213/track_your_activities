from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt
import sys



class FullScreenApp(QWidget):
    def __init__(self):
        super().__init__()



        self.setWindowTitle("Aplicatie management task uri")
        self.showMaximized()

        self.setStyleSheet("background-color: green;")

        # self.layout = QVBoxLayout()

        # Partea pentru butoanele signup/login

        
        self.layout = QHBoxLayout()

        button_layout = QHBoxLayout()

        self.login_button = QPushButton("Login", self)
        self.signup_button = QPushButton("Signup", self)

        self.login_button.setStyleSheet("background-color: white; color:black; font-size:18px;")
        self.signup_button.setStyleSheet("background-color: white; color:black; font-size:18px")
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(self.signup_button)
        button_layout.setAlignment(Qt.AlignTop | Qt.AlignRight)
        self.layout.addLayout(button_layout)
        self.setLayout(self.layout)





        # self.central_label = QLabel("Welcome, Welcome !", self)
        # self.central_label.setStyleSheet("color: white; font-size:24px;")
        # self.central_label.setAlignment(Qt.AlignCenter)
        # self.layout.addWidget(self.central_label)


        self.setLayout(self.layout)










    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape:
            self.close()


if __name__ == "__main__":


    app = QApplication(sys.argv)

    window = FullScreenApp()
    window.show()


    sys.exit(app.exec())