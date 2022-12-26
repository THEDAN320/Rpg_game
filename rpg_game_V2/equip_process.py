def equiping(player,equip,number):
	print("\033[H\033[J")
	equip_type = equip.type
	
	if equip_type == "Armor":
		player.hp -= player.armor.hp
		player.max_hp -= player.armor.hp
		player.defense -= player.armor.defense
		player.inventory["equip"]["Armor"].append(player.armor)
		
		player.armor = equip
		player.hp += equip.hp
		player.max_hp += equip.hp
		player.defense += equip.defense
		player.inventory["equip"]["Armor"].pop(int(number) - 1)
		
	if equip_type == "Weapon":
		player.damage -= player.weapon.damage
		player.inventory["equip"]["Weapon"].append(player.weapon)
		
		player.weapon = equip
		player.damage += equip.damage
		player.inventory["equip"]["Weapon"].pop(int(number) - 1)
		
	if equip_type == "Bots":
		player.dodge -= player.bots.dodge
		player.inventory["equip"]["Bots"].append(player.bots)
		
		player.bots = equip
		player.dodge += equip.dodge
		player.inventory["equip"]["Bots"].pop(int(number) - 1)
		
	if equip_type == "Amulet":
		player.hp_recovery -= player.amulet.hp_recovery
		player.inventory["equip"]["Amulet"].append(player.amulet)
		
		player.amulet = equip
		player.hp_recovery += equip.hp_recovery
		player.inventory["equip"]["Amulet"].pop(int(number) - 1)

def info(tip,player):
			tip.get_attr(tip)
			print("--------------")
			print("Вещей в инвенторе:\n")
			
			count = 0
			for i in player.inventory["equip"][tip.type]:
				count += 1
				print(f"{count}:")
				i.get_attr(i)
				
			if count > 0:
				choice = input("Одеть другую вещь?\n[1]Да\n[2]Нет\n- ")
			
				if choice == "1":
					number = int(input("Введите номер - "))
					if number > 0 and number <= count:
						equiping(player,player.inventory["equip"][tip.type][number - 1],number)
						print("\033[H\033[J")
				print("\033[H\033[J")

def equip(player):
		
	while True:
		print("Ваша экипировка: ")
		print(player.armor.name)
		print(player.weapon.name)
		print(player.bots.name)
		print(player.amulet.name)
		print()

		choice = input("[1]Броня\n[2]Оружие\n[3]Ботиники\n[4]Амулет\n[0]Выход\n- ")
		print("\033[H\033[J")
		
		if choice == "1":
			info(player.armor,player)
			
		if choice == "2":
			info(player.weapon,player)
			
		if choice == "3":
			info(player.bots,player)
			
		if choice == "4":
			info(player.amulet,player)
		
		if choice == "0":
			print()
			break
		print("\033[H\033[J")