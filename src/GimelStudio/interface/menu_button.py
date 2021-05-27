
import wx


class MenuButton(object):
    def __init__(
        self, parent, rect=wx.Rect(0, 0, 56, 56), _id=wx.ID_ANY
    ):
        self._parent = parent
        self._rect = rect

        if _id == wx.ID_ANY:
            self._id = wx.NewIdRef()
        else:
            self._id = _id

    def GetParent(self):
        return self._parent

    def GetId(self):
        return self._id

    def SetId(self, id_):
        self._id = id_

    def GetRect(self):
        return self._rect

    def SetRect(self, rect):
        self._rect = rect

    def Draw(self, dc, hide=False):
        dc.ClearId(self.GetId())
        dc.SetId(self.GetId())

        node_count = len(self._parent._nodes)

        if hide == False:
            pos = self._parent.GetMenuButtonWidgetPos()
            self.SetRect(wx.Rect(pos[0] + 15, pos[1] - 20, 56, 56))

            rect = self.GetRect()

            # Button
            dc.SetPen(wx.Pen(wx.Colour("#2B2B2B"), 2))
            dc.SetBrush(wx.Brush(wx.Colour((86, 86, 86, 255))))
            dc.DrawCircle(rect[0] + 32, rect[1] + 32, 30)

            # Drawing of nodes
            dc.SetPen(wx.Pen(wx.Colour("#fff"), 1))
            dc.SetBrush(wx.Brush(wx.Colour("#fff")))
            dc.DrawRectangle(rect[0] + 16, rect[1] + 23, 14, 9)

            dc.SetPen(wx.Pen(wx.Colour("#fff"), 2))
            dc.DrawLine(rect[0] + 28, rect[1] + 26, rect[0] + 34, rect[1] + 38)

            dc.SetPen(wx.Pen(wx.Colour("#fff"), 1))
            dc.DrawRectangle(rect[0] + 34, rect[1] + 35, 14, 9)

            # Info text
            info_text = "Node Graph ({} nodes)".format(node_count)
            dc.SetTextForeground(wx.Colour("#ccc"))
            dc.DrawText(info_text, rect[0] + 78, rect[1] + 20)

            help_text = "Shift+A to add node | LMB to move node or box select | MMB to pan graph"
            dc.SetTextForeground(wx.Colour("#ccc"))
            dc.DrawText(help_text, rect[0] + 78, rect[1] + 40)

        dc.SetIdBounds(self.GetId(), self.GetRect())
