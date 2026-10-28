"""Codigo realizado por:
        Edgar Santiesteban Mendo
        Daniel San Miguel Lopez
"""

import os
import wx
import wx.media

from Music_Player import Music_Player
from Clase_Juego_v2 import Juego
from Clase_Carta_Representada import Carta_Representada

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        
        self.__juego=Juego()
        self.__mano_mostrada=0  #INT con la posicion de la mano mostrada actualmente
        self.__contador = 10       
    

    #CODIGO GENERADO POR GLADE  --------------------------------------------------------------------------------------
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.CAPTION | wx.CLIP_CHILDREN | wx.CLOSE_BOX | wx.FULL_REPAINT_ON_RESIZE | wx.MINIMIZE_BOX | wx.SYSTEM_MENU
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((1600, 900))
        self.SetTitle("BlackJack")

        self.panel_principal = wx.Panel(self, wx.ID_ANY)

        self.mi_reproductor = Music_Player(self.panel_principal)
        
        sizer_principal = wx.BoxSizer(wx.VERTICAL)

        self.window_separador_info_juego = wx.SplitterWindow(self.panel_principal, wx.ID_ANY)
        self.window_separador_info_juego.SetMinimumPaneSize(20)
        sizer_principal.Add(self.window_separador_info_juego, 1, wx.EXPAND, 0)

        self.window_pane_info = wx.Panel(self.window_separador_info_juego, wx.ID_ANY, style=wx.BORDER_SIMPLE | wx.FULL_REPAINT_ON_RESIZE | wx.TAB_TRAVERSAL)

        sizer_info_general = wx.BoxSizer(wx.HORIZONTAL)

        self.window_info_croupier = wx.SplitterWindow(self.window_pane_info, wx.ID_ANY, style=wx.SP_BORDER)
        self.window_info_croupier.SetBackgroundColour(wx.Colour(116, 116, 116))
        self.window_info_croupier.SetMinimumPaneSize(20)
        sizer_info_general.Add(self.window_info_croupier, 1, wx.ALL | wx.EXPAND, 0)

        self.panel_croupier = wx.Panel(self.window_info_croupier, wx.ID_ANY)

        sizer_croupier_general = wx.BoxSizer(wx.VERTICAL)

        self.window_croupier_timer = wx.SplitterWindow(self.panel_croupier, wx.ID_ANY, style=wx.SP_BORDER)
        self.window_croupier_timer.Enable(False)
        self.window_croupier_timer.SetMinimumPaneSize(20)
        sizer_croupier_general.Add(self.window_croupier_timer, 1, wx.EXPAND, 0)

        self.window_croupier = wx.Panel(self.window_croupier_timer, wx.ID_ANY)
        self.window_croupier.SetMinSize((465, 397))
        self.window_croupier.SetBackgroundColour(wx.Colour(255, 0, 127))

        sizer_croupier = wx.BoxSizer(wx.HORIZONTAL)

        ruta_base = os.path.dirname(os.path.abspath(__file__))
        ruta_croupier = os.path.join(ruta_base, "files", "images", "croupier.jpg")

        imagen_img = wx.Image(ruta_croupier, wx.BITMAP_TYPE_ANY)
        imagen_img = imagen_img.Scale(480, 360, wx.IMAGE_QUALITY_HIGH)
        imagen = wx.Bitmap(imagen_img)

        imagen_croupier = wx.StaticBitmap(self.window_croupier, wx.ID_ANY, imagen)
        sizer_croupier.Add(imagen_croupier, 3, wx.ALIGN_CENTER_VERTICAL, 0)

        self.window_timer = wx.Panel(self.window_croupier_timer, wx.ID_ANY)
        self.window_timer.SetBackgroundColour(wx.Colour(78, 0, 39))

        sizer_timer = wx.BoxSizer(wx.HORIZONTAL)

        self.label_timer = wx.StaticText(self.window_timer, wx.ID_ANY, "Timer", style=wx.ALIGN_CENTER_HORIZONTAL)
        self.label_timer.SetMinSize((130, 40))
        self.label_timer.SetBackgroundColour(wx.Colour(47, 47, 47))
        self.label_timer.SetForegroundColour(wx.Colour(255, 226, 79))
        self.label_timer.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_timer.Add(self.label_timer, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 330)

        self.window_info_boton = wx.Panel(self.window_info_croupier, wx.ID_ANY)

        sizer_info_boton = wx.BoxSizer(wx.HORIZONTAL)

        self.panel_info = wx.Panel(self.window_info_boton, wx.ID_ANY, style=wx.BORDER_THEME)
        sizer_info_boton.Add(self.panel_info, 1, wx.EXPAND, 0)

        sizer_info = wx.BoxSizer(wx.VERTICAL)

        self.panel_BalanceTotal = wx.Panel(self.panel_info, wx.ID_ANY)
        self.panel_BalanceTotal.SetMinSize((210, 103))
        self.panel_BalanceTotal.SetBackgroundColour(wx.Colour(66,46,79))
        sizer_info.Add(self.panel_BalanceTotal, 1, wx.EXPAND, 0)

        sizer_BalanceTotal = wx.BoxSizer(wx.VERTICAL)

        label_BalanceTotal = wx.StaticText(self.panel_BalanceTotal, wx.ID_ANY, "Balance Total", style=wx.ALIGN_CENTER_HORIZONTAL | wx.ST_ELLIPSIZE_MIDDLE)
        label_BalanceTotal.SetMinSize((505, 16))
        label_BalanceTotal.SetBackgroundColour(wx.Colour(255, 255, 255))
        label_BalanceTotal.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 1, ""))
        sizer_BalanceTotal.Add(label_BalanceTotal, 0, 0, 0)

        self.label_ContadorBalanceTotal = wx.StaticText(self.panel_BalanceTotal, wx.ID_ANY, "0", style=wx.ALIGN_CENTER_HORIZONTAL)
        self.label_ContadorBalanceTotal.SetMinSize((86, 15))
        self.label_ContadorBalanceTotal.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.label_ContadorBalanceTotal.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_BalanceTotal.Add(self.label_ContadorBalanceTotal, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 4)

        self.panel_BalancePartida = wx.Panel(self.panel_info, wx.ID_ANY)
        self.panel_BalancePartida.SetMinSize((210, 102))
        self.panel_BalancePartida.SetBackgroundColour(wx.Colour(66,46,79))
        sizer_info.Add(self.panel_BalancePartida, 1, wx.EXPAND, 0)

        sizer_BalancePartida = wx.BoxSizer(wx.VERTICAL)

        label_BalancePartida = wx.StaticText(self.panel_BalancePartida, wx.ID_ANY, "Balance de la partida", style=wx.ALIGN_CENTER_HORIZONTAL | wx.ST_ELLIPSIZE_MIDDLE)
        label_BalancePartida.SetMinSize((505, 16))
        label_BalancePartida.SetBackgroundColour(wx.Colour(255, 255, 255))
        sizer_BalancePartida.Add(label_BalancePartida, 0, 0, 0)

        self.label_ContadorBalancePartida = wx.StaticText(self.panel_BalancePartida, wx.ID_ANY, "1", style=wx.ALIGN_CENTER_HORIZONTAL)
        self.label_ContadorBalancePartida.SetMinSize((86, 15))
        self.label_ContadorBalancePartida.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.label_ContadorBalancePartida.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_BalancePartida.Add(self.label_ContadorBalancePartida, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 4)

        self.panel_NumeroPartidas = wx.Panel(self.panel_info, wx.ID_ANY)
        self.panel_NumeroPartidas.SetMinSize((210, 103))
        self.panel_NumeroPartidas.SetBackgroundColour(wx.Colour(66,46,79))
        sizer_info.Add(self.panel_NumeroPartidas, 1, wx.EXPAND, 0)

        sizer_NumeroPartidas = wx.BoxSizer(wx.VERTICAL)

        label_NumeroPartidas = wx.StaticText(self.panel_NumeroPartidas, wx.ID_ANY, u"Número de partidas", style=wx.ALIGN_CENTER_HORIZONTAL | wx.ST_ELLIPSIZE_MIDDLE)
        label_NumeroPartidas.SetMinSize((505, 16))
        label_NumeroPartidas.SetBackgroundColour(wx.Colour(255, 255, 255))
        label_NumeroPartidas.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 1, ""))
        sizer_NumeroPartidas.Add(label_NumeroPartidas, 0, 0, 0)

        self.label_ContadorNumeroPartidas = wx.StaticText(self.panel_NumeroPartidas, wx.ID_ANY, "0", style=wx.ALIGN_CENTER_HORIZONTAL)
        self.label_ContadorNumeroPartidas.SetMinSize((86, 15))
        self.label_ContadorNumeroPartidas.SetBackgroundColour(wx.Colour(0, 255, 127))
        self.label_ContadorNumeroPartidas.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_NumeroPartidas.Add(self.label_ContadorNumeroPartidas, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 4)

        self.panel_boton = wx.Panel(self.window_info_boton, wx.ID_ANY, style=wx.BORDER_THEME)
        self.panel_boton.SetMinSize((140, 312))
        self.panel_boton.SetBackgroundColour(wx.Colour(66,46,79))
        sizer_info_boton.Add(self.panel_boton, 1, wx.EXPAND, 0)

        sizer_boton_miliseg = wx.BoxSizer(wx.VERTICAL)

        self.automatico = wx.ToggleButton(self.panel_boton, wx.ID_ANY, u"Automático\n")
        self.automatico.SetMinSize((100, 73))
        self.automatico.SetBackgroundColour(wx.Colour(234, 188, 73))
        sizer_boton_miliseg.Add(self.automatico, 0, wx.ALL, 67)

        sizer_miliseg = wx.BoxSizer(wx.VERTICAL)
        sizer_boton_miliseg.Add(sizer_miliseg, 1, wx.ALL | wx.EXPAND, 0)

        label_Miliseg = wx.StaticText(self.panel_boton, wx.ID_ANY, "Miliseg", style=wx.ALIGN_CENTER_HORIZONTAL)
        label_Miliseg.SetMinSize((258, 16))
        label_Miliseg.SetBackgroundColour(wx.Colour(255, 255, 255))
        label_Miliseg.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 1, ""))
        sizer_miliseg.Add(label_Miliseg, 0, 0, 0)

        self.text_ctrl_Miliseg = wx.TextCtrl(self.panel_boton, wx.ID_ANY, "")
        sizer_miliseg.Add(self.text_ctrl_Miliseg, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 6)

        self.window_juego_botones = wx.SplitterWindow(self.window_separador_info_juego, wx.ID_ANY, style=wx.SP_3D | wx.SP_LIVE_UPDATE | wx.SP_NOBORDER | wx.SP_THIN_SASH)
        self.window_juego_botones.SetMinimumPaneSize(20)

        self.window_juego = wx.Panel(self.window_juego_botones, wx.ID_ANY)
        self.window_juego.SetMinSize((1042, 650))
        self.window_juego.SetBackgroundColour(wx.Colour(48, 76, 27))

        sizer_juego = wx.BoxSizer(wx.VERTICAL)

        self.panel_juego_croupier = wx.Panel(self.window_juego, wx.ID_ANY, style=wx.BORDER_SUNKEN)
        self.panel_juego_croupier.SetMinSize((991, 30))
        sizer_juego.Add(self.panel_juego_croupier, 1, wx.LEFT | wx.RIGHT | wx.TOP, 35)

        self.sizer_juego_croupier = wx.BoxSizer(wx.HORIZONTAL)

        self.bitmap_button_croupier = wx.BitmapButton(self.panel_juego_croupier, wx.ID_ANY, wx.NullBitmap)
        self.bitmap_button_croupier.SetSize(self.bitmap_button_croupier.GetBestSize())
        self.sizer_juego_croupier.Add(self.bitmap_button_croupier, 0, wx.ALL, 0)

        self.panel_tablero = wx.Panel(self.window_juego, wx.ID_ANY)
        self.panel_tablero.SetBackgroundColour(wx.Colour(48, 76, 27))
        sizer_juego.Add(self.panel_tablero, 1, wx.EXPAND, 0)

        sizer_tablero = wx.BoxSizer(wx.HORIZONTAL)

        self.panel_puntuacion_jugador = wx.Panel(self.panel_tablero, wx.ID_ANY, style=wx.BORDER_RAISED)
        self.panel_puntuacion_jugador.SetBackgroundColour(wx.Colour(216, 216, 191))
        sizer_tablero.Add(self.panel_puntuacion_jugador, 0, wx.ALIGN_BOTTOM | wx.LEFT | wx.TOP, 115)

        sizer_puntuacion_jugador = wx.BoxSizer(wx.HORIZONTAL)

        self.label_contador_puntuacion_jugador = wx.StaticText(self.panel_puntuacion_jugador, wx.ID_ANY, "0", style=wx.ALIGN_CENTER_HORIZONTAL)
        self.label_contador_puntuacion_jugador.SetMinSize((56, 36))
        self.label_contador_puntuacion_jugador.SetFont(wx.Font(17, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        self.label_contador_apuesta_jugador = wx.StaticText(self.panel_puntuacion_jugador, wx.ID_ANY, "0$", style=wx.ALIGN_CENTER_HORIZONTAL)
        self.label_contador_apuesta_jugador.SetMinSize((56, 36))
        self.label_contador_apuesta_jugador.SetFont(wx.Font(17, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        
        sizer_puntuacion_jugador.Add(self.label_contador_puntuacion_jugador, 0, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM, 1)
        sizer_puntuacion_jugador.Add(self.label_contador_apuesta_jugador, 0, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM, 1)
        

        self.panel_mensaje = wx.Panel(self.panel_tablero, wx.ID_ANY, style=wx.BORDER_RAISED)
        sizer_tablero.Add(self.panel_mensaje, 1, wx.ALL, 102)

        sizer_mensaje = wx.BoxSizer(wx.HORIZONTAL)

        self.label_mensaje = wx.StaticText(self.panel_mensaje, wx.ID_ANY, "MENSAJE DE EJEMPLO")
        self.label_mensaje.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.label_mensaje.SetForegroundColour(wx.Colour(255, 255, 255))
        self.label_mensaje.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        sizer_mensaje.Add(self.label_mensaje, 1, wx.EXPAND, 0)

        self.panel_puntuacion_croupier = wx.Panel(self.panel_tablero, wx.ID_ANY, style=wx.BORDER_RAISED)
        self.panel_puntuacion_croupier.SetBackgroundColour(wx.Colour(216, 216, 191))
        sizer_tablero.Add(self.panel_puntuacion_croupier, 0, wx.RIGHT, 60)

        sizer_puntuacion_croupier = wx.BoxSizer(wx.VERTICAL)

        self.label_contador_puntuacion_croupier = wx.StaticText(self.panel_puntuacion_croupier, wx.ID_ANY, "0", style=wx.ALIGN_CENTER_HORIZONTAL)
        self.label_contador_puntuacion_croupier.SetMinSize((56, 36))
        self.label_contador_puntuacion_croupier.SetFont(wx.Font(17, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        sizer_puntuacion_croupier.Add(self.label_contador_puntuacion_croupier, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM, 1)

        sizer_21 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_juego.Add(sizer_21, 1, 0, 0)

        self.button_mano_anterior = wx.Button(self.window_juego, wx.ID_ANY, "<--")
        self.button_mano_anterior.SetMinSize((100, 73))
        self.button_mano_anterior.SetBackgroundColour(wx.Colour(204, 50, 50))
        sizer_21.Add(self.button_mano_anterior, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 15)

        self.panel_juego_jugador = wx.Panel(self.window_juego, wx.ID_ANY, style=wx.BORDER_SUNKEN)
        self.panel_juego_jugador.SetMinSize((826, 160))
        sizer_21.Add(self.panel_juego_jugador, 1, wx.BOTTOM | wx.EXPAND, 24)

        self.sizer_juego_jugador = wx.BoxSizer(wx.HORIZONTAL)

        self.bitmap_button_jugador = wx.BitmapButton(self.panel_juego_jugador, wx.ID_ANY, wx.NullBitmap)
        self.bitmap_button_jugador.SetSize(self.bitmap_button_jugador.GetBestSize())
        self.sizer_juego_jugador.Add(self.bitmap_button_jugador, 0, 0, 0)

        self.button_mano_siguiente = wx.Button(self.window_juego, wx.ID_ANY, "-->")
        self.button_mano_siguiente.SetMinSize((100, 73))
        self.button_mano_siguiente.SetBackgroundColour(wx.Colour(204, 50, 50))
        sizer_21.Add(self.button_mano_siguiente, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 15)

        self.window_botones = wx.Panel(self.window_juego_botones, wx.ID_ANY)
        self.window_botones.SetBackgroundColour(wx.Colour(47, 47, 79))

        sizer_botones = wx.BoxSizer(wx.HORIZONTAL)

        self.Pedir = wx.Button(self.window_botones, wx.ID_ANY, "Pedir")
        self.Pedir.SetMinSize((130, 70))
        self.Pedir.SetBackgroundColour(wx.Colour(0, 127, 255))
        self.Pedir.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        sizer_botones.Add(self.Pedir, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 129)

        self.Cerrar = wx.Button(self.window_botones, wx.ID_ANY, "Cerrar")
        self.Cerrar.SetMinSize((130, 70))
        self.Cerrar.SetBackgroundColour(wx.Colour(255, 0, 0))
        self.Cerrar.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        sizer_botones.Add(self.Cerrar, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 87)

        self.Doblar = wx.Button(self.window_botones, wx.ID_ANY, "Doblar")
        self.Doblar.SetMinSize((130, 70))
        self.Doblar.SetBackgroundColour(wx.Colour(0, 255, 0))
        self.Doblar.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        sizer_botones.Add(self.Doblar, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 87)

        self.Separar = wx.Button(self.window_botones, wx.ID_ANY, "Separar")
        self.Separar.SetMinSize((130, 70))
        self.Separar.SetBackgroundColour(wx.Colour(252, 169, 10))
        self.Separar.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        sizer_botones.Add(self.Separar, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 78)

        self.window_botones.SetSizer(sizer_botones)

        self.panel_juego_jugador.SetSizer(self.sizer_juego_jugador)

        self.panel_puntuacion_croupier.SetSizer(sizer_puntuacion_croupier)

        self.panel_mensaje.SetSizer(sizer_mensaje)

        self.panel_puntuacion_jugador.SetSizer(sizer_puntuacion_jugador)

        self.panel_tablero.SetSizer(sizer_tablero)

        self.panel_juego_croupier.SetSizer(self.sizer_juego_croupier)

        self.window_juego.SetSizer(sizer_juego)

        self.window_juego_botones.SplitHorizontally(self.window_juego, self.window_botones)

        self.panel_boton.SetSizer(sizer_boton_miliseg)

        self.panel_NumeroPartidas.SetSizer(sizer_NumeroPartidas)

        self.panel_BalancePartida.SetSizer(sizer_BalancePartida)

        self.panel_BalanceTotal.SetSizer(sizer_BalanceTotal)

        self.panel_info.SetSizer(sizer_info)

        self.window_info_boton.SetSizer(sizer_info_boton)

        self.window_timer.SetSizer(sizer_timer)

        self.window_croupier.SetSizer(sizer_croupier)

        self.window_croupier_timer.SplitHorizontally(self.window_croupier, self.window_timer)

        self.panel_croupier.SetSizer(sizer_croupier_general)

        self.window_info_croupier.SplitHorizontally(self.panel_croupier, self.window_info_boton, 489)

        self.window_pane_info.SetSizer(sizer_info_general)

        self.window_separador_info_juego.SplitVertically(self.window_pane_info, self.window_juego_botones, 472)

        self.panel_principal.SetSizer(sizer_principal)

        self.Layout()
        self.Centre()
        
        self.timer = wx.Timer(self)
        self.timer_retardo = wx.Timer(self)

        self.Bind(wx.EVT_TOGGLEBUTTON, self.boton_automatico, self.automatico)
        self.Bind(wx.EVT_BUTTON, self.anterior_mano, self.button_mano_anterior)
        self.Bind(wx.EVT_BUTTON, self.siguiente_mano, self.button_mano_siguiente)
        self.Bind(wx.EVT_BUTTON, self.boton_pedir, self.Pedir)
        self.Bind(wx.EVT_BUTTON, self.boton_cerrar, self.Cerrar)
        self.Bind(wx.EVT_BUTTON, self.boton_doblar, self.Doblar)
        self.Bind(wx.EVT_BUTTON, self.boton_separar, self.Separar)
        self.Bind(wx.EVT_TIMER, self.actualiza_timer, self.timer)
        self.Bind(wx.EVT_TIMER, self.timer_automatico, self.timer_retardo)
        
        
    #TERMINA CODIGO GENERADO POR GLADE   --------------------------------------------------------------------------------------
        
        self.dlg_apuesta = ApuestaInicial(self)
        self.dlg_blackjack = blackjack(self)
        
        
        self.inicializado = False
        self.Bind(wx.EVT_ACTIVATE, self.evt_activate, self) 
        
        self.music_player_casino = Music_Player(self.panel_principal)
        self.music_player_countdown = Music_Player(self.panel_principal)
        self.music_player_sound_effects = Music_Player(self.panel_principal)
        
        # Bind the event handler for the media control to ensure it starts properly
        self.Bind(wx.media.EVT_MEDIA_LOADED, self.media_play_casino, self.music_player_casino)
        self.Bind(wx.media.EVT_MEDIA_LOADED, self.media_play_countdown, self.music_player_countdown)
        self.Bind(wx.media.EVT_MEDIA_LOADED, self.media_play_sound_effects, self.music_player_sound_effects)
        
        
        if not self.music_player_casino.load_casino():
            wx.MessageBox("Error al cargar la musica", "Error", wx.ICON_ERROR | wx.OK)
            
        if not self.music_player_countdown.load_countdown():
            wx.MessageBox("Error al cargar la musica", "Error", wx.ICON_ERROR | wx.OK)
        # end wxGlade
        
        

    #COMIENZAN FUNCIONES --------------------------------------------------------------------------------------

    def media_play_sound_effects(self, event):
        # Play the sound once the media is loaded
        self.music_player_sound_effects.Play()

    def media_play_casino(self, event):
        # Play the sound once the media is loaded
        self.music_player_casino.Play()
        
    def media_play_countdown(self, event):
        self.music_player_countdown.Play()

    def timer_automatico(self, event):
        if self.__mano_mostrada>=len(self.__juego.get_manos()):
            self.__mano_mostrada = 0
        array_manos = self.__juego.get_manos()
        mano_actual = array_manos[self.__mano_mostrada]
        if(mano_actual.is_pasado() or mano_actual.is_cerrado()):
            self.__mano_mostrada+=1
            self.music_player_sound_effects.load_nexthand2()
        respuesta_estratega = self.__juego.repuesta_estratega(self.__mano_mostrada)
        if respuesta_estratega == "P":
            self.__juego.pedir(self.__mano_mostrada)
            self.music_player_sound_effects.load_button()
            self.actualiza_estado_mano()
        elif respuesta_estratega == "C":
            self.__juego.cerrar(self.__mano_mostrada)
            self.music_player_sound_effects.load_button()
            self.actualiza_estado_mano()
        elif respuesta_estratega == "D":
            self.__juego.doblar(self.__mano_mostrada)
            self.music_player_sound_effects.load_button()
            self.actualiza_estado_mano()
        elif respuesta_estratega == "S":
            self.__juego.separar(self.__mano_mostrada)
            self.music_player_sound_effects.load_button()
            self.actualiza_estado_mano()

    def boton_automatico(self, event):  # wxGlade: MyFrame.<event_handler>
        retardo = int(self.text_ctrl_Miliseg.GetValue())
        if(self.automatico.GetValue() == True):
            self.timer_retardo.Stop()
            self.__contador=10
            self.timer.Start(1000)
            self.automatico.SetLabelText("AUTOMATICO\n OFF")
            self.__juego.set_estrategia(False)
            self.automatico.SetBackgroundColour(wx.Colour(205,0,0))
        elif(self.automatico.GetValue() == False):
            self.automatico.SetLabelText("AUTOMATICO\n ON")
            self.__juego.set_estrategia(True)
            self.timer_retardo.Start(retardo)
            self.automatico.SetBackgroundColour(wx.Colour(255,0,0))
        self.panel_boton.Layout()
        self.music_player_sound_effects.load_coin()

    def anterior_mano(self, event):  # wxGlade: MyFrame.<event_handler>
        if self.__mano_mostrada<1:
            event.Skip()
        else:
            self.__mano_mostrada-=1
            
            self.music_player_sound_effects.load_nexthand2()
            
            self.__contador=10
            self.music_player_countdown.load_countdown()
            
            self.actualiza_estado_mano()

    def siguiente_mano(self, event):  # wxGlade: MyFrame.<event_handler>
        cantidad_manos = self.__juego.get_manos()
        cantidad_manos = len(cantidad_manos)
        if self.__mano_mostrada>=cantidad_manos-1:
            event.Skip()
        else:
            self.__mano_mostrada+=1
            
            self.music_player_sound_effects.load_nexthand2()
            
            self.__contador=10
            self.music_player_countdown.load_countdown()
            
            self.actualiza_estado_mano()

    def boton_pedir(self, event):  # wxGlade: MyFrame.<event_handler>
        self.__juego.pedir(self.__mano_mostrada)
        
        self.music_player_sound_effects.load_button()
        
        self.__contador=10
        self.music_player_countdown.load_countdown()
        
        self.actualiza_estado_mano()

    def boton_cerrar(self, event):  # wxGlade: MyFrame.<event_handler>
        self.__juego.cerrar(self.__mano_mostrada)
        
        self.music_player_sound_effects.load_button()
        
        self.__contador=10
        self.music_player_countdown.load_countdown()
        
        self.actualiza_estado_mano()

    def boton_doblar(self, event):  # wxGlade: MyFrame.<event_handler>
        self.__juego.doblar(self.__mano_mostrada)
        
        self.music_player_sound_effects.load_button()
        
        self.__contador=10
        self.music_player_countdown.load_countdown()
        
        self.actualiza_estado_mano()

    def boton_separar(self, event):  # wxGlade: MyFrame.<event_handler>
        self.__juego.separar(self.__mano_mostrada)
        
        self.music_player_sound_effects.load_button()
        
        self.__contador=10
        self.music_player_countdown.load_countdown()
        
        self.actualiza_estado_mano()
        
    def muestra_cartas(self, is_player):
        if is_player:
            parent = self.panel_juego_jugador
            sizer = self.sizer_juego_jugador
            mano_actual=self.__juego.get_manos()
            array_cartas = mano_actual[self.__mano_mostrada].get_mano()
        else:
            parent = self.panel_juego_croupier
            sizer = self.sizer_juego_croupier
            mano_actual=self.__juego.get_croupier()
            array_cartas = mano_actual.get_mano()
        
        sizer.Clear(True)
        for i in array_cartas:
            carta = Carta_Representada(parent, i)
            sizer.Add(carta.getBitMap(), 0, 0, 0)
            
        sizer.Layout()
        
    def actualiza_estado_croupier(self):
        mano_actual=self.__juego.get_croupier()
        puntuacion_mano=mano_actual.get_points()
        str_puntuacion_mano = str(puntuacion_mano)
        self.label_contador_puntuacion_croupier.SetLabelText(str_puntuacion_mano)
        self.muestra_cartas(False)
        
    def actualiza_estado_mano(self):
        array_manos = self.__juego.get_manos()
        mano_actual = array_manos[self.__mano_mostrada]
        
        self.Pedir.Enable(True)
        self.Doblar.Enable(True)
        self.Cerrar.Enable(True)
        self.Separar.Enable(True)
        
        if(mano_actual.is_pasado() or mano_actual.is_cerrado()):
            self.Pedir.Enable(False)
            self.Doblar.Enable(False)
            self.Cerrar.Enable(False)
            self.Separar.Enable(False)
            
        if(not mano_actual.puede_separar()):
            self.Separar.Enable(False)
            
        puntuacion_mano=mano_actual.get_points()
        apuesta_mano=mano_actual.get_apuesta()
        str_puntuacion_mano = str(puntuacion_mano)
        str_apuesta_mano = str(apuesta_mano)
        self.label_contador_puntuacion_jugador.SetLabelText(str_puntuacion_mano)
        self.label_contador_apuesta_jugador.SetLabelText(str_apuesta_mano+"$")
        self.panel_tablero.Layout()
        self.muestra_cartas(True)
        self.print_estado_mano()
        if self.__juego.is_fin_partida():
            self.fin_partida()

    def print_estado_mano(self):
        array_manos = self.__juego.get_manos()
        mano_actual = array_manos[self.__mano_mostrada]
        str_estado = mano_actual.str_get_estado()
        self.label_mensaje.SetLabelText(str_estado)
        self.label_mensaje.SetWindowStyle(style=wx.ALIGN_CENTER)
        self.label_mensaje.Parent.Layout()  
    
    def actualiza_timer(self, event):
        if self.__contador>0:
            self.__contador-=1
            self.label_timer.SetLabelText( str(self.__contador) )
            self.label_timer.Parent.Layout()
        elif self.__contador==0:
            self.music_player_countdown.load_countdown()
            self.music_player_sound_effects.load_timeout()
            self.__contador=10
            respuesta_estratega = self.__juego.repuesta_estratega(self.__mano_mostrada)
            if respuesta_estratega == "P":
                self.__juego.pedir(self.__mano_mostrada)
                self.music_player_sound_effects.load_button()
                self.actualiza_estado_mano()
            elif respuesta_estratega == "C":
                self.__juego.cerrar(self.__mano_mostrada)
                self.music_player_sound_effects.load_button()
                self.actualiza_estado_mano()
            elif respuesta_estratega == "D":
                self.__juego.doblar(self.__mano_mostrada)
                self.music_player_sound_effects.load_button()
                self.actualiza_estado_mano()
            elif respuesta_estratega == "S":
                self.__juego.separar(self.__mano_mostrada)
                self.music_player_sound_effects.load_button()
                self.actualiza_estado_mano()
            
    def fin_partida(self):
        
        self.timer.Stop()
        self.music_player_countdown.Stop()
        self.label_mensaje.SetLabelText("NO QUEDAN MANOS ABIERTAS")
        
        if self.__juego.is_blackjack():
            self.music_player_sound_effects.load_blackjack()
            btn_blackjack = self.dlg_blackjack.ShowModal()
        
        self.__juego.turno_croupier()
        self.actualiza_estado_croupier()
        
        resultado_partida = self.__juego.fin_partida_v2()
        
        self.label_ContadorBalancePartida.SetLabelText(str(resultado_partida))
        if resultado_partida<0:
            self.label_ContadorBalancePartida.SetForegroundColour(wx.Colour(204,50,0))
        else:
            if resultado_partida<11:
                self.music_player_sound_effects.load_lowbet()
            if resultado_partida<21:
                self.music_player_sound_effects.load_medbet()
            else:  
                self.music_player_sound_effects.load_highbet()  
            self.label_ContadorBalancePartida.SetForegroundColour(wx.Colour(127,255,0))
            
        balance_total = int(self.label_ContadorBalanceTotal.GetLabelText())
        balance_total+=int(resultado_partida)
        
        self.label_ContadorBalanceTotal.SetLabelText(str(balance_total))
        if balance_total<0:
            self.label_ContadorBalanceTotal.SetForegroundColour(wx.Colour(204,50,0))
        else:
            self.label_ContadorBalanceTotal.SetForegroundColour(wx.Colour(127,255,0))
        
        num_partidas = int(self.label_ContadorNumeroPartidas.GetLabelText())
        num_partidas += 1
        
        self.label_ContadorNumeroPartidas.SetLabelText(str(num_partidas))
        
        if self.__juego.is_estrategia():
            self.__juego.vaciar_manos()
            self.__juego.inicio(0)
            if self.__juego.is_fin_partida():
                self.fin_partida()
            self.actualiza_estado_croupier()
            self.actualiza_estado_mano()
        else:
            self.inicio_partida()
        
    def inicio_partida(self):
        btn_apuesta = self.dlg_apuesta.ShowModal()
        self.timer.Stop()
        if btn_apuesta == wx.ID_OK:
            respuesta_apuesta = self.dlg_apuesta.get_valor_apuesta()
            wx.LogMessage("La apuesta seleccionada es: " + str(respuesta_apuesta))
            self.timer.Start(1000)
            self.music_player_countdown.load_countdown()
        else:
            wx.LogMessage("Se cerro el dialogo")
            
        self.__juego.vaciar_manos()
        self.__juego.inicio(respuesta_apuesta)
        if self.__juego.is_fin_partida():
            self.fin_partida()
        self.music_player_sound_effects.load_deal()
        self.actualiza_estado_croupier()
        self.actualiza_estado_mano()
            
    def evt_activate(self, event):
        if not self.inicializado:
            self.inicializado = True
            self.inicio_partida()
        # Mostrar el diálogo de elegir apuesta
        else:
            event.Skip()
            
class blackjack(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: blackjack.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.SetTitle("B L A C K J A C K")

        sizer_blackjack = wx.BoxSizer(wx.VERTICAL)

        label_blackjack = wx.StaticText(self, wx.ID_ANY, "\n    ******************\n   ***BLACKJACK***\n   ******************")
        label_blackjack.SetMinSize((2003, 2003))
        label_blackjack.SetBackgroundColour(wx.Colour(0, 0, 0))
        label_blackjack.SetForegroundColour(wx.Colour(179, 179, 92))
        label_blackjack.SetFont(wx.Font(30, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        sizer_blackjack.Add(label_blackjack, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, 0)

        self.SetSizer(sizer_blackjack)

        self.Layout()
        self.Centre()
        # end wxGlade

class ApuestaInicial(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: ApuestaInicial.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.SetTitle("Introduzca apuesta inicial")

        sizer_ai_general = wx.BoxSizer(wx.VERTICAL)

        self.window_ai_general = wx.SplitterWindow(self, wx.ID_ANY)
        self.window_ai_general.SetMinimumPaneSize(20)
        sizer_ai_general.Add(self.window_ai_general, 1, wx.EXPAND, 0)

        self.window_texto_ai = wx.Panel(self.window_ai_general, wx.ID_ANY)
        self.window_texto_ai.SetBackgroundColour(wx.Colour(65, 115, 14))

        sizer_texto_ai = wx.BoxSizer(wx.HORIZONTAL)

        label_texto_ai = wx.StaticText(self.window_texto_ai, wx.ID_ANY, "Por favor, introduzca una apuesta inicial:", style=wx.ALIGN_CENTER_HORIZONTAL)
        label_texto_ai.SetForegroundColour(wx.Colour(249, 249, 0))
        label_texto_ai.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        sizer_texto_ai.Add(label_texto_ai, 7, wx.EXPAND | wx.TOP, 27)

        self.window_num_ai = wx.Panel(self.window_ai_general, wx.ID_ANY)
        self.window_num_ai.SetBackgroundColour(wx.Colour(0, 0, 0))

        sizer_num_ai = wx.BoxSizer(wx.VERTICAL)

        self.choice_apuesta = wx.Choice(self.window_num_ai, wx.ID_ANY, choices=["10", "20", "50"])
        self.choice_apuesta.SetBackgroundColour(wx.Colour(192, 192, 192))
        self.choice_apuesta.SetForegroundColour(wx.Colour(255, 255, 0))
        self.choice_apuesta.SetSelection(0)
        sizer_num_ai.Add(self.choice_apuesta, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.SHAPED, 30)

        sizer_2 = wx.StdDialogButtonSizer()
        sizer_ai_general.Add(sizer_2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 4)

        self.button_OK = wx.Button(self, wx.ID_OK, "Confirmar")
        self.button_OK.SetBackgroundColour(wx.Colour(255, 0, 15))
        self.button_OK.SetDefault()
        sizer_2.Add(self.button_OK, 0, 0, 0)

        sizer_2.Realize()

        self.window_num_ai.SetSizer(sizer_num_ai)

        self.window_texto_ai.SetSizer(sizer_texto_ai)

        self.window_ai_general.SplitHorizontally(self.window_texto_ai, self.window_num_ai)

        self.SetSizer(sizer_ai_general)

        self.SetAffirmativeId(self.button_OK.GetId())

        self.Layout()
        self.Centre()
        # end wxGlade
        
    def get_valor_apuesta(self):
        index_valor = self.choice_apuesta.GetSelection()
        if index_valor == 0:
            return 10
        elif index_valor == 1:
            return 20
        else: 
            return 50

        
# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
