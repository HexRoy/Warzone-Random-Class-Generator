import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image
from kivy.uix.label import Label

import pandas as pd
from random import choice


import sys
import os


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# ==========================================================================================
#       Home GUI:
# ==========================================================================================
class HomeGui(Screen):

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

    def generate_class(self):
        self.home_image_grid_layout.clear_widgets()
        self.home_text_grid_layout.clear_widgets()

        selected_guns = ['Assault_Rifles', 'Submachine_Guns', 'Shotguns', 'Light_Machine_Guns', 'Tactical_Rifle', 'Marksmen_Rifles', 'Sniper_Rifles', 'Melee_Primary', 'Rocket_Launchers', 'Pistols', 'Melee_Secondary']

        primary_guns = ['Assault_Rifles', 'Submachine_Guns', 'Shotguns', 'Light_Machine_Guns', 'Tactical_Rifle', 'Marksmen_Rifles', 'Sniper_Rifles', 'Melee_Primary']
        secondary_guns = ['Rocket_Launchers', 'Pistols', 'Melee_Secondary']

        df = pd.read_csv(resource_path('assets/warzone_gun_names.csv'))

        primary_gun_list = []
        secondary_gun_list = []

        for column in df:
            if column in selected_guns:
                if column in primary_guns:
                    for gun in df[column].dropna().values:
                        primary_gun_list.append(gun)
                else:
                    for gun in df[column].dropna().values:
                        secondary_gun_list.append(gun)

        overkill = True

        if overkill is False:
            gun_one = choice(primary_gun_list)
            gun_two = choice(secondary_gun_list)
        else:
            gun_one = choice(primary_gun_list)
            gun_two = choice(primary_gun_list)

        gun_one_name = Label(text="Primary:    " + gun_one)
        gun_two_name = Label(text="Secondary:  " + gun_two)
        gun_one_image = Image(source=resource_path('assets/gun_photos/' + gun_one + '.png'))
        gun_two_image = Image(source=resource_path('assets/gun_photos/' + gun_two + '.png'))

        self.home_text_grid_layout.add_widget(gun_one_name)
        self.home_image_grid_layout.add_widget(gun_one_image)
        self.home_text_grid_layout.add_widget(gun_two_name)
        self.home_image_grid_layout.add_widget(gun_two_image)



# ==========================================================================================
#       Settings GUI:
# ==========================================================================================
class SettingsGui(Screen):

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)


# ==========================================================================================
#       Gui Manager:
# ==========================================================================================
class GuiManager(ScreenManager):
    pass

# ==========================================================================================
# Driver Code
# ==========================================================================================
kv = Builder.load_string(
    '''
    
GuiManager:
    HomeGui:
    SettingsGui:

# ==========================================================================================
#       Home Gui:
# ==========================================================================================
<HomeGui>:
    name: "home"
    home_text_grid_layout: homeTextGridLayout
    home_image_grid_layout: homeImageGridLayout
    Button:
        size_hint: .1, .1
        pos_hint: {"x": .9, "y": .9}
        text: "Settings"

    Button:
        size_hint: .25, .1
        pos_hint: {"x": .375}
        text: "Generate"
        on_release:
            root.generate_class()

    GridLayout:
        id: homeTextGridLayout
        cols: 1
        spacing: [0, 0.1 * root.height]
        size_hint: .5, .5
        pos_hint: {'x': .05, 'y':.2}

    GridLayout:
        id: homeImageGridLayout
        cols: 1
        size_hint: .5, .5
        pos_hint: {'x': .45, 'y':.2}


# ==========================================================================================
#       Setting Gui:
# ==========================================================================================
<SettingsGui>:
    name: "settings"
    '''

)


class RandomClassApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    RandomClassApp().run()
