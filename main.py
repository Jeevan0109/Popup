from turtle import width
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
# from kivy.uix.carousel import Carousel
# from kivy.uix.checkbox import CheckBox


Builder.load_file('main.kv')


class MyLayout(Widget):
    pass


class AwesomeApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    AwesomeApp().run()
