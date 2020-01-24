from OOPmodule import exceptions
from OOPmodule import settings
from OOPmodule import models
"""
this file contain the maine information 
"""


def play():
    """
    play function
    """
    settings.name = input("Enter your name ")

    while settings.start != "start":
        settings.start = input("Enter 'start' for the beginning\n")

    player = models.Player(settings.name, settings.your_lives, settings.score)
    enemy = models.Enemy(settings.level)
    while True:
        try:
            models.Player.attack(player, enemy)
            models.Player.defence(player, enemy)
        except exceptions.EnemyDown:
            settings.score += 5
            print(f"Enemy number {settings.level} defeated\nYour current score is {settings.score}")
            settings.level += 1
            enemy = models.Enemy(settings.level)


def main():
    """
    Maine function
    """
    try:
        play()
    except exceptions.GameOver:
        exceptions.GameOver.saving_score_method()
        print(f"Game over, mr.{settings.name}\nYour score is {settings.score}")
    except KeyboardInterrupt:
        pass
    finally:
        print("Good bye")


if __name__ == '__main__':
    main()

