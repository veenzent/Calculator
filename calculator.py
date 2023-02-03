import re
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ListProperty
from kivy.core.window import Window

Window.size = (360, 640)

class AllowedInputs(TextInput):

    def insert_text(self, substring, from_undo=False):
        return super().insert_text(substring, from_undo)

class Calc(BoxLayout):
    canvas_color = ListProperty(None)
    button_color = ListProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.canvas_color = [0, 0, 0, 1]
        self.button_color = [255, 250, 250, .5]
        self.operators = ['/', '*', '-', '+']
        self.inputs = []
        self.expression = []

    def colorSwitch(self, switch):
        if switch.active:
            self.canvas_color = [255, 250, 250, 1]    # snow_white
            self.button_color = [0, 0, 0, 1]    # black
            self.ids.c_btn = self.button_color
            self.ids.bck_btn = self.button_color
            self.ids.percent_btn = self.button_color
            self.ids.dec_btn = self.button_color
            self.ids.lcd2.color = self.button_color
        elif not switch.active:
            self.canvas_color = [0, 0, 0, 1]    # black
            self.button_color = [255, 250, 250, .5]    # snow_white
            self.ids.c_btn = self.button_color
            self.ids.bck_btn = self.button_color
            self.ids.percent_btn = self.button_color
            self.ids.dec_btn = self.button_color
            self.ids.lcd2.color = [1, 1, 1, .5]

    def clear_screen(self):
        self.inputs.clear()
        self.expression.clear()
        self.ids.lcd1.text = ""
        self.ids.lcd2.text = ""

    def backspace(self):
        if self.expression:
            self.inputs, self.expression = self.expression, self.inputs
            self.ids.lcd1.text = ''.join(self.inputs)
            self.ids.lcd2.text = str(eval(''.join(self.inputs)))
        else:
            # ignore press if there are no inputs
            if not self.inputs:
                pass
            else:
                self.inputs.pop()
                self.ids.lcd1.text = ''.join(self.inputs)
                # backspace on a single digit scenario
                if not self.inputs:
                    pass
                # avoid error from 'expressions ending with an operator' while evaluating
                elif self.inputs[-1] in self.operators:
                    self.ids.lcd2.text = str(eval(''.join(self.inputs[:-1])))
                # clear lcd2 if there's no operator in self.inputs(lcd1)
                else:
                    if '+' in self.inputs or '-' in self.inputs or '*' in self.inputs or '/' in self.inputs:
                        self.ids.lcd2.text = str(eval(''.join(self.inputs)))
                    else:
                        self.ids.lcd2.text = ''

    def pressed_number(self, number):
        self.inputs.append(number.text)
        self.ids.lcd1.text = ''.join(self.inputs)
        for i in self.operators:
            if i in self.inputs:
                self.ids.lcd2.text = str(eval(''.join(self.inputs)))
                break
            else:
                self.ids.lcd2.text = ""

    def add_operator(self, operator):
        if self.inputs[-1] in self.operators:
            self.inputs.pop()
            self.inputs.append(operator.text)
        else:
            self.inputs.append(operator.text)
        self.ids.lcd1.text = ''.join(self.inputs)

    def equal_to(self):
        if not self.ids.lcd2.text:
            pass
        else:
            self.expression, self.inputs = self.inputs, self.expression
            self.ids.lcd1.text = str(eval(''.join(self.expression)))
            self.ids.lcd2.text = ""

class CalculatorApp(MDApp):
    def build(self):
        return super().build()

CalculatorApp().run()
