

class EvalInfo(object):
    """
    Evaluate node properties and parameters
    """

    def __init__(self, node):
        if node == None:
            raise TypeError
        self.node = node

    def EvaluateParameter(self, name):
        """
        Evaluates the value of a parameter.
        """
        p = self.node.Parameters[name]
        if p.binding:
            # Make sure the next node is not disabled
            if p.binding.IsMuted() != True:
                # Evaluate the next node
                info = EvalInfo(p.binding)
                return p.binding.EvaluateNode(info)
        return p.value

    def EvaluateProperty(self, name):
        """
        Evaluates the value of a property.
        """
        p = self.node.Properties[name]
        return p.value
