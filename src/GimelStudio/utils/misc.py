
import os
import platform
import subprocess


def PopOpenExplorer(path):
    """ Method for opening the path in the system's File Explorer or Image viewer.

    Copied directly from:
    https://stackoverflow.com/questions/6631299/python-opening-a-folder-in-explorer-nautilus-finder
    """
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])


def LoadPythonScripts(directory):
    """ Loads python scripts from the given directory. """

    paths = os.listdir(directory)
    for path in paths:
        name, ext = os.path.splitext(path)
        if ext != ".py":
            continue
        node_module = __import__(directory, fromlist=[name])
