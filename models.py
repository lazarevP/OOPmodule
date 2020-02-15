"""
This file include information about Player and Enemy functions
"""
from random import randint

import settings
import exceptions


class Enemy:
    """
    describe everything about enemy
    """

    def __init__(self, level):
        """define enemy level and lives"""
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        """generate random integer"""
        return randint(1, 3)

    def decrease_enemy_lives(self):
        """decreasing method"""
        self.lives -= 1
        if self.lives == 0:
            raise exceptions.EnemyDown


class Player:
    """
    describe everything about player
    """

    def __init__(self, name, your_lives):
        """describe character"""
        self.name = name
        self.your_lives = your_lives

    @staticmethod
    def fight(attack, defence):
        """show the result"""
        if attack == 1:
            if defence == 1:
                result = 0
            elif defence == 2:
                result = 1
            elif defence == 3:
                result = -1
            else:
                result = 404
        elif attack == 2:
            if defence == 1:
                result = -1
            elif defence == 2:
                result = 0
            elif defence == 3:
                result = 1
            else:
                result = 404
        elif attack == 3:
            if defence == 1:
                result = 1
            elif defence == 2:
                result = -1
            elif defence == 3:
                result = 0
            else:
                result = 404
        else:
            result = 404
        return result

    def decrease_lives(self):
        """decreasing lives method"""
        self.your_lives -= 1
        if self.your_lives == 0:
            raise exceptions.GameOver

    def attack(self, enemy_obj):
        """
        attack method
        """
        your_character = int(input("Choose the character for attack:\n"
                                   f"1 - {settings.characters[0]}\n"
                                   f"2 - {settings.characters[1]}\n"
                                   f"3 - {settings.characters[2]}\n"))

        enemy_character = Enemy.select_attack()
        calling_fight_method_for_attack = Player.fight(attack=your_character, defence=enemy_character)

        if calling_fight_method_for_attack == 0:
            print(f'It\'s draw!\nYour current lives is {self.your_lives}')
        elif calling_fight_method_for_attack == 1:
            enemy_obj.decrease_enemy_lives()
            print(f'You attacked successfully!\nYour current lives is {self.your_lives}')
        elif calling_fight_method_for_attack == -1:
            print(f'You missed!\nYour current lives is {self.your_lives}')
        else:
            print("You chose an incorrect number. Pres 1, 2 or 3")

    def defence(self, enemy_obj):
        """
        defence method
        """
        your_character = int(input("Choose the character for attack:\n"
                                   f"1 - {settings.characters[0]}\n"
                                   f"2 - {settings.characters[1]}\n"
                                   f"3 - {settings.characters[2]}\n"))

        enemy_character = enemy_obj.select_attack()
        calling_fight_method_for_defence = Player.fight(attack=enemy_character, defence=your_character)

        if calling_fight_method_for_defence == 0:
            print(f'It\'s draw!\nYour current lives is {self.your_lives}')
        elif calling_fight_method_for_defence == 1:
            self.decrease_lives()
            print(f'Enemy attacked successfully!\nYour current lives is {self.your_lives}')
        elif calling_fight_method_for_defence == -1:
            print(f'Enemy missed!\nYour current lives is {self.your_lives}')
        else:
            print("You chose an incorrect number. Pres 1, 2 or 3")
