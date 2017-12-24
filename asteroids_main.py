from screen import Screen
from ship import Ship
from asteroid import Asteroid
import random
import sys

DEFAULT_ASTEROIDS_NUM = 5
MIN_SPEED = 1
MAX_SPEED = 4

class GameRunner:
    RIGHT_ANGLE = 7
    LEFT_ANGLE = -7

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
            self._screen.register_asteroid(new_asteroid, new_asteroid.size)
            self.asteroids.append(new_asteroid)

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
        speed = (random.randint(MIN_SPEED, MAX_SPEED),
                 random.randint(MIN_SPEED, MAX_SPEED))
        return Asteroid((x_location, y_location), speed)

    def draw_asteroids(self):
        for asteroid in self.asteroids:
            self._screen.draw_asteroid(asteroid, asteroid.get_location()[0],
                                       asteroid.get_location()[1])

    def destroy_asteroid(self, asteroid):
        self._screen.unregister_asteroid(asteroid)
        self.asteroids.remove(asteroid)

    def run(self):
        self._do_loop()
        self._screen.start_screen()

    def check_input(self):
        if self._screen.is_left_pressed():
            self.ship.change_heading(self.LEFT_ANGLE)
        if self._screen.is_right_pressed():
            self.ship.change_heading(self.RIGHT_ANGLE)
        if self._screen.is_up_pressed():
            self.ship.accelerate()
        if self._screen.is_space_pressed():
            # TODO: Add torpedo launch here.
            print('nothing for now')

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
        for asteroid in self.asteroids:
            if asteroid.has_intersection(self.ship):
                self.ship.lose_life(self._screen)
                self.destroy_asteroid(asteroid)
            asteroid.move((self.screen_min_x, self.screen_min_y),
                          (self.screen_max_x, self.screen_max_y))
        self.check_input()
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
