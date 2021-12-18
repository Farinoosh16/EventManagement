import kivy.utils
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
import kivy.utils




class EventBanner(GridLayout):
    rows = 1
    def __init__(self, **kwargs):
        super(EventBanner,self).__init__(**kwargs)
        with self.canvas.before:
            Color(rgt = (kivy.utils.get_color_from_hex("#67697C")))
            self.rect = Rectangle(size = self.size, pos = self.pos)
            self.bind(pos= self.update_rect, size= self.update_rect)

        #Need left Floatlayout
        left = FloatLayout()
        left_image = Image( source = "icons/" + kwargs['event_image'] , size_hint = (1,0.8) , pos_hint ={"top": 1, "left": 1})
        left_label = Label(text = kwargs['description'], size_hint = (1,0.2) , pos_hint ={"top": .2, "left": 1})
        left.add_widget(left_image)
        left.add_widget(left_label)

        self.add_widget(left)
    def update_rect(self,*args):
        self.rect.pos = self.pos
        self.rect.size = self.size
