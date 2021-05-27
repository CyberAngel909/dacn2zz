
import os
import wx
from PIL import Image

from GimelStudio.utils import GetFileExt
from GimelStudio.file_support import SupportFTOpen


class NodeGraphDropTarget(wx.DropTarget):
    def __init__(self, window, *args, **kwargs):
        super(NodeGraphDropTarget, self).__init__(*args, **kwargs)
        self._window = window
        self._composite = wx.DataObjectComposite()
        self._textDropData = wx.TextDataObject()
        self._fileDropData = wx.FileDataObject()
        self._composite.Add(self._textDropData)
        self._composite.Add(self._fileDropData)
        self.SetDataObject(self._composite)

    def OnDrop(self, x, y):
        return True

    def OnData(self, x, y, result):
        self.GetData()
        formatType, formatId = self.GetReceivedFormatAndId()
        if formatType in (wx.DF_TEXT, wx.DF_UNICODETEXT):
            return self.OnTextDrop()
        elif formatType == wx.DF_FILENAME:
            return self.OnFileDrop()

    def GetReceivedFormatAndId(self):
        _format = self._composite.GetReceivedFormat()
        formatType = _format.GetType()
        try:
            formatId = _format.GetId()  # May throw exception on unknown formats
        except:
            formatId = None
        return formatType, formatId

    def OnTextDrop(self):
        try:
            node = self._window.AddNode(self._textDropData.GetText(), where="CURSOR")
        except Exception as error:
            self.ShowError(error)
        return wx.DragCopy

    def OnFileDrop(self):
        for filename in self._fileDropData.GetFilenames():
            try:
                ext = GetFileExt(filename, add_dot=True)
                if ext.lower() in SupportFTOpen(list_all=True):
                    if os.path.exists(filename) == True:
                        # Create Image node with path
                        node = self._window.AddNode("corenode_image", where="CURSOR")
                        node.NodeEditProp(idname="File Path",
                                          value=filename, render=False)

                        # Set initial thumb for Image node
                        img = Image.open(filename)
                        node.NodeSetThumb(img, force_refresh=True)
                    else:
                        self.ShowError()

                else:
                    dlg = wx.MessageDialog(
                        None,
                        "That file type isn't currently supported!",
                        "Cannot Open File!",
                        style=wx.ICON_EXCLAMATION
                    )
                    dlg.ShowModal()
                    return False

            except Exception as error:
                self.ShowError(error)

        return wx.DragCopy

    def ShowError(self, error=""):
        dlg = wx.MessageDialog(
            None,
            "Error \n {}!".format(str(error)),
            "Error!",
            style=wx.ICON_ERROR
        )
        dlg.ShowModal()
        return False
