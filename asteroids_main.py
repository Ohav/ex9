from screen import Screen
from ship import Ship
import random
import sys

DEFAULT_ASTEROIDS_NUM = 5

class GameRunner:

    def __init__(self, asteroids_amnt):
        self._screen = Screen()

        self.screen_max_x = Screen.SCREEN_MAX_X
        self.screen_max_y = Screen.SCREEN_MAX_Y
        self.screen_min_x = Screen.SCREEN_MIN_X
        self.screen_min_y = Screen.SCREEN_MIN_Y

        self.ship = self.create_new_ship()

    def create_new_ship(self):
        random.seed()
        x_location = random.randint(self.screen_min_x, self.screen_max_x)
        y_location = random.randint(self.screen_min_y, self.screen_max_y)
        return Ship((x_location, y_location))

    def create_new_asteroids(selfs):
        random.seed()


    def run(self):
        self._do_loop()
        self._screen.start_screen()

    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self._screen.update()
        self._screen.ontimer(self._do_loop,5)

    def _game_loop(self):
        '''
        Your code goes here!
        '''
        self._screen.draw_ship(100, 100, 150)

        pass

def main(amnt):
    runner = GameRunner(amnt)
    runner.run()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main( int( sys.argv[1] ) )
    else:
        main( DEFAULT_ASTEROIDS_NUM )
