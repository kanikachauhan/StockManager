from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen , SlideTransition
import configparser
from kivy.properties import StringProperty

config = configparser.RawConfigParser()
config.read('app.properties')
app_dict = dict(config.items('APP_PROPERTIES'))
barcode_path = app_dict['barcode_path']

Builder.load_file('appsettings.kv')
class AppSettings(Screen):
    barCodePath = StringProperty(barcode_path)
    def build(self):
        self.filepath = barCodePath
        pass

    def save(self,filepath):
        cfgfile = open('app.properties', 'w')
        config.set('APP_PROPERTIES','barcode_path',filepath)
        config.write(cfgfile)
        cfgfile.close()
        self.errorLabel.text = "Values changed!!!"
        pass