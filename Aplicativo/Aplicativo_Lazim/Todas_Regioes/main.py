from carregando_modelo_criado import modelo_famacha

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup

nome_arquivo = ''

class Gerenciador(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Mensagem(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
    def get_label_text(self):
        global nome_arquivo
        self.ids.label_text.text = nome_arquivo

class FileManager(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.select_file = ''
    
    def selection(self,filename):
        self.select_file = filename

    def get_file(self):
        #Essa função vai retornar o nome do arquivo
        resultado = self.select_file
        global nome_arquivo
        print(resultado[0])
        nome_arquivo = modelo_famacha(resultado[0])

class MenuInicial(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def on_botao_sair_pressed(self):
        quit()

class TelaPrincipal(Screen): 
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    

class FamachaApp(App):
    def build(self):
        return Gerenciador()
    
     

if __name__ == "__main__":
    FamachaApp().run()