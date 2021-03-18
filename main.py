from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from modules.persons import Persons


class BMIScreen(Screen):
    pass


class FormScreen(Screen):
    pass


class TableScreen(Screen):
    pass


class MainScreen(Screen):
    pass


class Test(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Gray"
        builder = Builder.load_file('bmi.kv')

        persons = Persons()
        builder.ids.navigation.ids.tab_manager.screens[2].add_widget(persons)

        return builder


Test().run()
