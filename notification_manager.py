import hadith_manager as hm
import time
import plyer
from PyQt5 import QtWidgets, uic, QtGui, QtCore

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