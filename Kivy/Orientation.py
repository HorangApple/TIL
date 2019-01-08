from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

Builder.load_string('''

<BoxLayout>
    orientation : 'horizontal'
    Button:
        text:'B1'
    Button:
        text:'B1'
    Button:
        text:'B1'
''')

class MyList(BoxLayout):
    pass

if __name__ =='__main__' :
    runTouchApp(MyList())