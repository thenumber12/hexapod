import numpy as np

class ForwardKinematics:
    def __init__(self, leg):
        self.leg = leg
        self.origin_transform = self._origin_transform()

    def _origin_transform(self):
        x,y,z,theta = self.leg.origin
        origin_transform = np.asarray([
            [np.cos(theta), -np.sin(theta), 0, x],
            [np.sin(theta), np.cos(theta), 0, y],
            [0, 0, 1, z],
            [0, 0, 0, 1]
        ])
        return origin_transform

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
        # Returns the tibia endpoint WITHOUT ORIGIN OFFSET
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

        return np.asarray([x,y,z]).T


    def coxa_xyz_transform(self):
        c_transform = self.xy_transform(self.leg.coxa_length, self.leg.coxa_theta)
        B = np.asarray([0,0,0,1])
        B = B.T
        return np.dot(self.origin_transform @ c_transform, B)

    def femur_xyz_transform(self):
        c_transform = self.xy_transform(self.leg.coxa_length, self.leg.coxa_theta)
        f_transform = self.xz_transform(self.leg.femur_length, self.leg.femur_theta)
        B = np.asarray([0,0,0,1])
        B = B.T
        return np.dot(self.origin_transform @ c_transform @ f_transform, B)

    def tibia_xyz_transform(self):
        c_transform = self.xy_transform(self.leg.coxa_length, self.leg.coxa_theta)
        f_transform = self.xz_transform(self.leg.femur_length, self.leg.femur_theta)
        t_transform = self.xz_transform(self.leg.tibia_length, self.leg.femur_theta + self.leg.tibia_theta)
        B = np.asarray([0,0,0,1])
        B = B.T
        return np.dot(self.origin_transform @ c_transform @ f_transform @ t_transform, B)


    def forward_kinematics_solver(self):
        c_xyz = self.coxa_xyz_transform()
        f_xyz = self.femur_xyz_transform()
        t_xyz = self.tibia_xyz_transform()
        return {"origin": self.leg.origin, "coxa": c_xyz, "femur": f_xyz, "tibia": t_xyz}
