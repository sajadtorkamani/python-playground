class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def is_alive(self):
        return self.health > 0

    def is_dead(self):
        return self.health <= 0

    def attack(self, opponent):
        opponent.take_damage(self)

    def take_damage(self, opponent):
        self.health -= opponent.damage_per_attack

    def __str__(self):
        return self.name


def declare_winner(fighter_a, fighter_b, first_fighter_name):
    if fighter_a.name == first_fighter_name:
        first_fighter, second_fighter = [fighter_a, fighter_b]
    else:
        first_fighter, second_fighter = [fighter_b, fighter_a]

    while True:
        first_fighter.attack(second_fighter)
        if second_fighter.is_dead():
            return first_fighter.name

        second_fighter.attack(first_fighter)
        if first_fighter.is_dead():
            return second_fighter.name

