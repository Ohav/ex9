from screen import Screen
from ship import Ship
from asteroid import Asteroid
import random
import sys

DEFAULT_ASTEROIDS_NUM = 5
MIN_SPEED = 1
MAX_SPEED = 4
SCORE_TABLE = [20, 50, 100]
LEFT_ANGLE = 7
RIGHT_ANGLE = -7

class GameRunner:

    def __init__(self, asteroids_amnt):
        self._screen = Screen()

        self.screen_max_x = Screen.SCREEN_MAX_X
        self.screen_max_y = Screen.SCREEN_MAX_Y
        self.screen_min_x = Screen.SCREEN_MIN_X
        self.screen_min_y = Screen.SCREEN_MIN_Y

        self.ship = self.create_new_ship()
        self.score = 0
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

    def delete_asteroid(self, asteroid):
        self._screen.unregister_asteroid(asteroid)
        self.asteroids.remove(asteroid)

    def destroy_asteroid(self, asteroid, torpedo):
        ast_size = asteroid.get_size()
        self.score += SCORE_TABLE[-ast_size]
        self._screen.set_score(self.score)
        self.delete_asteroid(asteroid)
        if ast_size > 1:
            torp_speed = torpedo.get_speed()
            ast_speed = asteroid.get_speed()
            new_speed_x = (torp_speed[0] + ast_speed[0]) / \
                        (ast_speed[0] ** 2 + ast_speed[1] ** 2) ** 0.5
            new_speed_y = (torp_speed[1] + ast_speed[1]) / \
                        (ast_speed[0] ** 2 + ast_speed[1] ** 2) ** 0.5
            self.create_smaller_asteroid(asteroid.get_location(),
                                         (new_speed_x, new_speed_y),
                                         ast_size - 1)
            self.create_smaller_asteroid(asteroid.get_location(),
                                         (-new_speed_x, -new_speed_y),
                                         ast_size - 1)

    def create_smaller_asteroid(self, location, speed, size):
        new_asteroid = Asteroid(location, speed, size)
        self.asteroids.append(new_asteroid)
        self._screen.register_asteroid(new_asteroid, size)


    def run(self):
        self._do_loop()
        self._screen.start_screen()

    def check_input(self):
        if self._screen.is_left_pressed():
            self.ship.change_heading(LEFT_ANGLE)
        if self._screen.is_right_pressed():
            self.ship.change_heading(RIGHT_ANGLE)
        if self._screen.is_up_pressed():
            self.ship.accelerate()
        if self._screen.is_space_pressed():
            self.ship.fire_torpedo(self._screen)

    def move_torpedos(self, torpedo_list):
        for torpedo in torpedo_list:
            # drop_lifespan() returns true if the torpedo is expired
            if torpedo.drop_lifespan():
                self.ship.remove_torpedo(self._screen, torpedo)
            else:
                torpedo.move((self.screen_min_x, self.screen_min_y),
                             (self.screen_max_x, self.screen_max_y))
                self._screen.draw_torpedo(torpedo, torpedo.get_location()[0],
                                          torpedo.get_location()[1],
                                          torpedo.get_heading())

    def check_asteroid_collision(self, asteroid):
        """Checks and handles asteroid collisions with other objects.
        If the asteroid survives, moves and draws it to the screen"""
        for torpedo in self.ship.get_torpedoes():
            if asteroid.has_intersection(torpedo):
                self.destroy_asteroid(asteroid, torpedo)
                self.ship.remove_torpedo(self._screen, torpedo)
                return

        if asteroid.has_intersection(self.ship):
            self.ship.lose_life(self._screen)
            self.delete_asteroid(asteroid)
            return

        # This part only happens if the asteroid survived.
        asteroid.move((self.screen_min_x, self.screen_min_y),
                      (self.screen_max_x, self.screen_max_y))
        self._screen.draw_asteroid(asteroid, asteroid.get_location()[0],
                                   asteroid.get_location()[1])

    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self._screen.update()
        self._screen.ontimer(self._do_loop,5)

    def _game_loop(self):
        """Iterates a single tick of the game.
        Checks for collisions, handles user input and moves objects.
        """
        for asteroid in self.asteroids:
            self.check_asteroid_collision(asteroid)
        self.check_input()
        self.move_torpedos(self.ship.get_torpedoes())
        self.ship.move((self.screen_min_x, self.screen_min_y),
                       (self.screen_max_x, self.screen_max_y))
        ship_location = self.ship.get_location()
        self._screen.draw_ship(ship_location[0], ship_location[1],
                               self.ship.get_heading())

def main(amnt):
    runner = GameRunner(amnt)
    runner.run()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main( int( sys.argv[1] ) )
    else:
        main( DEFAULT_ASTEROIDS_NUM )
