class Enemy:
	name = ""
	hp = 0
	defense = 0
	damage = 0
	dodge = 0
	money = 25

class Goblin(Enemy):
	name = "Goblin"
	hp = 50
	damage = 20
	
class Zombie(Enemy):
	name = "Zombie"
	hp = 100
	damage = 15
	
class Spider(Enemy):
	name = "Spider"
	hp = 80
	damage = 35
	
class Skelet(Enemy):
	name = "Skelet"
	hp = 75
	damage = 25
	defense = 5
	
class Mutant(Enemy):
	name = "mutant (mini boss)"
	hp = 200
	damage = 30
	money = 150
	
def get_vrag(player,vrag):
	if player.stage == 1:
		return Goblin
		
	if player.stage == 2:
		return Zombie
	
	if player.stage == 3:
		return Spider
		
	if player.stage == 4:
		return Skelet
		
	if player.stage == 5:
		return Mutant
	else:
		print("Мододец! Ты всех победил!\nПока это все:)")
	