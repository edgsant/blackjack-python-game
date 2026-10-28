"""Codigo realizado por:
        Edgar Santiesteban Mendo
        Daniel San Miguel Lopez
"""

import os

import wx
from Clase_Carta import Carta

ruta_base = os.path.dirname(os.path.abspath(__file__))
RUTA_IMAGEN = os.path.join(ruta_base, "files", "images", "Cartas") + os.sep
WIDTH = 86
HEIGHT = 132

class Carta_Representada():
    
    def __init__(self, parent, carta):
        self.__Carta = carta
        image  = wx.Image(RUTA_IMAGEN + self.getNombreCarta() + ".png")
        image = image.Scale(WIDTH, HEIGHT, wx.IMAGE_QUALITY_HIGH)
        self.__MiBitMap = wx.StaticBitmap(parent, wx.ID_ANY, wx.Bitmap(image), size=wx.Size(width=WIDTH, height=HEIGHT))
        
    def getNombreCarta(self):
        nombre = self.__Carta.valorChar() + self.__Carta.paloLetra()
        return nombre
    
    def getCarta(self):
        return self.__Carta
    
    def getBitMap(self):
        return self.__MiBitMap