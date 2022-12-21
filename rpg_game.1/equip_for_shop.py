import equip

#all equip arr
armor_arr = []
weapon_arr = []
bots_arr = []
amulet_arr = []

#create common equip
class CommonArmor(equip.Armor):
	name = "Common Armor"
	defense = 3
	hp = 20
	price = 10
	
class CommonWeapon(equip.Weapon):
	name = "Common Weapon"
	damage = 4
	price = 10
	
class CommonBots(equip.Bots):
	name = "Common Bots"
	dodge = 3
	price = 10
	
class CommonAmulet(equip.Amulet):
	name = "Common Amulet"
	hp_recovery = 10
	price = 10
	
#add equip
armor_arr.append(CommonArmor)
weapon_arr.append(CommonWeapon)
bots_arr.append(CommonBots)
amulet_arr.append(CommonAmulet)


#create uncommon equip
class UncommonArmor(equip.Armor):
	name = "Uncommon Armor"
	defense = 7
	hp = 35
	price = 25
	
class UncommonWeapon(equip.Weapon):
	name = "Uncommon Weapon"
	damage = 8
	price = 25
	
class UncommonBots(equip.Bots):
	name = "Uncommon Bots"
	dodge = 6
	price = 25
	
class UncommonAmulet(equip.Amulet):
	name = "Uncommon Amulet"
	hp_recovery = 15
	price = 25
	
#add equip
armor_arr.append(UncommonArmor)
weapon_arr.append(UncommonWeapon)
bots_arr.append(UncommonBots)
amulet_arr.append(UncommonAmulet)


#create Epic equip
class EpicArmor(equip.Armor):
	name = "Epic Armor"
	defense = 10
	hp = 50
	price = 40
	
class EpicWeapon(equip.Weapon):
	name = "Epic Weapon"
	damage = 12
	price = 40
	
class EpicBots(equip.Bots):
	name = "Epic Bots"
	dodge = 10
	price = 40
	
class EpicAmulet(equip.Amulet):
	name = "Epic Amulet"
	hp_recovery = 25
	price = 40
	
#add equip
armor_arr.append(EpicArmor)
weapon_arr.append(EpicWeapon)
bots_arr.append(EpicBots)
amulet_arr.append(EpicAmulet)


#create Legendary equip
class LegendaryArmor(equip.Armor):
	name = "Legendary Armor"
	defense = 15
	hp = 100
	price = 75
	
class LegendaryWeapon(equip.Weapon):
	name = "Legendary Weapon"
	damage = 20
	price = 75
	
class LegendaryBots(equip.Bots):
	name = "Legendary Bots"
	dodge = 18
	price = 75
	
class LegendaryAmulet(equip.Amulet):
	name = "Legendary Amulet"
	hp_recovery = 40
	price = 75
	
#add equip
armor_arr.append(LegendaryArmor)
weapon_arr.append(LegendaryWeapon)
bots_arr.append(LegendaryBots)
amulet_arr.append(LegendaryAmulet)
