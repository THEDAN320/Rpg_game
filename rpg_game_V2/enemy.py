import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset = True)

class Enemy:
	name = ""
	hp:int = 0
	max_hp:int = 0
	defense = 0
	damage:int = 0
	dodge = 0
	money = 0
	exp = 0
	
	@staticmethod
	def get_attr(cls):
		print(Fore.RED + f"Имя врага  - {cls.name}")
		print(Fore.RED + f"Здоровье врага  - {cls.hp}/{cls.max_hp}")
		print(Fore.LIGHTBLACK_EX + f"Урон врага  - {cls.damage}\n")

class Goblin(Enemy):
	name = "Goblin"
	max_hp = 50
	hp = max_hp
	damage = 20
	money = 15
	exp = 30
	
class Zombie(Enemy):
	name = "Zombie"
	max_hp = 100
	hp = max_hp
	damage = 15
	money = 20
	exp = 35
	
class Spider(Enemy):
	name = "Spider"
	max_hp = 80
	hp = max_hp
	damage = 35
	money = 25
	exp = 50
	
class Skelet(Enemy):
	name = "Skelet"
	max_hp = 75
	hp = max_hp
	damage = 25
	defense = 5
	money = 35
	exp = 40
	
class Mutant(Enemy):
	name = "mutant (mini boss)"
	max_hp = 200
	hp = max_hp
	damage = 30
	money = 50
	exp = 100
	
monster_arr = [Goblin, Zombie, Spider,Skelet,Mutant]
	
def get_vrag(player):
	
	stage = player.stage
	
	if player.stage <= 5:
		vrag = monster_arr[stage - 1]
		return vrag
		
	if player.stage <= 10:
		
		stage -= 5
		vrag = monster_arr[stage - 1]
		vrag.max_hp = round(vrag.max_hp * 1.2)
		vrag.damage = round(vrag.damage * 1.2)
		vrag.defense += 2
		vrag.money += 10
		vrag.hp = vrag.max_hp
		vrag.exp += 25
		return vrag
			
	if player.stage <= 15:
		
		stage -= 10
		vrag = monster_arr[stage - 1]
		vrag.max_hp = round(vrag.max_hp * 1.35)
		vrag.damage = round(vrag.damage * 1.35)
		vrag.defense += 4
		vrag.money += 20
		vrag.hp = vrag.max_hp
		vrag.exp += 120
		return vrag
			
	if player.stage <= 20:
		
		stage -= 15
		vrag = monster_arr[stage - 1]
		vrag.max_hp = round(vrag.max_hp * 1.5)
		vrag.damage = round(vrag.damage * 1.5)
		vrag.defense += 8
		vrag.money += 30
		vrag.hp = vrag.max_hp
		vrag.exp += 267
		
		return vrag
		
	else:
		print("Мододец! Ты всех победил!\nПока это все:)")
	