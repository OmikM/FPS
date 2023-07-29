from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random
import time

class Enemy:
    def __init__(self,pos):
        self.hp= 100
        self.pos = pos
        self
class Fight():
  def __init__(self) -> None:
    boxes = []
    grass = []
    for n in range(-10,200):
        for k in range(-6,6):
            gras = Button(color=color.white, model='cube', position=(k,0,n),
                         texture='assets\grass',parent=scene, origin_y=0.5)
            grass.append(gras)

        box = Button(color=color.red, model='assets\EnemyHatGhost.obj', position=(0,2,10),
                     parent=scene, origin_y=0.5, scale=(.02,.02,.02))
        boxes.append(box)
    