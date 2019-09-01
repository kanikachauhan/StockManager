from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
import configparser
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen , SlideTransition
from kivy.garden.filebrowser import FileBrowser
import code128
import os
import csv
import datetime
from kivy.garden.filebrowser import FileBrowser
from os.path import sep, expanduser, isdir, dirname
import sys

config = configparser.RawConfigParser()
config.read('app.properties')
app_dict = dict(config.items('APP_PROPERTIES'))
barcode_path = app_dict['barcode_path']

Builder.load_file('generatebarcode.kv')
class GenerateBarCodeWindow(Screen):
    barCodePath = StringProperty(barcode_path)
    now = datetime.datetime.now()
    filename = None
    skulist = None
    popup = None
    def build(self):
        pass
    
    def generateBarCode(self):
        if self.sku.text is None or self.sku.text is "" and self.skulist is None:
            self.errorLabel = "Please enter suvs or browse a file"
        else:
            skuarr = None
            inputStr = self.sku.text
            inputlist = inputStr.split(',')
            if self.barCodePath is None or self.barCodePath is "":
                self.errorLabel = "Go to settings and specify folder location to save the codes"
                return 
            try:
                if self.skulist is not None:
                    skuarr = self.skulist
                else:
                    inputStr = self.sku.text
                    skuarr = inputStr.split(',')
                for s in skuarr:
                    str = self.now.strftime("%Y-%m-%d")
                    fullPath = self.barCodePath+'/'+str
                    if not os.path.exists(fullPath):
                        os.makedirs(fullPath)
                    code128.image(s).save(fullPath+"/"+s+".png")
                if self.skulist is not None:
                    self.skulist = None
                self.errorLabel = "Done"
            except Exception as e:
                print(e)
                self.errorLabel = "Error in generating SKU's"
    
    def chooseFile(self):
        if sys.platform == 'win':
            user_path = dirname(expanduser('~')) + sep + 'Documents'
        else:
            user_path = expanduser('~') + sep + 'Documents'
        browser = FileBrowser(select_string='Select',favorites=[(user_path, 'Documents')])
        self.popup = Popup(size_hint=(None, None),content=browser,auto_dismiss=False,size=(700, 500))
        browser.bind(on_success=self.selectFile,on_canceled=self.popup.dismiss)
        self.popup.open()
    
    def selectFile(self,instance):
        self.filename = instance.selection
        self.skulist = self.readFile(self.filename)
        self.popup.dismiss()
        return 

    def readFile(self,filename):
        with open(filename[0], 'rt') as f:
            reader = csv.DictReader(f, delimiter='\t')
            data = {}
            for row in reader:
                for header, value in row.items():
                    try:
                       data[header].append(value)
                    except KeyError:
                        data[header] = [value]
        return data['sku']