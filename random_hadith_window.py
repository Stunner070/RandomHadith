import hadith_manager as hm
import notification_manager as nm
from PyQt5 import QtWidgets, uic

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('main_window.ui', self)

        # Connect button to function
        self.randomButton.clicked.connect(self.display_random_hadith)

        # Load notification status from config file
        not_state = nm.load_config()
        self.notiBox.setChecked(not_state)


    def get_noti_status(self):
        return self.notiBox.isChecked()

    def display_random_hadith(self):
        hadith_num = hm.randomHadithNum()
        result = hm.hadith_getter(hadith_num)
        chapter = result[0]

        hadith = result[1]
        hadith = ' '.join(hadith.split())

        self.hadithText.setPlainText(hadith)
        self.chapter.setText(chapter)
        self.hadithNo.setText(str(hadith_num))