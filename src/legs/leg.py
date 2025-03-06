from src.kinematics.inverse_kinematics import InverseKinematics
#from src.hardware.motor_driver import MotorDriver


#
#
# C = COXA
#
#
#  C5 -------- C0
#  |            |
#  |            |
#  C4          C1
#  |            |
#  |            |
#  C3 -------- C2
#

# NOTE: Because Inverse Kinematics will be used to move a specific distance
# we will change the distance each step should be regardless of leg length
# to find optimal speed for walking in any combination. That way we can determine
# if leg length as an impact by finding optimal speed at each length

BODY_WIDTH = 1
BODY_LENGTH = 3
BODY_HEIGHT = 2 # starting height for BOT from ground. # should be defined in gait

# mounted [x,y,z,theta] based on the leg
LEG_ORIGINS = {0: [0,BODY_WIDTH,BODY_HEIGHT,0],
               1: [BODY_LENGTH/2,BODY_WIDTH,BODY_HEIGHT,0],
               2: [BODY_LENGTH,BODY_WIDTH,BODY_HEIGHT,0],
               3: [BODY_LENGTH,0,BODY_HEIGHT,0],
               4: [BODY_LENGTH/2,0,BODY_HEIGHT,0],
               5: [0,0,BODY_HEIGHT,0]}


class Leg:
    # consider making this a leg struct instead so we have less input variable
    def __init__(self, coxa, coxa_length, femur_length, tibia_length, coxa_theta, femur_theta, tibia_theta, gait):
        self.origin = LEG_ORIGINS.get(coxa) # determines relative location
        self.gait = gait # Informs us of initial positions

        # Forward Kinematics Variables
        self.coxa_length = coxa_length
        self.femur_length = femur_length
        self.tibia_length = tibia_length
        self.coxa_theta = coxa_theta
        self.femur_theta = femur_theta
        self.tibia_theta = tibia_theta



    def __getstate__(self):
        return self.coxa_theta, self.femur_theta, self.tibia_theta


    def diagnostic(self):
        # Lift leg as high as possible, go back to initial position
        # Lift leg halfway up from initial position, rotate coxa by full 180, go back to initial position
        # Life leg quarter up, lift tibia, ba back to initial position
        raise NotImplemented



