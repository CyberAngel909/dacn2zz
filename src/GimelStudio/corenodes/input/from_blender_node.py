import os
import os.path
from PIL import Image, ImageOps

from GimelStudio import api
from GimelStudio.renderer import EvalInfo


class ImageFromBlenderNode(api.NodeBase):
    def __init__(self, _id):
        api.NodeBase.__init__(self, _id)


    @property
    def NodeMeta(self):
        meta_info = {
            "label": "Image From Blender",
            "author": "Correct Syntax",
            "version": (0, 5, 0),
            "supported_app_version": (0, 5, 0),
            "category": "INPUT",
            "description": "Add images directly from blender"
        }
        return meta_info

    def QueryBlenderImageLayers(self):
        blender_layers = []
        self._layers = {}

        self._dirname = os.path.expanduser("~/.gimelstudio/blenderaddontemp/")

        for file in os.listdir(self._dirname):
            #print(file)
            filepath = os.path.join(self._dirname, file)
            layername = file.split(".")[0]
            blender_layers.append(layername)
            print(layername)
            self._layers[layername] = filepath

        return blender_layers

    def NodeInitProps(self):
        self.layer_prop = api.ChoiceProp(
            idname="Layer",
            default="",
            label="Layer:",
            choices=self.QueryBlenderImageLayers()
        )

        self.NodeAddProp(self.layer_prop)

    def WidgetEventHook(self, idname, value):
        if idname in ["Layer"]:
            self.RefreshLayers()

    def RefreshLayers(self):
        # Update the thumbnail
        img = self.NodeEvaluation(EvalInfo(self)).GetImage()
        self.NodeSetThumb(img, force_refresh=True)
        self.RefreshPropertyPanel()

        # Update the property choices (only available for ChoiceProp)
        self.layer_prop.SetChoices(self.QueryBlenderImageLayers())

    def NodeEvaluation(self, eval_info):
        layer = eval_info.EvaluateProperty('Layer')

        layer_path = self._layers[layer]

        image = api.RenderImage()

        image.SetAsOpenedImage(layer_path)

        self.NodeSetThumb(image.GetImage())
        return image


api.RegisterNode(ImageFromBlenderNode, "corenode_imagefromblender")
