from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.config import Config

import numpy as np

Config.set('graphics', 'width', '850')


class GridElement(Widget):
    pass


class GridArray(GridLayout):
    def __init__(self, **kwargs):
        super(GridArray, self).__init__(**kwargs)
        self.add_elements()

    def add_elements(self):
        for i in range(160):
            element = GridElement()
            self.add_widget(element)


class GridController(Widget):
    pass


class GridApp(App):
    def build(self):
        return GridController()


if __name__ == '__main__':
    GridApp().run()
