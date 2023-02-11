from GraphHelperFuncs.BaseClass import BaseClass

class MakeFrame(BaseClass):
    'Class for a single coordinate frame'
    def __init__(self, origin, FS, SW, ax, textPos=1, name='', varargin='', scale=1.0):
        super().__init__(origin, FS, SW, ax, textPos=textPos, name=name, varargin=varargin, scale=scale)

        self.quivers = [ax.quiver(0, 0, 0, 0, 0, 0, length=0) for _ in range(3)]
        self.texts = [ax.text(0, 0, 0, '') for _ in range(3)]

    def setRotation(self, R):
        self.R = R

    def update(self):
        for i, axis in enumerate(['i', 'j', 'k']):
            quivDirection = self.R[:, i]
            endPoint = self.origin + self.scale*quivDirection
            self.quivers[i], self.texts[i] = self.updateArrow(
                self.origin, endPoint, self.quivers[i], self.texts[i], name=f'${axis}\u0302_{self.name}$')

