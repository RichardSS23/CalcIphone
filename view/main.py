from PyQt5.QtWidgets import QMainWindow, QShortcut, QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QKeySequence
from funcoes import somar, subitrair, multiplicar, dividir, porcentagem
import tkinter as tk

root = tk.Tk()
entrada = tk.StringVar()


class calculadora(QMainWindow):
      
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("view/telaCalculadora.ui", self)
        self.show()
        
        self.num1 = 0
        self.num2 = 0
        
        self.selectedOperation = None
        self.operationList = {
            "+": somar,
            "-": subitrair,
            "x": multiplicar,
            "÷": dividir,
            "%": porcentagem
        }
        
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
        
        self.btnVirgu.clicked.connect(self.addComma)
        
        self.btnMais.clicked.connect(lambda: self.setOperation("+"))
        self.btnMenos.clicked.connect(lambda: self.setOperation("-"))
        self.btnVezes.clicked.connect(lambda: self.setOperation("x"))
        self.btnDivisao.clicked.connect(lambda: self.setOperation("÷"))
        
        self.btnMaisMenos.clicked.connect(lambda: self.inverterSinal())
        
        self.btnApagarTdo.clicked.connect(self.cleanNumber)
        self.btnIgual.clicked.connect(self.showResult)
        self.btnApagar.clicked.connect(lambda: self.deleteNumber(entrada))
        
        self.btnPorcentagem.clicked.connect(lambda: self.setOperation("%"))
        
        
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
     
    def percent(self):
        perc = self.getNumberDisplay(self.display)
        resultado = porcentagem(self.num1, perc)
        self.setNumberDisplay(resultado)
    
    def cleanNumber(self):
        self.display.setText("0")
        if self.display.text() == "0":
            self.display_2.setText("0")
            
    def deleteNumber(self, entrada):
        numero = self.display.text()
        if len(numero) <= 1:
            self.display.setText("0")
        else:
            novoNumero = numero[:-1]
            self.display.setText(novoNumero)        
       
    def getNumberDisplay(self, display):
        num = display.text()   
        if "," in num:
            num = float(num.replace(",", "."))
        else:
            num = int(num)
        return num
      
    def setNumberDisplay(self, number):
        number = str(number)
        number = number.replace(".", ",")
        self.display.setText(number)  
     
    def setCalcDisplay(self, n1, n2, operator):
         n1 = str(n1).replace(".", ",")
         n2 = str(n2).replace(".", ",")
         calc = f"{n1} {operator} {n2} ="
         self.display_2.setText(calc)
       
    def setOperation(self, operation):
        self.selectedOperation = operation
        self.num1 = self.getNumberDisplay(self.display)
        self.num2 = 0
        result = self.display.text()
        self.display_2.setText(result)
        self.display.setText("0")
        
    def showResult(self):
        if self.num2 == 0:
            self.num2 = self.getNumberDisplay(self.display)
        
        num1 = self.num1
        num2 = self.num2
        
        operation = self.operationList.get(self.selectedOperation)  
        result = operation(num1, num2)
        self.num1 = result
        
        
        self.setNumberDisplay(result)
        self.setCalcDisplay(num1, num2, f"{self.selectedOperation}")
        
    def inverterSinal(self):
        numeroDisplay = int(self.display.text())
        numero = str(numeroDisplay * -1)
        self.display.setText(numero)
        
        
    
    
    
    
    
    
    
  