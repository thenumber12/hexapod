import numpy as np
from src.kinematics.forward_kinematics import ForwardKinematics

class InverseKinematics:
    def __init__(self, leg, step_length):
        self.leg = leg


    def inverse_kinematics_solver(self):
        fk = ForwardKinematics(self.leg).forward_kinematics_solver()
        origin_theta = fk.get("origin")[3]
        x, y, z, theta = np.subtract(fk.get("tibia"),fk.get("origin"))
        print(f'x = {x}, y = {y}, z = {z}, theta = {theta}')
        x = x * np.cos(origin_theta) + y * np.sin(origin_theta)
        y = -x * np.sin(origin_theta) + y * np.cos(origin_theta)


        c_theta = np.arctan2(y, x)

        R = np.sqrt(x**2 + y**2) - self.leg.coxa_length

        # Law of Cosines
        D = (R**2 + z**2 - self.leg.femur_length**2 - self.leg.tibia_length**2) / (2 * self.leg.femur_length * self.leg.tibia_length)
        if abs(D) > 1:
            # Maybe consider closest point?
            raise Exception("Requested point is not reachable.")
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




