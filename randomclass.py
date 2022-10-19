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
        # self.selected_guns = ['Assault_Rifles', 'Submachine_Guns', 'Shotguns', 'Light_Machine_Guns', 'Tactical_Rifle', 'Marksmen_Rifles', 'Sniper_Rifles', 'Melee_Primary', 'Rocket_Launchers', 'Pistols', 'Melee_Secondary']
        # self.primary_guns = ['Assault_Rifles', 'Submachine_Guns', 'Shotguns', 'Light_Machine_Guns', 'Tactical_Rifle', 'Marksmen_Rifles', 'Sniper_Rifles', 'Melee_Primary']
        # self.secondary_guns = ['Rocket_Launchers', 'Pistols', 'Melee_Secondary']

        self.selected_guns = ['Assault Rifle', 'Submachine Gun', 'Shotgun', 'Light Machine Gun', 'Tactical Rifle', 'Marksmen Rifle', 'Sniper Rifle', 'Melee Primary', 'Rocket Launcher', 'Pistol', 'Melee Secondary']
        self.primary_guns = ['Assault Rifle', 'Submachine Gun', 'Shotgun', 'Light Machine Gun', 'Tactical Rifle', 'Marksmen Rifle', 'Sniper Rifle', 'Melee Primary']
        self.secondary_guns = ['Rocket Launcher', 'Pistol', 'Melee Secondary']
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

        print("Gun 1:", gun_one, '\nGun 2:', gun_two)

        gun_one_name = Label(text="Primary:    " + gun_one, bold=True, font_size=30)
        gun_two_name = Label(text="Secondary:  " + gun_two, bold=True, font_size=30)

        if os.path.isfile('assets/gun_photos/' + gun_one + '.png'):
            gun_one_image = Image(source=resource_path('assets/gun_photos/' + gun_one + '.png'))
        else:
            gun_one_image = Image(source=resource_path('assets/gun_photos/' + 'None.png'))

        if os.path.isfile('assets/gun_photos/' + gun_two + '.png'):
            gun_two_image = Image(source=resource_path('assets/gun_photos/' + gun_two + '.png'))
        else:
            gun_two_image = Image(source=resource_path('assets/gun_photos/' + 'None.png'))

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

        if config['Assault Rifle']:
            self.assault_rifles.state = 'down'
        else:
            self.assault_rifles.state = 'normal'

        if config['Submachine Gun']:
            self.smgs.state = 'down'
        else:
            self.smgs.state = 'normal'

        if config['Light Machine Gun']:
            self.lmgs.state = 'down'
        else:
            self.lmgs.state = 'normal'

        if config['Shotgun']:
            self.shotguns.state = 'down'
        else:
            self.shotguns.state = 'normal'

        if config['Tactical Rifle']:
            self.tactical_rifles.state = 'down'
        else:
            self.tactical_rifles.state = 'normal'

        if config['Marksmen Rifle']:
            self.marksmen_rifles.state = 'down'
        else:
            self.marksmen_rifles.state = 'normal'

        if config['Sniper Rifle']:
            self.sniper_rifles.state = 'down'
        else:
            self.sniper_rifles.state = 'normal'

        if config['Melee Primary']:
            self.melee_primary.state = 'down'
        else:
            self.melee_primary.state = 'normal'

        if config['Melee Secondary']:
            self.melee_secondary.state = 'down'
        else:
            self.melee_secondary.state = 'normal'

        if config['Pistol']:
            self.pistols.state = 'down'
        else:
            self.pistols.state = 'normal'

        if config['Rocket Launcher']:
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
            if config_file['Assault Rifle'] is True:
                config_file['Assault Rifle'] = False
            else:
                config_file['Assault Rifle'] = True

        with open('config.yaml', 'w') as file2:
            yaml.dump(config_file, file2)

    @staticmethod
    def toggle_smgs():
        with open('config.yaml') as file:
            config_file = yaml.load(file, Loader=yaml.FullLoader)
            if config_file['Submachine Gun'] is True:
                config_file['Submachine Gun'] = False
            else:
                config_file['Submachine Gun'] = True

        with open('config.yaml', 'w') as file2:
            yaml.dump(config_file, file2)

    @staticmethod
    def toggle_lmgs():
        with open('config.yaml') as file:
            config_file = yaml.load(file, Loader=yaml.FullLoader)
            if config_file['Light_Machine Gun'] is True:
                config_file['Light_Machine Gun'] = False
            else:
                config_file['Light Machine_Gun'] = True

        with open('config.yaml', 'w') as file2:
            yaml.dump(config_file, file2)

    @staticmethod
    def toggle_shotguns():
        with open('config.yaml') as file:
            config_file = yaml.load(file, Loader=yaml.FullLoader)
            if config_file['Shotgun'] is True:
                config_file['Shotgun'] = False
            else:
                config_file['Shotgun'] = True

        with open('config.yaml', 'w') as file2:
            yaml.dump(config_file, file2)

    @staticmethod
    def toggle_tactical_rifles():
        with open('config.yaml') as file:
            config_file = yaml.load(file, Loader=yaml.FullLoader)
            if config_file['Tactical Rifle'] is True:
                config_file['Tactical Rifle'] = False
            else:
                config_file['Tactical Rifle'] = True

        with open('config.yaml', 'w') as file2:
            yaml.dump(config_file, file2)

    @staticmethod
    def toggle_marksmen_rifles():
        with open('config.yaml') as file:
            config_file = yaml.load(file, Loader=yaml.FullLoader)
            if config_file['Marksmen Rifle'] is True:
                config_file['Marksmen Rifle'] = False
            else:
                config_file['Marksmen Rifle'] = True

        with open('config.yaml', 'w') as file2:
            yaml.dump(config_file, file2)

    @staticmethod
    def toggle_sniper_rifles():
        with open('config.yaml') as file:
            config_file = yaml.load(file, Loader=yaml.FullLoader)
            if config_file['Sniper Rifle'] is True:
                config_file['Sniper Rifle'] = False
            else:
                config_file['Sniper Rifle'] = True

        with open('config.yaml', 'w') as file2:
            yaml.dump(config_file, file2)

    @staticmethod
    def toggle_melee_primary():
        with open('config.yaml') as file:
            config_file = yaml.load(file, Loader=yaml.FullLoader)
            if config_file['Melee Primary'] is True:
                config_file['Melee Primary'] = False
            else:
                config_file['Melee Primary'] = True

        with open('config.yaml', 'w') as file2:
            yaml.dump(config_file, file2)

    @staticmethod
    def toggle_melee_secondary():
        with open('config.yaml') as file:
            config_file = yaml.load(file, Loader=yaml.FullLoader)
            if config_file['Melee Secondary'] is True:
                config_file['Melee Secondary'] = False
            else:
                config_file['Melee Secondary'] = True

        with open('config.yaml', 'w') as file2:
            yaml.dump(config_file, file2)

    @staticmethod
    def toggle_pistols():
        with open('config.yaml') as file:
            config_file = yaml.load(file, Loader=yaml.FullLoader)
            if config_file['Pistol'] is True:
                config_file['Pistol'] = False
            else:
                config_file['Pistol'] = True

        with open('config.yaml', 'w') as file2:
            yaml.dump(config_file, file2)

    @staticmethod
    def toggle_rocket_launchers():
        with open('config.yaml') as file:
            config_file = yaml.load(file, Loader=yaml.FullLoader)
            if config_file['Rocket Launcher'] is True:
                config_file['Rocket Launcher'] = False
            else:
                config_file['Rocket Launcher'] = True

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
# GuiManager:
#     HomeGui:
#     SettingsGui:
#
# # ==========================================================================================
# #       Home Gui:
# # ==========================================================================================
# <HomeGui>:
#     name: "home"
#     home_text_grid_layout: homeTextGridLayout
#     home_image_grid_layout: homeImageGridLayout
#     canvas:
#         Rectangle:
#             pos: self.pos
#             size: self.size
#             source: "assets/background.jpg"
#
#
#     Button:
#         size_hint: .1, .1
#         pos_hint: {"x": .9, "y": .9}
#         text: "Settings"
#         on_release:
#             app.root.current = "settings"
#             app.root.transition.direction = "left"
#
#     Button:
#         size_hint: .25, .1
#         pos_hint: {"x": .375}
#         text: "Generate"
#         on_release:
#             root.generate_class()
#
#     GridLayout:
#         id: homeTextGridLayout
#         cols: 1
#         spacing: [0, 0.1 * root.height]
#         size_hint: .5, .5
#         pos_hint: {'x': .05, 'y':.2}
#
#     GridLayout:
#         id: homeImageGridLayout
#         cols: 1
#         size_hint: .5, .5
#         pos_hint: {'x': .45, 'y':.2}
#
#
# # ==========================================================================================
# #       Setting Gui:
# # ==========================================================================================
# <SettingsGui>:
#     name: "settings"
#     use_overkill: UseOverkill
#     assault_rifles: AssaultRifles
#     smgs: SMGs
#     lmgs: LMGs
#     shotguns: Shotguns
#     tactical_rifles: TacticalRifles
#     marksmen_rifles: MarksmenRifles
#     sniper_rifles: SniperRifles
#     melee_primary: MeleePrimary
#     melee_secondary: MeleeSecondary
#     pistols: Pistols
#     rocket_launchers: RocketLaunchers
#     canvas:
#         Rectangle:
#             pos: self.pos
#             size: self.size
#             source: "assets/settingsbackground.jpg"
#
#     Button:
#         size_hint: .1, .1
#         pos_hint: {"x": .9, "y": .9}
#         text: "Home"
#         on_release:
#             app.root.current = "home"
#             app.root.transition.direction = "right"
#
#     Label:
#         text: "Default: All guns are selected and overkill is disabled"
#         pos_hint: {"x": -.25, "y": .45}
#
#     ToggleButton:
#         text: "Use Overkill"
#         pos_hint: {"x": .10, "y": .7}
#         size_hint: .3, .1
#         id: UseOverkill
#         state: 'down'
#         on_press:
#             root.toggle_overkill()
#     ToggleButton:
#         text: "Assault Rifles"
#         pos_hint: {"x": .10, "y": .6}
#         size_hint: .3, .1
#         id: AssaultRifles
#         on_press:
#             root.toggle_assault_rifles()
#     ToggleButton:
#         text: "SMGs"
#         pos_hint: {"x": .10, "y": .5}
#         size_hint: .3, .1
#         id: SMGs
#         on_press:
#             root.toggle_smgs()
#     ToggleButton:
#         text: "LMGs"
#         pos_hint: {"x": .10, "y": .4}
#         size_hint: .3, .1
#         id: LMGs
#         on_press:
#             root.toggle_lmgs()
#     ToggleButton:
#         text: "Shotguns"
#         pos_hint: {"x": .10, "y": .3}
#         size_hint: .3, .1
#         id: Shotguns
#         on_press:
#             root.toggle_shotguns()
#     ToggleButton:
#         text: "Tactical Rifles"
#         pos_hint: {"x": .10, "y": .2}
#         size_hint: .3, .1
#         id: TacticalRifles
#         on_press:
#             root.toggle_tactical_rifles()
#     ToggleButton:
#         text: "Marksmen Rifles"
#         pos_hint: {"x": .60, "y": .7}
#         size_hint: .3, .1
#         id: MarksmenRifles
#         on_press:
#             root.toggle_marksmen_rifles()
#     ToggleButton:
#         text: "Sniper Rifles"
#         pos_hint: {"x": .60, "y": .6}
#         size_hint: .3, .1
#         id: SniperRifles
#         on_press:
#             root.toggle_sniper_rifles()
#     ToggleButton:
#         text: "Melee Primary"
#         pos_hint: {"x": .60, "y": .5}
#         size_hint: .3, .1
#         id: MeleePrimary
#         on_press:
#             root.toggle_melee_primary()
#     ToggleButton:
#         text: "Melee Secondary"
#         pos_hint: {"x": .60, "y": .4}
#         size_hint: .3, .1
#         id: MeleeSecondary
#         on_press:
#             root.toggle_melee_secondary()
#     ToggleButton:
#         text: "Pistols"
#         pos_hint: {"x": .60, "y": .3}
#         size_hint: .3, .1
#         id: Pistols
#         on_press:
#             root.toggle_pistols()
#     ToggleButton:
#         text: "Rocket Launchers"
#         pos_hint: {"x": .60, "y": .2}
#         size_hint: .3, .1
#         id: RocketLaunchers
#         on_press:
#             root.toggle_rocket_launchers()
#
#     '''
# )
kv = Builder.load_file("randomclass.kv")


class RandomClassApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    RandomClassApp().run()
