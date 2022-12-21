def equiping(player,equip,number):
	print("\033[H\033[J")
	equip_type = equip.type
	
	if equip_type == "armor":
		player.hp -= player.armor.hp
		player.max_hp -= player.armor.hp
		player.defense -= player.armor.defense
		player.inventory["equip"]["Armor"].append(player.armor)
		
		player.armor = equip
		player.hp += equip.hp
		player.max_hp += equip.hp
		player.defense += equip.defense
		player.inventory["equip"]["Armor"].pop(int(number) - 1)
		
	if equip_type == "weapon":
		player.damage -= player.weapon.damage
		player.inventory["equip"]["Weapon"].append(player.weapon)
		
		player.weapon = equip
		player.damage += equip.damage
		player.inventory["equip"]["Weapon"].pop(int(number) - 1)
		
	if equip_type == "bots":
		player.dodge -= player.bots.dodge
		player.inventory["equip"]["Bots"].append(player.bots)
		
		player.bots = equip
		player.dodge += equip.dodge
		player.inventory["equip"]["Bots"].pop(int(number) - 1)
		
	if equip_type == "amulet":
		player.hp_recovery -= player.amulet.hp_recovery
		player.inventory["equip"]["Amulet"].append(player.amulet)
		
		player.amulet = equip
		player.hp_recovery += equip.hp_recovery
		player.inventory["equip"]["Amulet"].pop(int(number) - 1)

def equip(player):
		
	while True:
		print("Ваша экипировка: ")
		print(player.armor.name)
		print(player.weapon.name)
		print(player.bots.name)
		print(player.amulet.name)
		print()

		choice = input("[1]Броня\n[2]Оружие\n[3]Ботиники\n[4]Амулет\n[5]Выход\n- ")
		print("\033[H\033[J")
		
		if choice == "1":
			player.armor.get_armor(player.armor)
			print("--------------")
			print("Броня в инвенторе:\n")
			
			count = 0
			for i in player.inventory["equip"]["Armor"]:
				count += 1
				print(f"{count}:")
				i.get_armor(i)
				
			if count > 0:
				choice = input("Одеть другую броню?\n[1]Да\n[2]Нет\n- ")
			
				if choice == "1":
					number = input("Введите номер брони - ")
					equiping(player,player.inventory["equip"]["Armor"][int(number) - 1],number)
						
			
		if choice == "2":
			player.weapon.get_weapon(player.weapon)
			print("--------------")
			print("Оружие в инвенторе:\n")
			
			count = 0
			for i in player.inventory["equip"]["Weapon"]:
				count += 1
				print(f"{count}:")
				i.get_weapon(i)
				
			if count > 0:
				choice = input("Одеть другое оружие?\n[1]Да\n[2]Нет\n- ")
			
				if choice == "1":
					number = input("Введите номер оружия - ")
					equiping(player,player.inventory["equip"]["Weapon"][int(number) - 1],number)
			
		if choice == "3":
			player.bots.get_bots(player.bots)
			print("--------------")
			print("Ботинки в инвенторе:\n")
			
			count = 0
			for i in player.inventory["equip"]["Bots"]:
				count += 1
				print(f"{count}:")
				i.get_bots(i)
				
			if count > 0:
				choice = input("Одеть другие ботинки?\n[1]Да\n[2]Нет\n- ")
			
				if choice == "1":
					number = input("Введите номер ботинок - ")
					equiping(player,player.inventory["equip"]["Bots"][int(number) - 1],number)
			
		if choice == "4":
			player.amulet.get_amulet(player.amulet)
			print("--------------")
			print("Амулеты в инвенторе:\n")
			
			count = 0
			for i in player.inventory["equip"]["Amulet"]:
				count += 1
				print(f"{count}:")
				i.get_amulet(i)
				
			if count > 0:
				choice = input("Одеть другой амулет?\n[1]Да\n[2]Нет\n- ")
			
				if choice == "1":
					number = input("Введите номер амулета - ")
					equiping(player,player.inventory["equip"]["Amulet"][int(number) - 1],number)
		
		if choice == "5":
			print()
			break