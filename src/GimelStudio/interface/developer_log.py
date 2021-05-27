
import sys

import wx

from GimelStudio import meta


class RedirectText(object):
    def __init__(self, textctrl):
        self.out = textctrl

    def write(self, string):
        self.out.WriteText(string)


class DeveloperLog(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        sizer = wx.BoxSizer(wx.VERTICAL)

        developer_log = wx.TextCtrl(self,
                                    wx.ID_ANY, style=wx.TE_READONLY | wx.TE_MULTILINE)
        sizer.Add(developer_log, 1, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(sizer)

        developer_log.SetBackgroundColour("black")
        developer_log.SetForegroundColour("white")

        redirect = RedirectText(developer_log)

        # Only redirect if APP_DEBUG is not True
        # so that the stdout and stderr go to the
        # Python console during development.
        if meta.APP_DEBUG == False:
            sys.stdout = redirect
            sys.stderr = redirect
