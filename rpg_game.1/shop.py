import equip_for_shop

def purshe(player,equip,number):
	
	if player.money < equip.price:
		print("\033[H\033[J")
		print("Недостаточно средств!\n")
		return
	
	if equip.type == "armor":
		player.inventory["equip"]["Armor"].append(equip)
		player.money -= equip.price
		equip_for_shop.armor_arr.pop(number)
		print("\033[H\033[J")
		print("Успешная покупка!\n")
		
	if equip.type == "weapon":
		player.inventory["equip"]["Weapon"].append(equip)
		player.money -= equip.price
		equip_for_shop.weapon_arr.pop(number)
		print("\033[H\033[J")
		print("Успешная покупка!\n")
		
	if equip.type == "bots":
		player.inventory["equip"]["Bots"].append(equip)
		player.money -= equip.price
		equip_for_shop.bots_arr.pop(number)
		print("\033[H\033[J")
		print("Успешная покупка!\n")
		
	if equip.type == "amulet":
		player.inventory["equip"]["Amulet"].append(equip)
		player.money -= equip.price
		equip_for_shop.amulet_arr.pop(number)
		print("\033[H\033[J")
		print("Успешная покупка!\n")
		

def shop(player):
	while True:
		choice = input("Что вы хотите купить?\n[1]Броня\n[2]Оружие\n[3]Ботинки\n[4]Амулет\n[5]Зелье\n[6]Выход\n- ")
		print("\033[H\033[J")
		
		if choice == "1":
			print(f"Ваши деньги - {player.money}")
			print("Весь список брони:\n")
			count = 1
			
			for i in equip_for_shop.armor_arr:
				print(count)
				count += 1
				i.get_armor(i)
				print(f"Цена - {i.price}\n")
				
			choice = int(input("[0]Выход\nВведите номер брони, которую хотите купить - "))
			if choice == 0:
				print("\033[H\033[J")
				return
				
			purshe(player,equip_for_shop.armor_arr[choice - 1], choice - 1)
			
		if choice == "2":
			print(f"Ваши деньги - {player.money}")
			print("Весь список оружия:\n")
			count = 1
			
			for i in equip_for_shop.weapon_arr:
				print(count)
				count += 1
				i.get_weapon(i)
				print(f"Цена - {i.price}\n")
				
			choice = int(input("[0]Выход\nВведите номер оружия, которое хотите купить - "))
			if choice == 0:
				print("\033[H\033[J")
				return
				
			purshe(player,equip_for_shop.weapon_arr[choice - 1], choice - 1)
			
		if choice == "3":
			print(f"Ваши деньги - {player.money}")
			print("Весь список ботинок:\n")
			count = 1
			
			for i in equip_for_shop.bots_arr:
				print(count)
				count += 1
				i.get_bots(i)
				print(f"Цена - {i.price}\n")
				
			choice = int(input("[0]Выход\nВведите номер ботинок, которые хотите купить - "))
			if choice == 0:
				print("\033[H\033[J")
				return
				
			purshe(player,equip_for_shop.bots_arr[choice - 1], choice - 1)
				
		if choice == "4":
			print(f"Ваши деньги - {player.money}")
			print("Весь список амулетов:\n")
			count = 1
			
			for i in equip_for_shop.amulet_arr:
				print(count)
				count += 1
				i.get_amulet(i)
				print(f"Цена - {i.price}\n")
				
			choice = int(input("[0]Выход\nВведите номер амулеты, который хотите купить - "))
			if choice == 0:
				print("\033[H\033[J")
				return
				
			purshe(player,equip_for_shop.amulet_arr[choice - 1], choice - 1)
		
		if choice == "5":
			print(f"Ваши деньги - {player.money}")
			choice = input("Цена зелья - 15\nПокупаете?\n[1]Да\n[2]Нет\n- ")
			if choice == "1":
				if player.money >= 15:
					player.money -= 15
					player.inventory["hill_potion"] += 1
					print("\033[H\033[J")
					print("Успешная покупка!\n")
				else:
					print("\033[H\033[J")
					print("Недостаточно средств!\n")
			else:
				print("\033[H\033[J")
		
		if choice == "6":
			break
		