import kivy  # import kivy module
from kivy.app import App # import Kivy App module to create a Kivy interface
from kivy.uix.image import Image # import image Module

kivy.require('1.11.1')  # version required to run Kivy Application

class MyKivyApp(App): # Create a class MyKivyApp
    def build(self):
        return Image(source ="./imagenes/imagen.jpg") #return an Image as a root widget

MyKivyApp().run()  # Class MyKivyApp is initialized and run () method is called to run the App.
