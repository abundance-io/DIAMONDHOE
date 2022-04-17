import pygame as pg
import random
from game import Context


grid = [[0 for i in range(Context.no_of_cols)] for j in range(Context.no_of_rows)]
test = [[random.random().__round__() for i in range(Context.no_of_cols)] for j in range(Context.no_of_rows)]
print(test)
players_turn = True
active = (-1,-1)
def draw_grid():
    for row in range(Context.no_of_rows):
        for col in range(Context.no_of_cols):
            x = Context.block_size * col + Context.gap_size + (Context.screen_width / 8)
            y = Context.block_size * row + Context.gap_size + (Context.screen_height / 8)
            # print(x, y)
            rect = pg.rect.Rect(
                x, y, Context.block_size-Context.gap_size, Context.block_size-Context.gap_size)
            if grid[row][col] == 1:
                color = Context.green_color
            elif grid[row][col] == 2:
                color = Context.red_color
            else:
                color = Context.foreground_color

            pg.draw.rect(Context.display,color, rect)

def get_cell_clicked(mouse):
    global active
    buttons = pg.mouse.get_pressed(3)
    mouseX, mouseY = mouse
    row = (mouseY // Context.block_size) - 2
    col = (mouseX // Context.block_size) - 2


    if 0 <= row < Context.no_of_rows and 0 <= col < Context.no_of_cols and players_turn:
        res = 1
        if test[row][col] == 1:
            res = 1
        else:
            res = 2
        if buttons[0]:
            # if active != (-1,-1):
                # grid[active[0]][active[1]] = 0
            grid[row][col] = res
            active = (row, col)
        elif buttons[2]:
            grid[row][col] = 0
            active = (-1, -1)


pg.init()
while Context.running:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            Context.running = False
        elif e.type == pg.MOUSEBUTTONDOWN:
            get_cell_clicked(pg.mouse.get_pos())
    Context.display.fill(Context.background_color)
    draw_grid()
    pg.display.update()
    Context.time.tick(60)

pg.quit()
