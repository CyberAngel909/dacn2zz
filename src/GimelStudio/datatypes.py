
from PIL import Image


class RenderImage(object):
    """ Represents an image data type for the renderer. """

    def __init__(self, size=(100, 100), color=(0, 0, 0, 1), packed_data=None):
        self._img = Image.new("RGBA", (size[0], size[1]), color)
        self._packedData = packed_data

    def GetPILImage(self):
        """ Returns the image.

        :returns: PIL ``Image`` object
        """
        return self._img

    def GetImage(self):
        """ Returns the image.

        :returns: PIL ``Image`` object
        """
        return self._img

    def SetAsOpenedImage(self, path):
        """ Sets the image and opens it. If the image is non-existent,
        it will try to get packed data from the file, if possible.

        :param path: image filepath to be opened
        """
        try:
            self._img = Image.open(path)
        except FileNotFoundError:
            if self._packedData is not None:
                self._img = self._packedData
            else:
                print("WARNING: COULD NOT GET PACKED IMAGE DATA!")

    def SetAsImage(self, image):
        """ Sets the image.

        :param image: PIL ``Image`` object
        """
        self._img = image
