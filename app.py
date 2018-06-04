from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
import xml.etree.cElementTree as ET
import fileinput
import sys

from kivy.lang import Builder


customwidget = Builder.load_file("layout.kv")
class Reg(FloatLayout):
    # define the multiplication of a function
    def loadFile(self, instance):
       with open('output.txt') as f:
          self.result.text = f.read()

    def saveFile(self, instance):
        with open('output.txt', 'w') as f:
            f.write(self.result.text)
            f.close()

class RegistrationApp(App):
    def build(self):
        return Reg()

if __name__ == '__main__':
    RegistrationApp().run()