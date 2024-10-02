from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSizePolicy, QSpacerItem
from PySide6.QtCore import Qt


class DashboardWindow(QWidget):

    def __init__(self, username):
        super().__init__()

        self.username = username
        self.setWindowTitle("Workbench")
        self.setStyleSheet("background-color: #f0f0f0;")

        main_layout = QVBoxLayout()


        top_layout = QHBoxLayout()



        self.notes_button = QPushButton("Notes", self)
        self.quiz_button = QPushButton("Quiz", self)
        self.math_test_button = QPushButton("Math", self)


        self.notes_button.setStyleSheet("font-size: 18px; padding: 10px;")
        self.quiz_button.setStyleSheet("font-size: 18px; padding: 10px;")
        self.math_test_button.setStyleSheet("font-size: 18px; padding: 10px;")


        top_layout.addWidget(self.notes_button)
        top_layout.addWidget(self.quiz_button)
        top_layout.addWidget(self.math_test_button)

        top_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum))



        self.username_label = QLabel(f"User: {self.username}", self)
        self.username_label.setStyleSheet("font-size: 18px; font-weight: bold; margin-right: 10px;")


        self.logout_button = QPushButton("Logout", self)
        self.logout_button.setStyleSheet("font-size: 18px; padding: 10px; background-color: red; color:white;")
        self.logout_button.clicked.connect(self.logout)

        top_layout.addWidget(self.username_label)
        top_layout.addWidget(self.logout_button)



        main_layout.addLayout(top_layout)

        self.setLayout(main_layout)
    
    def logout(self):
        self.close()