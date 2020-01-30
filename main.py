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
import requests


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
            text:'Actualizar'
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

#------------------------------------------MENU-----------------------------------------------------
class MenuScreen(Screen):
    pass
    
#------------------------------------------DELETE-----------------------------------------------------
class DeleteScreen(Screen):
    def __init__(self, **kwargs):
        super(DeleteScreen, self).__init__(**kwargs)

    def auth(self):
        print("Eliminando..")
        search_url = "https://bazarapi.herokuapp.com/Lamina"
        params = {'id': str(self.ids.num.text)}
        req = requests.delete(search_url, data=params)
        print(req.text)
    pass


#------------------------------------------POST-----------------------------------------------------
class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
    def auth(self):
        print('Guardando..')
        search_url = "https://bazarapi.herokuapp.com/Lamina"
        params = { 'numero': str(self.ids.num.text), 
                                   'nombre': str(self.ids.nom.text), 
                                   'numero_seccion': self.ids.num_sec.text,
                                   'seccion': str(self.ids.sec.text), 
                                   'stock': self.ids.stock.text}
        req = requests.post(search_url, data=params)
        print(req.url)
        print(req.text)   
    pass

#------------------------------------------PUT----------------------------------------------------
    
class UpdateScreen(Screen):
    def __init__(self, **kwargs):
        super(UpdateScreen, self).__init__(**kwargs)
    def auth(self):
        print('Actualizando..')
        search_url = "https://bazarapi.herokuapp.com/Lamina/"+self.ids.ide.text
        
        params = {'numero': str(self.ids.num.text), 
                                   'nombre': str(self.ids.nom.text), 
                                   'numero_seccion': self.ids.num_sec.text,
                                   'seccion': str(self.ids.sec.text), 
                                   'stock': self.ids.stock.text}
        req = requests.put(search_url,data=params)
        print(req.text)    
    pass

#------------------------------------------GET-----------------------------------------------------
class SeeScreen(Screen):
    def __init__(self, **kwargs):
        super(SeeScreen, self).__init__(**kwargs)
        search_url = "https://bazarapi.herokuapp.com/Lamina?desde=0&limite=1000"
        response = requests.get(search_url)
        laminas = response.json()['laminas']
        lim = response.json()['cuantos']
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

        
        self.root3.add_widget(layout3)
        self.add_widget(self.root3)
        
        self.root.add_widget(layout)
        self.add_widget(self.root)
           
     
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