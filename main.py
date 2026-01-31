from pygame import *
from settings import *
from sounds import load_sounds
from keys import draw_keys, create_key_rects
from buttons import Button

init()
screen = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption("Piano Game")

sounds = load_sounds(KEYS)
key_rects = create_key_rects(len(KEYS))
keys_list = list(KEYS.keys())
my_font = font.SysFont("Arial", 24)
pressed_keys = set()

# кнопки меню
def start_game(): pass
def open_settings(): pass
def exit_game(): quit()

buttons = [
    Button(60, 20, 120, 40, "Settings", open_settings)
]

running = True
while running:
    screen.fill(WHITE)

    # кнопки
    for button in buttons:
        button.draw(screen, my_font)

    # клавіші
    draw_keys(screen, key_rects, pressed_keys)

    display.flip()

    for e in event.get():
        if e.type == QUIT:
            running = False

        # кнопки
        for button in buttons:
            button.handle_event(e)

        # клавіатура
        
