from flying_object import FlyingObject
import math

DEFAULT_SPEED = (0, 0)
DEFAULT_HEADING = 0
X_COORD = 0
Y_COORD = 1


class Ship(FlyingObject):
    def __init__(self, location, speed=DEFAULT_SPEED,
                 heading=DEFAULT_HEADING):
        super(Ship, self).__init__(speed, location)
        self._heading = heading

    def change_heading(self, angle_to_add):
        self._heading += angle_to_add

    def accelerate(self):
        new_speed_x = self._speed[X_COORD] + math.cos(
            self.get_heading_in_radians())
        new_speed_y = self._speed[y_COORD] + math.sin(
            self.get_heading_in_radians())
        self._heading = (new_speed_x, new_speed_y)

    def get_heading(self):
        return self._heading

    def get_heading_in_radians(self):
        # TODO: Heading should be returned as a tuple.
        return math.radians((self._heading[X_COORD] ** 2 + self._heading[Y_COORD]
                        ** 2) ** 0.5)

    def get_radius(self):
        # TODO: Return the ship's actual radius.
        return 0
