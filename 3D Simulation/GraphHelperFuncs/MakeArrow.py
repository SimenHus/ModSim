from GraphHelperFuncs.BaseClass import BaseClass

class MakeArrow(BaseClass):
    'Class for a single arrow on the graph'
    def __init__(self, origin, FS, SW, ax, textPos=0.5, name='', varargin='', scale=1.0):
        super().__init__(origin, FS, SW, ax, textPos=textPos, name=name, varargin=varargin, scale=scale)

        self.quiver = ax.quiver(0, 0, 0, 0, 0, 0, length=0)
        self.text = ax.text(0, 0, 0, '')
        self.textPos = 0.5 # Middle of the arrow

    def update(self, end, newOrigin=False):
        if newOrigin: self.origin = newOrigin
        self.quiver, self.text = self.updateArrow(end, self.quiver, self.text)

