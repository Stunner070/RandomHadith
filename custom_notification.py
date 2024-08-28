from PyQt5 import QtWidgets, QtGui, QtCore


class CustomNotification(QtWidgets.QWidget):
    def __init__(self, title, message, timeout=8000):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.ToolTip | QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet("background-color: white; border: 1px solid black;")

        layout = QtWidgets.QVBoxLayout()
        title_label = QtWidgets.QLabel(title)
        title_label.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Bold))
        layout.addWidget(title_label)

        message_label = QtWidgets.QLabel(message)
        message_label.setWordWrap(True)
        layout.addWidget(message_label)

        self.setLayout(layout)
        self.adjustSize()
        self.setWindowOpacity(0.9)

        # Position the window in the lower-right corner
        self.position_in_lower_right()

        QtCore.QTimer.singleShot(timeout, self.close)  # Automatically close after timeout

    def position_in_lower_right(self):
        screen_geometry = QtWidgets.QApplication.desktop().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        # Calculate the position for the lower-right corner
        x = screen_width - self.width() - 10  # 10 pixels from the right edge
        y = screen_height - self.height() - 10  # 10 pixels from the bottom edge

        self.move(x, y)

    def show_notification(self):
        self.show()
        self.raise_()


# Example usage
def show_custom_notification(message):
    app = QtWidgets.QApplication([])
    notification = CustomNotification("Random Hadith of the day!",
                                      message)
    notification.show_notification()
    app.exec_()