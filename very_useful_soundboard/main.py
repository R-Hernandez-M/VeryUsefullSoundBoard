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
from random import *
from android.permissions import request_permissions, Permission

request_permissions([Permission.READ_EXTERNAL_STORAGE])
  
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
            sound=SoundLoader.load("bruh.ogg")
        else:
            sound=SoundLoader.load("test_sound.ogg")
        if sound:
            sound.volume=0.5
            sound.play()
    
    
    def build(self):
        layout=GridLayout(cols=3)
        fotito=Image(source="./kawaii.jpg")
        fotito2=Image(source="./kawaii.jpg")
        #primer boton
        #name="test_sound.mp3"
        btnsound=Button(text ='what.ogg',color =(0,0,0,0),background_normal='what.jpg')
        #btnsound.bind(on_press=firstApp.playSound("test_sound.mp3"))
        #sound=SoundLoader.load("test_sound2.mp3");
        btnsound.bind(on_press=firstApp.playSound)
        layout.add_widget(btnsound)
        #segundo boton
        btnsound=Button(text ='horse.ogg',color =(0,0,0,0),background_normal='horseamazing.jpg')
        btnsound.bind(on_press=firstApp.playSound)
        #btnsound.bind(on_press=firstApp.playSound("test_sound.mp3"))
        layout.add_widget(btnsound)
        #tercer boton
        btnsound=Button(text ='door.ogg',color =(0,0,0,0),background_normal='doory.jpg')
        btnsound.bind(on_press=firstApp.playSound)
        #btnsound.bind(on_press=firstApp.playSound("test_sound.mp3"))
        layout.add_widget(btnsound)
        #cuarto boton
        btnsound=Button(text ='bear.ogg',color =(0,0,0,0),background_normal='oso.jpg')
        btnsound.bind(on_press=firstApp.playSound)
        #btnsound.bind(on_press=firstApp.playSound("test_sound.mp3"))
        layout.add_widget(btnsound)
        #quinto boton
        btnsound=Button(text ='dog.ogg',color =(0,0,0,0),background_normal='perro.jpg')
        btnsound.bind(on_press=firstApp.playSound)
        #btnsound.bind(on_press=firstApp.playSound("test_sound.mp3"))
        layout.add_widget(btnsound)
        #sexto boton
        btnsound=Button(text ='scream.ogg',color =(0,0,0,0),background_normal='aaah.jpg')
        btnsound.bind(on_press=firstApp.playSound)
        #btnsound.bind(on_press=firstApp.playSound("test_sound.mp3"))
        layout.add_widget(btnsound)
        #septimo boton
        btnsound=Button(text ='explosion.ogg',color =(0,0,0,0),background_normal='boom.jpg')
        btnsound.bind(on_press=firstApp.playSound)
        #btnsound.bind(on_press=firstApp.playSound("test_sound.mp3"))
        layout.add_widget(btnsound)
        #octavo boton
        btnsound=Button(text ='aguila.ogg',color =(0,0,0,0),background_normal='pajarito.jpg')
        btnsound.bind(on_press=firstApp.playSound)
        #btnsound.bind(on_press=firstApp.playSound("test_sound.mp3"))
        layout.add_widget(btnsound)
        #noveno boton
        btnsound=Button(text ='NONE',color =(0,0,0,0),background_normal='bruh.jpg')
        btnsound.bind(on_press=firstApp.playSoundRandom)
        #btnsound.bind(on_press=firstApp.playSound("test_sound.mp3"))
        layout.add_widget(btnsound)
        
        
        layout.add_widget(fotito)
        #este boton cierra la app
        btn=Button(text="Bye world")
        btn.bind(on_press=firstApp.closeApp)
        layout.add_widget(btn)
        layout.add_widget(fotito2)
        return layout
  

# running the application
firstApp().run()
