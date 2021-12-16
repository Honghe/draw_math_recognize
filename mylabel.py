# -*- coding:utf-8 -*-
from PySide6.QtGui import QMouseEvent, QPainter, QPen, QPixmap
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QPointF, Qt

class Canvas(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        pixmap = QPixmap(620, 300)
        pixmap.fill(Qt.white)
        self.setPixmap(pixmap)
        
        # data
        self.last_x: float = None
        self.last_y: float = None

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self.last_x is None: # First event.
            self.last_x = event.position().x()
            self.last_y = event.position().y()
            return # Ignore the first time.

        canvas = self.pixmap()
        painter = QPainter(canvas)
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(Qt.black)
        painter.setPen(pen)
        painter.drawLine(QPointF(self.last_x, self.last_y), event.position())
        painter.end()
        self.setPixmap(canvas)

        # Update the origin for next time
        self.last_x = event.position().x()
        self.last_y = event.position().y()
    
    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self.last_x = None
        self.last_y = None

    def clear(self):
        pixmap = self.pixmap()
        pixmap.fill(Qt.white)
        self.setPixmap(pixmap)
        # self.update()