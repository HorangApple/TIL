from kivy.uix.accordion import Accordion, AccordionItem
from kivy.app import App
from kivy.uix.label import Label

class AccordionApp(App):
    def build(self):
        root = Accordion()
        for x in range(5):
            item = AccordionItem(title='Title %d' %x, min_space=35) # min_space의 default는 40
            item.add_widget(Label(text='Hello World\n'*5))
            root.add_widget(item)
        return root


if __name__ == '__main__':
    AccordionApp().run()