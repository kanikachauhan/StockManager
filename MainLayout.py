from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from database import DatabaseManagement
import kivy.uix.button  as kb


Builder.load_file('mainlayout.kv')
class MainLayout(BoxLayout):
    db = DatabaseManagement()
    def maintainStock(self):
        brands = self.db.fetchBrands()
        dbbrands = [t[0] for t in brands]
        self.sm.screens[3].brand_spinner.values = dbbrands
        self.sm.screens[3].brand_spinner.text = 'Select Brand'
        self.sm.screens[3].model_spinner.text = 'Select Model'
        self.sm.screens[3].quantity.text = ''
        self.sm.screens[3].errorLabel.text = ''
        self.sm.current = 'MaintainStock'
        pass

    def generateBarCode(self):
        self.sm.screens[0].sku.text = ''
        self.sm.screens[0].errorLabel.text = ''
        self.sm.current = 'GenerateBarCodeWindow'
        pass

    def addEntry(self):
        self.sm.screens[2].errorLabel.text = ''
        self.sm.screens[2].model.text = ''
        self.sm.screens[2].brand.text = ''
        self.sm.screens[2].quantity.text = ''
        self.sm.current = 'AddEntry'
        pass
