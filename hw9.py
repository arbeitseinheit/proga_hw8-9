import sys
import string
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QDockWidget, QLineEdit, QVBoxLayout, QWidget, QAction, QMessageBox, QPushButton, QLabel
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('удаление пунктуации')
        self.setGeometry(100, 100, 600, 400)

        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)
        self.dock = QDockWidget('путь к файл', self)
        self.dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.line_edit = QLineEdit(self)
        self.dock.setWidget(self.line_edit)
        self.addDockWidget(Qt.TopDockWidgetArea, self.dock)

        self.statusBar()

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('файл')

        open_action = QAction('открыть файл', self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        remove_punctuation_action = QAction('удалить пунктуацию', self)
        remove_punctuation_action.triggered.connect(self.remove_punctuation)
        file_menu.addAction(remove_punctuation_action)

        continue_action = QAction('продолжить', self)
        continue_action.triggered.connect(self.continue_to_next_window)
        file_menu.addAction(continue_action)


    def open_file(self):
        file_path = self.line_edit.text()
        if not file_path:
            QMessageBox.warning(self, 'ошибка ввода', 'введите валидный путь до файла')
            return

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                self.text_edit.setText(content)
        except FileNotFoundError:
            QMessageBox.warning(self, 'ошибка', 'файл не найден')
        except UnicodeDecodeError:
            QMessageBox.warning(self, 'Error', 'Unable to decode the file. Make sure it is in UTF-8 encoding.')
        except Exception as e:
            QMessageBox.warning(self, 'Error', f"An error occurred: {str(e)}")


    def remove_punctuation(self):
        text = self.text_edit.toPlainText()
        extended_punctuation = string.punctuation + '«»—…'

        removed_count = sum(1 for char in text if char in extended_punctuation)
        text_without_punctuation = ''.join(char for char in text if char not in extended_punctuation)

        self.text_edit.setText(text_without_punctuation)
        self.removed_count = removed_count


    def continue_to_next_window(self):
        self.next_window = NextWindow(self.text_edit.toPlainText(), self.removed_count)
        self.next_window.show()
        self.hide()


class NextWindow(QWidget):
    def __init__(self, text, removed_count):
        super().__init__()
        self.initUI(text, removed_count)


    def initUI(self, text, removed_count):
        self.setWindowTitle('обработанный текст')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.label = QLabel(f"кол-во удалённых знаков: {removed_count}", self)
        layout.addWidget(self.label)

        self.text_edit = QTextEdit(self)
        self.text_edit.setText(text)
        layout.addWidget(self.text_edit)

        self.save_button = QPushButton('сохранить', self)
        self.save_button.clicked.connect(self.save_text)
        layout.addWidget(self.save_button)

        self.back_button = QPushButton('назад', self)
        self.back_button.clicked.connect(self.back_to_main)
        layout.addWidget(self.back_button)

        self.setLayout(layout)


    def save_text(self):
        file_path = 'processed_text.txt'
        with open(file_path, 'w') as file:
            file.write(self.text_edit.toPlainText())
        QMessageBox.information(self, 'инфо', 'текст сохранён')


    def back_to_main(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()


def open_window():
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())


open_window()
