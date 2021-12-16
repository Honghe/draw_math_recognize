import os
import sys
from PySide6.QtGui import QPainter, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
from mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Math OCR")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        canvas = QPixmap(620, 300)
        canvas.fill(Qt.white)
        self.ui.label.setPixmap(canvas)

        self.draw_something()

    def draw_something(self):
        canvas = self.ui.label.pixmap()
        painter = QPainter(canvas)
        painter.drawLine(10,10,300,200)
        painter.end()
        self.ui.label.setPixmap(canvas)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()

    sys.exit(app.exec())