from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout



class DashboardWindow(QWidget):
    def __init__(self, username):
        super().__init__()
        self.setWindowTitle("Dashboard")
        self.setFixedSize(400, 300)

        layout = QVBoxLayout()

        welcome_label = QLabel(f"Welcome, {username}!", self)
        layout.addWidget(welcome_label)



        button_layout = QHBoxLayout()
        notes_button = QPushButton("Notite")
        quizzes_button = QPushButton("Quiz-uri")
        tests_button = QPushButton("Teste matematica")

        

        button_layout.addWidget(notes_button)
        button_layout.addWidget(quizzes_button)
        button_layout.addWidget(tests_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

        print("Dashboard initialized")