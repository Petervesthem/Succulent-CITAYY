class StatManager:
    def __init__(self, health, speed, attack_power):
        self.health = health
        self.speed = speed
        self.attack_power = attack_power

    #Makes sure health does not go below 0
    def take_damage(self, amount):
        self.health = max(0, self - amount)
        return self.health

    def increase_speed(self, amount):
        self.speed += amount
        return self.speed        