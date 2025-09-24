import random
import os

# clear screen helper function
def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

# wait for input helper function
def wait():
    input("Press any key")

def basic_attack(attacker, defender):
    damage = max(0, attacker.attack - defender.defense)
    print(f"{attacker.name} attacks {defender.name} and causes {damage} damage.")
    defender.take_damage(damage)

def fight(player, enemy):
    player.hp = player.max_hp # reset lives before each fight
    player.special_cooldown = 0 # reset the cool down at the start of each fight
    print(f"\n=== {enemy.name} appears! ===")

    if enemy.ascii_art:
        print(enemy.ascii_art)
        wait()

    round_num = 1
    while player.hp > 0 and enemy.hp > 0:
        print(f"\n--- Round {round_num} ---")
        print(f"{player.name}: {player.hp} HP | {enemy.name}: {enemy.hp} HP")

        # dynamic menu
        print("1. Attack")
        if player.special_cooldown == 0:
            print("2. Special attack (ready!)")
        else:
            print(f"2. Special attack (ready in {player.special_cooldown} rounds.)")
        
        # Player turn
        choice = input("Choice: ")
        if choice == "1":
            basic_attack(player, enemy)
        elif choice == "2":
            if hasattr(player, "special_attack"):
                player.special_attack(enemy)
            else:
                print("Special attack not available!")
                wait()
        else:
            print("Invalid entry, you lose a round")
            wait()

        if enemy.hp <= 0:
            print(f"{enemy.name} was defeated! You earn {enemy.reward_money} Gold!")
            if hasattr(enemy, 'reward_money'):
                player.money += enemy.reward_money
            wait()

        # Enemy Turn
        if hasattr(enemy, "special_attack") and random.random() < 0.3: # 30 % Chance to use special attack
            enemy.special_attack(player)
        else:
            basic_attack(enemy, player)
        
        if player.hp <= 0:
            print(f"\n{player.name} was defeated, Game Over!")
            wait()
            return False
        
        player.reduce_cooldown()
        round_num += 1