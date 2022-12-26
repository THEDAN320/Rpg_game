from random import randint
import time
import sys

import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset = True)

def up_level(player,exp):
	player.exp += exp
	print(f"Получено {exp} опыта!")
	
	if player.exp >= player.needle_exp:
		player.exp -= player.needle_exp
		player.needle_exp *= 2
		player.level += 1
		player.attribut_point += 1
		print(Fore.MAGENTA + "Вы подняли уровень!")

def fight(player,enemy):
		
	while True:
		if enemy.hp < 0:
			enemy.hp = 0
			
		print(Fore.GREEN + f"Ваше здоровье - {player.hp}/{player.max_hp}\n")
		print(f"Уровень {player.stage}")
		enemy.get_attr(enemy)
		
		if player.hp <= 0:
			print(Fore.RED + "Вы проиграли!")
			sys.exit()
			break
			
		if enemy.hp == 0:
			print(Fore.GREEN + "Вы победили врага!")
			player.stage += 1
			player.money += enemy.money
			print(Fore.YELLOW + f"Получено {enemy.money} золота")
			up_level(player,enemy.exp)
			print("Подождите 5 секунд")
			time.sleep(5)
			print("\033[H\033[J")
			print()
			break
			
		choice = input("Выберите действие:\n[1]ударить\n[2]Выпить зелье здоровья\n- ")
		print("\033[H\033[J")
	
		if choice == "1":
			print("\033[H\033[J")
			dmg_on_enemy = player.damage - enemy.defense
			
			if dmg_on_enemy <= 0:
				dmg_on_enemy = 0
				
			enemy.hp -= dmg_on_enemy
			print(Fore.GREEN + f"Нанесено {dmg_on_enemy} урона")
			
			dmg_on_player = enemy.damage - player.defense
			
			if randint(1,100) <= player.dodge:
				print(Fore.MAGENTA + "Вы уклонились от атаки!")
				dmg_on_player = 0
			
			if dmg_on_player <= 0:
				dmg_on_player = 0

			player.hp -= dmg_on_player
			print(Fore.RED + f"Получено {dmg_on_player} урона\n")
			
		if choice == "2":
			
			if player.inventory["hill_potion"] <= 0:
				print(Fore.RED + "У вас нет зелий!")
				
			else:
				print(Fore.GREEN + "Вы использовали зелье!")
				recovery = 50 + player.hp_recovery
				player.hp += recovery
				if player.hp > player.max_hp:
					recovery -= player.hp - player.max_hp
					player.hp = player.max_hp
				print(Fore.GREEN + f"Восстановлено - {recovery} hp")
				player.inventory["hill_potion"] -= 1
		