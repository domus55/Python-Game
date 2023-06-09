import pygame

import Camera
from CloudManager import CloudManager
from Screen import screen


class Background:
    _instance = None

    def __init__(self):
        super().__init__()
        self.images = []
        self.imageWidth = []
        self._loadImages()

    @staticmethod
    def getInstance():
        if Background._instance is None:
            Background._instance = Background()
        return Background._instance

    def _loadImages(self):
        NUMBER_OF_IMAGES = 3

        for i in range(NUMBER_OF_IMAGES):
            img = pygame.image.load(f"images/background/{i + 1}.png")
            if i is 0:  # sky
                readyImg = pygame.transform.scale(img, (1600, 367))
                self.images.append(readyImg.convert())
            elif i is 1:  # mountain
                readyImg = pygame.transform.scale(img, (1600, 692))
                self.images.append(readyImg.convert_alpha())
            elif i is 2:  # forest
                readyImg = pygame.transform.scale(img, (1600, 367))
                self.images.append(readyImg.convert_alpha())
            else:
                readyImg = pygame.transform.scale(img, (1600, 900))
                self.images.append(readyImg.convert_alpha())

            self.imageWidth.append(self.images[i].get_rect().width)

    def render(self):
        for i in range(len(self.images)):
            positionY = 0
            movingSpeed = 0
            if i is 0:  # Sky
                screen.fill((118, 185, 227))
            if i is 1:  # mountain
                movingSpeed = 0.02
                CloudManager.renderBeforeMountains()
                positionY = 114
            if i is 2:  # forest
                movingSpeed = 0.1
                positionY = 533

            positionX = ((-Camera.Camera.posX * movingSpeed) % self.imageWidth[i]) - self.imageWidth[i]
            screen.blit(self.images[i], (positionX, positionY))
            screen.blit(self.images[i], (positionX + self.imageWidth[i], positionY))

            if i is 2:
                CloudManager.renderAfterMountains()

    def update(self):
        CloudManager.update()
