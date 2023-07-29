from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random
import time

class shootingRange():
    def __init__(self) -> None:
        self.boxes = []
        self.grases = []
        for n in range(-10,200):
            for k in range(-6,6):
                self.grass = Button(color=color.white, model='cube', position=(k,0,n)
                                    ,parent=scene, origin_y=0.5)
                self.grases.append(self.grass)
        for _ in range(20):
            self.box = Button(color=color.red, model='cube', 
                              position=(random.randint(-6,6),random.randint(2,6),random.randint(0,50)),
                              parent=scene, origin_y=0.5)
            self.boxes.append(self.box)