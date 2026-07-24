import pgzrun
import random

WIDTH = 800
HEIGHT = 600
TITLE = "Waste Management"
CENTER_X = 400
CENTER_Y = 300
CENTER = (CENTER_X,CENTER_Y)
FINAL_LEVEL = 6
START_SPEED = 10
ITEMS = ["battery","bottle","chips","glass","plastic"]

is_game_over = False
Is_game_complete = False
current_level = 1

items = []
animations = []

def draw():
    screen.clear()
    screen.blit("bg",(0,0))

def update():
    pass

def get_option(extra_items):
    items_to_create = ["compost"]
    for i in range(extra_items):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

def create_items(items_to_create):
    new_items = []
    for option in items_to_create:
        item = Actor(option + "img")
        new_items.append(item)
    return new_items

def layout_items(items_to_layout):
    gaps = len(items_to_layout) + 1
    gap_size = WIDTH/gaps
    random.shuffle(items_to_layout)
    for index,item in enumerate(items_to_layout):
        x_pos = (index+1)*gap_size
        item.x = x_pos
















pgzrun.go()