
resultado = 0

def somar(num1, num2):
    return num1 + num2
def subitrair(num1, num2):
    return num1 - num2
def multiplicar(num1, num2):
    return num1 * num2
def dividir(num1, num2):
    if num2 == 0:
        return "Erro Divisão"
    
    return num1 / num2
def porcentagem(num1, percent):
    return num1 * (percent / 100) 
