from flying_object import FlyingObject

MIN_SIZE = 1
MAX_SIZE = 3

class Asteroid(FlyingObject):

    def __init__(self, location, speed, heading, size):
        FlyingObject.__init__(location, speed)
        self.heading = heading

        self.size = max(min(size, MAX_SIZE), MIN_SIZE)

