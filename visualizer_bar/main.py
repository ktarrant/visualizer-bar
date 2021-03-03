from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector

import numpy as np


class GridArray(Widget):
    pass


class GridElement(Widget):
    pass


class GridApp(App):
    def build(self):
        return GridArray()


if __name__ == '__main__':
    GridApp().run()
