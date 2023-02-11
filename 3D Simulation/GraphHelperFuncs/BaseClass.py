
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

    def setOrigin(self, origin):
        self.origin = origin
    
    def getOrigin(self):
        return self.origin

    def updateArrow(self, origin, end, quiver, text, name=None):
        if not name: name = self.name
        quivDirection = end - origin
        quiver.remove()
        text.remove()
        quiver = self.ax.quiver(origin[0], origin[1], origin[2],
                                     quivDirection[0], quivDirection[1], quivDirection[2],
                                     length=self.scale)
        textLoc = origin + quivDirection*self.textPos
        text = self.ax.text(textLoc[0], textLoc[1], textLoc[2],
                                 name, fontsize=self.FS)
        return quiver, text
