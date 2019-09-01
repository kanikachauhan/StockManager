from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen , SlideTransition
import mysql.connector
from kivy.properties import StringProperty,ListProperty
import configparser
from database import DatabaseManagement
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout

config = configparser.RawConfigParser()
config.read('database.properties')
details_dict = dict(config.items('DATABASE_PROPERTIES'))
databasename = details_dict['databasename']
username = details_dict['username']
password = details_dict['password']
hosturl = details_dict['hosturl']
port = details_dict['port']

db = mysql.connector.connect( host=hosturl,user=username, passwd=password,db=databasename,buffered=True)
Builder.load_file('maintainstock.kv')
class MaintainStock(Screen):
    db = DatabaseManagement()
    brandsList = ListProperty()
    modelsList = ListProperty()

    def populateModelsForBrands(self,brand):
        models = self.db.getModelsForBrand(brand)
        dbmodels = [t[0] for t in models]
        self.modelsList = dbmodels

    def addValues(self,brand,model,quantity):
        quant = self.db.getQuantityForEntry(brand,model)
        newqty = quant[0] + int(quantity)
        self.db.updateQuantity(brand,model,newqty)
        self.errorLabel.text = "Updated to "+str(newqty)
    
    def subtractValues(self,brand,model,quantity):
        quant = self.db.getQuantityForEntry(brand,model)
        newqty = quant[0] - int(quantity)
        if newqty < 0:
            newqty = 0
        self.db.updateQuantity(brand,model,newqty)
        self.errorLabel.text = "Updated to "+str(newqty)