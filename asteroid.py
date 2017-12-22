from flying_object import FlyingObject

MIN_SIZE = 1
MAX_SIZE = 3
DEF_HEADING = 0
SIZE_COEFFICIENT = 10
NORMALIZER = -5


class Asteroid(FlyingObject):

    def __init__(self, location, speed, heading=DEF_HEADING, size=MAX_SIZE):
        FlyingObject.__init__(location, speed, heading)

        self.size = max(min(size, MAX_SIZE), MIN_SIZE)

    def get_radius(self):
        return SIZE_COEFFICIENT * self.size + NORMALIZER

    def has_intersection(self, obj):
        obj_location = obj.get_location()
        ast_location = self.get_location()
        distance = ((obj_location[0] - ast_location[0]) ** 2
                    + (obj_location[1] - ast_location[1]) ** 2) ** 0.5

        return distance <= self.get_radius() + obj.get_radius()


