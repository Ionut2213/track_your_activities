from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt
import sys



class FullScreenApp(QWidget):
    def __init__(self):
        super().__init__()



        self.setWindowTitle("Aplicatie management task uri")
        self.showMaximized()

        self.setStyleSheet("background-color: green;")

        self.layout = QVBoxLayout()

        self.central_label = QLabel("Welcome, Welcome !", self)
        self.central_label.setStyleSheet("color: white; font-size:24px;")
        self.central_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.central_label)


        self.setLayout(self.layout)










    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape:
            self.close()


if __name__ == "__main__":


    app = QApplication(sys.argv)

    window = FullScreenApp()
    window.show()


    sys.exit(app.exec())