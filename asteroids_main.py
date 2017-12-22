from screen import Screen
from ship import Ship
from asteroid import Asteroid
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
        self.asteroids = []
        for i in range(asteroids_amnt):
            new_asteroid = self.create_new_asteroid()
            self._screen.repister_asteroid(new_asteroid, new_asteroid.size)
            self.asteroids += new_asteroid

    def create_new_ship(self):
        random.seed()
        x_location = random.randint(self.screen_min_x, self.screen_max_x)
        y_location = random.randint(self.screen_min_y, self.screen_max_y)
        return Ship((x_location, y_location))

    def create_new_asteroid(self):
        ship_location = self.ship.get_location()
        random.seed()
        x_location = random.randint(self.screen_min_x, self.screen_max_x)
        while x_location == ship_location[0]:
            x_location = random.randint(self.screen_min_x, self.screen_max_x)
        y_location = random.randint(self.screen_min_y, self.screen_max_y)
        while y_location == ship_location[1]:
            y_location = random.randint(self.screen_min_y, self.screen_max_y)
        return Asteroid((x_location, y_location))

    def draw_asteroids(self):
        for asteroid in self.asteroids:
            self._screen.draw_asteroid(asteroid, asteroid.location[0],
                                       asteroid.location[1])

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
        ship_location = self.ship.get_location()
        self._screen.draw_ship(ship_location[0], ship_location[1],
                               self.ship.get_heading())
        self.draw_asteroids()

        pass

def main(amnt):
    runner = GameRunner(amnt)
    runner.run()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main( int( sys.argv[1] ) )
    else:
        main( DEFAULT_ASTEROIDS_NUM )
