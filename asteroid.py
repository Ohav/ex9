from flying_object import FlyingObject

MIN_SIZE = 1
MAX_SIZE = 3
SIZE_COEFFICIENT = 10
NORMALIZER = -5
X_COORD = 0
Y_COORD = 1


class Asteroid(FlyingObject):
    def __init__(self, location, speed, size=MAX_SIZE):
        """Creates a new Asteroid object"""
        FlyingObject.__init__(self, location, speed)

        self._size = max(min(size, MAX_SIZE), MIN_SIZE)

        # An asteroids radius is calculated by this formula. The size of a
        # given asteroid shouldn't change, so we calculate once.
        self._radius = SIZE_COEFFICIENT * self._size + NORMALIZER

    def get_radius(self):
        """Returns the asteroid's radius"""
        return self._radius

    def get_size(self):
        """Returns the asteroid's size."""
        return self._size

    def has_intersection(self, obj):
        """Returns true if the asteroid is intersecting with the object.
        Object must have a radius.
        """
        obj_location = obj.get_location()
        ast_location = self.get_location()
        distance = ((obj_location[X_COORD] - ast_location[X_COORD]) ** 2
                    + (obj_location[Y_COORD] - ast_location[Y_COORD]) ** 2)\
            ** 0.5

        return distance <= self.get_radius() + obj.get_radius()



