import random


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = random.randint(20, 40)

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        turn = 0
        while self.player.is_alive() and self.computer.is_alive():
            if turn % 2 == 0:
                self.player.attack(self.computer)
                print(f"Здоровье {self.computer.name}: {self.computer.health}")
            else:
                self.computer.attack(self.player)
                print(f"Здоровье {self.player.name}: {self.player.health}")
            turn += 1

        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")


# Игровой процесс
player_name = input("Введите имя игрока: ")
game = Game(player_name)
game.start()
