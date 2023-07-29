from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import Entity

import random
import time

from fight import *
from shootingrange import *

class Player(FirstPersonController):
    def __init__(self):
        super().__init__(model='cube',
                         scale=(1,1,1),
                         z=-10, 
                         color=color.orange, 
                         origin_y=-.5, 
                         speed=15,
                         jump_height = 5)

        self.gun = Entity(model='assets\\Ghost', 
                          parent=camera, 
                          position=(.5,-.25,.25), 
                          scale=(.02,.02,.1), 
                          origin_z=-.5, 
                          color=color.black, 
                          on_cooldown=False)

    def input(self,key):
        super().input(key)
        if key == 'left mouse down':
            game.GhostShot.play()
            for box in game.boxes:
                if box.hovered:
                    game.boxes.remove(box)
                    destroy(box)
                    if len(game.boxes)==0:
                        print(time.time()-game.tstart)
                        time.sleep(0.5)
                        quit() 
        if key == 'escape':
            quit()
        if key == 'shift':
            if self.scale_y == 0.75:
                self.scale_y = 1
            else:
                self.scale_y = 0.75

    def update(self):
        super().update()
        if self.y < -80:
            quit()
        if held_keys['left mouse']:
            self.gun.position=(.3,-.2,.25)
        elif held_keys['right mouse']:
            self.gun.position=(.3,-.2,.25)
        else:
            self.gun.position=(.3,-.3,.25)

class Game:
    def __init__(self, GameType) -> None:
        self.app = Ursina()
        Sky(texture='sky_sunset')
        self.GhostShot = Audio('assets\\Ghostsound.mp3', loop=False,autoplay=False)
        self.player = Player()#model='cube',scale=(1,1,1), z=-10, color=color.orange, origin_y=-.5, speed=5,
        
        self.tstart = time.time()

        if GameType==1:
            srsu = shootingRange()
            self.boxes = srsu.boxes
            self.grases = srsu.grases

        elif GameType==2:
            fight = Fight
            self.box = fight.box
            self.grases = fight.grases

if __name__ == "__main__":
    game = Game(1)
    game.app.run()