# Code by madmattp https://github.com/madmattp

from ursina import *
from ursina.prefabs.first_person_controller import *
from random import choice

application.development_mode = False
    
app = Ursina()

window.title = 'A weird place in the matrix'
window.show_ursina_splash = True
window.fullscreen = False
window.borderless = False
window.size = (720, 576)
# window.vsync = True

texoffset = 0.0
texoffset1 = 0.0

def update():
    global texoffset, texoffset1
    texoffset += time.dt * 0.4 
    texoffset1 += time.dt * 0.1
    
    if player.controller.y < -3:
        player.controller.position = (-13.1947, 0, 8.8722)
    
    if held_keys['shift']:  
        player.controller.speed = 10
    else:
        player.controller.speed = 5

    for cube in cubes:
        cube.rotation_x += 50 * time.dt
        cube.rotation_y += 50 * time.dt
        setattr(cube, "texture_offset", (0, texoffset))
                                            
    setattr(ambient, "texture_offset", (0, texoffset))  
    setattr(sky, "texture_offset", (0, texoffset1))

class Player(Entity):
    def __init__(self, **kwargs):
        self.controller = FirstPersonController()
        super().__init__(parent=self.controller)

        self.controller.cursor = Entity(parent=camera.ui, model='quad', color=color.rgb(151, 252, 187), scale=0.008, rotation_z=45)
        self.controller.position = (-13.1947, 0, 8.8722)
           
sky = Sky(texture="background")
ambient = Entity(model ="matrix_floor",
    texture="groundnwalls",
    scale=60,
    collider="mesh",
    position=(0, 0, 0))
txt = Text(text="Welcome back to the Matrix, Neo_",
    font="pixelated.ttf",
    color=color.rgb(151, 252, 187),
    size=50.0,
    origin=(0,-15))

index = 0
cubes = []
while(index != 30):
    min_x = -58
    max_x = 58
    min_y = 4
    max_y = 16
    min_z = -57
    max_z = 58

    cube = Entity(model="cube",
        texture="cube_tex",
        scale=1,
        position=(choice(range(min_x, max_x + 1)), choice(range(min_y, max_y + 1)), choice(range(min_z, max_z + 1))))     

    cubes.append(cube)
    index += 1

player = Player()

app.run()
