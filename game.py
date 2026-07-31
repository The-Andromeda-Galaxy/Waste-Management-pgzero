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
is_game_complete = False
current_level = 1

items = []
animations = []

def draw():
    global items,animations,current_level,is_game_complete,is_game_over
    screen.clear()
    screen.blit("bg",(0,0))
    if is_game_over:
        display_message("You Lose","Try again")
        

def update():
    pass

def make_items(extra_items):
    items_to_create = get_option(extra_items)
    new_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

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

def animate_items(items_to_animate):
    global animations
    for item in items_to_animate:
        duration = START_SPEED - current_level
        item.anchor = ("center","bottom")
        animation = animate(item,duration = duration,on_finished = game_over,y = HEIGHT)
        animations.append(animation)

def game_over():
    global is_game_over
    is_game_over = True

def on_mouse_down(pos):
    global items,current_level
    for item in items:
        if item.collidepoint(pos):
            if "compost" in item.image:
                game_complete()
            else:
                game_over()

def game_complete():
    global current_level,animations,is_game_complete,items
    stop_animations(animations)
    if current_level == FINAL_LEVEL:
        is_game_complete = True
    else:
        current_level += 1
        animations = []
        items = []

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running():
            animation.stop()

def display_message(main_text,sub_text):
    screen.draw.text(main_text,fontsize = 60, center = CENTER, color = "#1D2910")
    screen.draw.text(sub_text,fontsize = 40, center = (CENTER_X,CENTER_Y+50), color = "#141F09")














pgzrun.go()