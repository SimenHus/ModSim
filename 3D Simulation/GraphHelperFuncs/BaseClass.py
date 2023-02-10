
class BaseClass:
    'Base class for graphed elements'
    def __init__(self, origin, FS, SW, ax, textPos=1, name='', varargin='', scale=1.0):
        self.ax = ax
        self.FS = FS
        self.SW = SW
        self.name = name
        self.scale = scale
        self.origin = origin
        self.textPos = textPos
        self.varargin = varargin

    def updateArrow(self, end, quiver, text, name=None):
        if not name: name = self.name
        quivDirection = end - self.origin
        quiver.remove()
        text.remove()
        quiver = self.ax.quiver(self.origin[0], self.origin[1], self.origin[2],
                                     quivDirection[0], quivDirection[1], quivDirection[2],
                                     length=self.scale)
        textLoc = self.origin + quivDirection*self.textPos
        text = self.ax.text(textLoc[0], textLoc[1], textLoc[2],
                                 name, fontsize=self.FS)
        return quiver, text
