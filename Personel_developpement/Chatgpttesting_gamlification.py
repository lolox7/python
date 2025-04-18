from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget, QLabel, QPushButton, QProgressBar, QHBoxLayout, QTableWidget, QTableWidgetItem
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class ProfilWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Objectif Polymath - Profil")
        self.setGeometry(100, 100, 600, 400)

        self.total_xp = 0  # Initialiser l'XP total

        # Création du layout principal avec un QTabWidget (navigation par onglets)
        self.tabs = QTabWidget(self)
        self.tabs.addTab(self.create_profil_tab(), "Profil")
        self.tabs.addTab(self.create_quests_tab(), "Quêtes")
        self.tabs.addTab(self.create_talents_tab(), "Talents")
        self.tabs.addTab(self.create_tasks_tab(), "Tâches")

        # Layout général
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)

    def create_profil_tab(self):
        profil_tab = QWidget()
        layout = QVBoxLayout()

        # Photo de profil
        self.photo_label = QLabel(self)
        self.photo_pixmap = QPixmap("photo_profil.png")
        self.photo_label.setPixmap(self.photo_pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio))
        self.photo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Nom, niveau et pièces
        self.name_label = QLabel("Nom Prénom: John Doe")
        self.level_label = QLabel("Niveau: 1")
        self.pieces_label = QLabel("Pièces: 50")

        # Progression XP
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(20)

        # Ajouter les widgets dans l'onglet Profil
        layout.addWidget(self.photo_label)
        layout.addWidget(self.name_label)
        layout.addWidget(self.level_label)
        layout.addWidget(self.pieces_label)
        layout.addWidget(self.progress_bar)

        profil_tab.setLayout(layout)
        return profil_tab

    def create_quests_tab(self):
        quests_tab = QWidget()
        layout = QVBoxLayout()

        # Liste des quêtes
        self.quests_table = QTableWidget(self)
        self.quests_table.setRowCount(5)
        self.quests_table.setColumnCount(2)
        self.quests_table.setHorizontalHeaderLabels(['Quête', 'XP', 'Compléter'])

        # Exemple de quêtes
        self.quests_table.setItem(0, 0, QTableWidgetItem("Apprendre Python"))
        self.quests_table.setItem(0, 1, QTableWidgetItem("50"))
        self.quests_table.setItem(1, 0, QTableWidgetItem("Faire du sport"))
        self.quests_table.setItem(1, 1, QTableWidgetItem("30"))

        # Ajouter des boutons pour compléter les quêtes
        self.quest_button1 = QPushButton("Compléter Quête 1")
        self.quest_button2 = QPushButton("Compléter Quête 2")
        self.quest_button1.clicked.connect(lambda: self.complete_task(50))  # Ajoute 50 XP
        self.quest_button2.clicked.connect(lambda: self.complete_task(30))  # Ajoute 30 XP

        layout.addWidget(self.quests_table)
        layout.addWidget(self.quest_button1)
        layout.addWidget(self.quest_button2)

        quests_tab.setLayout(layout)
        return quests_tab

    def create_talents_tab(self):
        talents_tab = QWidget()
        layout = QVBoxLayout()

        # Liste des talents (exemples)
        self.talents_label = QLabel("Talents à débloquer")
        layout.addWidget(self.talents_label)

        talents_tab.setLayout(layout)
        return talents_tab

    def create_tasks_tab(self):
        tasks_tab = QWidget()
        layout = QVBoxLayout()

        # Liste des tâches avec XP
        self.tasks_table = QTableWidget(self)
        self.tasks_table.setRowCount(5)
        self.tasks_table.setColumnCount(3)
        self.tasks_table.setHorizontalHeaderLabels(['Tâche', 'XP', 'Compléter'])

        # Exemple de tâches
        self.tasks_table.setItem(0, 0, QTableWidgetItem("Coder une fonction"))
        self.tasks_table.setItem(0, 1, QTableWidgetItem("20"))
        self.tasks_table.setItem(1, 0, QTableWidgetItem("Apprendre une langue"))
        self.tasks_table.setItem(1, 1, QTableWidgetItem("40"))

        # Ajouter des boutons pour compléter les tâches
        self.task_button1 = QPushButton("Compléter Tâche 1")
        self.task_button2 = QPushButton("Compléter Tâche 2")
        self.task_button1.clicked.connect(lambda: self.complete_task(20))  # Ajoute 20 XP
        self.task_button2.clicked.connect(lambda: self.complete_task(40))  # Ajoute 40 XP

        layout.addWidget(self.tasks_table)
        layout.addWidget(self.task_button1)
        layout.addWidget(self.task_button2)

        tasks_tab.setLayout(layout)
        return tasks_tab

    def complete_task(self, xp):
        """Fonction qui ajoute de l'XP et met à jour la barre de progression"""
        self.total_xp += xp
        self.update_progress_bar()

    def update_progress_bar(self):
        """Met à jour la barre de progression en fonction de l'XP total"""
        xp_for_next_level = 100  # On suppose que chaque niveau nécessite 100 XP
        progress_percentage = (self.total_xp % xp_for_next_level) / xp_for_next_level * 100
        self.progress_bar.setValue(progress_percentage)

# Fonction principale
def main():
    app = QApplication([])
    window = ProfilWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
