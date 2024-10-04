import random

from pico2d import *


# fill here
TUK_WIDTH, TUK_HEIGHT = 1280 , 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
hand_arrow = load_image('hand_arrow.png')
character = load_image('run_animation.png')


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def draw_hand_arrow():
    pass


def draw_charactor():
    global frame,x,y
    hand_x = random.randint(0 , TUK_WIDTH)
    hand_y = random.randint(0 ,TUK_HEIGHT)
    if (x <= hand_x):
        temp = 1
    else:
        temp = 0
    for i in range(0, 50):
        clear_canvas()
        tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        hand_arrow.draw(hand_x, hand_y)
        t = i / 50

        x = (1 - t) * x + t * hand_x # x1 , x2 1-t:t의 비율로 더한다
        y = (1 - t) * y + t * hand_y  # y1 , y2 1-t:t의 비율로 더한다
        if (temp == 1):
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
        else:
            character.clip_composite_draw(frame * 100, 0, 100, 100, 0, 'h', x, y, 100, 100)
        frame = (frame + 1) % 8
        update_canvas()
        delay(0.04)
    delay(0.2)


running = True
frame = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2


while running:
    draw_charactor()
    handle_events()

close_canvas()
