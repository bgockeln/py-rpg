# wait for input helper function
def wait():
    input("Press any key")
    
class Item:
    def __init__(self, name, cost, stat_bonus, allowed_classes):
        self.name = name
        self.cost = cost
        self.stat_bonus = stat_bonus
        self.allowed_classes = allowed_classes

class Store:
    def __init__(self, items):
        self.items = items

    def display(self, player):
        print(f"Welcome to the shop, {player.name}!")
        for idx, item in enumerate(self.items, 1):
            if player.__class__.__name__ in item.allowed_classes:
                print(f"{idx}. {item.name} - {item.cost} Gold")

    def shop_menu(self, player):
        while True:
            print(f"\nYou have {player.money} Gold")
            print("=== Shop ===")
            available_items = [item for item in self.items
                               if player.__class__.__name__ in item.allowed_classes
                               and item.name not in player.inventory]
            
            if not available_items:
                print("No items left.")
                break
            
            for idx, item in enumerate(available_items, 1):
                print(f"{idx}. {item.name} - {item.cost} Gold")
            print(f"{len(available_items) + 1}. Back")

            choice = input("Choice: ")
            if not choice.isdigit():
                print("Invalid entry")
                continue
            choice = int(choice)
        
            if choice == len(available_items)+1:
                break  # exit shop
            elif 1 <= choice <= len(available_items):
                selected_item = available_items[choice-1]
                if player.money >= selected_item.cost:
                    player.money -= selected_item.cost
                    player.inventory.append(selected_item.name)
                    # apply stat bonuses
                    for stat, bonus in selected_item.stat_bonus.items():
                        setattr(player, stat, getattr(player, stat) + bonus)
                    print(f"{selected_item.name} bought! Stats updated.")
                else:
                    print("Not enough Gold!")
                    wait()
            else:
                print("Invalid entry")
all_items = [
    Item(name = "Stapler of Fury +5 attack", cost = 20, stat_bonus = {"attack": 5}, allowed_classes = ["Warrior"]),
    Item(name = "Bulletproof Blazer +5 HP", cost = 20, stat_bonus = {"hp": 5}, allowed_classes = ["Warrior"]),
    Item(name = "Filing Cabinet Shield + 5 defense", cost = 20, stat_bonus = {"defense": 5}, allowed_classes = ["Warrior"]),
    Item(name = "Laser Pointer Wand +5 attack", cost = 20, stat_bonus = {"attack": 5}, allowed_classes = ["Mage"]),
    Item(name = "Bubble Wrap Coat + 5 HP", cost = 20, stat_bonus = {"hp": 5}, allowed_classes = ["Mage"]),
    Item(name = "Laptop Lid + 5 defense", cost = 20, stat_bonus = {"defense": 5}, allowed_classes = ["Mage"])
]