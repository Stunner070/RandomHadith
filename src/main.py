import sys
import random_hadith_window as rhw
from PyQt5 import QtWidgets, uic

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = rhw.MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
