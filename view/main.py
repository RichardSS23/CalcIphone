from PyQt5.QtWidgets import QMainWindow, QShortcut, QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QKeySequence
from funcoes import soma,sub,mult,div
import tkinter as tk

root = tk.Tk()
entrada = tk.StringVar()


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
        
        self.btnVirgu.clicked.connect(self.addComma)
        
        self.btnMais.clicked.connect(lambda: self.addNumber("+"))
        self.btnMenos.clicked.connect(lambda: self.addNumber("-"))
        self.btnVezes.clicked.connect(lambda: self.addNumber("*"))
        self.btnDivisao.clicked.connect(lambda: self.addNumber("/"))
        self.btnZero.clicked.connect(lambda: self.addNumber(0))
        self.btnApagarTdo.clicked.connect(self.cleanNumber)
        self.btnIgual.clicked.connect(self.showResult)
        self.btnApagar.clicked.connect(self.deleteNumber)
        
        
    def addComma(self):
        ultimo = self.display.text()
        if "," in ultimo:
            resultado = ultimo 
        else:   
            resultado = ultimo + "," 
        self.display.setText(resultado)

            
        
    def addNumber(self, numero):
        textoAtual = self.display.text()
        if textoAtual == '0':
            textoAdicionado = numero
        else:
            textoAdicionado = textoAtual + str(numero)
        self.display.setText(str(textoAdicionado))
        
    def cleanNumber(self):
        self.display.setText("0")
        
    def deleteNumber(self, entrada ):
        valor = entrada.get()
        
        if valor:
            entrada.set(valor[:-1])

        
    def showResult(self):
        n1 = self.display.text()   
        n2 = 2
        
        if "," in n1:
            n1 = float(n1.replace(",", "."))
        else:
            n1 = int(n1)
        
        result = soma(n1, n2)
        print(f'{n1} + {n2} = {result}')
        print("Tipo: ", type(result))

        
        
    
    
    
    
    
    
    
  