from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty, ColorProperty
from kivy.vector import Vector
from kivy.config import Config

from typing import List
import numpy as np

Config.set('graphics', 'width', '850')


color_map = np.zeros(shape=(4, 40, 3), dtype=float)


class GridElement(Widget):
    row = NumericProperty(0)
    col = NumericProperty(0)
    color = ColorProperty('#000000')

    def update_color(self):
        self.color = tuple(color_map[self.row, self.col])


class GridArray(GridLayout):
    def __init__(self, **kwargs):
        super(GridArray, self).__init__(**kwargs)
        self.elements = self.add_elements()

    def add_elements(self) -> List[GridElement]:
        rv = []
        for col in range(40):
            for row in range(4):
                element = GridElement(row=row, col=col)
                self.add_widget(element)
                rv.append(element)
        return rv

    def update_elements(self):
        for element in self.elements:
            element.update_color()


class GridController(Widget):
    pass


class GridApp(App):
    def build(self):
        return GridController()


if __name__ == '__main__':
    GridApp().run()
