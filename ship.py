from flying_object import FlyingObject
from torpedo import Torpedo
import math

DEFAULT_SPEED = (0, 0)
DEFAULT_HEADING = 0
X_COORD = 0
Y_COORD = 1
SHIP_RADIUS = 1
SHIP_STARTING_LIVES = 3
MAX_TORPEDOES = 15
HIT_ASTEROID_MESSAGE = "You've hit an asteroid and lost 1 life!"
A_CRY_OF_ENCOURAGEMENT = "Keep trying, the entire galaxy's fate depends on " \
                         "you!"
TORPEDO_ACCELERATION_CONSTANT = 2


class Ship(FlyingObject):
    def __init__(self, location, speed=DEFAULT_SPEED,
                 heading=DEFAULT_HEADING):
        super().__init__(location, speed)
        self._heading = heading
        self._radius = SHIP_RADIUS
        self._lives = SHIP_STARTING_LIVES
        self._torpedoes = []

    def change_heading(self, angle_to_add):
        self._heading += angle_to_add

    def accelerate(self):
        new_speed_x = self._speed[X_COORD] + math.cos(
            math.radians(self._heading))
        new_speed_y = self._speed[Y_COORD] + math.sin(
            math.radians(self._heading))
        self._speed = (new_speed_x, new_speed_y)

    def get_heading(self):
        return self._heading

    def get_radius(self):
        return self._radius

    def lose_life(self, screen):
        self._lives -= 1
        screen.remove_life()
        screen.show_message(HIT_ASTEROID_MESSAGE, A_CRY_OF_ENCOURAGEMENT)

    def calc_torpedo_speed(self):
        torpedo_speed_x = self._speed[X_COORD] + \
                          TORPEDO_ACCELERATION_CONSTANT * math.cos(
                              math.radians(self._heading))
        torpedo_speed_y = self._speed[Y_COORD] + \
                          TORPEDO_ACCELERATION_CONSTANT * math.sin(
                              math.radians(self._heading))
        return torpedo_speed_x, torpedo_speed_y

    def fire_torpedo(self, screen):
        if len(self._torpedoes) >= MAX_TORPEDOES:
            pass
        else:
            torpedo = Torpedo(self._location, self.calc_torpedo_speed(),
                              self._heading)
            self._torpedoes.append(torpedo)
            screen.register_torpedo(torpedo)

    def remove_torpedo(self, screen, torpedo):
        self._torpedoes.remove(torpedo)
        screen.unregister_torpedo(torpedo)

    def get_torpedoes(self):
        return self._torpedoes

    def check_torpedoes(self, screen):
        for torpedo in self._torpedoes:
            torpedo.drop_lifespan()
            if torpedo.get_lifspan() == 0:
                self.remove_torpedo(screen, torpedo)
