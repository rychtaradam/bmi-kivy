import json
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import MDList, TwoLineAvatarListItem, ImageLeftWidget

person_list = [
    {"name": "Alexandra Švajdová", "state": "CZE", "img": "images/female.png"},
    {"name": "Adam Rychtář", "state": "CZE", "img": "images/male.png"},
    {"name": "Donald Trump", "state": "USA", "img": "images/male.png"}
]


class MyItem(TwoLineAvatarListItem):

    def __init__(self, name, state, img, *args, **kwargs):
        super(MyItem, self).__init__(*args)
        self.text = name
        self.secondary_text = state
        self.image = ImageLeftWidget(source=img)
        self.add_widget(self.image)

    def on_press(self):
        print(self.text)


class Persons(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(Persons, self).__init__(orientation="horizontal")
        scroll_view = ScrollView()
        list_osob = MDList()

        for person in person_list:
            list_osob.add_widget(MyItem(name=person['name'], state=person['state'], img=person['img']))

        scroll_view.add_widget(list_osob)
        self.add_widget(scroll_view)
