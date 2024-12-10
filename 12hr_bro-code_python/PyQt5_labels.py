import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        label = QLabel("Hello", self)
        label.setFont(QFont("Calibri", 30))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #273b3a;"
                           "background-color: #6d869c;"
                           "font-weight: bold;"
                           "font-style: italic;"
                           "text-decoration: underline;")
        
        # label.setAlignment(Qt.AlignTop) Vertically Top
        # label.setAlignment(Qt.AlignBottom) Vertically Bottom
        # label.setAlignment(Qt.AlignVCenter) Vertically Center
        
        # label.setAlignment(Qt.AlignRight) Horizontically Right
        # label.setAlignment(Qt.AlignHCenter) Horizontally Center
        # label.setAlignment(Qt.AlignLeft) Horizontally Left

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) Center & Top
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) Center & Bottom
        # label.setAlignment(Qt.AlignCenter) Center

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

    