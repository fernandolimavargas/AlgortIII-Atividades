from List import *

class EasterEgg(): 
    def __init__(self, tamanho, casca, recheio) -> None:
        self.tamanho = tamanho
        self.casca = casca
        self.recheio = recheio

    def getTamanho (self): 
        return self.tamanho

    def getCasca (self): 
        return self.casca

    def get_recheio(self): 
        return self.recheio

    def setTamanho(self, tamanho):
        if (self.tamanhoIsValid(tamanho)):
            self.tamanho = tamanho
        else:
            raise Exception("Tamanho de casca não é compaível com o disponível")

    def setCasca(self, casca): 
        if (self.cascaIsValid(casca)):
            self.casca = casca
        else:
            raise Exception("Casca não é possível fazer")

    def setRecheio(self, recheio): 
        if (self.recheioIsValid(recheio)): 
            self.recheio = recheio  
        else: 
            raise Exception("Recheio é indisponível para pedido")
    
    def cascaIsValid(self, casca): 
        if self.casca in CASCAS_DISPONIVEIS:
            return casca 

    def tamanhoIsValid(self, tamanho):
        if self.tamanho in TAMANHO_DISPONIVEL:
            return tamanho

    def recheioIsValid(self, recheio): 
        if self.recheio in RECHEIO_DISPONIVEL:
            return recheio

    def reaDate(self): 
        self.casca = input("Casca [PRETO ou BRANCO]: ")
        self.tamanho = int(input("Tamanho [250 ou 500]: "))
        self.recheio = input("Recheio [BRIGADEIRO ou BRANQUINHO]: ")