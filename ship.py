from flying_object import FlyingObject

DEFAULT_SPEED = (0, 0)
DEFAULT_HEADING = 0


class Ship(FlyingObject):

    def __init__(self, location, speed=DEFAULT_SPEED, heading=DEFAULT_HEADING):
        FlyingObject.__init__(speed, location, heading)

