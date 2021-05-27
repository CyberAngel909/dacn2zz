
import wx
import wx.lib.dialogs

from GimelStudio import meta


class LicenseDialog(object):
    def __init__(self, parent):
        self._parent = parent

    def ShowDialog(self):
        LICENSE_TEXT = """
Gimel Studio (C) 2021-2022 by dragon. All rights reserved.



        """.format(
            meta.APP_VERSION[0],
            meta.APP_VERSION[1],
            meta.APP_VERSION[2],
            meta.APP_VERSION_TAG
        )

        dlg = wx.lib.dialogs.ScrolledMessageDialog(
            self._parent,
            LICENSE_TEXT,
            "Gimel Studio License",
            size=(600, 750)
        )
        dlg.ShowModal()
