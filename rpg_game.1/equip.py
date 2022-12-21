#create parent armor
class Armor:
	name = "None"
	defense = 0
	hp = 0
	price = 0
	type = "armor"
	
	@staticmethod
	def get_armor(cls):
		print(f"Название брони - {cls.name}")
		print(f"Параметр defense - {cls.defense}")
		print(f"Параметр hp - {cls.hp}\n")
	
#create parent weapon
class Weapon:
	name = "None"
	damage = 0
	price = 0
	type = "weapon"
	
	@staticmethod
	def get_weapon(cls):
		print(f"Название оружия - {cls.name}")
		print(f"Параметр damage - {cls.damage}\n")

#create parent amulet
class Amulet:
	name = "None"
	hp_recovery = 0
	price = 0
	type = "amulet"
	
	@staticmethod
	def get_amulet(cls):
		print(f"Название амулета - {cls.name}")
		print(f"Параметр hp_recovery - {cls.hp_recovery}\n")
	
#create parent bots
class Bots:
	name = "None"
	dodge = 0
	price = 0
	type = "bots"
	
	@staticmethod
	def get_bots(cls):
		print(f"Название ботинок - {cls.name}")
		print(f"Параметр dodge - {cls.dodge}\n")
	