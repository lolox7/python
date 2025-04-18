import sys
from PySide6.QtWidgets import QApplication, QLabel

#create the application instance
app = QApplication(sys.argv)

#Create a label widget with the text "hello world"
label = QLabel("Hello world !")

#show the label 
label.show()

#run the application event loop
sys.exit(app.exec())