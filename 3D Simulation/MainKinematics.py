import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

from time import time
from Kinematics import Kinematics, Rotations
from GraphHelperFuncs.MakeFrame import MakeFrame
from GraphHelperFuncs.MakeArrow import MakeArrow

time_final = 20.

# Initial state values and parameter values
state = np.array([0, 0, 0])
parameters = np.array([1, 1, 1])

# Simulate dynamics
print('Calculating trajectory...')
sol = solve_ivp(fun=lambda t, y: Kinematics(t, y, parameters), t_span=[0, time_final], y0=state)
time_axis = sol.t
statetraj = sol.y
interp1 = interp1d(time_axis, statetraj) # Interpolation operator
print('Trajectory calculated')



class Animation:
    def __init__(self):
        super(Animation, self).__init__()
        self.plotEnv()
        self.initSimItems()

    def initSimItems(self):
        # Initiate frames
        ScaleFrame = 1.0  # Scale factor for frames and arrows
        FS = 15  # Font size
        SW = 0.035  # Arrow size (not implemented)
        o = np.array([0, 0, 0]) # Origin of world frame
        p = np.array([3, 3, 3]) # Origin of body frame
        self.origin = MakeFrame(o, FS, SW, self.ax, name='o', scale=ScaleFrame)
        self.body = MakeFrame(p, FS, SW, self.ax, name='b', scale=ScaleFrame)
        self.arrow = MakeArrow(o, FS, SW, self.ax, name='r', scale=ScaleFrame)

    def plotEnv(self):
        # Initiate plot figure
        self.running = False
        self.fig = plt.figure()
        self.fig.canvas.mpl_connect('button_press_event', self.onclick)
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.set_title('Click to start the animation')
        self.ax.set_xlabel('$x$')
        self.ax.set_ylabel('$y$')
        self.ax.set_zlabel('$z$')
        lim = 5
        self.ax.set_xlim(-lim, lim)
        self.ax.set_ylim(-lim, lim)
        self.ax.set_zlim(-lim, lim)
        plt.ion()  # Enable interactive display
        plt.show()

    def onclick(self, *args, **kwargs):
        if not self.running:
            self.running = True
            self.run()
            self.running = False

    def run(self):
        time_display = 0  # initialise time_display
        t0 = time()  # Initiate t0
        while time_display < time_axis[-1]:
            # interpolate the simulated state at the current clock time
            state_animate = interp1(time_display)

            omega = parameters
            R, M = Rotations(state_animate)

            self.origin.update(np.identity(3))
            self.body.update(R)
            self.arrow.update(self.body.origin)

            self.fig.canvas.draw()
            self.fig.canvas.flush_events()

            time_display = time()-t0 # get the current clock time


animClass = Animation()
input('Press enter to exit')

