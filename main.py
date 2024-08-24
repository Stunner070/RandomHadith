import random as random
import csv as csv
import sys

from PyQt5 import QtWidgets, uic


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


def randomHadithNum():
    return random.randint(1, 2006)

def hadithChapter(hadithNum):
    with open('all_hadiths_clean.csv') as hadiths:
        one_hadith = csv.DictReader(hadiths)
        for row in one_hadith:
            if int(row['hadith_no']) == (hadithNum):
                return row['chapter']

def hadithText(hadithNum):
    with open('all_hadiths_clean.csv') as hadiths:
        one_hadith = csv.DictReader(hadiths)
        for row in one_hadith:
            if int(row['hadith_no']) == (hadithNum):
                return row['text_en']


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('main_window.ui', self)

        # Connect button to function
        self.randomButton.clicked.connect(self.display_random_hadith)

    def display_random_hadith(self):
        hadith_num = randomHadithNum()
        chapter = hadithChapter(hadith_num)

        hadith = hadithText(hadith_num)
        hadith = ' '.join(hadith.split())

        self.hadithText.setPlainText(hadith)
        self.chapter.setText(chapter)

if __name__ == "__main__":
    main()
