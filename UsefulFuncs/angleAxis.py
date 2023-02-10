import numpy as np

def angleAxis(R: np.array) -> np.array:
    r00, r11, r22, r33 = np.hstack([np.trace(R), np.diag(R)])
    rii = max([r00, r11, r22, r33])
    i = [r00, r11, r22, r33].index(rii)

    zi = np.sqrt(1 + 2*rii - r00)
    z0z1, z2z3 = R[2][1] - R[1][2], R[2][1] + R[1][2]
    z0z2, z3z1 = R[0][2] - R[2][0], R[0][2] + R[2][0]
    z0z3, z1z2 = R[1][0] - R[0][1], R[1][0] + R[0][1]
    situations = {
        0: [zi, z0z1, z0z2, z0z3],
        1: [z0z1, zi, z1z2, z3z1],
        2: [z0z2, z1z2, zi, z2z3],
        3: [z0z3, z3z1, z2z3, zi]
    }
    z = np.array(situations[i])/(2*zi)
    z[i] *= zi

    eta = z[0]
    epsilon = z[1:]

    # From 6.159 in the book
    theta = 2*np.arccos(eta)
    k = epsilon / (np.sin(theta/2))
    return theta, k
