from ascii import banner, thugg, mr, dead, kev, kar
class Enemy:
    def __init__(self, name, hp, attack, defense, reward_money=0, ascii_art = ""):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.reward_money = reward_money
        self.ascii_art = ascii_art

    def take_damage(self, amount):
        self.hp -= amount 
        print(f"{self.name} takes {amount} damage! ({self.hp} HP left)")
        if self.hp <= 0:
            print(f"{self.name} was defeated!")

# Thug
class Intern(Enemy):
    def __init__(self, level = 1):
        name = "Intern"
        hp = 30 + (level - 1) * 10
        attack = 5 + (level - 1) * 2
        defense = 2 + (level - 1)
        reward_money = 5 + (level - 1) * 2
        super().__init__(name, hp, attack, defense, reward_money, ascii_art = thugg)
        
    def special_attack(self, player):
        damage = max(1, self.attack + 3 - player.defense)
        print(f"{self.name} throws paperclips at {player.name}!")
        player.take_damage(damage)

# Boss 1
class MrClip(Enemy):
    def __init__(self):
        super().__init__("Mr. Clipboard(Team Lead)", hp = 50, attack = 10, defense = 3, reward_money = 20, ascii_art = mr)

    def special_attack(self, player):
        damage = max(0, self.attack + 5 - player.defense)
        print(f"{self.name} smacks {player.name} with his clipboard!")
        player.take_damage(damage)

# Boss 2
class Deadld(Enemy):
    def __init__(self):
        super().__init__("Deadline Dave(Project Manager)", hp = 70, attack = 12, defense = 5, reward_money = 40, ascii_art = dead)

    def special_attack(self, player):
        damage = max(0, self.attack + 5 - player.defense)
        print(f"{self.name} floods {player.name}'s phone with messages!")
        player.take_damage(damage)

# Boss 3
class Kevin(Enemy):
    def __init__(self):
        super().__init__("Kevin(HR Manager)", hp = 90, attack = 15, defense = 7, reward_money = 40, ascii_art = kev)

    def special_attack(self, player):
        damage = max(0, self.attack + 5 - player.defense)
        print(f"{self.name} attacks {player.name} with a formal reprimand!")
        player.take_damage(damage)

# Boss 4
class Karen(Enemy):
    def __init__(self):
        super().__init__("Karen(CEO)", hp = 120, attack = 18, defense = 10, reward_money = 50, ascii_art = kar)

    def special_attack(self, player):
        damage = max(0, self.attack + 5 - player.defense)
        print(f"{self.name} attacks {player.name} with a layoff threat!")
        player.take_damage(damage)