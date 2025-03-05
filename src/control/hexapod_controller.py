from src.legs.leg_controller import LegController


class Hexapod:
    def __init__(self, gait):
        self.gait = gait

    def forward(self):
        lc = LegController(self.gait)




    def walk(self, steps):
        for i in range(steps):
            self.forward()

