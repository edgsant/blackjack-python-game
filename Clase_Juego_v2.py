"""Codigo realizado por:
        Edgar Santiesteban Mendo
        Daniel San Miguel Lopez
"""


from Clase_Carta import Carta
from Clase_Mano import Mano
from Codigo_Externo import Estrategia
from Codigo_Externo import Mazo


NUM_BARAJAS=2
APU_LOW=2
APU_MED=10
APU_HI=50

class Juego(object):
    """
        Clase que contendrá todas las operaciones del juego blackjack
        Atributos:
            -balance: Double con el dinero ganado o perdido en total de todas las partidas que juegue el usuario
            -contador_partidas: Int con el contador de partidas que haya jugado en total el usuario
            -partidas_analisis
            -manos[]: array de clase Mano que contendrá las manos del usuario
            -croupier: clase Mano con la mano del croupier
            -baraja: clase Mazo del codigo externo
            -estratega: clase Estrategia del codigo externo
            -blackjack: booleano para saber si ha ocurrido blackjack en la partida actual
    """
    
    def __init__(self):
        
        self.__balance=0
        self.__manos=[]
        self.__croupier=Mano(0, "Croupier")
        self.__estratega=Estrategia(NUM_BARAJAS)
        self.__baraja=Mazo(Carta, self.__estratega)
        self.__blackjack=False
        self.__isEstrategia = False     #Sera el toggle button
        return None
            
    def inicio(self, apuesta_recibida):
        """
            Metodo general para el inicio de la partida.
            Solicita a los jugadores la cantidad de dinero que quieren apostar e inicializa la mano del croupier y la del jugador
        """
        self.__blackjack=False
        if self.__isEstrategia:
           apuesta=self.__estratega.apuesta(APU_LOW, APU_MED, APU_HI)
        else:
            apuesta=apuesta_recibida
        self.__croupier.anadir_carta(self.__baraja.reparte())
        primera_mano=Mano(int(apuesta), "Mano")
        primera_mano.anadir_carta(self.__baraja.reparte())
        primera_mano.anadir_carta(self.__baraja.reparte())
        self.__manos.append(primera_mano)
        if(primera_mano.get_points()==21):
            self.__blackjack=True
            self.blackjack(primera_mano)        
        return None
                
    def add_mano(self, mano):
        """Añade al array de Manos del jugador una nueva mano recibida

        Args:
            mano (Mano): clase Mano recibida a meter en el array
        """
        self.__manos.append(mano)
        return None
    
    def blackjack(self, mano):
        """
            Multiplica la apuesta de la mano recibida por 1.5 y pone el estado de la mano a Cerrado
        Args:
            mano (Mano): Mano en la que ha ocurrido el blackjack
        """
        mano.set_cerrado()
        mano.blackjack_apuesta()
        return None

    def pedir(self, pos_mano):
        """
            Reparte una carta mas a la mano recibida.
            Si se pasa de 21, pone el estado de la mano a Pasado
        Args:
            mano (Mano): Mano para la que se ha pedido otra carta
        """
        mano=self.__manos[pos_mano]
        mano.anadir_carta(self.__baraja.reparte())
        if(mano.get_points()>21):
            mano.set_pasado()
        return None
    
    def doblar(self, pos_mano):
        """
            Dobla la apuesta de la mano recibida, le reparte una carta y establece el estado de la mano a Cerrado
            Si se pasa de 21, pone el estado de la mano a Pasado
        Args:
            mano (Mano): Mano en la que se ha pedido doblar
        """
        mano=self.__manos[pos_mano]
        mano.anadir_carta(self.__baraja.reparte())
        mano.doblar_apuesta()
        if(mano.get_points()>21):
            mano.set_pasado()
        else:
            mano.set_cerrado()
        return None
    
    def cerrar(self, pos_mano):
        """
            Establece el estado de la mano a Cerrado
        Args:
            mano (Mano): Mano en la que se ha pedido cerrar
        """
        mano=self.__manos[pos_mano]
        mano.set_cerrado()
        return 
    
    def separar(self, pos_mano):
        """
            Dada una mano recibida, comprueba si solo tiene dos cartas y son del mismo valor
            En caso afirmativo, genera una nueva mano con la segunda carta de la mano original, 
            elimina dicha carta de la mano original y establece un nuevo nombre a ambas manos.
            En caso negativo, devuelve False

        Args:
            mano_recibida (Mano): Mano recibida desde la que se desea separar

        Returns:
            Boolean: True si se ha podido separar, False si la mano no es valida para separarse
        """
        mano_recibida=self.__manos[pos_mano]
        
        if(mano_recibida.puede_separar()):
            nombre_nueva_mano=mano_recibida.get_nombre()
            nueva_mano=Mano(mano_recibida.get_apuesta(), nombre_nueva_mano)
            carta_de_nueva_mano=mano_recibida.se_separa()
            nueva_mano.anadir_carta(carta_de_nueva_mano)
            self.set_nuevo_nombre_manos(mano_recibida, nueva_mano)
            self.add_mano(nueva_mano)
            return True
        else:
            return False
        
    def turno_croupier(self):
        """
            Imprime las cartas del croupier y pide cartas hasta llegar a 17 puntos o pasarse.
        """
        if(self.todas_pasadas() or self.__blackjack):
            return None
        while(self.__croupier.get_points()<17):
            self.__croupier.anadir_carta(self.__baraja.reparte())
        return None  
    
    def vaciar_manos(self):
        """
            Elimina las Manos del array de Mano del jugador y la clase Mano del croupier
        """
        self.__manos.clear()
        self.__croupier.vaciar_mano()
        return None
    
    def todas_pasadas(self):
        """
            Devuelve si todas las manos del jugador estan pasadas
        Returns:
            Boolean:True si todas las manos del jugador estan pasadas
                    False si hay alguna mano que no este pasada
        """
        mi_bool=True
        for i in self.__manos:
            if not i.is_pasado():
                mi_bool=False
        return mi_bool
    
    def imprimir_blackjack(self):
        """
            Metodo que imprime por pantalla la celebracion del blackjack
        """
        print("*****************")
        print("*** BLACKJACK ***")
        print("*****************")
        return None
    
    def is_blackjack(self):
        """
            Devuelve si hay blackjack
        Returns:
            Boolean:True si hay blackjack
                    False si no hay blackjack
        """
        return self.__blackjack
        
    def set_nuevo_nombre_manos(self, mano_original, mano_nueva):
        """
            Genera un nuevo nombre para dos manos recibidas, la original de la que se produjo la separacion 
            y la nueva mano generada despues de esa operacion.
        Args:
            mano_original (Mano): Mano de la que se ejecutó la operacion Separar
            mano_nueva (Mano): Mano generada de dicha operacion
        """
        nuevo_nombre_mano_original=mano_original.get_nombre()
        
        nuevo_nombre_mano_nueva=nuevo_nombre_mano_original+"B"
        nuevo_nombre_mano_original=nuevo_nombre_mano_original+"A"
        
        mano_original.set_nombre(nuevo_nombre_mano_original)
        mano_nueva.set_nombre(nuevo_nombre_mano_nueva)
        
        return None
    
    def get_manos(self):
        return self.__manos
    
    def get_croupier(self):
        return self.__croupier
    
    def repuesta_estratega(self, pos_mano):
        mano_que_responder = self.__manos[pos_mano].get_mano()
        return self.__estratega.jugada(self.__croupier.get_mano()[0], mano_que_responder)
    
    def is_fin_partida(self):
        todas_cerradas=True
        for i in self.__manos: 
            if i.is_abierto():
                todas_cerradas= False
        return todas_cerradas
    
    def fin_partida_v2(self):
        resultado_partida=0
        for i in self.__manos:
            if(self.__croupier.get_points())==(i.get_points()):
                pass
            elif(((self.__croupier.get_points())>(i.get_points()) and (self.__croupier.get_points()<22)) or (i.get_points()>21)):
                self.__balance-=i.get_apuesta()
                resultado_partida-=i.get_apuesta()
            else:
                self.__balance+=i.get_apuesta()
                resultado_partida+=i.get_apuesta()
        return resultado_partida

    def set_estrategia(self, bool):
        self.__isEstrategia=bool
        
    def is_estrategia(self):
        return self.__isEstrategia