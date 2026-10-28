"""Codigo realizado por:
        Edgar Santiesteban Mendo
        Daniel San Miguel Lopez
"""

from Codigo_Externo import CartaBase

class PALO():
    """ Strings de los distintos palos """
    TREBOL="♣"
    CORAZON="♥"
    PICAS="♠"
    ROMBO="♦"
    
class Carta(CartaBase):
    """Clase que hereda de CartaBase del codigo externo
    """    
    def __init__(self, ind) -> None:
        super().__init__(ind)
        return None
    
    """Metodo que devuelve un String con el palo al que pertenece la carta
        El String devuelto esta definido den la clase PALO
    """
    def palo(self) -> str:
        if(self.ind<13):
            return PALO.TREBOL
        elif(self.ind<26):
            return PALO.CORAZON
        elif(self.ind<38):
            return PALO.PICAS
        elif(self.ind<52):
            return PALO.ROMBO
        
    def paloLetra(self):
        if(self.ind<13):
            return 'C'
        elif(self.ind<26):
            return 'H'
        elif(self.ind<38):
            return 'S'
        elif(self.ind<52):
            return 'D'
        
    """
        Metodo que devuelve un String dependiendo del valor de la carta indicando que figura es la carta
    """
    def valorChar(self):
        
        if self.valor==1:
            return "A"
        elif (self.ind%13==10):
            return "J"
        elif (self.ind%13==11):
            return "Q"
        elif (self.ind%13==12):
            return "K"
        else:
            return str(self.valor)