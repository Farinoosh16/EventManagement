from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker
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
import calendar
from datetime import date
from eventbanner import EventBanner
import requests
import json
from kivy.app import App


class HomeScreen(Screen):
    t = str(date.today())
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    pass
class LoginScreen(Screen):
    pass
class ForgetScreen(Screen):
    pass
class ProfileScreen(Screen):
    pass
class AddEventScreen(Screen):
    t = str(date.today())
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    pass
class DateScreen(Screen):
    t = str(date.today())
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    pass

class ImageButton(ButtonBehavior, Image):
    pass
class LabelButton(ButtonBehavior , Label):
    pass

class SignupScreen(Screen):
    pass


GUI = Builder.load_file('main.kv')

class MainApp(MDApp):
    #event_image = None
    #option_choice = None
    def build(self):
        self.my_firebase = MyFirebase()
        return GUI
    #def update_event_image(self, filename, widget_id):
        #self.event_image = filename


    def on_start(self):
        # populate event image grid
        event_image_grid = self.root.ids['add_event_screen'].ids['event_image_grid']
        for root_dir, folders, files in walk("icons/events"):
            for f in files:
                if '.png' in f:
                    img = ImageButton(source="icons/events/" + f)
                    event_image_grid.add_widget(img)







        try:
            #try to read refresh token
            with open("refresh_Token.txt", 'r') as f:
                refresh_token=f.read()
            # use refreshtoken to get new idtoken
            id_token,local_id = self.my_firebase.exchange_refresh_token(refresh_token)
            # get the database

            result = requests.get("https://wazzup-1bca4-default-rtdb.firebaseio.com/" +local_id + ".json?auth=" + id_token)

            print("was it ok?", result.ok)
            print(result.json())
            data = json.loads(result.content.decode())

            # get and update avatar image
            #avatar_image= self.root.ids['profile_screen'].ids['avatar_image']
            #avatar_image.source="icons/"+data['avatar']

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
                #for i in range(5):
                    # populate workout grid in home screen
                    #E =EventBanner(event_image=event['event_image'],description= event['description'])
                    #banner_grid.add_widget(E)



            self.change_screen("home_screen")
        except:
            pass



    def change_screen(self, screen_name):
        screen_manager= self.root.ids['screen_manager']
        screen_manager.current = screen_name
        pass

    # calendar in data screen
    #in calendar you click on OK

    def on_save(self, instance, value , date_range):
        self.root.ids['date_screen'].ids['date_label'].text = str(value)

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save =self.on_save)
        date_dialog.open()

    def add_event(self):
        # Get data from all fields in add event screen
        event_ids = self.root.ids['add_event_screen'].ids
        # Already have workout image in self.workout_image variable
        #print(self.root.ids['add_event_screen'].ids['event_name'].text)
        #event_song = self.root.ids['event_song'].text.replace("\n","")
        # Already have option choice in self.option_choice
        number_label = event_ids['number_label'].text
        number_input = event_ids['number_input'].text
        month_input = event_ids['month_input'].text
        day_input = event_ids['day_input'].text
        year_input = event_ids['year_input'].text

        # Make sure fields aren't garbage
        #if self.event_image == None:
            #print("back to this later")
            #return
        # They are allowed to leave no description
        #if self.option_choice == None:
            #event_ids['private_label'].color = (1, 0, 0, 1)
            #event_ids['back_label'].color = (1, 0, 0, 1)
            #return
        try:
            int_number = int(number_input)
        except:
            event_ids['number_input'].background_color = (1, 0, 0, 1)
            return
        #another way to avoid junks below:
        try:
            int_month = int(month_input)
            if int_month > 12:
                event_ids['month_input'].background_color = (1, 0, 0, 1)
                return
        except:
            event_ids['month_input'].background_color = (1, 0, 0, 1)
            return
        try:
            int_day = int(day_input)
            if int_day > 31:
                event_ids['day_input'].background_color = (1, 0, 0, 1)
                return
        except:
            event_ids['day_input'].background_color = (1, 0, 0, 1)
            return
        try:
            if len(year_input) == 2:
                year_input = '20' + year_input
            int_year = int(year_input)
        except:
            event_ids['year_input'].background_color = (1, 0, 0, 1)
            return




MainApp().run()