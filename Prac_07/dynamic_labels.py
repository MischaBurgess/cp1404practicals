
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    label_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["John", "Sean", "Sam", "Max", "Tyler"] # test names to create labels

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=name, id=name)
            self.root.ids.label_box.add_widget(temp_label)


DynamicLabelsApp().run()
