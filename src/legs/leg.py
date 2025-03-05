from src.kinematics.inverse_kinematics import InverseKinematics
#from src.hardware.motor_driver import MotorDriver


#
#
# C = COXA
#
#
#  C1 -------- C2
#  |            |
#  |            |
#  C3          C4
#  |            |
#  |            |
#  C5 -------- C6
#

# NOTE: Because Inverse Kinematics will be used to move a specific distance
# we will change the distance each step should be regardless of leg length
# to find optimal speed for walking in any combination. That way we can determine
# if leg length as an impact by finding optimal speed at each length


class Leg:
    # consider making this a leg struct instead so we have less input variable
    def __init__(self, coxa, coxa_length, femur_length, tibia_length, coxa_theta, femur_theta, tibia_theta, gait):
        self.coxa = coxa # determines relative location
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



