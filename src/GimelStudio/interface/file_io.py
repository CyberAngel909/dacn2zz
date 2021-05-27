
import os

import wx

from GimelStudio import utils
from GimelStudio.file_support import SupportFTSave


def ExportImageAs(parent, image):
    """ Method defining image export.

    :param parent: MainApplication class
    :param image: Rendered image to export
    """
    wildcard = "JPG file (*.jpg)|*.jpg|" \
        "JPEG file (*.jpeg)|*.jpeg|" \
        "PNG file (*.png)|*.png|" \
        "BMP file (*.bmp)|*.bmp|" \
        "GIF file (*.gif)|*.gif|" \
        "EPS file (*.eps)|*.eps|" \
        "PCX file (*.pcx)|*.pcx|" \
        "XBM file (*.xbm)|*.xbm|" \
        "WEBP file (*.webp)|*.webp|" \
        "TGA file (*.tga)|*.tga|" \
        "TIFF file (*.tiff)|*.tiff|" \
        "All files (*.*)|*.*"

    dlg = wx.FileDialog(
        parent,
        message="Export rendered image as...",
        defaultDir=os.getcwd(),
        defaultFile="untitled.png",
        wildcard=wildcard,
        style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
    )
    dlg.Center()

    # This sets the default filter that the user will initially see.
    # Otherwise, the first filter in the list will be used by default.
    dlg.SetFilterIndex(11)

    if dlg.ShowModal() == wx.ID_OK:
        path = dlg.GetPath()
        filetype = os.path.splitext(path)[1]

        if filetype not in SupportFTSave(list_all=True):
            dlg = wx.MessageDialog(
                None,
                "That file type isn't currently supported!",
                "Cannot Save Image!",
                style=wx.ICON_EXCLAMATION
            )
            dlg.ShowModal()

        else:

            # Export the image with the export options
            utils.ExportRenderedImageToFile(
                image,
                path
            )

            utils.PopOpenExplorer(path)

            notify = wx.adv.NotificationMessage(
                title="Image Exported Sucessfully",
                message="Your image was exported to \n {}".format(path),
                parent=None, flags=wx.ICON_INFORMATION)
            notify.Show(timeout=2)  # 1 for short timeout, 100 for long timeout

    dlg.Destroy()
