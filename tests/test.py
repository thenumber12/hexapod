from src.legs.leg import Leg
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, art3d
from matplotlib.patches import Circle, Ellipse
import numpy as np

from src.kinematics.forward_kinematics import ForwardKinematics
from src.kinematics.inverse_kinematics import InverseKinematics

test_leg = Leg(0, 1,3, 3, -np.pi/4,0,0,0)

def plot_leg(leg, fk_leg):
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')


    joints = np.asarray([leg.origin[:3], fk_leg.get("coxa")[:3], fk_leg.get("femur")[:3], fk_leg.get("tibia")[:3]], dtype=float)
    #TODO: Add 3D orientation markers to the points to check for correct orientation w.r.t. origin theta
    ax.scatter(joints[:, 0], joints[:, 1], joints[:, 2], color='blue', label='Points')
    #ax.plot_wireframe(X, Y, Z, color='r')
    plt.show()


# Consider finding the coordinates at each joint
def test_forward_kinematics():
    fk = ForwardKinematics(test_leg)
    fk_leg = fk.forward_kinematics_solver()
    #plot_leg(test_leg, fk_leg)
    print(fk.forward_kinematics_solver())
#test_forward_kinematics()

def test_inverse_kinematics():
    ik = InverseKinematics(test_leg, 3)
    raise NotImplemented

def test_kinematics():
    ik = InverseKinematics(test_leg, 3)
    print(ik.inverse_kinematics_solver())
test_kinematics()



def test_leg():
    raise NotImplemented


#test_forward_kinematics()



