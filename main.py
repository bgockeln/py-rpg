import os
from store import Store, all_items
from ascii import banner, banner2
from character import Warrior, Mage
from enemy import Intern, MrClip, Deadld, Kevin, Karen
from actions import fight

boss_order = [MrClip, Deadld, Kevin, Karen]

# Advance from Boss to Boss
class game_state:
    def __init__(self):
        self.current_level = 1
        self.defeated_bosses = []
        self.final_boss_defeated = False # Flag to end game after last boss is defeated

    def advance_level(self, boss_name):
        self.defeated_bosses.append(boss_name)
        self.current_level += 1
        if boss_name == "Karen(CEO)":
            self.final_boss_defeated = True # flip the switch
    
    def get_next_boss(self):
        next_index = len(self.defeated_bosses)
        if next_index < len(boss_order):
            return boss_order[next_index]()
        return None

# clear screen helper function
def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

# wait for input helper function
def wait():
    input("Press any key")

# main menu
def main_menu():
    clear_screen()
    print(banner)
    print("\n==== Main Menu ====")
    print("1. New Game")
    print("2. Exit")
    choice = input("Choice: ")
    return choice

# game menu
def game_menu():
    clear_screen()
    print("\n==== Game Menu ====")
    print("1. Fight an intern")
    print("2. Fight the next boss")
    print("3. Go shopping")
    print("4. Back to Main Menu")
    choice = input("Choice: ")
    return choice

# Main function
def main():
    running = True
    game_stat = game_state()

    while running:
        choice = main_menu()
    # Char choice
        if choice == "1":
            clear_screen()
            print("Pick a Class: ")
            print("1. Office Warrior")
            print("2. Office Mage")
            choice = input("Choice: ")

            char_name = input("Enter your name: ")
            if choice == "1":
                player = Warrior(name=char_name)
            elif choice == "2":
                player = Mage(name=char_name)
            else:
                print("Invalid entry")
            
            in_game = True
            while in_game:
                action = game_menu()

                if action == "1":
                    clear_screen()
                    thug = Intern(level=game_stat.current_level)
                    fight(player, thug)
                elif action == "2":
                    clear_screen()
                    boss = game_stat.get_next_boss()
                    if boss:
                        fight(player, boss)
                        if boss.hp <= 0:
                            print(f"{boss.name} defeated!")
                            game_stat.advance_level(boss.name)
                            if game_stat.final_boss_defeated: # check the switch
                                clear_screen()
                                print(banner2)
                                wait()
                                in_game = False
                                running = False
                        else:
                            print("A Boss is still alive!")
                            wait()
                elif action == "3":
                    clear_screen()
                    shop = Store(all_items)
                    shop.shop_menu(player)
                    wait()
                elif action == "4":
                    in_game = False
                else:
                    print("Invalid entry")
                    wait()
        
        elif choice == "2":
            print("Running away?")
            running = False
        else:
            print("Invalid entry")
            wait()

if __name__ == "__main__":
    main()