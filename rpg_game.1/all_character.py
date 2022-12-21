import equip

#create all character parent
class Character:
	name = ""
	max_hp = 0
	hp = 0
	defense = 0
	damage = 0
	dodge = 0
	hp_recovery = 0
	
	stage = 1
	money = 0
	
	inventory = {
	"equip" : { 
	"Armor" : [],
	"Weapon":[],
	"Bots":[],
	"Amulet":[]
	},
	"hill_potion":0
}
	
	armor = equip.Armor
	weapon = equip.Weapon
	bots = equip.Bots
	amulet = equip.Amulet
	
	@staticmethod
	def get_attr(cls):
		print(f"Ваш класс - {cls.name}")
		print(f"Ваше здоровье - {cls.hp}/{cls.max_hp}")
		print(f"Ваша защита - {cls.defense}")
		print(f"Ваш урон - {cls.damage}")
		print(f"Ваш шанс на уклонение - {cls.dodge}")
		print(f"Ваше восстановление жизней - {cls.hp_recovery}")
		print("Зелья восстановления(50 хп) -", cls.inventory["hill_potion"])
		print(f"Ваши деньги - {cls.money}\n")
		
#create class knight
class Knight(Character):
	name = "Knight"
	max_hp = 200
	hp = 200
	defense = 10
	damage = 15