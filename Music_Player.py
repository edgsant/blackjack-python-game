"""Codigo realizado por:
        Edgar Santiesteban Mendo
        Daniel San Miguel Lopez
"""

import os
import wx
import wx.media

ruta_base = os.path.dirname(os.path.abspath(__file__))
RUTA_SONIDOS = os.path.join(ruta_base, "files", "sounds") + os.sep

class Music_Player(wx.media.MediaCtrl):
    
    def __init__(self, parent):
        super().__init__(parent, style=wx.SIMPLE_BORDER, szBackend=wx.media.MEDIABACKEND_WMP10)
        
    def load_blackjack(self):
        music = RUTA_SONIDOS + "Blackjack_Sound.wav"
        if(super().Load(music)):
            return True
        else:
            return False
        
    def load_button(self):
        music = RUTA_SONIDOS + "Button_Sound.wav"
        if(super().Load(music)):
            return True
        else:
            return False
        
    def load_casino(self):
        music = RUTA_SONIDOS + "Casino_Music.wav"
        if(super().Load(music)):
            self.SetVolume(0.5)
            return True
        else:
            return False
        
    def load_coin(self):
        music = RUTA_SONIDOS + "Coin_Sound.wav"
        if(super().Load(music)):
            return True
        else:
            return False
        
    def load_countdown(self):
        music = RUTA_SONIDOS + "Countdown_Sound.wav"
        if(super().Load(music)):
            return True
        else:
            return False
        
    def load_deal(self):
        music = RUTA_SONIDOS + "Deal_Sound.wav"
        if(super().Load(music)):
            return True
        else:
            return False
        
    def load_highbet(self):
        music = RUTA_SONIDOS + "HighBet_Sound.wav"
        if(super().Load(music)):
            return True
        else:
            return False
        
    def load_lowbet(self):
        music = RUTA_SONIDOS + "LowBet_Sound.wav"
        if(super().Load(music)):
            return True
        else:
            return False
        
    def load_medbet(self):
        music = RUTA_SONIDOS + "MedBet_Sound.wav"
        if(super().Load(music)):
            return True
        else:
            return False
        
    def load_nexthand(self):
        music = RUTA_SONIDOS + "Next_Hand_Sound.wav"
        if(super().Load(music)):
            return True
        else:
            return False
        
    def load_nexthand2(self):
        music = RUTA_SONIDOS + "Next_Hand2_Sound.wav"
        if(super().Load(music)):
            return True
        else:
            return False
        
    def load_timeout(self):
        music = RUTA_SONIDOS + "TimeOut_Sound.wav"
        if(super().Load(music)):
            return True
        else:
            return False