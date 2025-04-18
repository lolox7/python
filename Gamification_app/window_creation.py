from PySide6.QtWidgets import QApplication,QLabel

class Personnage:
    def __init__(self):
        self.last_name = "last_name "
        self.first_name = "first_name"


if __name__ == "__main__":
    app = QApplication([])
    Personnage = QLabel(f"Hello {Personnage.first_name}{Personnage.last_name}")
    Personnage.resize(1080, 720)
    Personnage.show()

    app.exec()
     