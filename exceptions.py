from OOPmodule import settings
"""exceptions file"""

class GameOver(Exception):
    @staticmethod
    def saving_score_method():
        with open("scores.txt", "a") as scores:
            scores.write(f'{settings.name}, {settings.score}\n')
            scores.close()
            return print("String was added")


class EnemyDown(Exception):
    pass

