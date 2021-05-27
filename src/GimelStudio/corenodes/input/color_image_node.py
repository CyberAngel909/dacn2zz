import os
from PIL import Image

from GimelStudio import api
from GimelStudio.renderer import EvalInfo


class ColorImageNode(api.NodeBase):
    def __init__(self, _id):
        api.NodeBase.__init__(self, _id)

    @property
    def NodeMeta(self):
        meta_info = {
            "label": "Color Image",
            "author": "Correct Syntax",
            "version": (1, 1, 0),
            "supported_app_version": (0, 5, 0),
            "category": "INPUT",
            "description": "Creates a blank colored image."
        }
        return meta_info

    def NodeInitProps(self):
        self.color_prop = api.ColorProp(
            idname="Color",
            default=(0, 0, 0, 255),
            label="Image Color:"
        )
        self.size_prop = api.SizeProp(
            idname="Size",
            default=[255, 255],
            label="Image Size:"
        )

        self.NodeAddProp(self.color_prop)
        self.NodeAddProp(self.size_prop)

    def WidgetEventHook(self, idname, value):
        if idname == "Color":
            img = self.NodeEvaluation(EvalInfo(self)).GetImage()
            self.NodeSetThumb(img, force_refresh=True)
            self.RefreshPropertyPanel()

    def NodeEvaluation(self, eval_info):
        color = eval_info.EvaluateProperty('Color')
        imgsize = eval_info.EvaluateProperty('Size')

        image = api.RenderImage()
        image.SetAsImage(Image.new("RGBA", (imgsize[0], imgsize[1]), color))
        self.NodeSetThumb(image.GetImage())
        return image


api.RegisterNode(ColorImageNode, "corenode_colorimage")
