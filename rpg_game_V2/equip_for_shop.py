import equip
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset = True)

#all equip arr
armor_arr = []
weapon_arr = []
bots_arr = []
amulet_arr = []

#create common equip
class CommonArmor(equip.Armor):
	name = Fore.LIGHTWHITE_EX + "Common Armor"
	defense = 3
	hp = 20
	price = 15
	
class CommonWeapon(equip.Weapon):
	name = Fore.LIGHTWHITE_EX + "Common Weapon"
	damage = 6
	price = 15
	
class CommonBots(equip.Bots):
	name = Fore.LIGHTWHITE_EX + "Common Bots"
	dodge = 4
	price = 15
	
class CommonAmulet(equip.Amulet):
	name = Fore.LIGHTWHITE_EX + "Common Amulet"
	hp_recovery = 10
	price = 15
	
#add equip
armor_arr.append(CommonArmor)
weapon_arr.append(CommonWeapon)
bots_arr.append(CommonBots)
amulet_arr.append(CommonAmulet)


#create uncommon equip
class UncommonArmor(equip.Armor):
	name = Fore.LIGHTGREEN_EX + "Uncommon Armor"
	defense = 8
	hp = 35
	price = 30
	
class UncommonWeapon(equip.Weapon):
	name = Fore.LIGHTGREEN_EX + "Uncommon Weapon"
	damage = 10
	price = 30
	
class UncommonBots(equip.Bots):
	name = Fore.LIGHTGREEN_EX + "Uncommon Bots"
	dodge = 7
	price = 30
	
class UncommonAmulet(equip.Amulet):
	name = Fore.LIGHTGREEN_EX + "Uncommon Amulet"
	hp_recovery = 25
	price = 35
	
#add equip
armor_arr.append(UncommonArmor)
weapon_arr.append(UncommonWeapon)
bots_arr.append(UncommonBots)
amulet_arr.append(UncommonAmulet)


#create Epic equip
class EpicArmor(equip.Armor):
	name = Fore.LIGHTMAGENTA_EX + "Epic Armor"
	defense = 12
	hp = 50
	price = 55
	
class EpicWeapon(equip.Weapon):
	name = Fore.LIGHTMAGENTA_EX + "Epic Weapon"
	damage = 16
	price = 55
	
class EpicBots(equip.Bots):
	name = Fore.LIGHTMAGENTA_EX + "Epic Bots"
	dodge = 13
	price = 55
	
class EpicAmulet(equip.Amulet):
	name = Fore.LIGHTMAGENTA_EX + "Epic Amulet"
	hp_recovery = 50
	price = 55
	
#add equip
armor_arr.append(EpicArmor)
weapon_arr.append(EpicWeapon)
bots_arr.append(EpicBots)
amulet_arr.append(EpicAmulet)


#create Legendary equip
class LegendaryArmor(equip.Armor):
	name = Fore.LIGHTYELLOW_EX + "Legendary Armor"
	defense = 20
	hp = 100
	price = 80
	
class LegendaryWeapon(equip.Weapon):
	name = Fore.LIGHTYELLOW_EX + "Legendary Weapon"
	damage = 25
	price = 80
	
class LegendaryBots(equip.Bots):
	name = Fore.LIGHTYELLOW_EX + "Legendary Bots"
	dodge = 21
	price = 80
	
class LegendaryAmulet(equip.Amulet):
	name = Fore.LIGHTYELLOW_EX + "Legendary Amulet"
	hp_recovery = 90
	price = 80
	
#add equip
armor_arr.append(LegendaryArmor)
weapon_arr.append(LegendaryWeapon)
bots_arr.append(LegendaryBots)
amulet_arr.append(LegendaryAmulet)

#create arkan equip
class ArkanArmor(equip.Armor):
	name = Fore.LIGHTRED_EX + "Arkan Armor"
	defense = 35
	hp = 200
	price = 140
	
class ArkanWeapon(equip.Weapon):
	name = Fore.LIGHTRED_EX + "Arkan Weapon"
	damage = 40
	price = 140
	
class ArkanBots(equip.Bots):
	name = Fore.LIGHTRED_EX + "Arkan Bots"
	dodge = 30
	price = 140
	
class ArkanAmulet(equip.Amulet):
	name = Fore.LIGHTRED_EX + "Arkan Amulet"
	hp_recovery = 130
	price = 140
	
#add equip
armor_arr.append(ArkanArmor)
weapon_arr.append(ArkanWeapon)
bots_arr.append(ArkanBots)
amulet_arr.append(ArkanAmulet)
