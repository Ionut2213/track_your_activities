from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt
import sys



class FullScreenApp(QWidget):
    def __init__(self):
        super().__init__()



        self.setWindowTitle("Aplicatie management task uri")
        self.showMaximized()

        self.setStyleSheet("background-color: green;")


    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape:
            self.close()


app = QApplication(sys.argv)

window = FullScreenApp()
window.show()


sys.exit(app.exec())