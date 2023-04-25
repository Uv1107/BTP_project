def drawPolygon():
    pygame.font.init()
    myfont2 = pygame.font.SysFont('Comic Sans MS', 10)

    for i in range(len(points) - 1):
        pygame.draw.aaline(screen, BLUE, points[i], points[i + 1])
        textsurface = myfont2.render(str(i), False, (0, 0, 0))
        screen.blit(textsurface, (points[i][0], points[i][1]))
    textsurface = myfont2.render(str(len(points) - 1), False, (0, 0, 0))
    screen.blit(
        textsurface, (points[len(points) - 1][0], points[len(points) - 1][1]))
    pygame.draw.aaline(screen, BLUE, points[len(points) - 1], points[0])

