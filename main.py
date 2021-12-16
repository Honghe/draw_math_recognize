import os
import sys
from PySide6.QtGui import QMouseEvent, QPainter, QPen, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QPointF, Qt
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

        # data
        self.last_x: float = None
        self.last_y: float = None

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self.last_x is None: # First event.
            self.last_x = event.position().x()
            self.last_y = event.position().y()
            return # Ignore the first time.

        canvas = self.ui.label.pixmap()
        painter = QPainter(canvas)
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(Qt.black)
        painter.setPen(pen)
        painter.drawLine(QPointF(self.last_x, self.last_y), event.position())
        painter.end()
        self.ui.label.setPixmap(canvas)

        # Update the origin for next time
        self.last_x = event.position().x()
        self.last_y = event.position().y()
    
    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self.last_x = None
        self.last_y = None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()

    sys.exit(app.exec())