from pico2d import *
import random

class LBall:
    def __init__(self):
        self.x, self.y = random.randint(100,500), random.randint(500,100)
        self.frame = random.randint(0,7)
        self.image = load_image('ball41x41.png')

class SBall:
    def __init__(self):
        self.x, self.y = random.randint(100,500), random.randint(500,100)
        self.frame = random.randint(0,7)
        self.image = load_image('ball21x21.png')

class Grass:
    # 생성자 함수: 객체의 초기 상태를 설정
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400,30)

    pass

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global grass
    global lball
    global sball
    global world

    running = True
    world = []
    grass = Grass() # 잔디를 생성한다.
    world.append(grass)
    lball = [LBall() for i in range(random.randint(5, 15))]

def update_world():
    pass

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

open_canvas()

reset_world()
# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
# finalization code

close_canvas()
