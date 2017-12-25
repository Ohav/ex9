from flying_object import FlyingObject

TORPEDO_RADIUS = 4
TORPEDO_STARTING_LIFESPAN = 200


class Torpedo(FlyingObject):
    def __init__(self, location, speed, heading):
        """Creates a new Torpedo object."""
        super().__init__(location, speed)
        self._heading = heading
        self._radius = TORPEDO_RADIUS
        self._lifespan_left = TORPEDO_STARTING_LIFESPAN

    def drop_lifespan(self):
        """Lowers the torpedo's lifespan by one. Returns true if the lifespan
        is now 0."""
        self._lifespan_left -= 1
        return self._lifespan_left == 0

    def get_lifespan(self):
        """Returns the current lifetime left for the torpedo."""
        return self._lifespan_left

    def get_heading(self):
        """Returns the torpedo's current heading (in degrees)"""
        return self._heading

    def get_radius(self):
        """Returns the torpedo's radius"""
        return self._radius
