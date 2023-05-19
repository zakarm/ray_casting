class Player:
    def __init__(self, x, y, angle, fov, half_fov):
        self.__x = x
        self.__y = y
        self.__angle = angle
        self.__fov = fov
        self.__half_fov = half_fov

    # getters
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_angle(self):
        return self.__angle

    def get_fov(self):
        return self.__fov

    def get_half_fov(self):
        return self.__half_fov

    # setters
    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_angle(self, angle):
        self.__angle = angle

    def set_fov(self, fov):
        self.__fov = fov

    def set_half_fov(self, half_fov):
        self.__half_fov = half_fov


