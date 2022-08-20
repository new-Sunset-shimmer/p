import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label  
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout

Window.size = (250,400)

Builder.load_file('kivr12.kv') 

class MyLayout(Widget):
    def number(self):
        self.ids.calcu_main.text = "0"

    def Butpress(self, button):
            prior = self.ids.calcu_main.text

            if "ERROR" in prior:
                prior = ""
                
            if prior == "0":
                self.ids.calcu_main.text = ''
                self.ids.calcu_main.text = f'{button}'
            else:
                self.ids.calcu_main.text = f'{prior}{button}'
    def Changepos(self):
        prior = self.ids.calcu_main.text

        if "-" in prior:
            self.ids.calcu_main.text = "{}".format(prior.replace("-", "+"))
        else:
            self.ids.calcu_main.text = f"-{prior}"

        
    def backspace(self):
        prior = self.ids.calcu_main.text
        
        if prior == "0":
            pass
        else:
            prior = prior[:-1]

            self.ids.calcu_main.text = "{}".format(prior)


    def dot(self):
        prior = self.ids.calcu_main.text

        num_list = prior.split("+")

        if "+" in prior and "." not in num_list[-1]:

            prior = f"{prior}."

            self.ids.calcu_main.text = prior

        if "." in prior:
            pass
        else:
            prior = "{}.".format(prior)

            self.ids.calcu_main.text = prior

    def sign(self,sig):
        prior = self.ids.calcu_main.text
        self.ids.calcu_main.text = f'{prior}{sig}'
    
    def equal(self):
        prior = self.ids.calcu_main.text 

        try:
            answer = eval(prior)

            self.ids.calcu_main.text = str(answer)
        except:
            self.ids.calcu_main.text = "ERROR"

        '''
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0
            for number in num_list:
                answer = answer + float(number)
        if "X" in prior:
            num_list = prior.split("X")
            answer = 1
            for number in num_list:
                answer = answer * float(number)

        self.ids.calcu_main.text = str(answer)
        '''

    
class calculatorapp(App):
    def build(self):
        return MyLayout()
        
if __name__ == '__main__':
    calculatorapp().run()
