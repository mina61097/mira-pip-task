from abc import ABC, abstractmethod
import random

# =========================================
# Abstract Base Class
# =========================================

class GameCharacter(ABC):

    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    @abstractmethod
    def attack(self, other):
        pass

    @abstractmethod
    def defend(self, damage):
        pass

    def is_alive(self):
        return self.health > 0


# =========================================
# Subclasses
# =========================================

class Warrior(GameCharacter):

    def attack(self, other):
        damage = random.randint(15, 25)
        print(f"{self.name} slashes {other.name} for {damage} damage!")
        other.defend(damage)

    def defend(self, damage):
        reduced = int(damage * 0.7)  # Warrior reduces damage by 30%
        self.health -= reduced
        print(f"{self.name} blocks! Health reduced by {reduced}, current health: {self.health}")


class Mage(GameCharacter):

    def attack(self, other):
        damage = random.randint(20, 30)
        print(f"{self.name} casts a spell on {other.name} for {damage} damage!")
        other.defend(damage)

    def defend(self, damage):
        reduced = int(damage * 0.8)  # Mage reduces damage by 20%
        self.health -= reduced
        print(f"{self.name} uses magic shield! Health reduced by {reduced}, current health: {self.health}")


class Archer(GameCharacter):

    def attack(self, other):
        damage = random.randint(10, 35)
        print(f"{self.name} shoots an arrow at {other.name} for {damage} damage!")
        other.defend(damage)

    def defend(self, damage):
        reduced = int(damage * 0.9)  # Archer reduces damage by 10%
        self.health -= reduced
        print(f"{self.name} dodges! Health reduced by {reduced}, current health: {self.health}")


# =========================================
# Battle Simulation
# =========================================

def simulate_battle(characters):
    if not characters:
        print("No characters to battle!")
        return

    print("\n--- Battle Start ---")
    alive_chars = [c for c in characters if c.is_alive()]

    # simple round-robin battle: each character attacks next one
    while len([c for c in alive_chars if c.is_alive()]) > 1:
        for i, attacker in enumerate(alive_chars):
            if not attacker.is_alive():
                continue
            # target is next alive character
            targets = [c for c in alive_chars if c.is_alive() and c != attacker]
            if not targets:
                break
            target = random.choice(targets)
            attacker.attack(target)
        alive_chars = [c for c in alive_chars if c.is_alive()]

    print("\n--- Battle Over ---")
    for c in alive_chars:
        print(f"{c.name} survives with {c.health} health!")


# =========================================
# Menu and Character Creation
# =========================================

def create_character():
    print("\nChoose character type:")
    print("1 - Warrior")
    print("2 - Mage")
    print("3 - Archer")

    choice = input("Choice: ")
    name = input("Enter character name: ")

    if choice == "1":
        return Warrior(name)
    elif choice == "2":
        return Mage(name)
    elif choice == "3":
        return Archer(name)
    else:
        raise ValueError("Invalid character type")


def main():
    characters = []

    while True:
        print("\n===== Game Menu =====")
        print("1 - Create Character")
        print("2 - Simulate Battle")
        print("0 - Exit")

        try:
            choice = input("Enter choice: ")

            if choice == "1":
                character = create_character()
                characters.append(character)
                print(f"{character.name} created!")

            elif choice == "2":
                simulate_battle(characters)

            elif choice == "0":
                break

            else:
                print("Invalid menu choice. Try again.")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
