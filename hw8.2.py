import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QCheckBox, QPushButton, QGridLayout, QWidget
from PyQt5.QtGui import QFont


class Window1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QGridLayout")
        self.resize(400, 200)
        self.setFont(QFont('Georgia', 12))

        self.label = QLabel("Введите текст:")
        self.line_edit = QLineEdit()
        self.line_edit.setEchoMode(QLineEdit.Password)

        self.check_box = QCheckBox("Разблокировать проверку")
        self.button = QPushButton("Проверить")
        self.button.setEnabled(False)

        self.check_box.toggled.connect(self.toggle_button)

        self.button.clicked.connect(self.check_input)

        layout = QGridLayout()
        layout.addWidget(self.label, 0, 0)
        layout.addWidget(self.line_edit, 0, 1)
        layout.addWidget(self.check_box, 1, 0, 1, 2)
        layout.addWidget(self.button, 2, 0, 1, 2)
        self.setLayout(layout)

    def toggle_button(self):
        if self.check_box.isChecked():
            self.button.setEnabled(True)
        else:
            self.button.setEnabled(False)

    def check_input(self):
        text = self.line_edit.text()
        if text.isdigit():
            self.label.setText("Цифры")
        elif text.isalpha():
            self.label.setText("Буквы")
        else:
            self.label.setText("Другое")


def open_window():
    app = QApplication(sys.argv)
    wind = Window1()
    wind.show()
    sys.exit(app.exec_())


open_window()