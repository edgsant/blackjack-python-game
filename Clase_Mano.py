"""Codigo realizado por:
        Edgar Santiesteban Mendo
        Daniel San Miguel Lopez
"""
class Mano(object):
    """Clase que representa una mano del blackjack con sus diferentes operaciones
            Esta compuesta de:
                -Array de Carta
                -Double con el valor de la apuesta
                -String con el nombre de la mano
                -Boolean para saber el estado de la mano (Abierto/Cerrado/Pasado)
    """
    
    def __init__(self, apuesta, nombre):
        self.__mano=[]  #array de cartas
        self.__apuesta=apuesta
        self.__nombre=nombre
        self.__cerrado=False
        self.__pasado=False
        self.__abierto=True
        return None

    
    def anadir_carta(self, carta):
        """
            Añade una Carta al array de Carta
        """
        self.__mano.append(carta)
        
    def get_mano(self):
        """
            Devuelve el array de Carta
        """
        return self.__mano
        
    def get_nombre(self):
        """
            Devuelve el nombre de la mano
        """ 
        return self.__nombre
    
    def get_apuesta(self):
        """
            Devuelve el valor de la apuesta actual de la mano
        """ 
        return self.__apuesta
    
    def doblar_apuesta(self):
        """
            Multiplica por 2 el valor de la apuesta de la mano
        """ 
        self.__apuesta*=2
        return None
        
    def blackjack_apuesta(self):
        """
            Multiplica por 1.5 el valor de la apuesta de la mano en el caso de que ocurra un blackjack
        """ 
        self.__apuesta*=1.5
        return None
        
    def is_cerrado(self):
        """
            Devuelve el valor del booleano cerrado para saber si la mano esta cerrada
        """ 
        return self.__cerrado
    
    def is_abierto(self):
        """
            Devuelve el valor del booleano abierto para saber si la mano esta abierta
        """ 
        return self.__abierto
    
    def is_pasado(self):
        """
            Devuelve el valor del booleano pasado para saber si la mano esta pasada
        """ 
        return self.__pasado
    
    def set_pasado(self):
        """
            Establece el valor del booleano pasado a verdadero y abierto y cerrado a falso,
            indicando que la mano esta pasada.
        """ 
        self.__abierto=False
        self.__cerrado=False
        self.__pasado=True
        return None
    
    def set_cerrado(self):
        """
            Establece el valor del booleano cerrada a verdadero y cerrado y abierto a falso,
            indicando que la mano esta cerrada.
        """ 
        self.__abierto=False
        self.__cerrado=True
        self.__pasado=False
        return None
    
    def set_abierto(self):
        """
            Establece el valor del booleano cerrada a verdadero y cerrado y abierto a falso,
            indicando que la mano esta cerrada.
        """ 
        self.__abierto=True
        self.__cerrado=False
        self.__pasado=False
        return None
        
    def get_points(self):
        """
            Devuelve el valor de la suma de todas las cartas del array de Carta que compone la mano.
            En el caso de que la Carta sea figura suma 10, y en el caso de que la carta sea As suma 1 u 11 en función 
            de si la suma total pasaba de 21 o no.
        """ 
        valor_total=0
        contadorAS=0
        for i in self.__mano:
            #Sumamos valor de la carta
            valor_total=valor_total+i.valor
            if ((i.valor==1)):
                valor_total=valor_total+10
                contadorAS+=1
        for i in range(contadorAS):
            if valor_total>21:
                valor_total-=10
        return valor_total
    
    def str_get_estado(self):
        """
            Devuelve un String ("Abierto"/"Cerrado"/"Pasado") en funcion de que boolean sea verdadero
        """
        if self.__abierto:
            return "Abierto"
        elif self.__cerrado:
            return "Cerrado" 
        elif self.__pasado:
            return "Pasado"
       
    def se_separa(self):
        """
            Para la operacion de separar mano, elimina la segunda carta del array Carta de la mano actual
            y la devuelve para uso posterior.
        """ 
        carta_de_nueva_mano=self.__mano[1]
        self.__mano.remove(carta_de_nueva_mano)
        return carta_de_nueva_mano
    
    def vaciar_mano(self):
        """
            Elimina todos los componentes del array de Carta y establece el estado de la mano como Abierto
        """
        self.__mano.clear()
        self.set_abierto()
        return None
    
    def set_nombre(self, nombreNuevo):
        """
            Dado un String, establece el nombre de la mano como el String recibido
        """
        self.__nombre=nombreNuevo
        return None
    
    def puede_separar(self):
        return (len(self.__mano)==2 and (self.__mano[0].valor==self.__mano[1].valor))