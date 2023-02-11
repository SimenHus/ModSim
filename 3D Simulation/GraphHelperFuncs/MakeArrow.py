from GraphHelperFuncs.BaseClass import BaseClass

class MakeArrow(BaseClass):
    'Class for a single arrow on the graph'
    def __init__(self, origin, FS, SW, ax, textPos=0.5, name='', varargin='', scale=1.0):
        super().__init__(origin, FS, SW, ax, textPos=textPos, name=name, varargin=varargin, scale=scale)

        self.endpoint = origin
        self.quiver = ax.quiver(0, 0, 0, 0, 0, 0, length=0)
        self.text = ax.text(0, 0, 0, '')

    def update(self):
        self.origin = self.originElement.getOrigin()
        self.endpoint = self.endpointElement.getOrigin()
        self.quiver, self.text = self.updateArrow(self.origin, self.endpoint, self.quiver, self.text)

    def connectEndpoint(self, endpointElement):
        self.endpointElement = endpointElement

    def connectOrigin(self, originElement):
        self.originElement = originElement
