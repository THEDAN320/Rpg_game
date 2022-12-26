import all_character
import enemy
import fight
import equip
import equip_process
import shop
import attribut

import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset = True)

vrag = None
player = all_character.Knight
player.inventory["hill_potion"] = 3
while True:
	choice = input("Что вы хотите сделать?\n[1]Узнать статистику\n[2]В бой\n[3]Посмотреть экипировку\n[4]Магазин\n[5]Улучшить статистику\n - ")
	print("\033[H\033[J")
	
	if choice == "1":
		player.get_attr(player)
		
	if choice == "2":
		vrag = enemy.get_vrag(player)
		
		if vrag == None:
			break
			
		fight.fight(player,vrag)
		
	if choice == "3":
		equip_process.equip(player)
		
	if choice == "4":
		shop.shop(player)
	
	if choice == "5":
		attribut.attribut_menu(player)
		
print(Fore.GREEN + "Ты прошел игру!")