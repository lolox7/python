import sys,random
from PySide6 import QtCore,QtWidgets,QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt","Hei maailma","Bonjour le monde","Hola mundo","Hello world"]

        self.text = QtWidgets.QLabel("Hello world", alignment=QtCore.Qt.AlignCenter)
        self.button = QtWidgets.QPushButton("Click me!")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)
    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.resize(1080, 720)
    widget.show()

    sys.exit(app.exec())