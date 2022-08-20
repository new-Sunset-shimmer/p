import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label  
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('kyrus.kv') 

class MyLayout(Widget):
   pass

class kyrusapp(App):
    def build(self):
        return MyLayout()
        
if __name__ == '__main__':
    kyrusapp().run()
