import kivy
kivy.require('2.0.0') # replace with your current kivy version !



from kivy.app import App
from kivy.uix.button import Button

class MyfirstApp(App):

     def build(self):
      return Button(text='GO', pos=(80,80),size=(500,600),size_hint=(0.8,0.8))

#size_hint=(None,None))
if __name__ == '__main__':
    MyfirstApp().run()