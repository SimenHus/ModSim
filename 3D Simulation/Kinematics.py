import numpy as np
from SymbolicEuler import Rotations

def Kinematics(t, state, omega):
    Rba, M = Rotations(state)
    return np.linalg.inv(M)@omega