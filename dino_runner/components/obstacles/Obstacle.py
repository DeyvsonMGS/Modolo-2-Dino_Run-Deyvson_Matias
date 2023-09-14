import random


    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed 

        if self.rect.x < -self.rect.width:
            obstacles.pop()