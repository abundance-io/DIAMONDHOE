# from audioop import reverse
import sys
import pygame as pg
from game import Context

# class Context:

#     screen_size = (screen_width, screen_height) = (600, 600)
#     time = pg.time.Clock()
#     display = pg.display.set_mode(screen_size)
#     background_color = pg.Color(0, 23, 31)
#     foreground_color = pg.Color(252, 250, 250)
#     # select_color = pg.Color(247, 247, 247)
#     select_color = pg.Color(236, 236, 236)
#     running = True
#     no_of_rows = 10
#     no_of_cols = 10
#     block_size = (screen_width - 200) // no_of_cols
#     grid = [[0 for i in range(10)] for j in range(no_of_rows)]
#     gap_size = 5




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
        draw_text(self.x, self.y, self.text)

        

# screen_size = (screen_width, screen_height) = (600, 600)
# time = pg.time.Clock()
# display = pg.display.set_mode(screen_size)
# background_color = pg.Color(0, 23, 31)
# foreground_color = pg.Color(252, 250, 250)
# # select_color = pg.Color(247, 247, 247)
# select_color = pg.Color(236, 236, 236)
current_shape = 1
names = ["T", "C", "X"]

pg.display.set_caption("DIAMONDHOE")

# running = True
# no_of_rows = 10
# no_of_cols = 10
# block_size = (screen_width - 200) // no_of_cols
# grid = [[0 for i in range(no_of_cols)] for j in range(no_of_rows)]
# gap_size = 5


def get_cell_clicked(mouse):
    buttons = pg.mouse.get_pressed(3)
    mouseX, mouseY = mouse
    row = (mouseY // Context.block_size) - 2
    col = (mouseX // Context.block_size) - 2


    if 0 <= row < Context.no_of_rows and 0 <= col < Context.no_of_cols:
        if buttons[0]:
            Context.grid[row][col] = current_shape
        elif buttons[2]:
            Context.grid[row][col] = 0


# print(pg.font.get_fonts())


def btn_func(num):
    global current_shape
    current_shape = num




def draw_grid():
    for row in range(Context.no_of_rows):
        for col in range(Context.no_of_cols):
            x = Context.block_size * col + Context.gap_size + (Context.screen_width / 8)
            y = Context.block_size * row + Context.gap_size + (Context.screen_height / 8)
            # print(x, y)
            rect = pg.rect.Rect(
                x, y, Context.block_size-Context.gap_size, Context.block_size-Context.gap_size)
            pg.draw.rect(Context.display, Context.foreground_color, rect)
            text = ""
            if Context.grid[row][col] == 1:
                text = "T"
            elif Context.grid[row][col] == 2:
                text = "C"
            elif Context.grid[row][col] == 3:
                text = "X"
            Context.draw_text(x, y, text)


def create_buttons():
    buttons = []
    names = ["T", "C", "X"]
    funcs = [lambda : btn_func(1),lambda : btn_func(2),lambda : btn_func(3)]
    startx = Context.screen_width / 8
    y = Context.screen_height - 50
    spacing = 50
    for i in range(3):
        b = Button(startx + (spacing * i), y, names[i])
        b.onclick = funcs[i]
        buttons.append(b)
    return buttons

pg.init()

# button = Button(screen_width / 8, screen_height - 50, 25, 25, "Click me")
buttons = create_buttons()
submit_button = Button(Context.screen_width - (Context.screen_width/8), Context.screen_height - 50, "Submit")
while Context.running:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            Context.running = False
        elif e.type == pg.MOUSEBUTTONDOWN:
            mouse = pg.mouse.get_pos()
            get_cell_clicked(mouse)


    Context.display.fill(Context.background_color)
    draw_grid()
    for button in buttons:
        button.draw()
        button.update()
        button.click(pg.mouse.get_pos())
    submit_button.draw()
    pg.display.update()
    Context.time.tick(60)

pg.quit()
sys.exit()
