from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window

from kivy.lang import Builder

class TestApp(App):
    def build(self):
        btn=Button(text="hello world",font_size=30)
        btn.bind(on_press=self.callback)
        return btn
    def callback(instance):
        print("The button has been pressed")

TestApp().run()
