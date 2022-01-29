from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.app import App
import kivy.utils


class EventBanner(GridLayout):

    def __init__(self, **kwargs):
        self.rows = 1

        #super(WorkoutBanner, self).__init__(**kwargs)
        super().__init__()#**kwargs)
        with self.canvas.before:
            Color(rgba=(kivy.utils.get_color_from_hex("#696969"))[:3] + [.5])
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(pos=self.update_rect, size=self.update_rect)


        # Need left FloatLayout
        left = FloatLayout()
        left_image = Image(source="icons/events/" + kwargs['event_image'], size_hint=(1, 0.5),
                           pos_hint={"top": .75, "right": 1})
        left_label = Label(text=kwargs['event_name'], size_hint=(1, .2), pos_hint={"top": .225, "right": 1})

        left.add_widget(left_image)
        left.add_widget(left_label)
        self.add_widget(left)


    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
