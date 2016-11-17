import numpy as np

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
from enum import Enum, unique

# camera is an observer
# so the keyboard would manipulate roll and direction and move around
# so im representing it with 4 vectors
# an up, forward, and right vector to represent orientation on all axes
# and a position vector to represent the translation


#  makes a 3x3 rotation matrix from the given angle and axis and pointer to a 3x3 matrix
def rotate_mat3x3(mat, axis, angle):
    cos1 = math.cos(angle)
    cos2 = 1 - cos1
    sin1 = math.sin(angle)

    mat[0] = cos1 + (axis[0]**2)*cos2
    mat[1] = axis[0]*axis[1]*cos2 - axis[2]*sin1
    mat[2] = axis[0]*axis[2]*cos2 + axis[1]*sin1

    mat[3] = axis[1]*axis[0]*cos2 + axis[2]*sin1
    mat[4] = cos1 + (axis[1]**2)*cos2
    mat[5] = axis[1]*axis[2]*cos2 - axis[0]*sin1

    mat[6] = axis[2]*axis[0]*cos2 - axis[1]*sin1
    mat[7] = axis[2]*axis[1]*cos2 + axis[0]*sin1
    mat[8] = cos1 + (axis[2]**2)*cos2


def mul_vec3_by_mat3x3(v, mat):
    res_v = np.zeros(v.size)
    res_v[0] = v[0] * mat[0] + v[1] * mat[1] + v[2] * mat[2]
    res_v[1] = v[0] * mat[3] + v[1] * mat[4] + v[2] * mat[5]
    res_v[2] = v[0] * mat[6] + v[1] * mat[7] + v[2] * mat[8]
    return res_v


# rotate a vector v1 around the axis v2 by angle and put the result into v3
def rotate_around_vec3(v1, v2, angle):
    # make a rotation matrix for it
    mat = np.zeros(9)
    rotate_mat3x3(mat, v2, angle)
    return mul_vec3_by_mat3x3(v1, mat)


def norm_vec(v):
    return v/np.linalg.norm(v)


