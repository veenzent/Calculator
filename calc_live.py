from kaki.app import App
from kivy.factory import Factory
from kivy.core.window import Window
import os

Window.size = (360, 640)


class CalculatorLive(App):
    CLASSES = {
        #"class name": "Location"
        "CalculatorAPP": "calculator"
    }

    KV_FILES = [os.path.join(os.getcwd(), "calculator.kv")]

    AUTORELOADER_PATHS = [
        (os.getcwd(), {"recursive": True})
    ]

    def build_app(self, first=False):
        print("Calc Auto Reloaded")
        return Factory.CalculatorApp()


CalculatorLive().run()
