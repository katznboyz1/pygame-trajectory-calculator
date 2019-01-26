import pygame as pygame
import math as math
import time as time

class app:
    running = True
    clock = pygame.time.Clock()
    fillColor = (0, 0, 0)
    screenSize = None
    screen = None
    fps = 0
    def text(fontFace, size, text, color):
        font = pygame.font.Font(fontFace, size)
        text = font.render(text, 1, color)
        return text

pygame.display.init()
pygame.font.init()
pygame.mouse.set_visible(True)

app.screenSize = (pygame.display.Info().current_w, pygame.display.Info().current_h)

app.screen = pygame.display.set_mode(app.screenSize, pygame.FULLSCREEN)

while (app.running):
    lastTime = time.time()
    app.screen.fill(app.fillColor)
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE):
                app.running = False
    mousePos = pygame.mouse.get_pos()
    app.screen.blit(app.text('./consolas.ttf', int(app.screenSize[0] / 50), str(app.fps) + ' FPS', (255, 255, 255)), (0, 0))
    pygame.draw.line(app.screen, (255, 255, 255), (0, app.screenSize[1]), mousePos)
    pygame.draw.line(app.screen, (255, 255, 255), (0, app.screenSize[1] - (app.screenSize[1] - mousePos[1])), mousePos)
    pygame.draw.line(app.screen, (255, 255, 255), (0, app.screenSize[1] - (app.screenSize[1] - mousePos[1])), (0, app.screenSize[1]))

    A_measure = (mousePos[0])
    A_text = app.text('./consolas.ttf', int(app.screenSize[0] / 50), str(mousePos[0]), (255, 255, 255))
    A_textpos = [0, 0]
    A_textpos[0] = (mousePos[0] - A_text.get_size()[0]) / 2
    A_textpos[1] = (mousePos[1] - A_text.get_size()[1])
    app.screen.blit(A_text, A_textpos)

    B_measure = (app.screenSize[1] - mousePos[1])
    B_text = app.text('./consolas.ttf', int(app.screenSize[0] / 50), str(app.screenSize[1] - mousePos[1]), (255, 255, 255))
    B_textpos = [0, 0]
    B_textpos[0] = 0
    B_textpos[1] = -(app.screenSize[1] - mousePos[1])
    B_textpos[1] += app.screenSize[1] + (((app.screenSize[1] - mousePos[1]) + B_text.get_size()[1]) / 2)
    app.screen.blit(B_text, B_textpos)

    C_measure = int(math.sqrt((A_measure ** 2) + B_measure ** 2))

    C_text = app.text('./consolas.ttf', int(app.screenSize[0] / 50), str(C_measure), (255, 255, 255))
    C_textpos = [0, 0]
    C_textpos[0] = A_textpos[0]
    C_textpos[1] = B_textpos[1]
    app.screen.blit(C_text, C_textpos)

    X, Y = mousePos[0], mousePos[1]
    LX, LY = X, Y

    acceleration_y = 9.8
    vi_x = A_measure
    vi_y = B_measure
    distance_x = app.screenSize[0]

    for change in range(vi_x, distance_x):
        LX, LY = X, Y
        X += vi_x
        Y -= acceleration_y
        Y -= vi_y
        vi_y -= acceleration_y
        pygame.draw.line(app.screen, (255, 255, 255), (X, Y), (LX, LY))

    pygame.display.update()
    app.clock.tick(30)
    currentTime = time.time()
    app.fps = int(1 / (currentTime - lastTime))
