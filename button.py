import pygame as pg
from game import Context
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
    
    
    def draw(self):
        rect = pg.rect.Rect(
            self.x, self.y,self.w,self.h)
        if self.selected:
            pg.draw.rect(Context.display, Context.select_color, rect)
        else:
            pg.draw.rect(Context.display, Context.foreground_color, rect)
        Context.draw_text(self.x, self.y, self.text)
