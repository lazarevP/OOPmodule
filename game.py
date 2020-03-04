import exceptions
import settings
import models
"""
this file contain the maine information 
"""
score = 0
name = input("Enter your name: ")


def play():
    """
    play function
    """
    global score
    start = None
    while start != "start":
        start = input("Enter 'start' for the beginning\n")

    player = models.Player(name, settings.your_lives)
    enemy = models.Enemy(settings.level)
    while True:
        try:
            models.Player.attack(player, enemy)
            models.Player.defence(player, enemy)
        except exceptions.EnemyDown:
            score += 5
            print(f"Enemy number {settings.level} defeated\nYour current score is {score}")
            settings.level += 1
            enemy = models.Enemy(settings.level)


def main():
    """
    Maine function
    """
    try:
        play()
    except exceptions.GameOver:
        exceptions.GameOver.saving_score_method(name, score)
        print(f"Game over, {name}\nYour score is {score}")
    except KeyboardInterrupt:
        pass
    finally:
        print("Good bye")


if __name__ == '__main__':
    main()

