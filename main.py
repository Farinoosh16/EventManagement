from kivy.app import App
from kivy.uix.widget import Widget
from kivy.app import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior
from kivy.uix.label import Label
from os import walk
from myfirebase import MyFirebase
from functools import partial
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from datetime import datetime, date, time, timedelta
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
import time
from eventbanner import EventBanner

import requests
import json

class HomeScreen(Screen):
    t = time.asctime()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    pass
class LoginScreen(Screen):
    pass
class ForgetScreen(Screen):
    pass
class ProfileScreen(Screen):
    pass
class ImageButton(ButtonBehavior, Image):
    pass
class LabelButton(ButtonBehavior , Label):
    pass

class SignupScreen(Screen):
    pass


GUI = Builder.load_file('main.kv')

class MainApp(App):
    def build(self):
        self.my_firebase= MyFirebase()
        return GUI
    def on_start(self):
        try:
            #try to read refresh token
            with open("refresh_Token.txt", 'r') as f:
                refresh_token=f.read()
            # use refreshtoken to get new idtoken
            id_token,local_id = self.my_firebase.exchange_refresh_token(refresh_token)
            # get the database

            result = requests.get("https://wazzup-1bca4-default-rtdb.firebaseio.com" +  local_id + ".json?auth=" + id_token)

            print("was it ok?", result.ok)
            print(result.json())
            data = json.loads(result.content.decode())

            # get and update avatar image
            #avatar_image= self.root.ids['profile_screen'].ids['avatar_image']
            #avatar_image.source="icons/"+data['avatar_image']
            #logo = self.root.ids['logo']
            #logo.source = "icons/" + data['logo']
            # get and update the first label

            #email = self.root.ids['home_screen'].ids['email']
            #email.text = str(data['email'])
            #password = self.root.ids['home_screen'].ids['password']
            #password.text = str(data['password'])
            #print(data)

            # get and update the first label
            #user_id_label=self.root.ids['setting_screen'].ids['user_id_label']
            #user_id_label.text="USER ID: " + str(self.new_user_id)


            #banner_grid= self.root.ids['home_screen'].ids['banner_grid']
            #events = data['events'][1:]
            #for event in events:
             #   for i in range(5):
                    # populate workout grid in home screen
              #      E =EventBanner(event_image=event['event_image'],description= event['description'])
               #     banner_grid.add_widget(E)



            self.change_screen("home_screen")
        except:
            pass

    def change_screen(self, screen_name):

        screen_manager= self.root.ids['screen_manager']
        screen_manager.current = screen_name
        pass


MainApp().run()