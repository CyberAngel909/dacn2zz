
from threading import *

import wx


# Define notification event for thread completion
EVT_RESULT_ID = wx.NewIdRef()


def EVT_RENDER_RESULT(win, func):
    """ Define result event """
    win.Connect(-1, -1, EVT_RESULT_ID, func)


class ResultEvent(wx.PyEvent):
    """ Simple event to carry arbitrary result data """

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_RESULT_ID)
        self.data = data


class RenderThread(Thread):
    """ Thread class that executes processing """

    def __init__(self, parent):
        """ Init the worker thread"""
        Thread.__init__(self)
        self._parent = parent
        # Starts the thread running
        self.start()

    def run(self):
        """ Run the worker thread """
        # Code executing in the new thread.
        render_image = self._parent._renderer.Render(self._parent._nodeGraph.GetNodes())

        # The result returned
        wx.PostEvent(self._parent, ResultEvent(render_image))
