def main():
	combo = []
	for i in range(3):
		combo.append(input(f"Enter Skill {i+1}: ").capitalize()) 
    
	if combo[0] == "Quas":
		if combo[1] == "Quas":
			if combo[2] == "Quas":
				skill = "Cold Snap"
			elif combo[2] == "Wex":
				skill = "Ghost Walk"
			elif combo[2] == "Exort":
				skill = "Ice Wall"
		elif combo[1] == "Wex":
			if combo[2] == "Wex":
				skill = "Tornado"
			elif combo[2] == "Exort":
				skill = "Deafening Blast"
		elif combo[1] == "Exort":
			if combo[2] == "Exort":
				skill = "Forge Spirit"
	elif combo[0] == "Wex":
		if combo[1] == "Wex":
			if combo[2] == "Wex":
				skill = "EMP"
			elif combo[2] == "Exort":
				skill = "Alacrity"
		elif combo[1] == "Exort":
			if combo[2] == "Exort":
				skill = "Exort"
	elif combo[0] == "Exort":
		if combo[1] == "Exort":
			if combo[2] == "Exort":
				skill = "Sun Strike"
    
	print("Spell Casted:", skill)
    
if __name__ == "__main__":
    main()