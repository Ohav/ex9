from flying_object import FlyingObject

TORPEDO_RADIUS = 4
TORPEDO_STARTING_LIFESPAN = 200


class Torpedo(FlyingObject):
    def __init__(self, location, speed, heading):
        super().__init__(location, speed)
        self._heading = heading
        self._radius = TORPEDO_RADIUS
        self._lifespan_left = TORPEDO_STARTING_LIFESPAN

    def drop_lifespan(self):
        self._lifespan_left -= 1

    def get_lifspan(self):
        return self._lifespan_left