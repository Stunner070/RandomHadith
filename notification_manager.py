import json
import os
import threading
import time
import random
import random_hadith_window as rhw
import hadith_manager as hm
from plyer import notification

CONFIG_FILE = 'config.json'

def send_notification():
    """Send a random notification."""
    while True:
        message = hm.hadith_getter(hm.randomHadithNum())[1]
        notification.notify(
            title="Daily Hadith",
            message=message,
            app_name="RandomHadith",
            timeout=15
        )
        # Random sleep interval between notifications (1 to 2 hours)
        # interval = random.randint(3600, 7200)
        time.sleep(10)

def toggle_notifications(checked):
    """Start or stop notifications based on checkbox state."""
    if checked:
        notification_thread = threading.Thread(target=send_notification, daemon=True)
        notification_thread.start()

def save_config(checked):
    """Save the checkbox state to a JSON file."""
    with open(CONFIG_FILE, 'w') as f:
        json.dump({"notify": checked}, f)

def load_config():
    """Load the checkbox state from a JSON file."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
            return config.get("notify",False)
    return False

def on_closing(MainWindow):
    """Save the checkbox state and exit the application."""
    state = rhw.MainWindow.get_noti_status(MainWindow)
    save_config(state)
    toggle_notifications(state)