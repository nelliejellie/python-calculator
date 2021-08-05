from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


# set the default size of the app
Window.size = (500,600)


# Builder.load_file('Calc.kv')

class Calcky(BoxLayout):
    # the erase function
    def erase_last(self):
        lister = list(self.ids.tex_in.text)
        lister.pop()
        self.ids.tex_in.text = ''.join(lister)
        print('erase')

    def erase(self):
        self.ids.tex_in.text = ''
        print('erase')
    
    # adding numnbers function
    def nine(self):
        if self.ids.tex_in.text == "0":
            self.ids.tex_in.text = ""
        self.ids.tex_in.text = self.ids.tex_in.text + "9"
    def eight(self):
        if self.ids.tex_in.text == "0":
            self.ids.tex_in.text = ""
        self.ids.tex_in.text = self.ids.tex_in.text + "8"
    def seven(self):
        if self.ids.tex_in.text == "0":
            self.ids.tex_in.text = ""
        self.ids.tex_in.text = self.ids.tex_in.text + "7"
    def six(self):
        if self.ids.tex_in.text == "0":
            self.ids.tex_in.text = ""
        self.ids.tex_in.text = self.ids.tex_in.text + "6"
    def five(self):
        if self.ids.tex_in.text == "0":
            self.ids.tex_in.text = ""
        self.ids.tex_in.text = self.ids.tex_in.text + "5"
    def four(self):
        if self.ids.tex_in.text == "0":
            self.ids.tex_in.text = ""
        self.ids.tex_in.text = self.ids.tex_in.text + "4"
    def three(self):
        if self.ids.tex_in.text == "0":
            self.ids.tex_in.text = ""
        self.ids.tex_in.text = self.ids.tex_in.text + "3"
    def two(self):
        if self.ids.tex_in.text == "0":
            self.ids.tex_in.text = ""
        self.ids.tex_in.text = self.ids.tex_in.text + "2"
    def one(self):
        if self.ids.tex_in.text == "0":
            self.ids.tex_in.text = ""
        self.ids.tex_in.text = self.ids.tex_in.text + "1"
    def zero(self):
        if self.ids.tex_in.text == "0":
            self.ids.tex_in.text = ""
        self.ids.tex_in.text = self.ids.tex_in.text + "0"
    def dot(self):
        if self.ids.tex_in.text == "0":
            self.ids.tex_in.text = ""
        self.ids.tex_in.text = self.ids.tex_in.text + "."

    # the arithemetic operators
    def add(self):
        if self.ids.tex_in.text == "0":
            self.ids.tex_in.text = ""
        self.ids.tex_in.text = self.ids.tex_in.text + "+"
    def minus(self):
        if self.ids.tex_in.text == "0":
            self.ids.tex_in.text = ""
        self.ids.tex_in.text = self.ids.tex_in.text + "-"
    def divide(self):
        if self.ids.tex_in.text == "0":
            self.ids.tex_in.text = ""
        self.ids.tex_in.text = self.ids.tex_in.text + "/"
    def multiply(self):
        if self.ids.tex_in.text == "0":
            self.ids.tex_in.text = ""
        self.ids.tex_in.text = self.ids.tex_in.text + "*"
    def percentage(self):
        if self.ids.tex_in.text == "0":
            self.ids.tex_in.text = ""
        self.ids.tex_in.text = str(float(self.ids.tex_in.text)/100)
    def equals(self):
        if self.ids.tex_in.text == "0":
            self.ids.tex_in.text = ""
        try:
            self.ids.tex_in.text = str(eval(self.ids.tex_in.text))
        except:
            self.ids.tex_in.text = "invalid OP"

        
         


class CalcApp(App):
    def build(self):
        return Calcky()

if __name__ == '__main__':
    CalcApp().run()