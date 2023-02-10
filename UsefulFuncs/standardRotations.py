import numpy as np
import sympy as sp

symrho, symtheta, sympsi = sp.symbols('rho theta psi')

def Rx(numrho=None):
    sym = sp.Matrix([
        [1, 0, 0],
        [0, sp.cos(symrho), -sp.sin(symrho)],
        [0, sp.sin(symrho), sp.cos(symrho)]
    ])
    if numrho is None: return sym
    num = np.array([
        [1, 0, 0],
        [0, np.cos(numrho), -np.sin(numrho)],
        [0, np.sin(numrho), np.cos(numrho)]
    ])
    return num

def Ry(numtheta=None):
    sym = sp.Matrix([
        [sp.cos(symtheta), 0, sp.sin(symtheta)],
        [0, 1, 0],
        [-sp.sin(symtheta), 0, sp.cos(symtheta)]
    ])
    if numtheta is None: return sym
    num = np.array([
        [np.cos(numtheta), 0, np.sin(numtheta)],
        [0, 1, 0],
        [-np.sin(numtheta), 0, np.cos(numtheta)]
    ])

    return num

def Rz(numpsi=None):
    sym = sp.Matrix([
        [sp.cos(symrho), -sp.sin(symrho), 0],
        [sp.sin(symrho), sp.cos(symrho), 0],
        [0, 0, 1]
    ])
    if numpsi is None: return sym
    
    num = np.array([
        [np.cos(numpsi), -np.sin(numpsi), 0],
        [np.sin(numpsi), np.cos(numpsi), 0],
        [0, 0, 1]
    ])

    return num
