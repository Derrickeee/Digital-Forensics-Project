from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt5 import uic
import time
import datetime
import webbrowser

class NewWindow(QMainWindow):
    """
    Class definition for transaction window
    """
    def __init__(self, data, parent=None):
        super(NewWindow, self).__init__(parent)
        # Keep a local copy of the parent object
        self.homeparent = parent

        # Load the Home Window UI design from file
        uic.loadUi("./basic.ui", self)
        self.show()
        
def main():
    # Define the PyQT5 application object
    app = QApplication([])

    # Create the main window and show it
    tw = NewWindow()
    tw.show()

    # Start the PyQT5 app
    app.exec_()
