from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.network.urlrequest import UrlRequest
from kivy.uix.recycleview import RecycleView
from kivy.core.window import Window
import urllib.parse
import certifi as cfi
import os
import ssl
import unittest
import urllib.request

import certifi
import requests
from kivy.utils import platform

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    GridLayout:
        cols:1
        row:2
        spacing:10
        padding:[100,100,100,100]
        Button:
            text: 'Ver todas las Láminas'
            on_press: root.manager.current = 'ver'
        
        Button:
            text: 'Ingresar Nueva Lámina'
            on_press: root.manager.current = 'settings'
            
        Button:
            text:'Eliminar una Lámina'
            on_press: root.manager.current = 'delete'
            
        Button:
            text: 'Actualizar una Lámina'
            on_press: root.manager.current = 'update'
        Button:
            text: 'Salir'
            background_color:(255,0,0,1)
            on_release: app.stop()
<SettingsScreen>:
    GridLayout:
        cols:2
        row:2
        spacing:50
        Label:
            text:'Número de la lámina'
        TextInput:
            id:num
            multiline:False
        Label:
            text:'Nombre de la lámina'
        TextInput:
            id:nom
            multiline:False
        Label:
            text:'Número de la sección'
        TextInput:
            id:num_sec
            multiline:False
        Label:
            text:'Nombre de la seccion'
        TextInput:
            id:sec
            multiline:False
        Label:
            text:'Stock de la lámina'
        TextInput:
            id:stock
            multiline:False     
        Button:
            text:'Guardar'
            on_press: root.auth()
        Button:
            text: 'Regresar'
            background_color:(255,0,0,1) 
            on_press: root.manager.current = 'menu'
<UpdateScreen>:
    GridLayout:
        cols:2
        row:2
        spacing:50
        Label:
            text:'ID'
        TextInput:
            id:ide
            multiline:False
        Label:
            text:'Número de la lámina'
        TextInput:
            id:num
            multiline:False
        Label:
            text:'Nombre de la lámina'
        TextInput:
            id:nom
            multiline:False
        Label:
            text:'Número de la sección'
        TextInput:
            id:num_sec
            multiline:False
        Label:
            text:'Nombre de la seccion'
        TextInput:
            id:sec
            multiline:False
        Label:
            text:'Stock de la lámina'
        TextInput:
            id:stock
            multiline:False     
        Button:
            text:'Guardar'
            on_press: root.auth()
        Button:
            text: 'Regresar'
            background_color:(255,0,0,1)
            on_press: root.manager.current = 'menu'
<DeleteScreen>
    GridLayout:
        cols:2
        row:6
        spacing:50
        Label:
            text:'ID lámina a eliminar'
        TextInput:
            id:num
            multiline:False
        
        Label:
            text:''
        Label:
            text:''
        Label:
            text:''
        Label:
            text:''
        Label:
            text:''
        Label:
            text:''    
    
        
        Button:
            text:'Eliminar'
            on_press: root.auth()
            
        Button:
            text: 'Regresar'
            background_color:(255,0,0,1)
            on_press: root.manager.current = 'menu'
<SeeScreen>
    ScrollView:
        size_hint:(None, 1)
        GridLayout:
            cols: 1
            spacing: 10
            size_hint_y:None
            Button:
                text:"REGRESAR"
                size_hint_y:None
                height:60
                background_color:(255,0,0,1)
                on_press: root.manager.current = 'menu'
                
