import pygame

WIDTH, HEIGHT = 1500, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

grid = tuple(tuple((0, 0, 0) if i % 2 == 0 else (255, 255, 255) for i in range(1000)) for _ in range(1000))


def draw(win: pygame.Surface,top_right_x,top_right_y):
    win.fill((255, 255, 255))
    for row_num, row in enumerate(grid):
        for col_num, cell in enumerate(row):
            pygame.draw.rect(win, cell, [(row_num * 10) + top_right_x, (col_num * 10) + top_right_y, 10, 10])
    pygame.display.update()


def main():
    top_right_x = 0
    top_right_y = 0
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            top_right_y += 10
        elif keys[pygame.K_UP]:
            top_right_y -= 10
        elif keys[pygame.K_RIGHT]:
            top_right_x += 10
        elif keys[pygame.K_LEFT]:
            top_right_x -= 10
        draw(WIN,top_right_x,top_right_y)


if __name__ == '__main__':
    main()
