"""Convert Miles to Kilometres using Kivy GUI
Mischa Burgess
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty


MILES_TO_KM_UNIT = 1.60934


class MilesToKilometres(App):
    print_km = StringProperty()

    def build(self):
        Window.size = (500, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def calculate(self, text):
        miles = self.convert_input(text)
        self.update_result(miles)

    def increment(self, text, change):
        miles = self.convert_input(text) + change
        self.root.ids.input_number.text = str(miles)

    def update_result(self, miles):
        self.print_km = str(miles * MILES_TO_KM_UNIT)

    @staticmethod
    def convert_input(text):
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesToKilometres().run()
