from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton

from PySide6.QtCore import Qt
import datetime


class NotesWindow(QWidget):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Notes")
        self.showFullScreen()
        self.setStyleSheet("background-color: lightgray;")

        layout = QVBoxLayout()

        title_label = QLabel("Create a new note")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title_label)


        self.note_name_input = QLineEdit()
        self.note_name_input.setPlaceholderText("Note Name")
        layout.addWidget(self.note_name_input)



        self.importance_combo = QComboBox()
        self.importance_combo.addItems(["Low", "Medium", "High"])
        layout.addWidget(QLabel("Importance:"))
        layout.addWidget(self.importance_combo)



        self.date_label = QLabel(f"Date: {datetime.date.today()}")
        layout.addWidget(self.date_label)



        self.save_button = QPushButton("Save Note")
        self.save_button.clicked.connect(self.save_note)
        layout.addWidget(self.save_button)


        self.setLayout(layout)

    
    def save_note(self):
        note_name = self.note_name_input.text()
        importance = self.importance_combo.currentText()
        date = self.date_label.text().split(": ")[1]


        print(f"Note saved: Name: {note_name}, Importance: {importance}, Date: {date}")

        self.note_name_input.clear()
