import os

# clear screen helper function
def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

# wait for input helper function
def wait():
    input("Press any key")

# Player Class
class Player:
    def __init__(self, name, hp, attack, defense, money = 0, inventory = None):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.money = money
        self.inventory = inventory or []

    def take_damage(self, amount):
        self.hp -= amount
        print(f"{self.name} takes {amount} damage! ({self.hp} HP left)")
        if self.hp <= 0:
            print(f"{self.name} died on the coffee stained floor.")

# Subclass Warrior
class Warrior(Player):
    def __init__(self, name="Office Warrior"):
        super().__init__(name, hp = 100, attack = 15, defense = 10)
        self.special_cooldown = 0
       
    def special_attack(self, enemy):
        if self.special_cooldown > 0:
            print(f"Special attack not ready yet! (Ready in {self.special_cooldown} rounds.)")
            wait()
            return False

        damage = self.attack + 5
        print(f"{self.name} throws an office chair at {enemy.name} causing {damage} damage.")
        wait()
        enemy.take_damage(damage)
        self.special_cooldown = 4
        return True

    def reduce_cooldown(self):
        if self.special_cooldown > 0:
            self.special_cooldown -= 1

# Subclass Mage
class Mage(Player):
    def __init__(self, name="Mage"):
        super().__init__(name, hp = 70, attack = 20, defense = 5)
        self.special_cooldown = 0
       
    def special_attack(self, enemy):
        if self.special_cooldown > 0:
            print(f"Special attack not ready yet! (Ready in {self.special_cooldown} rounds.)")
            wait()
            return False

        damage = self.attack + 5
        print(f"{self.name} Throws a scalding hot coffee mug at {enemy.name} causing {damage} damage.")
        wait()
        enemy.take_damage(damage)
        self.special_cooldown = 4
        return True

    def reduce_cooldown(self):
        if self.special_cooldown > 0:
            self.special_cooldown -= 1