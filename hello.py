from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout


class hello_world(App):
    def build(self):
        f = FloatLayout()
        s = Scatter()
        l = Label(
            text='Hello ZaDy',
            font_size=80
        )
        f.add_widget(s)
        s.add_widget(l)
        return f


if __name__ == "__main__":
    hello_world().run()
