import random
class Character:
    def __init__(self, name, health, attack_power, defense, speed):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power
        self.defense = defense
        self.speed = speed

    def take_damage(self, amount):
            damage = max(1, amount - self.defense)
            self.health -= damage
            return damage

    def is_alive(self):
             return self.health > 0

    def attack(self, target):
            damage = self.attack_power
            target.take_damage(damage)


class Warrior(Character):
    def __init__(self, name, health, attack_power, defense, speed):
        super().__init__(name, health, attack_power, defense, speed)
        self.rage = 0


    def attack(self, target):
        if self.health < 0.30 * self.max_health:
            damage = self.attack_power * 2
            print(self.name, "enters Berserk Mode!")
        else:
            damage = self.attack_power

        return target.take_damage(damage)
    


class Mage(Character):
            def __init__(self, name, health, attack_power, defense, speed):
                super().__init__(name, health, attack_power, defense, speed)
                self.mana = 100
                #why def + super because the child wants to add something extra
                # super means it tells parensts you also do your parts

            def attack(self, target):
                if self.mana >= 30:
                    damage = self.attack_power * 1.5
                    self.mana -= 30
                    self.health -= 5

                    actual_damage = target.take_damage(damage)

                    print(self.name, "casts Fireball!")
                    return actual_damage

                else:
                    damage = self.attack_power
                    actual_damage = target.take_damage(damage)

                    print(self.name, "does a normal attack!")
                    return actual_damage




class Archer(Character):
            def __init__(self, name, health, attack_power, defense, speed):
                super().__init__(name, health, attack_power, defense, speed)
                self.critical_chance = 0.30

            def attack(self, target):
                if random.random() < self.critical_chance:
                    damage = self.attack_power * 2
                    actual_damage = target.take_damage(damage)

                    print(self.name, "lands a Critical Hit!")
                    return actual_damage

                else:
                    damage = self.attack_power
                    actual_damage = target.take_damage(damage)

                    print(self.name, "shoots an arrow!")
                    return actual_damage

warrior = Warrior("Thor", 130, 22, 12, 6)
mage = Mage("Gandalf", 90, 30, 5, 8)
archer = Archer("Alex", 100, 24, 7, 12)
print(warrior.name, warrior.health, warrior.rage)
print(mage.name, mage.health, mage.mana)
print(archer.name, archer.health, archer.critical_chance)

fighters = [warrior, mage, archer]

fighters.sort(key=lambda fighter: fighter.speed, reverse=True)

print("Turn Order:")
for fighter in fighters:
    print(fighter.name, "-", fighter.speed)



round_number = 1

while True:

  
    alive_count = 0

    for fighter in fighters:
        if fighter.is_alive():
            alive_count += 1

    if alive_count <= 1:
        break

    print("\n--- Round", round_number, "---")

    for fighter in fighters:

        
        if not fighter.is_alive():
            continue

        
        target = None

        for other in fighters:
            if other != fighter and other.is_alive():
                target = other
                break

        
        if target is not None:
            damage = fighter.attack(target)
            print(target.name, "has", target.health, "HP left")

            if not target.is_alive():
                print(target.name, "has been defeated!")

    round_number += 1



for fighter in fighters:
    if fighter.is_alive():
        print("\n", fighter.name, "wins the battle!")
        break