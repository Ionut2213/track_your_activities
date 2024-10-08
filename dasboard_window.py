from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy, QDialog
from PySide6.QtCore import Qt


class DashboardWindow(QWidget):
    def __init__(self, username):
        super().__init__()


        self.setWindowTitle("Dashboard")
        self.showMaximized()
        self.setStyleSheet("background-color:blue;")


        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)


        welcome_label = QLabel(f"Welcome, {username}!", self)
        welcome_label.setStyleSheet("font-size: 24px; color: white;")
        main_layout.addWidget(welcome_label)




        button_layout = QHBoxLayout()
        button_layout.setSpacing(20)



        self.notes_button = QPushButton("Notita")
        self.quizzes_button = QPushButton("Quiz-uri")
        self.tests_button = QPushButton("Teste Matematica")


        button_style = """
        QPushButton {
            background-color: white;
            color: black;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 10px;
        
        }
        QPushButton:hover {
            background-color: lightgray;
        }
        """

        self.notes_button.setStyleSheet(button_style)
        self.quizzes_button.setStyleSheet(button_style)
        self.tests_button.setStyleSheet(button_style)




        button_layout.addWidget(self.notes_button)
        button_layout.addWidget(self.quizzes_button)
        button_layout.addWidget(self.tests_button)







        main_layout.addLayout(button_layout)

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addItem(spacer)

        self.setLayout(main_layout)



        

        
        self.layout.addLayout(button_layout)

        layout.addLayout(button_layout)

        self.setLayout(layout)

        print("Dashboard initialized")