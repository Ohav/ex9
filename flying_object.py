class FlyingObject():

    def __init__(self, location, speed, heading):
        self.speed = speed
        self.location = location
        self.heading = heading

    def move(self, min_screen_size, max_screen_size):
        x_change = max_screen_size[0] - min_screen_size[0]
        new_coords_x = (self.speed[0] + self.location[0] - min_screen_size[0]) \
                       % x_change + min_screen_size[0]
        y_change = max_screen_size[1] - min_screen_size[1]
        new_coords_y = (self.speed[1] + self.location[1] - min_screen_size[0]) \
                       % y_change + min_screen_size[1]
        self.location = (new_coords_x, new_coords_y)