class Camera:

    #  holds the state of the controls for the camera
    @unique
    class CameraState(Enum):
        Forward = 1
        Backward = 2
        Left = 3
        Right = 4
        YawLeft = 5
        YawRight = 6
        PitchUp = 7
        PitchDown = 8
        RollLeft = 9
        RollRight = 10
        Stop = 11

    def __init__(self):
        # a vector pointing to the direction you're facing
        self.forward_vec = np.array([-0.398769796, 0.763009906, -0.508720219])
        # a vector pointing to the right of where you're facing
        self.right_vec = np.array([0.886262059, 0.463184059, 0.000000000])
        self.up_vec = np.array([-0.235630989, 0.450859368, 0.860931039])
        # a vector describing the position of the camera
        self.pos_vec = np.array([0.764331460, -1.66760659, 0.642456770])
        # the camera speed
        self.speed = 0.05
        self.turn_speed = 0.01
        self.states = set()
        self.camera_routes = dict()
        self.__init_camera_routes()

    def __init_camera_routes(self):
        self.camera_routes.update({Camera.CameraState.Forward: self.move_forward,
                                   Camera.CameraState.Backward: self.move_backward,
                                   Camera.CameraState.Left: self.move_left,
                                   Camera.CameraState.Right: self.move_right,
                                   Camera.CameraState.YawLeft: self.yaw_left,
                                   Camera.CameraState.YawRight: self.yaw_right,
                                   Camera.CameraState.PitchUp: self.pitch_up,
                                   Camera.CameraState.PitchDown: self.pitch_down,
                                   Camera.CameraState.RollLeft: self.roll_left,
                                   Camera.CameraState.RollRight: self.roll_right,
                                   Camera.CameraState.Stop: self.stop
                                   })

    # move camera according states
    def move(self):
        for state in self.states:
            self.camera_routes[state]()

    def add_state(self, state):
        self.states.add(state)

    def del_state(self, state):
        self.states.discard(state)

    # transform the opengl view matrix for the orientation
    def transform_orientation(self):
        # look in the direction of the orientation vectors
        gluLookAt(0, 0, 0, self.forward_vec[0], self.forward_vec[1], self.forward_vec[2], self.up_vec[0], self.up_vec[1], self.up_vec[2])

    # transform the opoengl view matrix for the translation
    def transform_translation(self):
        glTranslatef(-self.pos_vec[0], -self.pos_vec[1], -self.pos_vec[2])

    # points the camera at the given point in 3d space
    def point_at(self, target_vec):
        up = np.array([0., 0., 1.])
        # first work out the new forward vector by subtracting the target position from the camera position
        self.forward_vec = target_vec - self.pos_vec
        # then normalize it to 1 length
        self.forward_vec = norm_vec(self.forward_vec)
        # now to find the right vector we rotate the forward vector -pi/2 around the z axis
        temp_vec = rotate_around_vec3(self.forward_vec, up, math.pi/2)
        # and remove the y component to make it flat
        temp_vec[2] = 0 # ???
        # then normalize it
        temp_vec = norm_vec(temp_vec)
        # and assign it to right_vec
        self.right_vec = np.copy(temp_vec)
        # now work out the upvector by rotating the forward vector pi/2 around the rightvector
        temp_vec = rotate_around_vec3(self.forward_vec, self.right_vec, math.pi/2)
        self.up_vec = np.copy(temp_vec)

    # speed up the camera speed
    def speed_up(self):
        if self.speed < 1.0:
            self.speed *= 2

    # slow down the camera speed
    def slow_down(self):
        if self.speed > 0.000001:
            self.speed /= 2

    def stop(self):
        pass

    # move the camera forward
    def move_forward(self):
        # make a movement vector the right speed facing the forward direction
        move_vec = np.copy(self.forward_vec)
        move_vec *= self.speed
        # add the movement vec to the position vec
        self.pos_vec += move_vec

    def move_backward(self):
        # make a movement vector the right speed facing the backward direction
        move_vec = np.copy(self.forward_vec)
        move_vec *= -self.speed
        self.pos_vec += move_vec

    def move_left(self):
        move_vec = np.copy(self.right_vec)
        move_vec *= -self.speed
        self.pos_vec += move_vec

    def move_right(self):
        move_vec = np.copy(self.right_vec)
        move_vec *= self.speed
        self.pos_vec += move_vec

    def roll_right(self):
        # rotate the up and right vectors around the forward vector axis for roll
        temp_vec = rotate_around_vec3(self.up_vec, self.forward_vec, self.turn_speed)
        self.up_vec = np.copy(temp_vec)
        temp_vec = rotate_around_vec3(self.right_vec, self.forward_vec, self.turn_speed)
        self.right_vec = np.copy(temp_vec)

    def roll_left(self):
        temp_vec = rotate_around_vec3(self.up_vec, self.forward_vec, -self.turn_speed)
        self.up_vec = np.copy(temp_vec)
        temp_vec = rotate_around_vec3(self.right_vec, self.forward_vec, -self.turn_speed)
        self.right_vec = np.copy(temp_vec)

    def pitch_up(self):
        # rotate the forward and up vectors around the right vector axis for pitch
        temp_vec = rotate_around_vec3(self.forward_vec, self.right_vec, self.turn_speed)
        self.forward_vec = np.copy(temp_vec)
        temp_vec = rotate_around_vec3(self.up_vec, self.right_vec, self.turn_speed)
        self.up_vec = np.copy(temp_vec)

    def pitch_down(self):
        temp_vec = rotate_around_vec3(self.forward_vec, self.right_vec, -self.turn_speed)
        self.forward_vec = np.copy(temp_vec)
        temp_vec = rotate_around_vec3(self.up_vec, self.right_vec, -self.turn_speed)
        self.up_vec = np.copy(temp_vec)

    def yaw_left(self):
        temp_vec = rotate_around_vec3(self.forward_vec, self.up_vec, self.turn_speed)
        self.forward_vec = np.copy(temp_vec)
        temp_vec = rotate_around_vec3(self.right_vec, self.up_vec, self.turn_speed)
        self.right_vec = np.copy(temp_vec)

    def yaw_right(self):
        temp_vec = rotate_around_vec3(self.forward_vec, self.up_vec, -self.turn_speed)
        self.forward_vec = np.copy(temp_vec)
        temp_vec = rotate_around_vec3(self.right_vec, self.up_vec, -self.turn_speed)
        self.right_vec = np.copy(temp_vec)


