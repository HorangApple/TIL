from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''

BoxLayout:
    orientation:'vertical'
    padding:50

    ProgressBar:
        id:bar
        value:slider.value
        max:300
    Slider:
        id:slider
        max:300
        value:140
    Slider:
        orientation:'vertical'
        on_value:slider.value=self.value
        max:400

'''))