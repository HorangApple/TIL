from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''
ActionBar:
    pos_hint:{'top':1}

    ActionView:
        ActionPrevious: # 이전 버튼
            title:'Action Bar'
            with_previous:False # 이전 버튼 사용 안함
        
        ActionButton:
            text:'Bt1'
            icon:'atlas://data/images/defaulttheme/audio-volume-high'
        ActionButton:
            text:'Bt2'
        ActionButton:
            text:'Bt3'
        ActionButton:
            text:'Bt4'
        ActionGroup:
            text:'Group'
            color:.3,.9,0,1
            font_size:20
            ActionButton:
                text:'Bt1'
            ActionButton:
                text:'Bt2'
            ActionButton:
                text:'Bt3'
'''))