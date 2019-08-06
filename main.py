from kivy.app import App
from GenerateBarCode import GenerateBarCodeWindow
from MaintainStock import MaintainStock
from AppSettings import AppSettings
from AddEntry import AddEntry
from kivy.uix.screenmanager import ScreenManager, Screen , SlideTransition
from kivy.core.window import Window
from MainLayout import MainLayout

Window.size = (700, 400)
Window.borderless = 'True'
class App(App):

    def build(self):
        return MainLayout()

if __name__ == '__main__':
    App().run()