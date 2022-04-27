from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class Widgets(Widget):
    def btn(self):
        popup_window()


class P(FloatLayout):
    pass


def popup_window():
    show = P()
    popupWindow = Popup(title='My Popup', content=show, size_hint=(None, None), size=(400, 400))
    popupWindow.open()


class MyApp(App):
    def build(self):
        return Widgets()


if __name__ == '__main__':
    MyApp().run()