
from .model import NodeModel
from .view import NodeView


class NodeObject(object):
    """ Base node object which ties together the model and view. """

    def __init__(self, _id):
        self._model = NodeModel(_id)
        self._view = NodeView(_id)

    @property
    def Model(self):
        """ Return the node model.

        :returns: the node model object.
        """
        return self._model

    @property
    def View(self):
        """ Return the node view.

        :returns: the node view object.
        """
        return self._view

    def UpdateView(self):
        """ Update the view from the model. """
        self.View._viewData = self.Model.ModelViewData
