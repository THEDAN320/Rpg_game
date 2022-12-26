import equip_for_shop
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset = True)

def purshe(player,equip,number,equip_arr):
	
	if player.money < equip.price:
		print("\033[H\033[J")
		print(Fore.RED + "Недостаточно средств!\n")
		return
	
	player.inventory["equip"][equip.type].append(equip)
	player.money -= equip.price
	equip_arr.pop(number)
	print("\033[H\033[J")
	print(Fore.GREEN + "Успешная покупка!\n")
		

def assortiment(equip_arr,player):
	print("\033[H\033[J")
	print(Fore.YELLOW + f"Ваши деньги - {player.money}")
	print("Весь список товаров:\n")
	count = 1
			
	for i in equip_arr:
		print("-"*15)
		print(count)
		count += 1
		i.get_attr(i)
		print(Fore.YELLOW + f"Цена - {i.price}\n")
				
	choice = int(input("[0]Выход\nВведите номер товара, который хотите купить - "))
	print("\033[H\033[J")
	
	if choice == 0:
		return
	if choice > 0 and choice <= count:
		purshe(player,equip_arr[choice - 1], choice - 1,equip_arr)
		
def shop(player):
	while True:
		choice = input("Что вы хотите купить?\n[1]Броня\n[2]Оружие\n[3]Ботинки\n[4]Амулет\n[5]Зелье\n[0]Выход\n- ")
		print("\033[H\033[J")
		
		if choice == "1":
			assortiment(equip_for_shop.armor_arr,player)

		if choice == "2":
			assortiment(equip_for_shop.weapon_arr,player)
			
		if choice == "3":
			assortiment(equip_for_shop.bots_arr,player)
				
		if choice == "4":
			assortiment(equip_for_shop.amulet_arr,player)
		
		if choice == "5":
			print(Fore.YELLOW + f"Ваши деньги - {player.money}")
			choice = input("Цена зелья - 15\nПокупаете?\n[1]Да\n[2]Нет\n- ")
			if choice == "1":
				if player.money >= 15:
					player.money -= 15
					player.inventory["hill_potion"] += 1
					print("\033[H\033[J")
					print(Fore.GREEN + "Успешная покупка!\n")
				else:
					print("\033[H\033[J")
					print(Fore.RED + "Недостаточно средств!\n")
			else:
				print("\033[H\033[J")
		
		if choice == "0":
			break
		