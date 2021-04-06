import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy_deps import sdl2, glew

import yaml
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
        self.selected_guns = ['Assault_Rifles', 'Submachine_Guns', 'Shotguns', 'Light_Machine_Guns', 'Tactical_Rifle', 'Marksmen_Rifles', 'Sniper_Rifles', 'Melee_Primary', 'Rocket_Launchers', 'Pistols', 'Melee_Secondary']
        self.primary_guns = ['Assault_Rifles', 'Submachine_Guns', 'Shotguns', 'Light_Machine_Guns', 'Tactical_Rifle', 'Marksmen_Rifles', 'Sniper_Rifles', 'Melee_Primary']
        self.secondary_guns = ['Rocket_Launchers', 'Pistols', 'Melee_Secondary']
        self.use_overkill = False

    def on_enter(self, *args):
        """
        on_enter: Determines what happens when entering the Home Screen
        :param args:
        :return:
        """

        # Loads config for selected guns
        with open('config.yaml') as file:
            config_file = yaml.load(file, Loader=yaml.FullLoader)
        temp_gun_list = []
        for entry in config_file:
            if (entry in self.primary_guns) or (entry in self.secondary_guns):
                if config_file[entry]:
                    temp_gun_list.append(entry)
        self.selected_guns = temp_gun_list

        # Loads config for using overkill
        self.use_overkill = config_file['Use_Overkill']

    def generate_class(self):
        """
        generate_class: Generates a random primary and secondary weapon and adds them to the screen
        :return:
        """
        self.home_image_grid_layout.clear_widgets()
        self.home_text_grid_layout.clear_widgets()

        df = pd.read_csv(resource_path('assets/warzone_gun_names.csv'))

        primary_gun_list = []
        secondary_gun_list = []

        for column in df:
            if column in self.selected_guns:
                if column in self.primary_guns:
                    for gun in df[column].dropna().values:
                        primary_gun_list.append(gun)
                elif column in self.secondary_guns:
                    for gun in df[column].dropna().values:
                        secondary_gun_list.append(gun)
                else:
                    print("ERROR: Gun type not found")

        if self.use_overkill is False:
            gun_one = choice(primary_gun_list)
            gun_two = choice(secondary_gun_list)
        else:
            gun_one = choice(primary_gun_list)
            gun_two = choice(primary_gun_list)

        gun_one_name = Label(text="Primary:    " + gun_one, bold=True, font_size=30)
        gun_two_name = Label(text="Secondary:  " + gun_two, bold=True, font_size=30)
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

    def on_enter(self, *args):
        """
        on_enter: Determines what happens when entering the Settings Screen
        :param args:
        :return:
        """
        with open('config.yaml') as file:
            config_file = yaml.load(file, Loader=yaml.FullLoader)
        self.set_buttons(config_file)

    def set_buttons(self, config):
        if config['Use_Overkill']:
            self.use_overkill.state = 'down'
        else:
            self.use_overkill.state = 'normal'

        if config['Assault_Rifles']:
            self.assault_rifles.state = 'down'
        else:
            self.assault_rifles.state = 'normal'

        if config['Submachine_Guns']:
            self.smgs.state = 'down'
        else:
            self.smgs.state = 'normal'

        if config['Light_Machine_Guns']:
            self.lmgs.state = 'down'
        else:
            self.lmgs.state = 'normal'

        if config['Shotguns']:
            self.shotguns.state = 'down'
        else:
            self.shotguns.state = 'normal'

        if config['Tactical_Rifle']:
            self.tactical_rifles.state = 'down'
        else:
            self.tactical_rifles.state = 'normal'

        if config['Marksmen_Rifles']:
            self.marksmen_rifles.state = 'down'
        else:
            self.marksmen_rifles.state = 'normal'

        if config['Sniper_Rifles']:
            self.sniper_rifles.state = 'down'
        else:
            self.sniper_rifles.state = 'normal'

        if config['Melee_Primary']:
            self.melee_primary.state = 'down'
        else:
            self.melee_primary.state = 'normal'

        if config['Melee_Secondary']:
            self.melee_secondary.state = 'down'
        else:
            self.melee_secondary.state = 'normal'

        if config['Pistols']:
            self.pistols.state = 'down'
        else:
            self.pistols.state = 'normal'

        if config['Rocket_Launchers']:
            self.rocket_launchers.state = 'down'
        else:
            self.rocket_launchers.state = 'normal'

    @staticmethod
    def toggle_overkill():
        with open('config.yaml') as file:
            config_file = yaml.load(file, Loader=yaml.FullLoader)
            if config_file['Use_Overkill'] is True:
                config_file['Use_Overkill'] = False
            else:
                config_file['Use_Overkill'] = True

        with open('config.yaml', 'w') as file2:
            yaml.dump(config_file, file2)

    @staticmethod
    def toggle_assault_rifles():
        with open('config.yaml') as file:
            config_file = yaml.load(file, Loader=yaml.FullLoader)
            if config_file['Assault_Rifles'] is True:
                config_file['Assault_Rifles'] = False
            else:
                config_file['Assault_Rifles'] = True

        with open('config.yaml', 'w') as file2:
            yaml.dump(config_file, file2)

    @staticmethod
    def toggle_smgs():
        with open('config.yaml') as file:
            config_file = yaml.load(file, Loader=yaml.FullLoader)
            if config_file['Submachine_Guns'] is True:
                config_file['Submachine_Guns'] = False
            else:
                config_file['Submachine_Guns'] = True

        with open('config.yaml', 'w') as file2:
            yaml.dump(config_file, file2)

    @staticmethod
    def toggle_lmgs():
        with open('config.yaml') as file:
            config_file = yaml.load(file, Loader=yaml.FullLoader)
            if config_file['Light_Machine_Guns'] is True:
                config_file['Light_Machine_Guns'] = False
            else:
                config_file['Light_Machine_Guns'] = True

        with open('config.yaml', 'w') as file2:
            yaml.dump(config_file, file2)

    @staticmethod
    def toggle_shotguns():
        with open('config.yaml') as file:
            config_file = yaml.load(file, Loader=yaml.FullLoader)
            if config_file['Shotguns'] is True:
                config_file['Shotguns'] = False
            else:
                config_file['Shotguns'] = True

        with open('config.yaml', 'w') as file2:
            yaml.dump(config_file, file2)

    @staticmethod
    def toggle_tactical_rifles():
        with open('config.yaml') as file:
            config_file = yaml.load(file, Loader=yaml.FullLoader)
            if config_file['Tactical_Rifle'] is True:
                config_file['Tactical_Rifle'] = False
            else:
                config_file['Tactical_Rifle'] = True

        with open('config.yaml', 'w') as file2:
            yaml.dump(config_file, file2)

    @staticmethod
    def toggle_marksmen_rifles():
        with open('config.yaml') as file:
            config_file = yaml.load(file, Loader=yaml.FullLoader)
            if config_file['Marksmen_Rifles'] is True:
                config_file['Marksmen_Rifles'] = False
            else:
                config_file['Marksmen_Rifles'] = True

        with open('config.yaml', 'w') as file2:
            yaml.dump(config_file, file2)

    @staticmethod
    def toggle_sniper_rifles():
        with open('config.yaml') as file:
            config_file = yaml.load(file, Loader=yaml.FullLoader)
            if config_file['Sniper_Rifles'] is True:
                config_file['Sniper_Rifles'] = False
            else:
                config_file['Sniper_Rifles'] = True

        with open('config.yaml', 'w') as file2:
            yaml.dump(config_file, file2)

    @staticmethod
    def toggle_melee_primary():
        with open('config.yaml') as file:
            config_file = yaml.load(file, Loader=yaml.FullLoader)
            if config_file['Melee_Primary'] is True:
                config_file['Melee_Primary'] = False
            else:
                config_file['Melee_Primary'] = True

        with open('config.yaml', 'w') as file2:
            yaml.dump(config_file, file2)

    @staticmethod
    def toggle_melee_secondary():
        with open('config.yaml') as file:
            config_file = yaml.load(file, Loader=yaml.FullLoader)
            if config_file['Melee_Secondary'] is True:
                config_file['Melee_Secondary'] = False
            else:
                config_file['Melee_Secondary'] = True

        with open('config.yaml', 'w') as file2:
            yaml.dump(config_file, file2)

    @staticmethod
    def toggle_pistols():
        with open('config.yaml') as file:
            config_file = yaml.load(file, Loader=yaml.FullLoader)
            if config_file['Pistols'] is True:
                config_file['Pistols'] = False
            else:
                config_file['Pistols'] = True

        with open('config.yaml', 'w') as file2:
            yaml.dump(config_file, file2)

    @staticmethod
    def toggle_rocket_launchers():
        with open('config.yaml') as file:
            config_file = yaml.load(file, Loader=yaml.FullLoader)
            if config_file['Rocket_Launchers'] is True:
                config_file['Rocket_Launchers'] = False
            else:
                config_file['Rocket_Launchers'] = True

        with open('config.yaml', 'w') as file2:
            yaml.dump(config_file, file2)


# ==========================================================================================
#       Gui Manager:
# ==========================================================================================
class GuiManager(ScreenManager):
    pass


# ==========================================================================================
# Driver Code
# ==========================================================================================
# kv = Builder.load_string(
#     '''
#     '''
# )
kv = Builder.load_file("randomclass.kv")


class RandomClassApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    RandomClassApp().run()
