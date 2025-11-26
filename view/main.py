from PyQt5.QtWidgets import QMainWindow, QShortcut, QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QKeySequence

class calculadora(QMainWindow):
      
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("view/telaCalculadora.ui", self)
        self.show()
        
        self.btn1.clicked.connect(lambda: self.addNumber(1))
        self.btn2.clicked.connect(lambda: self.addNumber(2))
        self.btn3.clicked.connect(lambda: self.addNumber(3))
        self.btn4.clicked.connect(lambda: self.addNumber(4))
        self.btn5.clicked.connect(lambda: self.addNumber(5))
        self.btn6.clicked.connect(lambda: self.addNumber(6))
        self.btn7.clicked.connect(lambda: self.addNumber(7))
        self.btn8.clicked.connect(lambda: self.addNumber(8))
        self.btn9.clicked.connect(lambda: self.addNumber(9))
        self.btnZero.clicked.connect(lambda: self.addNumber(0))
        self.btnApagarTdo.clicked.connect(self.cleanNumber)
        
    def addNumber(self, numero):
        textoAtual = self.display.text()
        if textoAtual == '0':
            textoAdicionado = numero
        else:
            textoAdicionado = textoAtual + str(numero)
        self.display.setText(str(textoAdicionado))
        
    def cleanNumber(self):
        self.display.setText("0")
        
    def deleteNumber(self):
        self.setText[:-1]
    
    
    
    
    
    
  