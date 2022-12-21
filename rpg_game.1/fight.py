from random import randint
import time
import sys

def fight(player,enemy):
		
	while True:
		print(f"Ваше здоровье - {player.hp}/{player.max_hp}\n")
		print(f"Уровень {player.stage}")
		print(f"Имя врага  - {enemy.name}")
		print(f"Здоровье врага  - {enemy.hp}")
		print(f"Урон врага  - {enemy.damage}\n")
		
		if player.hp <= 0:
			print("Вы проиграли!")
			sys.exit()
			break
			
		if enemy.hp <= 0:
			print("Вы победили врага!")
			player.stage += 1
			player.money += enemy.money
			print(f"Получено {enemy.money} золота")
			print("Подождите 5 секунд")
			time.sleep(5)
			print("\033[H\033[J")
			print()
			break
			
		choice = input("Выберите действие:\n[1]ударить\n[2]Выпить зелье здоровья\n- ")
		print("\033[H\033[J")
	
		if choice == "1":
			dmg_on_enemy = player.damage - enemy.defense
			
			if dmg_on_enemy <= 0:
				dmg_on_enemy = 0
				
			enemy.hp -= dmg_on_enemy
			print(f"Нанесено {dmg_on_enemy} урона")
			
			dmg_on_player = enemy.damage - player.defense
			
			if randint(1,100) <= player.dodge:
				print("Вы уклонились от атаки!")
				dmg_on_player = 0
			
			if dmg_on_player <= 0:
				dmg_on_player = 0

			player.hp -= dmg_on_player
			print(f"Получено {dmg_on_player} урона")
			
		if choice == "2":
			
			if player.inventory["hill_potion"] <= 0:
				print("У вас нет зелий!")
				
			else:
				print("Вы использовали зелье!")
				player.hp += 50 + player.hp_recovery
				if player.hp > player.max_hp:
					player.hp = player.max_hp
				player.inventory["hill_potion"] -= 1
		
