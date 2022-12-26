#create parent armor
class Armor:
	name = "None"
	defense = 0
	hp = 0
	price = 0
	type = "Armor"
	
	@staticmethod
	def get_attr(cls):
		print(f"Название брони - {cls.name}")
		print(f"Параметр defense - {cls.defense}")
		print(f"Параметр hp - {cls.hp}")
	
#create parent weapon
class Weapon:
	name = "None"
	damage = 0
	price = 0
	type = "Weapon"
	
	@staticmethod
	def get_attr(cls):
		print(f"Название оружия - {cls.name}")
		print(f"Параметр damage - {cls.damage}")

#create parent amulet
class Amulet:
	name = "None"
	hp_recovery = 0
	price = 0
	type = "Amulet"
	
	@staticmethod
	def get_attr(cls):
		print(f"Название амулета - {cls.name}")
		print(f"Параметр hp_recovery - {cls.hp_recovery}")
	
#create parent bots
class Bots:
	name = "None"
	dodge = 0
	price = 0
	type = "Bots"
	
	@staticmethod
	def get_attr(cls):
		print(f"Название ботинок - {cls.name}")
		print(f"Параметр dodge - {cls.dodge}")
	