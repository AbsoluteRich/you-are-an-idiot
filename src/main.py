import pygame as pg


class Image:
    def __init__(self, path: str) -> None:
        self.path = path
        self.surface = pg.image.load(self.path)
        self.rect = self.surface.get_rect()
        self.width, self.height = self.surface.get_size()


class Sprite:
    def __init__(self, image_path: str, x: int | float, y: int | float) -> None:
        self.image = Image(image_path)
        self.x = x
        self.y = y

    def draw(self, display: pg.Surface) -> None:
        display.blit(self.image.surface, (self.x, self.y))


if __name__ == "__main__":
    pg.init()

    running = True
    time_elapsed = 0

    background = Sprite("background_white.gif", 0, 0)
    screen = pg.display.set_mode((background.image.width, background.image.height), pg.NOFRAME)
    clock = pg.time.Clock()
    fps = pg.display.get_current_refresh_rate()

    pg.mixer.music.load("idiot.mp3")
    pg.display.set_caption("You are an idiot!")
    pg.display.set_icon(pg.image.load("icon.png"))

    pg.mixer.music.play(-1)

    while running:
        time_elapsed += clock.tick(fps) / 1000  # clock.tick returns the time in milliseconds

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        background.draw(screen)
        pg.display.update()

        if time_elapsed >= 2:  # Ensures the black background stays on the screen for 1 second
            time_elapsed = 0
        elif time_elapsed >= 1:
            background.image = Image("background_black.gif")
        else:
            background.image = Image("background_white.gif")

    pg.quit()
