import numpy as np

class ForwardKinematics:
    def __init__(self, leg):
        self.leg = leg

    def xy_transform(self, len, theta):
        # mainly used for coxa equations
        xy_transform = np.asarray([
            [np.cos(theta), -np.sin(theta), 0, len*np.cos(theta)],
            [np.sin(theta), np.cos(theta), 0, len*np.sin(theta)],
            [0,0,1,0],
            [0,0,0,1]
        ])
        return xy_transform

    def xz_transform(self, len, theta):
        # tranform equations for femur and tibia
        xz_transform = np.asarray([
            [1, 0, 0, len*np.cos(theta)],
            [0, np.cos(theta), -np.sin(theta), 0],
            [0, np.sin(theta), np.cos(theta), len * np.sin(theta)],
            [0,0,0,1]
        ])
        return xz_transform

    def xyz_transform(self):
        # Returns the tibia endpoint
        c_len = self.leg.coxa_length
        f_len = self.leg.femur_length
        t_len = self.leg.tibia_length
        c_theta = self.leg.coxa_theta
        f_theta = self.leg.femur_theta
        t_theta = self.leg.tibia_theta

        xy_coeff = (c_len + f_len * np.cos(f_theta) + t_len * np.cos(f_theta + t_theta))
        x = np.cos(c_theta) * xy_coeff
        y = np.sin(c_theta) * xy_coeff
        z = f_len * np.sin(f_theta) + t_len * np.sin(f_theta + t_theta)

        return np.asarray([x,y,z,1]).T


    def forward_kinematics_solver(self):
        c_transform = self.xy_transform(self.leg.coxa_length, self.leg.coxa_theta)
        f_transform = self.xz_transform(self.leg.femur_length, self.leg.femur_theta)
        t_transform = self.xz_transform(self.leg.tibia_length, self.leg.femur_theta+self.leg.tibia_theta)

        print(c_transform, f_transform, t_transform)
        return self.xyz_transform()
