import pygame
from User import User
import math
import sys

WIN_H = 100 * 12
WIN_D = 100 * 12
size_rec = 100
map_data = [
    "############",
    "#   #   #  #",
    "#   #    # #",
    "#   #   ## #",
    "#   #   ## #",
    "#   #    # #",
    "#   #      #",
    "#   #   ## #",
    "#   #   ## #",
    "#       ## #",
    "#    #   # #",
    "############",
]

x_player = (WIN_H / 2) // 2
y_player = (WIN_D / 2) // 2


def draw_player(win):
    pygame.draw.circle(win, (255, 0, 0), (x_player, y_player), 12)


def draw_line(win):
    pygame.draw.line(win, (255, 0, 0), (x_player, y_player), (x_player + math.sin(x_player) * 1.2,
                                                              (y_player + math.cos(y_player)) * 1.2), 3)


def map_getter(win):
    for i, row in enumerate(map_data):
        for j, cell in enumerate(row):
            color = (255, 255, 255)
            color1 = (100, 100, 100)
            pygame.draw.rect(win, color if cell == "#" else color1, pygame.Rect(size_rec * j, size_rec * i,
                                                                                 size_rec - 2, size_rec - 2))
    draw_player(win)
    draw_line(win)


def main():
    print("------ RayCasting Using PyGame -------")
    obj = User(
            input("Type Username : "),
            input("Type firstname : "),
            input("Type lastname : "),
        )
    pygame.init()
    screen = pygame.display.set_mode((WIN_H, WIN_D))
    pygame.display.set_caption("RayCasting " + obj.get_username() +
                               "[" + obj.get_firstname() + " " + obj.get_lastname() + "]")
    fps = pygame.time.Clock()
    status = True
    while status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False
        map_getter(screen)
        pygame.display.flip()
        fps.tick(30)


if __name__ == "__main__":
    main()
