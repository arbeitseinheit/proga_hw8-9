import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon, QFont

class Window1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Hello world")
        self.resize(500, 200)
        self.setWindowIcon(QIcon('icon.png'))
        self.setFont(QFont('Georgia', 12))

        self.label1 = QLabel("Hello world!")
        self.line_edit = QLineEdit()
        self.button = QPushButton("Submit")
        self.button.clicked.connect(self.update_label)

        layout = QVBoxLayout()
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)
        layout.addWidget(self.label1)
        self.setLayout(layout)

    def update_label(self):
        text = self.line_edit.text()
        self.label1.setText(text)

def open_window():
    app = QApplication(sys.argv)
    wind = Window1()
    wind.show()
    sys.exit(app.exec_())

open_window()