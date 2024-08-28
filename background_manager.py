import threading
import schedule
import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction

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

def exit_app(self):
    self.notifications_enabled = False
    QtWidgets.QApplication.quit()

