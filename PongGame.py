from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from KivyCalendar import DatePicker
from kivy.core.window import Window
from kivy.calendar_ui import DatePicker, CalendarWidget
from kivymd.uix.label import MDLabel

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from KivyCalendar import CalendarWidget
from kivy.core.window import Window


Window.clearcolor = (0.5, 0.5, 0.5, 1)

class Calendar(BoxLayout):
    def __init__(self):
        super(Calendar, self).__init__()

    def show_calendar(self):
        datePicker = DatePicker()
        datePicker.show_popup(1,.3)


class Test(App):
    def build(self):
        return Calendar()


if __name__ == '__main__':
    Test().run()