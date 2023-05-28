from abc import ABC, abstractmethod

# Abstract class representing the Character
class Character(ABC):
    def __init__(self, weapon_behavior):
        self.weapon_behavior = weapon_behavior

    @abstractmethod
    def fight(self):
        pass

# Interface representing the Weapon Behavior
class WeaponBehavior(ABC):
    @abstractmethod
    def use_weapon(self):
        pass


class KnifeBehavior(WeaponBehavior):
    def use_weapon(self):
        print("Using a knife.")


class BowAndArrowBehavior(WeaponBehavior):
    def use_weapon(self):
        print("Using a bow and arrow.")


class AxeBehavior(WeaponBehavior):
    def use_weapon(self):
        print("Using an axe.")


class SwordBehavior(WeaponBehavior):
    def use_weapon(self):
        print("Using a sword.")


class Queen(Character):
    def fight(self):
        if self.weapon_behavior:
            self.weapon_behavior.use_weapon()
        else:
            print("No weapon set for this character.")


class King(Character):
    def fight(self):
        if self.weapon_behavior:
            self.weapon_behavior.use_weapon()
        else:
            print("No weapon set for this character.")


class Knight(Character):
    def fight(self):
        if self.weapon_behavior:
            self.weapon_behavior.use_weapon()
        else:
            print("No weapon set for this character.")


class Trool(Character):
    def fight(self):
        if self.weapon_behavior:
            self.weapon_behavior.use_weapon()
        else:
            print("No weapon set for this character.")


knife_behavior = KnifeBehavior()
queen = Queen(knife_behavior)
queen.fight()

bow_arrow_behavior = BowAndArrowBehavior()
knight = Knight(bow_arrow_behavior)
knight.fight()

king = King(None)
king.fight()
