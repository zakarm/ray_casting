class Window:
    def __init__(self, win_h, win_d, size_rec, player_x, player_y):
        self.__win_h = win_h
        self.__win_d = win_d
        self.__size_rec = size_rec
        self.__player_x = player_x
        self.__player_y = player_y

    def get_win_h(self):
        return self.__win_h

    def get_win_d(self):
        return self.__win_d

    def get_size_rec(self):
        return self.__size_rec

    def get_player_x(self):
        return self.__player_x

    def get_player_y(self):
        return self.__player_y

    # setters
    def set_win_h(self, win_h):
        self.__win_h = win_h

    def set_win_f(self, win_d):
        self.__win_d = win_d

    def set_size_rec(self, size_rec):
        self.__size_rec = size_rec

    def set_player_x(self, player_x):
        self.__player_x = player_x

    def set_player_y(self, player_y):
        self.__player_y = player_y
