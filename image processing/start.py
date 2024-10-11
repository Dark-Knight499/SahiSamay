import sys
import subprocess
import time
import register
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import Qt
import second
def analyze_fucn(app):
    second.main()
class BackgroundWidget(QWidget):
    def __init__(self, image_path, parent=None):
        super().__init__(parent)
        self.image_path = image_path

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap(self.image_path)
        painter.drawPixmap(0, 0, self.width(), self.height(), pixmap)

def load_register_page():
    pass

def main():
    app = QApplication(sys.argv)

    # Create the main window
    main_win = QWidget()
    main_win.setGeometry(0, 0, 1000, 500)
    main_win.setWindowTitle('PyQt5 Background Image Example')
    # Create the BackgroundWidget with the image
    img_win = BackgroundWidget(image_path=r"C:\Harsh\tt_manager\image.jpg", parent=main_win)
    img_win.setGeometry(0, 0, 700, 500)
    img_win.setStyleSheet("background: transparent;")  # Ensure the background is transparent

    # Create buttons
    analyze_button = QPushButton("Analyze", main_win)
    analyze_button.clicked.connect(lambda:analyze_fucn(main_win))
    register_member_button = QPushButton("Register Member", main_win)
    register_member_button.clicked.connect(lambda: register.main())

    # Create layout
    layout = QVBoxLayout()
    layout.addWidget(analyze_button)
    layout.addWidget(register_member_button)

    # Center the buttons in the layout
    layout.setAlignment(analyze_button, Qt.AlignCenter)
    layout.setAlignment(register_member_button, Qt.AlignCenter)

    # Create a widget to contain the layout
    button_widget = QWidget()
    button_widget.setLayout(layout)
    button_widget.setGeometry(700, 0, 300, 500)
    button_widget.setParent(main_win)

    # Show the main window
    main_win.show()

    # Run the application
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

