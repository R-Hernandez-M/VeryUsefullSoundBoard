import kivy
from kivy.app import App
from kivy.uix.button import Button #import Button
kivy.require("1.9.1")
class kivyButtonApp(App):
    def build(self):
        btn = Button(text = "Press Me!")
        return btn


root = kivyButtonApp()
root.run()
