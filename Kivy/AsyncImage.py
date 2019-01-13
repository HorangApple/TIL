from kivy.app import App
from kivy.lang import Builder

kv = """
AnchorLayout:
    canvas:
        Color:
            rgba:1,3,1,1
        Rectangle:
            pos:self.pos
            size:self.size
    AsyncImage:
        size_hint:None,None
        size:dp(560),dp(560)
        source:'https://raw.githubusercontent.com/kivy/kivy/master/kivy/data/logo/kivy-icon-256.png'
        anim_delay:0.03
"""

class TestApp(App):
    def build(self):
        return Builder.load_string(kv)
    
if __name__=='__main__':
    TestApp().run()