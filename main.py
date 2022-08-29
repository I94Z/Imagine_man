import pyperclip
from module import imagine_man
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.slider import Slider
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.core.window import Window
from os import listdir


class Container(Widget):
    lenght = ObjectProperty(None)
    output = ObjectProperty(None)

    def push_generate(self):
        self.output.text = imagine_man(self.lenght.value)

    def push_copy(self):
        pyperclip.copy(self.output.text)


class MainApp(App):
    def build(self):
        Window.size = (350, 600)
        Window.clearcolor = (203/255, 138/255, 88/255, 1)
        self.title = 'Представь чела...'
        return Container()


if __name__ == "__main__":
    MainApp().run()