import sys
from PyQt6.QtWidgets import QApplication
from IntegerDisplay import IntegerDisplay

def main():
    app = QApplication(sys.argv)
    display = IntegerDisplay()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
