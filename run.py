from PyQt5.QtWidgets import QApplication
from view.main import calculadora


if __name__ == "__main__":
    app = QApplication([])
    tela = calculadora()
    app.exec_()
    
