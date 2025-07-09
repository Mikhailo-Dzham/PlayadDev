import pygame as pg

SCREEN_SIZE = 0.5
X_SIZE = int(1536 * SCREEN_SIZE)
Y_SIZE = int(1024 * SCREEN_SIZE)


pg.init()
screen = pg.display.set_mode((X_SIZE, Y_SIZE))
pg.display.set_caption("t01")
bg = pg.image.load("images/bg01.png")

go = pg.image.load("images/green_one/go01.png")

k = 0
a = 1

running = True
while running:

    screen.blit(bg, (0, 0))

    screen.blit(go, (int(X_SIZE/2 + k), int(Y_SIZE/2 + k)))
    

    pg.display.update()

    for event in pg.event.get():
        if event.type is pg.QUIT:
            running = False
            pg.quit()


