import numpy as np
from src.kinematics.forward_kinematics import ForwardKinematics

class InverseKinematics:
    def __init__(self, leg, step_length):
        self.leg = leg


    def inverse_kinematics_solver(self):
        x, y, z = ForwardKinematics(self.leg).forward_kinematics_solver()[:3]
        print(f'x = {x}, y = {y}, z = {z}')

        c_theta = np.arctan2(y, x)

        R = np.sqrt(x**2 + y**2) - self.leg.coxa_length

        D = (R**2 + z**2 - self.leg.femur_length**2 - self.leg.tibia_length**2) / (2 * self.leg.femur_length * self.leg.tibia_length)
        t_theta = np.arccos(D)

        f_theta = np.arctan2(z, R) - np.arctan2(self.leg.tibia_length * np.sin(t_theta), self.leg.femur_length + self.leg.tibia_length * np.cos(t_theta))

        A = np.asarray([[1,0,0],
                        [0,1,-1],
                        [0,0,1]])
        A_inv = np.linalg.inv(A)

        B = np.asarray([c_theta, f_theta, t_theta]).T

        theta_out = np.dot(A_inv, B)

        #print(theta_out)
        return theta_out




