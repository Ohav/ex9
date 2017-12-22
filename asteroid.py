from flying_object import FlyingObject

MIN_SIZE = 1
MAX_SIZE = 3
DEF_HEADING = 0

class Asteroid(FlyingObject):

    def __init__(self, location, speed, heading=DEF_HEADING, size=MAX_SIZE):
        FlyingObject.__init__(location, speed, heading)

        self.size = max(min(size, MAX_SIZE), MIN_SIZE)

