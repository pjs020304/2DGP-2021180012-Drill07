from pico2d import *
import random

# Game object class here
class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,500), 90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame +1) %8
        self.x +=5

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

class Grass:
    # 생성자 함수: 객체의 초기 상태를 설정
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400,30)

    pass

class LBall:
    def __init__(self):
        self.x, self.y = random.randint(100,500), random.randint(150,500)
        self.image = load_image('ball41x41.png')
        self.fall = True
        self.speed = random.randint(2, 8)
    def update(self):
        self.x +=3
        if self.fall:
            self.y-=self.speed
        else:
            self.y+=self.speed


        if self.y<88:
            self.fall = False
        if self.y>550:
            self.fall = True

    def draw(self):
        self.image.draw(self.x,self.y)

class SBall:
    def __init__(self):
        self.x, self.y = random.randint(100,500), random.randint(150,500)
        self.image = load_image('ball21x21.png')
        self.fall = True
        self.speed = random.randint(2, 8)

    def update(self):
        self.x += 3
        if self.fall:
            self.y -= self.speed
        else:
            self.y += self.speed

        if self.y < 88:
            self.fall = False
        if self.y > 550:
            self.fall = True

    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# 초기화 코드
def reset_world():
    global running
    global grass
    global team
    global lball
    global sball
    global world

    running = True
    world = []
    grass = Grass() # 잔디를 생성한다.
    world.append(grass)
    team = [Boy() for i in range(11)]
    world +=team
    lball = [LBall() for i in range(random.randint(5, 15))]
    world +=lball
    sball = [SBall() for i in range(20-len(lball))]
    world +=sball

def update_world():
    for o in world:
        o.update()
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
