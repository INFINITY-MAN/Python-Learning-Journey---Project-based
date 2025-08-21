import random
import msvcrt
import time
print("The Martial Path awaits you! Prepare for an epic journey.")
# Martial Path Game Initialization Version 1.0
# Define monsters and their stats
# Monsters are represented as a dictionary with their names and difficulty levels
monsters = {"Goblin" : 1, "Orc" : 5, "Troll" : 10, "Dragon": 300}
stats={"Health": 100, "Strength": 10, "Defense": 5, "Magic": 0}
default_stats= {"Health": 100, "Strength": 10, "Defense": 5, "Magic": 0}
points = 2
# Function to run the game
def Run(stats, monsters, default_stats, points):
    print("Welcome to the Martial Path Game!")
    print("You will embark on a journey filled with challenges and monsters.")
    print("Your goal is to defeat monsters and improve your character's stats.")
    Run_way()
    while True:
        choice = todo()
        if choice == "1":
            fight(stats, monsters, default_stats, points)
        elif choice == "2":
            character_stats(points, stats)
        elif choice == "3":
            addpoints(points, stats)
        elif choice == "4":
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
def todo():
    print("1. Start your journey")
    print("2. View character stats")
    print("3. Add points to character")
    print("4. Exit game")
    choice = input("Choose an option (1-4): ")
    return choice
def Run_way():
    while True:
        print("|||| . . . . .  . . . . Press S for start  . . . . . . . . . . |||")
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key.lower() == b's':
                print("\nYou have chosen the path of the warrior.")
                break
        time.sleep(0.0001)
def select_monster(monsters):
    a= random.choice(monsters)
    print(f"A wild {a} appears!")
    return a
def character_stats(points, stats):
    print("Your character's stats:")
    for stat, value in stats.items():
        print(f"{stat}: {value}")
    print(f"Points available: {points}")
    s=input("do you want to add points to your character? (yes/no)")
    if s.lower() == "yes":
        if points > 0:
            addpoints(points, stats)
            character_stats(points,stats)
        else:
            print("You have no points to add.")    
    else:
        print("No points added. Proceeding with current stats.")
def addpoints(points, stats):
        print(f"You have {points} points to spend.")
        print("Choose how to spend your points:")
        print("1. Strength (+5)")
        print("2. Defense (+2)")
        print("3. Magic (+1)")
        print("4. Health (+20)")
        choice = input("Enter your choice: ").lower()
        if points > 0:
            if choice.lower == "strength":
                stats["Strength"] += 5
            elif choice.lower == "defense":
                stats["Defense"] += 2
            elif choice.lower == "magic":
                stats["Magic"] += 1
            elif choice.lower == "health":
                stats["Health"] += 20
            points -= 1
            print(f"Points left: {points}")
        else:
            print("Invalid choice. Please try again.")
def player_attack(stats, monster, action):
    if action == "physicalattack":
        damage = (stats["Strength"] * 10) - monster["Defense"]
        if damage < 0:
            damage = 0
        monster_health -= damage
        print(f"You dealt {damage} damage to the {monster}.")
    elif action == "defend":
        print("You brace yourself for the monster's attack.")
        temp_health = stats["Health"] + stats["Defense"]
        print(f"Your health is now {temp_health}.")
    elif action == "magic attack":
        damage = (stats["Magic"] * 100) -monster["Defense"] -(monster["Magic"]*10)
        if damage < 0:
            damage = 0
        monster_health -= damage
        print(f"You dealt {damage} magic damage to the {monster}.")
def monster_attack_defend(stats, monster, temp_health):
    monster_action = random.choice(["attack", "magic attack"])
    if monster_action == "attack":
        damage = (monster["Strength"] * 10) - temp_health
        if damage < 0:
            damage = 0
        stats["Health"] -= damage
        print(f"The {monster} dealt {damage} damage to you.")
    elif monster_action == "magic attack":
        damage = (monster["Magic"] * 100) - temp_health - (stats["Magic"] * 10)
        if damage < 0:
            damage = 0
        stats["Health"] -= damage
        print(f"The {monster} dealt {damage} magic damage to you.")
def player_defend(stats, monster, action):
    if action == "defend":
        temp_health = stats["Health"] + stats["Defense"]
        monster_attack_defend(stats, monster, temp_health)
    else:
        monster_action = random.choice(["attack", "magic attack"])
        if monster_action == "attack":
            damage = (monster["Strength"] * 10) - stats["Defense"]
            if damage < 0:
                damage = 0
            stats["Health"] -= damage
            print(f"The {monster} dealt {damage} damage to you.")
        elif monster_action == "magic attack":
            damage = (monster["Magic"] * 100) - stats["Defense"] - (stats["Magic"] * 10)
            if damage < 0:
                damage = 0
            stats["Health"] -= damage
            print(f"The {monster} dealt {damage} magic damage to you.")
def game_over(stats, monsters, points, monster):
    if stats["Health"] <= 0:
        print("You have been defeated! Game Over.")
        return True
    elif monsters["Health"] <= 0:
        print(f"You have defeated the {monster}! Congratulations!")
        points += monsters[monster]
        print(f"You gained {monsters[monster]} points. Total points: {points}")
        return True
    else:
        return False
def fight(stats, monsters,default_stats, points):
    monster=select_monster(monsters)
    print("Prepare for battle!")
    monster_health = monsters[monster]* default_stats["Health"]
    monster_strength = monsters[monster]* default_stats["Strength"]
    monster_defense = monsters[monster]* default_stats["Defense"]
    monster_magic = monsters[monster]* default_stats["Magic"]
    current_monster={"Health": monster_health, "Strength": monster_strength, "Defense": monster_defense, "Magic": monster_magic}
    current_player={"Health": stats["Health"], "Strength": stats["Strength"], "Defense": stats["Defense"], "Magic": stats["Magic"]}
    print(f"You encounter a {monster}!")
    print(f"Monster Stats - Health: {monster_health}, Strength: {monster_strength}, Defense: {monster_defense}, Magic: {monster_magic}")
    game_over_flag = True
    while game_over_flag:
        print(f"\nYour Health: {stats['Health']}")
        print(f"Monster's Health: {monster_health}")
        action = input("Choose your action (PhysicalAttack/Defend/Magic Attack): ").lower()
        player_attack(current_player, current_monster, action)
        player_defend(current_player, current_monster, action)
        game_over_flag = not game_over(current_player, current_monster)
    if game_over_flag:
        print("The battle is over. You can continue your journey.")

Run(stats, monsters, default_stats, points)
    




        