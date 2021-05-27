
from GimelStudio.datatypes import RenderImage


class Parameter(object):
    def __init__(self, idname, default):
        self.idname = idname
        self.default = default
        self.binding = None

    @property
    def IdName(self):
        """ Gets the name identifier of the parameter.
        :return: the name of the parameter.
        """
        return self.idname

    def GetDefault(self):
        return self.default

    def SetBinding(self, binding):
        self.binding = binding


class RenderImageParam(Parameter):
    def __init__(self, idname, default=RenderImage()):
        Parameter.__init__(self, idname, default)
        self.value = default

    def GetValue(self):
        return self.value

    def SetValue(self, value):
        self.value = value
