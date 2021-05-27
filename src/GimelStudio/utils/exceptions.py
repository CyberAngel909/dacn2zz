

class NodeExistsError(Exception):
    """ This exception is raised when a node is registered
    that already exists in the Node Registry. """

    def __init__(self, name):
        super(NodeExistsError, self).__init__(name)
        self._name = name

    def __str__(self):
        return "The node {} already exists within the registry.".format(self._name)


class NodeNotFoundError(Exception):
    """ This exception is raised when a node is not found in
    the Node Registry. """

    def __init__(self, name):
        super(NodeNotFoundError, self).__init__(name)
        self._name = name

    def __str__(self):
        return """The node {} could not be found in the registry.
        Maybe you forgot to register it? """.format(self._name)
