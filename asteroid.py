from flying_object import FlyingObject

MIN_SIZE = 1
MAX_SIZE = 3
SIZE_COEFFICIENT = 10
NORMALIZER = -5
X_COORD = 0
Y_COORD = 1


class Asteroid(FlyingObject):
    def __init__(self, location, speed, size=MAX_SIZE):
        FlyingObject.__init__(self, location, speed)

        self.size = max(min(size, MAX_SIZE), MIN_SIZE)
        self._radius = SIZE_COEFFICIENT * self.size + NORMALIZER

    def get_radius(self):
        return self._radius

    def has_intersection(self, obj):
        obj_location = obj.get_location()
        ast_location = self.get_location()
        distance = ((obj_location[X_COORD] - ast_location[X_COORD]) ** 2
                    + (obj_location[Y_COORD] - ast_location[
                        Y_COORD]) ** 2) ** 0.5

        return distance <= self.get_radius() + obj.get_radius()

