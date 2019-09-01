from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen , SlideTransition
import configparser
from kivy.properties import StringProperty
from database import DatabaseManagement


Builder.load_file('addEntry.kv')
class AddEntry(Screen):
    db = DatabaseManagement()
    def build(self):
        pass
    
    def saveEntry(self,brand,model,quantity):
        try:
            entryPresent = self.db.checkValuePresent(brand,model)
            if entryPresent is None:
                result = self.db.createNewBrand(brand,model,quantity)
                self.errorLabel.text = 'Value added'
            else:
                self.errorLabel.text = 'Brand and Model combination present'
        except Exception as e:
            print(e)
            self.errorLabel.text='Error while saving'   
