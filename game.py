
import pygame as pg
class Context:

    screen_size = (screen_width, screen_height) = (600, 600)
    time = pg.time.Clock()
    display = pg.display.set_mode(screen_size)
    background_color = pg.Color(0, 23, 31)
    foreground_color = pg.Color(252, 250, 250)
    green_color = pg.Color(0, 255, 0)
    red_color = pg.Color(255, 0,0)
    # select_color = pg.Color(247, 247, 247)
    select_color = pg.Color(236, 236, 236)
    running = True
    no_of_rows = 10
    no_of_cols = 10
    block_size = (screen_width - 200) // no_of_cols
    grid = [[0 for i in range(10)] for j in range(no_of_rows)]
    gap_size = 5

    def draw_text(x, y, text: str):
        half = Context.block_size // 8
        font = pg.font.SysFont(None, half*4)
        location = (x+half, y+half)
        text = font.render(text, True, pg.Color(0, 0, 0))
        Context.display.blit(text, location)




class Button:
    def __init__(self,x: float, y: float,  text: str):
        self.x = x
        self.y = y
        self.w = len(text) ** 2 + 30
        self.h = 5 ** 2
        self.text = text
        self.selected = False
        # self.onclick = lambda x: x
    
    def collide(self, mouse: tuple[int, int]) -> bool:
        x,y = mouse
        return self.x <= x <= self.x + self.w and self.y <= y <= self.y + self.h
    
    def click(self, mouse):
        button = pg.mouse.get_pressed(3)
        if self.collide(mouse) and button[0]:
            self.onclick()
    
    def update(self):
        self.selected = self.text == names[current_shape-1]

    
    def draw(self):
        rect = pg.rect.Rect(
            self.x, self.y,self.w,self.h)
        if self.selected:
            pg.draw.rect(Context.display, Context.select_color, rect)
        else:
            pg.draw.rect(Context.display, Context.foreground_color, rect)
        Context.draw_text(self.x, self.y, self.text)
