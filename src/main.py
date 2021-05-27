import argparse
import wx

from GimelStudio.meta import APP_TITLE, APP_DEBUG
from GimelStudio.application import MainApplication
from GimelStudio.program import StartupSplashScreen

# Fix blurry text on Windows 10
# from https://stackoverflow.com/questions/50884283/how-to-fix-blurry-text-in-wxpython-controls-on-windows
import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except Exception:
    pass


if __name__ == '__main__':

    # Parse the arguments to see if a file is given, otherwise
    # fallback on the default Gimel Studio project file.
    parser = argparse.ArgumentParser(description=APP_TITLE)
    parser.add_argument('file', nargs='?', default='DEFAULT_FILE',
                        help='open a GIMEL-STUDIO-PROJECT file or a supported image file in Gimel Studio (Not yet implemented)')
    parser.add_argument('--blender', default='',
                        help='file path for communicating internally to integrate with the Blender Gimel Studio Addon')
    args = parser.parse_args()

    # Create the app and startup
    app = wx.App(redirect=False)
    frame = MainApplication(arguments=args)

    # Only show the splash-screen if APP_DEBUG is False
    # and Gimel Studio is not launched via the Blender addon.
    if APP_DEBUG is not False:
        if args.blender == "":
            splash = StartupSplashScreen()
            splash.Show()

    frame.Show()
    app.SetTopWindow(frame)
    app.MainLoop()
