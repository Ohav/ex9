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
NO_MORE_LIVES = 0


class Ship(FlyingObject):
    def __init__(self, location, speed=DEFAULT_SPEED, heading=DEFAULT_HEADING):
        """Creates a new object of the type Ship"""
        super().__init__(location, speed)
        self._heading = heading
        self._radius = SHIP_RADIUS
        self._lives = SHIP_STARTING_LIVES
        self._torpedoes = []

    def change_heading(self, angle_to_add):
        """Adds the given angle to the ship's heading"""
        self._heading += angle_to_add

    def accelerate(self):
        """Increases the ship's speed according to it's current heading."""
        new_speed_x = self._speed[X_COORD] + math.cos(
            math.radians(self._heading))
        new_speed_y = self._speed[Y_COORD] + math.sin(
            math.radians(self._heading))
        self._speed = (new_speed_x, new_speed_y)

    def get_heading(self):
        """Returns the ship's current heading. (In degrees)"""
        return self._heading

    def get_radius(self):
        """Returns the ship's radius."""
        return self._radius

    def lose_life(self, screen):
        """Lowers the ship's life total by one."""
        self._lives -= 1
        if self._lives == NO_MORE_LIVES:
            return True
        screen.remove_life()
        screen.show_message(HIT_ASTEROID_MESSAGE, A_CRY_OF_ENCOURAGEMENT)

    def get_lives(self):
        return self._lives

    def calc_torpedo_speed(self):
        """Calculates a new torpedo's speed, according to the ship's current
        heading and speed.
        """
        torpedo_speed_x = self._speed[X_COORD] + \
                          TORPEDO_ACCELERATION_CONSTANT * math.cos(
                              math.radians(self._heading))
        torpedo_speed_y = self._speed[Y_COORD] + \
                          TORPEDO_ACCELERATION_CONSTANT * math.sin(
                              math.radians(self._heading))
        return torpedo_speed_x, torpedo_speed_y

    def fire_torpedo(self, screen):
        """Fires a new torpedo."""
        # There's a set max number of torpedoes we can have out at a time.
        if len(self._torpedoes) < MAX_TORPEDOES:
            torpedo = Torpedo(self._location, self.calc_torpedo_speed(),
                              self._heading)
            self._torpedoes.append(torpedo)
            screen.register_torpedo(torpedo)

    def get_torpedoes(self):
        """Returns a list contains all of the torpedoes fired by the ship
        that are still active.
        """
        return self._torpedoes

    def check_torpedoes(self, screen):
        """Checks the status of each of the ship's torpedoes, and destroys them
        if they have expired.
        Else, the method moves and draws them to the screen.
        """
        for torpedo in self._torpedoes:
            if torpedo.drop_lifespan():
                self.remove_torpedo(screen, torpedo)
            else:
                torpedo.move((screen.screen_min_x, screen.screen_min_y),
                             (screen.screen_max_x, screen.screen_max_y))
                screen.draw_torpedo(torpedo, torpedo.get_location()[0],
                                    torpedo.get_location()[1],
                                    torpedo.get_heading())

    def remove_torpedo(self, screen, torpedo):
        """Removes a given torpedo from the ship's list of torpedoes."""
        self._torpedoes.remove(torpedo)
        screen.unregister_torpedo(torpedo)
