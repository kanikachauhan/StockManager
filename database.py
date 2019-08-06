import mysql.connector
import configparser
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
class DatabaseManagement:
    def fetchBrands(self):
        query = 'select distinct brand from stock where brand is not null'
        cursor = db.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    
    def createNewBrand(self,brand,model,quantity):
        query = """ INSERT INTO `stock` (`brand`,`model`,`quantity`) values (%s,%s,%s) """
        data = [brand,model,int(quantity)]
        cursor = db.cursor()
        result = cursor.execute(query,data)
        db.commit()

    def checkValuePresent(self,brand,model):
        query = "select * from `stock` where `brand`=%s and `model`=%s"
        data = [brand,model]
        cursor = db.cursor()
        result = cursor.execute(query,data)
        return result
    
    def getModelsForBrand(self,brand):
        query = "select distinct model from `stock` where brand like %s"
        data = [brand]
        cursor = db.cursor()
        cursor.execute(query,data)
        result = cursor.fetchall()
        return result

    def getQuantityForEntry(self,brand,model):
        query = "select quantity from `stock` where brand like %s and model like %s"
        data = [brand,model]
        cursor = db.cursor()
        cursor.execute(query,data)
        result = cursor.fetchone()
        return result

    def updateQuantity(self,brand,model,quantity):
        query = "update stock set quantity=%s where brand like %s and model like %s"
        data = [quantity,brand,model]
        cursor = db.cursor()
        result = cursor.execute(query,data)
        db.commit()