import equip
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset = True)

#create all character parent
class Character:
	name = ""
	max_hp:int = 0
	hp:int = 0
	defense = 0
	damage:int = 0
	dodge = 0
	hp_recovery = 0
	
	attribut_point = 0
	level = 1
	exp = 0
	needle_exp = 100
	
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
		print(Fore.LIGHTBLACK_EX + f"Ваш класс - {cls.name}")
		print(Fore.MAGENTA + f"Уровень игрока - {cls.level}")
		print(Fore.MAGENTA + f"Опыт - {cls.exp}/{cls.needle_exp}")
		print(Fore.LIGHTRED_EX + f"Ваше здоровье - {cls.hp}/{cls.max_hp}")
		print(Fore.CYAN + f"Ваша защита - {cls.defense}")
		print(Fore.CYAN + f"Ваш урон - {cls.damage}")
		print(Fore.CYAN + f"Ваш шанс на уклонение - {cls.dodge}")
		print(Fore.CYAN + f"Ваше восстановление жизней - {cls.hp_recovery}")
		print(Fore.CYAN + "Зелья восстановления(50 хп) -", cls.inventory["hill_potion"])
		print(Fore.YELLOW + f"Ваши деньги - {cls.money}")
		print(Fore.LIGHTBLACK_EX + f"Стадия - {cls.stage}\n")
		
#create class knight
class Knight(Character):
	name = "Knight"
	max_hp = 200
	hp = 200
	defense = 10
	damage = 15