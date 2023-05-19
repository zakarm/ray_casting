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

x_player = int((WIN_H / 2) // 2)
y_player = int((WIN_D / 2) // 2)
FOV = math.pi / 3
HALF_FOV = FOV / 3
ANGLE = math.pi
CASTED_RAYS = 120
STEP_ANGLE = FOV / CASTED_RAYS
MAX_DEPTH = int(12 * size_rec)

def draw_player(win):
    pygame.draw.circle(win, (255, 0, 0), (x_player, y_player), 8)


def draw_lines(win):
    pygame.draw.line(win, (255, 0, 0), (x_player, y_player),
                     (x_player - int(math.sin(ANGLE) * size_rec),
                      y_player + int(math.cos(ANGLE) * size_rec)), 3)
    pygame.draw.line(win, (255, 0, 0), (x_player, y_player),
                     (x_player - int(math.sin(ANGLE - HALF_FOV) * size_rec),
                      y_player + int(math.cos(ANGLE - HALF_FOV) * size_rec)), 3)
    pygame.draw.line(win, (255, 0, 0), (x_player, y_player),
                     (x_player - int(math.sin(ANGLE + HALF_FOV) * size_rec),
                      y_player + int(math.cos(ANGLE + HALF_FOV) * size_rec)), 3)


def map_getter(win):
    for i, row in enumerate(map_data):
        for j, cell in enumerate(row):
            color = (255, 255, 255)
            color1 = (100, 100, 100)
            pygame.draw.rect(win, color if cell == "#" else color1, pygame.Rect(size_rec * j, size_rec * i,
                                                                                 size_rec - 2, size_rec - 2))
    draw_player(win)
    draw_lines(win)


def key_press():
    global ANGLE
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ANGLE -= 0.1
    elif keys[pygame.K_RIGHT]:
        ANGLE += 0.1
    elif keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit(0)


def ray_casting_algo(win):
    START_ANGLE = ANGLE - HALF_FOV
    for r in range(CASTED_RAYS):
        for d in range(MAX_DEPTH):
            target_x = x_player - math.sin(START_ANGLE) * d
            target_y = y_player + math.cos(START_ANGLE) * d
            j = int(target_x / size_rec)
            i = int(target_y / size_rec)
            # (target_y / size_rec) * 12 + target_x / 12
            if map_data[i][j] == "#":
                pygame.draw.rect(win, (255, 0, 0), (j * size_rec, i * size_rec, size_rec - 2, size_rec - 2))
                pygame.draw.line(win, (255, 0, 0), (x_player, y_player), (target_x, target_y), 3)
                break

        START_ANGLE += STEP_ANGLE


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
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, WIN_H, WIN_D))
        map_getter(screen)
        ray_casting_algo(screen)
        key_press()
        pygame.display.flip()
        fps.tick(30)


if __name__ == "__main__":
    main()
