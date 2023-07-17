from sys import exit
import random

#data structs

indoor = ["Video Game Date","Make Lightsabers","Self-care Night", "Coding Project Date", 
"Go to the store and make a \"First Date\" Dinner", "Indoor Picnic", "Learn a new Skill", 
"Make your own pizzas", "Tye-dye something", "Have a breakfast date", "At-home workout", "Watch a Netflix Show"];
active = ["Swimming", "WhoaZone at Pleasant Hill Lake Park","German Village Bike Ride",
"Get a tee time!", "Jog to a food place",
"Climbing Date", "Gym Date", "Ice/Rollerskating"];
drink = ["Studio35 Movie Date","Bar Hopping Night","Time to hit a club!", 
"Summit Music Hall (Whatever is going on that night", "Dirty Dungarees", "O'Reilly's Pub", "Cosi After Dark", 
"Comedy Show", "Trivia/Karaoke Night", "Brewery/Winery", "Skully's Music Diner", "Piano Bar", "The Bluestone",
"Arcade Bar"];
food = ["Cute Place for Dinner","Fox in the Snow", "Buddery Food Hall", 
"La Chatalane", "Go out for a dessert (Milkshake bar??)"];
other = ["Otherworld Date", "Columbus Coffe Trail", "Franklin County Conservatory", "Gateway Movie", 
"Cosi Date", "Easton Mall Date", "Drive-in Movie", "Picnic", "Zoo/Aquarium Date", 
"Museum Date","Berry/Apple Picking", "Go Kite Flying", "Farmer's Market", "Bowling", "Arcade Bar", 
"Thrift Outfits for each other", "Laser Tag", "Go-karts!", "Geocaching"];
cleveland = ["Aries Lounge (rave)", "Claridon Woodlands (ziplining/rock climbing)", 
"White water rafting in Chagrin River", "Pinspiration"];


#intro
print("Hello and welcome to the Date Decider!\n");
print("Answer these simple questions, and I'll plan a date for you!\n");



#start of questions

answer = input("1: In Cleveland or 2: Columbus?\n");

#if indoor
if answer=="1":
	rand = random.randrange(0,len(cleveland));
	print("Your date idea: ");
	print(cleveland[rand]);
	exit();

	
#if indoor
elif(answer=="2"):
	answer = input("1: Indoor or 2: outdoor?\n");

	if answer=="1":
		rand = random.randrange(0,len(indoor));
		print("Your date idea: ");
		print(indoor[rand]);
		exit();

	
#if outdoor
	elif(answer=="2"):
		answer = input("1: Active or 2: non-active activity\n");
	
		#outdoor, active
		if(answer=="1"):
			rand = random.randrange(0,len(active));
			print(active[rand]);
			exit();

		elif(answer=="2"):
				
			answer = input("1:Drinking or 2:non-drinking\n");
	
			#outdoor, drinking
			if(answer=="1"):
				rand = random.randrange(0,len(drink));
				print(drink[rand]);
				exit();

			elif(answer=="2"):
			
				answer = input("1:Get food or 2: nah\n");
	
				#outdoor, food
				if(answer=="1"):
					rand = random.randrange(0,len(food));
					print(food[rand]);
					exit();

				#outdoor, non-drinking, non-active, non-food
				elif(answer=="2"):
					rand = random.randrange(0,len(other));
					print(other[rand]);
					exit();


exit();



