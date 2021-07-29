# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 02:27:42 2021

@author: Kayserend
"""
# importing button widget from kivy framework
from kivy.uix.button import Button
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from kivy.uix.label import Label
from kivy.clock import Clock
from random import *
import time
  
  
# this is the main class which 
# will render the whole application


class firstApp(App):
  
    # method which will render our application
    def closeApp(self):
        # closing application
        App.get_running_app().stop()
        # removing window
        Window.close()
    
    def playSound(self):
        sound=SoundLoader.load(self.text)
        if sound:
            sound.volume=0.5
            sound.play()
            
    def playSoundRandom(self):
        a=randint(1,100)
        if a>=2:
            sound=SoundLoader.load("bruh.mp3")
        else:
            sound=SoundLoader.load("test_sound.mp3")
        if sound:
            sound.volume=0.5
            sound.play()
    
    
    def build(self):
        layout=GridLayout(cols=3)
        fotito=Image(source="./kawaii.jpg")
        fotito2=Image(source="./kawaii.jpg")
        #primer boton
        #name="test_sound.mp3"
        btnsound=Button(text ='what.mp3',color =(0,0,0,0),background_normal='what.jpg')
        #btnsound.bind(on_press=firstApp.playSound("test_sound.mp3"))
        #sound=SoundLoader.load("test_sound2.mp3");
        btnsound.bind(on_press=firstApp.playSound)
        layout.add_widget(btnsound)
        #segundo boton
        btnsound=Button(text ='horse.mp3',color =(0,0,0,0),background_normal='horseamazing.jpg')
        btnsound.bind(on_press=firstApp.playSound)
        #btnsound.bind(on_press=firstApp.playSound("test_sound.mp3"))
        layout.add_widget(btnsound)
        #tercer boton
        btnsound=Button(text ='door.mp3',color =(0,0,0,0),background_normal='doory.jpg')
        btnsound.bind(on_press=firstApp.playSound)
        #btnsound.bind(on_press=firstApp.playSound("test_sound.mp3"))
        layout.add_widget(btnsound)
        #cuarto boton
        btnsound=Button(text ='bear.mp3',color =(0,0,0,0),background_normal='oso.jpg')
        btnsound.bind(on_press=firstApp.playSound)
        #btnsound.bind(on_press=firstApp.playSound("test_sound.mp3"))
        layout.add_widget(btnsound)
        #quinto boton
        btnsound=Button(text ='dog.mp3',color =(0,0,0,0),background_normal='perro.jpg')
        btnsound.bind(on_press=firstApp.playSound)
        #btnsound.bind(on_press=firstApp.playSound("test_sound.mp3"))
        layout.add_widget(btnsound)
        #sexto boton
        btnsound=Button(text ='scream.mp3',color =(0,0,0,0),background_normal='aaah.jpg')
        btnsound.bind(on_press=firstApp.playSound)
        #btnsound.bind(on_press=firstApp.playSound("test_sound.mp3"))
        layout.add_widget(btnsound)
        #septimo boton
        btnsound=Button(text ='explosion.mp3',color =(0,0,0,0),background_normal='boom.jpg')
        btnsound.bind(on_press=firstApp.playSound)
        #btnsound.bind(on_press=firstApp.playSound("test_sound.mp3"))
        layout.add_widget(btnsound)
        #octavo boton
        btnsound=Button(text ='aguila.mp3',color =(0,0,0,0),background_normal='pajarito.jpg')
        btnsound.bind(on_press=firstApp.playSound)
        #btnsound.bind(on_press=firstApp.playSound("test_sound.mp3"))
        layout.add_widget(btnsound)
        #noveno boton
        btnsound=Button(text ='NONE',color =(0,0,0,0),background_normal='bruh.jpg')
        btnsound.bind(on_press=firstApp.playSoundRandom)
        #btnsound.bind(on_press=firstApp.playSound("test_sound.mp3"))
        layout.add_widget(btnsound)
        
        clock=IncrediblyCrudeClock()
        Clock.schedule_interval(clock.update, 1)
        layout.add_widget(fotito)
        #este boton cierra la app
        btn=Button(text="Bye world")
        btn.bind(on_press=firstApp.closeApp)
        layout.add_widget(btn)
        layout.add_widget(clock)
        return layout
  
class IncrediblyCrudeClock(Label):
    def update(self, *args):
        self.text = time.asctime()
# running the application
firstApp().run()