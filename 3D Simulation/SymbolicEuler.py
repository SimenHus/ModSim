import sympy as sp
import numpy as np

rho, theta, psi = sp.symbols('rho theta psi', real=True)
drho, dtheta, dpsi = sp.symbols('drho dtheta dpsi', real=True)

A = sp.Matrix([rho, theta, psi])
dA = sp.Matrix([drho, dtheta, dpsi])

# Rotation about x
Rx = sp.Matrix([
    [1, 0, 0],
    [0, sp.cos(A[0]), -sp.sin(A[0])],
    [0, sp.sin(A[0]), sp.cos(A[0])]
])

# Rotation about y
Ry = sp.Matrix([
    [sp.cos(A[1]), 0, sp.sin(A[1])],
    [0, 1, 0],
    [-sp.sin(A[1]), 0, sp.cos(A[1])]
])

# Rotation about z
Rz = sp.Matrix([
    [sp.cos(A[2]), -sp.sin(A[2]), 0],
    [sp.sin(A[2]), sp.cos(A[2]), 0],
    [0, 0, 1]
])

# Rotation matrix.
Rba = sp.simplify(Rx*Ry*Rz)

# Time deriviatve of the rotation matrix(Hint: use the function "diff"
# (the one from the Symbolic Math Toolbox) to differentiate the matrix w.r.t. the
# angles rho, theta, psi one by one, and form the whole time derivative using the
# chain rule and summing the deriviatives)
dRba = sp.zeros(3, 3)  # Create empty 3x3 matrix
for i in range(len(A)):
    dRba += sp.diff(Rba, A[i])*dA[i]


# Use the formula relating Rba, dRba and Omega(skew-symmetric matrix
# underlying the angular velocity omega)(6.9.5 in the book). Hint: What is the
# inverse of Rba?
# From 6.319 we see that we may simply pre-multiply with R transposed (since we want omega^b)
Omega = sp.simplify(Rba.T*dRba)

# Extract the angular velocity vector omega(3x1) from the matrix Omega(3x3)
omega = sp.Matrix([
    Omega[2, 1],
    Omega[0, 2],
    Omega[1, 0]
])

# This line generates matrix M in the relationship omega = M*dA
M = sp.simplify(omega.jacobian(dA))

# This line creates a Matlab function returning Rba and M for a given
# A = [rho
#      theta
#      psi], can be called using[Rba, M] = Rotations(state)
# matlabFunction(Rba, M, 'file', 'Rotations', 'vars', {A})

# Implemented corresponding functionality in python as an importable function

def Rotations(state):
    stateSubs = {rho: state[0], theta: state[1], psi: state[2]}
    return np.array(Rba.subs(stateSubs)).astype(np.float64), np.array(M.subs(stateSubs)).astype(np.float64)
