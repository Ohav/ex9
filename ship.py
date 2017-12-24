from flying_object import FlyingObject
import math

DEFAULT_SPEED = (0, 0)
DEFAULT_HEADING = 0
X_COORD = 0
Y_COORD = 1
SHIP_RADIUS = 1
SHIP_LIVES = 3


class Ship(FlyingObject):
    def __init__(self, location, speed=DEFAULT_SPEED,
                 heading=DEFAULT_HEADING):
        super().__init__(location, speed)
        self._heading = heading
        self._radius = SHIP_RADIUS
        self._lives = SHIP_LIVES

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
        return SHIP_RADIUS
