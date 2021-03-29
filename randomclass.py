import pandas as pd
from random import choice

selected_guns = ['Assault_Rifles', 'Submachine_Guns', 'Shotguns', 'Light_Machine_Guns', 'Tactical_Rifle', 'Marksmen_Rifles', 'Sniper_Rifles', 'Melee_Primary', 'Rocket_Launchers', 'Pistols', 'Melee_Secondary']

primary_guns = ['Assault_Rifles', 'Submachine_Guns', 'Shotguns', 'Light_Machine_Guns', 'Tactical_Rifle', 'Marksmen_Rifles', 'Sniper_Rifles', 'Melee_Primary']
secondary_guns = ['Rocket_Launchers', 'Pistols', 'Melee_Secondary']

df = pd.read_csv('warzone_gun_names.csv')

guns = {}
for column in df:
    if column in selected_guns:
        guns[column] = df[column].dropna().values


primary_gun_list = []
secondary_gun_list = []

for gun_type in guns:
    if gun_type in primary_guns:
        for gun in guns[gun_type]:
            primary_gun_list.append(gun)
    else:
        for gun in guns[gun_type]:
            secondary_gun_list.append(gun)

overkill = True

if overkill == False:
    gun_one = choice(primary_gun_list)
    gun_two = choice(secondary_gun_list)
else:
    gun_one = choice(primary_gun_list)
    gun_two = choice(primary_gun_list)

print("Primary:", gun_one, "\nSecondary:", gun_two)



