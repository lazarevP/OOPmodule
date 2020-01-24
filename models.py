"""
This file include information about Player and Enemy functions
"""
from random import randint

from OOPmodule import settings
from OOPmodule import exceptions


class Enemy:
    """
    describe everything about enemy
    """
    def __init__(self, level):
        self.level = level
    """define level"""

    @staticmethod
    def select_attack():
        return randint(1, 3)
    """generate random integer"""

    def decrease_enemy_lives(self):
        self.level -= 1
        if self.level == 0:
            raise exceptions.EnemyDown
    """decreasing method"""


class Player:
    def __init__(self, name, your_lives, score):
        self.name = name
        self.your_lives = your_lives
        self.score = score
        """describe character"""

    @staticmethod
    def fight(attack, defence):
        if attack == 1:
            if defence == 1:
                result = 0
            elif defence == 2:
                result = 1
            else:
                result = -1
        elif attack == 2:
            if defence == 1:
                result = -1
            elif defence == 2:
                result = 0
            else:
                result = 1
        else:
            if defence == 1:
                result = 1
            elif defence == 2:
                result = -1
            else:
                result = 0
        return result
    """show the resul"""

    def decrease_lives(self):
        self.your_lives -= 1
        if self.your_lives == 0:
            raise exceptions.GameOver

    def attack(self, enemy_obj):
        """
        attack method
        """
        your_character = input("Choose the character for attack:\n"
                               f"1 - {settings.characters[0]}\n"
                               f"2 - {settings.characters[1]}\n"
                               f"3 - {settings.characters[2]}\n")

        enemy_character = Enemy.select_attack()

        if self.fight(attack=your_character, defence=enemy_character) == 0:
            print(f'It\'s draw!\nYou current score is {settings.score}\nYour current lives is {self.your_lives}')
        elif self.fight(attack=your_character, defence=enemy_character) == 1:
            enemy_obj.decrease_enemy_lives()
            print(f'You attacked successfully!\nYou current score is {settings.score}\n'
                  f'Your current lives is {self.your_lives}')
        else:
            print(f'You missed!\nYou current score is {settings.score}\nYour current lives is {self.your_lives}')

    def defence(self, enemy_obj):
        """
        defence method
        """
        your_character = input("Choose the character for defence:\n"
                               f"1 - {settings.characters[0]}\n"
                               f"2 - {settings.characters[1]}\n"
                               f"3 - {settings.characters[2]}\n")

        enemy_character = enemy_obj.select_attack()

        if self.fight(attack=enemy_character, defence=your_character) == 0:
            print(f'It\'s draw!\nYou current score is {settings.score}\nYour current lives is {self.your_lives}')
        elif self.fight(attack=enemy_character, defence=your_character) == 1:
            self.decrease_lives()
            print(f'Enemy attacked successfully!\nYou current score is {settings.score}\n'
                  f'Your current lives is {self.your_lives}')
        else:
            print(f'Enemy missed!\nYou current score is {settings.score}\nYour current lives is {self.your_lives}')
