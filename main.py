import sys
import random_hadith_window as rhw
import notification_manager as nm
from PyQt5 import QtWidgets, uic

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = rhw.MainWindow()
    window.show()
    # nm.on_closing(window)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
