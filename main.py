import os
import ssl
import sys

from PySide6.QtCore import QPointF, Qt
from PySide6.QtGui import QMouseEvent, QPainter, QPen, QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

from mylabel import Canvas
from mainwindow import Ui_MainWindow
import base64
import argparse
import requests

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Math OCR")
        
        self.ui.clearButton.clicked.connect(self.ui.label.clear)
        self.ui.recognizeButton.clicked.connect(self.recognize)

    def recognize(self):
        img = self.ui.label.export_image()
        img_b64 = base64.b64encode(img)
        img_msg = img_b64.decode('ascii')
        
        data = {'img': img_msg}
        r = requests.post(url, json=data)
        print(r.json())
        self.ui.textEdit.setText(r.text)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='api url')
    args = parser.parse_args()
    url = args.url

    app = QApplication()
    main = MainWindow()
    main.show()

    sys.exit(app.exec())
