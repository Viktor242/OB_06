# Задание: Разработать консольную игру "Битва героев" на Python с использованием классов и разработать
# план проекта по этапам/или создать kanban доску для работы над данным проектом
# общее описание:Создайте простую текстовую боевую игру, где игрок и компьютер управляют героями с
# различными характеристиками. Игра состоит из раундов, в каждом раунде игроки по очереди наносят урон
# друг другу, пока у одного из героев не закончится здоровье.

# Требования:
# Используйте ООП (Объектно-Ориентированное Программирование) для создания классов героев.
# Игра должна быть реализована как консольное приложение.

# Классы:
# Класс Hero:
# Атрибуты:
# Имя (name)
# Здоровье (health), начальное значение 100
# Сила удара (attack_power), начальное значение 20

# Методы:
# attack(other): атакует другого героя (other), отнимая здоровье в размере своей силы удара
# is_alive(): возвращает True, если здоровье героя больше 0, иначе False

# Класс Game:
# Атрибуты:
# Игрок (player), экземпляр класса Hero
# Компьютер (computer), экземпляр класса Hero

# Методы:
# start(): начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет.
# Выводит информацию о каждом ходе (кто атаковал и сколько здоровья осталось у противника) и
# объявляет победителя.

import random

# Реализовать классы Hero с атрибутами name, health, attack_power
# Реализовать методы attack (other) для Hero
# Реализовать методы is_alive для Hero
# Реализовать класс Game

class Hero:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = random.randint(100, 200)
        self.attack_power = random.randint(20, 50)

        print(f"Имя: {self.name}, Здоровье: {self.health}, Сила удара: {self.attack_power}")

    def attack(self, other):
        other.health -= self.attack_power

    def is_alive(self):
        return self.health > 0

# реализовать метод start в классе Game
# реализовать пошаговый бой между игроком и компьютером
# добавить вывод статуса после каждого хода
# реализовать проверку здоровья игрока и компьютера


class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        round_number = 1
        while self.player.is_alive() and self.computer.is_alive():
            print(f"\n=== Раунд {round_number} ===")
            self.player.attack(self.computer)
            print(f"{self.player.name} атакует {self.computer.name}, осталось {self.computer.health} здоровья")
            if self.computer.is_alive():
                self.computer.attack(self.player)
                print(f"{self.computer.name} атакует {self.player.name}, осталось {self.player.health} здоровья")

            round_number += 1

        # Проверка победы
        if self.player.is_alive():
            print(f"Победил {self.player.name}, здоровье: {self.player.health}")
        else:
            print(f"Победил {self.computer.name}", f"здоровье: {self.computer.health}")


player = Hero("Игрок", 0, 0)
computer = Hero("Компьютер", 0, 0)

game = Game(player, computer)
game.start()

