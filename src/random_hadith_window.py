import plyer
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction


import hadith_manager as hm
import time
import schedule
import threading
from PyQt5 import QtWidgets, uic, QtGui, QtCore

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("resources/main_window.ui", self)

        # Connect button to function
        self.randomButton.clicked.connect(self.display_random_hadith)

        # System Tray Icon
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QtGui.QIcon("resources/hadith_logo.png"))
        self.activate_tray()

        # Notification Box
        self.notiBox.stateChanged.connect(self.toggle_notifications)

        # flag for notification
        self.notifications_enabled = False


    def display_random_hadith(self):
        hadith_num = hm.randomHadithNum()
        result = hm.hadith_getter(hadith_num)
        chapter = result[0]

        hadith = result[1]
        hadith = ' '.join(hadith.split())

        self.hadithText.setPlainText(hadith)
        self.chapter.setText(chapter)
        self.hadithNo.setText(str(hadith_num))

    def closeEvent(self, event):
        if self.notifications_enabled:
            event.ignore()
            self.hide()
            self.tray_icon.showMessage("Notification App", "The app is running in the background.",
                                       QSystemTrayIcon.Information)
        else:
            event.accept()

    def activate_tray(self):
        tray_menu = QMenu()
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.exit_app)
        tray_menu.addAction(exit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def start_background_task(self):
        if self.notifications_enabled:
            thread = threading.Thread(target=self.run_scheduler)
            thread.daemon = True  # Daemonize thread to close when the main program exits
            thread.start()

    def run_scheduler(self):
        # Schedule notifications
        # schedule.every().day.at("09:00").do(self.send_notification)
        # schedule.every().day.at("18:00").do(self.send_notification)
        schedule.every(7).seconds.do(self.send_notification)

        while self.notifications_enabled:
            schedule.run_pending()
            time.sleep(1)

    def send_notification(self):
        num = hm.randomHadithNum()
        message = hm.hadith_getter(num)
        hadith = message[1]
        hadith_final = ' '.join(hadith.split())

        hadith_max_length = 150
        if len(hadith_final) > hadith_max_length:
            hadith_final = hadith_final[:hadith_max_length] + "..."  # Truncate the message if it's too long

        if self.notifications_enabled:
            # This will display the notification in a custom window
            # self.tray_icon.showMessage("Hadith number: " + str(num), hadith_final, QSystemTrayIcon.Information)
            plyer.notification.notify(
                title="Daily Hadith: " + str(num),
                message=hadith_final,
                app_name="RandomHadith",
                timeout=15
            )
        # Random sleep interval between notifications (1 to 2 hours)
        # interval = random.randint(3600, 7200)
        time.sleep(10)

    def toggle_notifications(self, state):
        if state == QtCore.Qt.Checked:
            self.notifications_enabled = True
            self.start_background_task()
        else:
            self.notifications_enabled = False

    def exit_app(self):
        self.notifications_enabled = False
        QtWidgets.QApplication.quit()