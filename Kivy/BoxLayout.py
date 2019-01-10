from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''

BoxLayout:
	orientation:'vertical'
	spacing: 10
	padding: 100
	Button:
		text:'F1'
	Button:
		text:'F2'


'''))