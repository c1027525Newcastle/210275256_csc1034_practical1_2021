from math import pi, sin, cos

import pygame

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor

class WalkingPanda(ShowBase):
    #Adding the sound
    pygame.mixer.init()
    sound = pygame.mixer.Sound("C:/Users/DeadGru/PycharmProjects/210275256_csc1034_practical1_2021/Desiigner - Panda (Official Audio) (mp3cut.net).mp3")
    sound.play()

    def __init__(self, no_rotate=False, scale=1, environmentscale=1, pandaBaby=False):
        ShowBase.__init__(self)

        self.scene = self.loader.loadModel("models/environment")

        self.scene.reparentTo(self.render)

        self.scene.setScale(0.25*environmentscale, 0.25*environmentscale, 0.25*environmentscale)  #*environmentscale
        self.scene.setPos(-8, 42, 0)

        if no_rotate == True:
            self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005 * scale, 0.005 * scale, 0.005 * scale)####*scale
        self.pandaActor.reparentTo(self.render)
        self.pandaActor.loop("walk")

        ###BabyPanda added to the back of MainPanda
        if pandaBaby == True:
            self.pandaActorBaby = Actor("models/panda-model",
                                    {"walk": "models/panda-walk4"})
            self.pandaActorBaby.setScale(0.0035, 0.0035, 0.0035)
            self.pandaActorBaby.reparentTo(self.render)
            self.pandaActorBaby.setPos(0, 0, 2.3)





    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont
