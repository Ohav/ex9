X_COORD = 0
Y_COORD = 1


class FlyingObject():
    def __init__(self, location, speed):
        self._speed = speed
        self._location = location

    def move(self, min_screen_size, max_screen_size):
        x_change = max_screen_size[X_COORD] - min_screen_size[X_COORD]
        new_x_coords = (self._speed[X_COORD] + self._location[X_COORD] -
                        min_screen_size[X_COORD]) % x_change + \
                       min_screen_size[X_COORD]
        y_change = max_screen_size[Y_COORD] - min_screen_size[Y_COORD]
        new_y_coords = (self._speed[Y_COORD] + self._location[Y_COORD] -
                        min_screen_size[Y_COORD]) % y_change + \
                       min_screen_size[Y_COORD]
        self._location = (new_x_coords, new_y_coords)

    def get_location(self):
        return self._location

    def get_speed(self):
        return self._speed
