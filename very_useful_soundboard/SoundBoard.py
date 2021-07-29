# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 19:00:46 2021

@author: Kayserend
"""
from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

class BaseLayout(BoxLayout):
    
    def play_sound(self):
        sound=SoundLoader.load("test_sound.mp3")
        if sound:
            sound.volume=0.5
            sound.play()
        
class SoundBoard(App):
    def build(self):
        return BaseLayout()
    
SoundBoard().run()