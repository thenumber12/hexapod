from src.legs.leg import Leg
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, art3d
from matplotlib.patches import Circle, Ellipse
import numpy as np

from src.kinematics.forward_kinematics import ForwardKinematics
from src.kinematics.inverse_kinematics import InverseKinematics

test_leg = Leg(0, 1,3, 3, 1,0,0,0)

def plot_leg():
    # Plot 3D
    points = [[0,0,2,0], [2,0,2,0], [5,0,2,0], [7.236,0,0,0]]
    #add_point(ax3d, x=0, y=0, z=2)
    #add_point(ax3d, x=2, y=0, z=2)
    #add_point(ax3d, x=5, y=0, z=2)
    #add_point(ax3d, x=7, y=0, z=0)

    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    points = np.array(points, dtype=float)
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], color='blue', label='Points')


    #ax.plot_wireframe(X, Y, Z, color='r')
    plt.show()

#plot_leg()

# Consider finding the coordinates at each joint
def test_forward_kinematics():
    fk = ForwardKinematics(test_leg)
    print(fk.forward_kinematics_solver())
test_forward_kinematics()

def test_inverse_kinematics():
    ik = InverseKinematics(test_leg, 3)
    ik.calculate_theta()
    raise NotImplemented

def test_kinematics():
    ik = InverseKinematics(test_leg, 3)
    print(ik.inverse_kinematics_solver())
#test_kinematics()



def test_leg():
    raise NotImplemented


#test_forward_kinematics()



