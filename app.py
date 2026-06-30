from rajora_ai.vision import analyze_screen
import sys
from PyQt6.QtWidgets import QApplication
from rajora_ai.ui import MainWindow

def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()