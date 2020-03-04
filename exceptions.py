"""exceptions file"""


class GameOver(Exception):
    @staticmethod
    def saving_score_method(name, score):
        with open("scores.txt", "a") as scores:
            scores.write(f'Player - {name}, score - {score}\n')
            return scores.close()


class EnemyDown(Exception):
    pass

