import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset = True)

def attribut_menu(player):
	print("\033[H\033[J")
	print(f"Свободные очки распределения - {player.attribut_point}")
	print("Что вы хотите улучшить?")
	choice = input("[1]Здоровье (+20)\n[2]Броня (+2)\n[3]Урон (+5)\n[4]Шанс уклонения (+2)\n[5]Восстановление жизней (+10)\n[0]Выход\n - ")
	print("\033[H\033[J")
	
	if player.attribut_point < 1:
		print(Fore.RED + "Нет свободных очков распределения")
		return
		
	if choice == "1":
		player.hp += 20
		player.max_hp += 20
		player.attribut_point -= 1
		print("\033[H\033[J")
		print(Fore.GREEN + "Улучшено!")
		
	if choice == "2":
		player.defense += 2
		player.attribut_point -= 1
		print("\033[H\033[J")
		print(Fore.GREEN + "Улучшено!")
		
	if choice == "3":
		player.damage += 5
		player.attribut_point -= 1
		print("\033[H\033[J")
		print(Fore.GREEN + "Улучшено!")
		
	if choice == "4":
		player.dodge += 2
		player.attribut_point -= 1
		print("\033[H\033[J")
		print(Fore.GREEN + "Улучшено!")
		
	if choice == "5":
		player.hp_recovery += 10
		player.attribut_point -= 1
		print("\033[H\033[J")
		print(Fore.GREEN + "Улучшено!")
		
	if choice == "0":
		print("\033[H\033[J")
		return