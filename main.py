import kivy
from kivy.app import App
from kivy.uix.label import Label
from API_handler import ProductHandler
from EAN_reader import EANReader

api_handler = ProductHandler()
ean_handler = EANReader()

class MyApp(App):
    def build(self):
        print(ean_handler.ean_codes)
        return Label(text=f"{api_handler.get_response(ean_handler.ean_codes[0])}")


if __name__ == '__main__':
    MyApp().run()