""")

os.environ['SSL_CERT_FILE'] = certifi.where()    
#------------------------------------------MENU-----------------------------------------------------
class MenuScreen(Screen):
    pass

#------------------------------------------DELETE-----------------------------------------------------
class DeleteScreen(Screen):
    def __init__(self, **kwargs):
        super(DeleteScreen, self).__init__(**kwargs)

    def auth(self):
        print("Eliminando..")
        
        os.environ['SSL_CERT_FILE'] = certifi.where()  
        search_url = "https://bazarapi.herokuapp.com/Lamina"
        params = urllib.parse.urlencode({'id': str(self.ids.num.text)})
        headers = {'Content-type': 'application/x-www-form-urlencoded','Accept': 'text/plain'}
        self.req = UrlRequest(search_url, on_success=self.bug_posted, req_body=params,req_headers=headers,method="DELETE" , ca_file=cfi.where(), verify=True)


    def bug_posted(self,*args):
        print(self.req.result)
    pass


#------------------------------------------POST-----------------------------------------------------
class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
    def auth(self):
        print('Guardando..')
        
        os.environ['SSL_CERT_FILE'] = certifi.where()  
        search_url = "https://bazarapi.herokuapp.com/Lamina"
        params = urllib.parse.urlencode({'numero': str(self.ids.num.text), 
                                   'nombre': str(self.ids.nom.text), 
                                   'numero_seccion': self.ids.num_sec.text,
                                   'seccion': str(self.ids.sec.text), 
                                   'stock': self.ids.stock.text})
        headers = {'Content-type': 'application/x-www-form-urlencoded','Accept': 'text/plain'}
        self.req = UrlRequest(search_url, on_success=self.bug_posted, req_body=params,req_headers=headers , ca_file=cfi.where(), verify=True)


    def bug_posted(self,*args):
        print(self.req.result)    
    pass

#------------------------------------------PUT----------------------------------------------------

class UpdateScreen(Screen):
    def __init__(self, **kwargs):
        super(UpdateScreen, self).__init__(**kwargs)
    def auth(self):
        print('Actualizando..')
        os.environ['SSL_CERT_FILE'] = certifi.where()  
        search_url = "https://bazarapi.herokuapp.com/Lamina/"+self.ids.ide.text
        
        params = urllib.parse.urlencode({'numero': str(self.ids.num.text), 
                                   'nombre': str(self.ids.nom.text), 
                                   'numero_seccion': self.ids.num_sec.text,
                                   'seccion': str(self.ids.sec.text), 
                                   'stock': self.ids.stock.text})
        headers = {'Content-type': 'application/x-www-form-urlencoded','Accept': 'text/plain'}
        self.req = UrlRequest(search_url, on_success=self.bug_posted, req_body=params,req_headers=headers,method="PUT", ca_file=cfi.where(), verify=True)

    def bug_posted(self,*args):
        print(self.req.result)    
    pass

#------------------------------------------GET-----------------------------------------------------
class SeeScreen(Screen):
    def __init__(self, **kwargs):
        super(SeeScreen, self).__init__(**kwargs)
        os.environ['SSL_CERT_FILE'] = certifi.where()  
        search_url = "https://bazarapi.herokuapp.com/Lamina?desde=0&limite=1000"
        self.request = UrlRequest(search_url,on_success= self.res, ca_file=cfi.where(), verify=True)              

    
    def res(self,*args):
        lim = self.request.result['cuantos']
        laminas = self.request.result['laminas']
        self.root = ScrollView(size_hint=(1, .8), size=(Window.width, Window.height))
        layout = GridLayout(cols=5, spacing=10, size_hint_y=None)

        self.root3 = ScrollView(size_hint=(1, 0.9), size=(Window.width, Window.height))
        layout3 = GridLayout(cols=5, spacing=10, size_hint_y=None)
        btn3 = Button(text="Nº", size_hint=[.1,None], height=40)
        layout3.add_widget(btn3)
        btn3 = Button(text="Nombre",size_hint=[.8,None], height=40)
        layout3.add_widget(btn3)
        btn3 = Button(text="Nº", size_hint=[.1,None], height=40)
        layout3.add_widget(btn3)
        btn3 = Button(text="Sección", size_hint=[.8,None], height=40)
        layout3.add_widget(btn3)
        btn3 = Button(text="Stock", size_hint=[.1,None], height=40)
        layout3.add_widget(btn3)
        # Make sure the height is such that there is something to scroll.
        layout.bind(minimum_height=layout.setter('height'))
        for i in range(lim):
             btn = Button(text=laminas[i]["numero"], size_hint=[.1,None], height=40)

             layout.add_widget(btn)

             btn = Button(text=laminas[i]["nombre"], size_hint=[.8,None], height=40)
             layout.add_widget(btn)

             btn = Button(text=str(laminas[i]["numero_seccion"]), size_hint=[.1,None], height=40)
             layout.add_widget(btn)

             btn = Button(text=laminas[i]["seccion"], size_hint=[.8,None], height=40)
             layout.add_widget(btn)

             btn = Button(text=str(laminas[i]["stock"]), size_hint=[.1,None], height=40)
             layout.add_widget(btn)



        #self.root2.add_widget(layout2)
        #self.add_widget(self.root2)

        self.root3.add_widget(layout3)
        self.add_widget(self.root3)

        self.root.add_widget(layout)
        self.add_widget(self.root)        
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(UpdateScreen(name='update'))
sm.add_widget(DeleteScreen(name='delete'))
sm.add_widget(SeeScreen(name='ver'))


class TestApp(App):
    title="Cyber Nicole"
    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run() 