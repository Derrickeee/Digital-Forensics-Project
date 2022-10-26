from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt5 import uic
import time
import datetime
import webbrowser

data = [{ 'blockNumber': '6141243',
          'direction': 0,
          'from': '0x7ed2d423ba4bc317e45561caa823b7d6cc2024a9',
          'from_labels': None,
          'hash': '0x1a99ef8d9ae7087e276451d460f9b100a3c667d07c69a4b95bcd0296132e5738',
          'timestamp': '1534182274',
          'to': '0x7129bed9a5264f0cf279110ece27add9b6662bd5',
          'to_labels': None,
          'value': 26.10836602777778}]
          
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


def main():
    # Define the PyQT5 application object
    app = QApplication([])

    # Create the main window and show it
    tw = NewWindow(data)
    tw.show()

    # Start the PyQT5 app
    app.exec_()


if __name__ == "__main__":
    main()
