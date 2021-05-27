import os
from PIL import Image, ImageOps

from GimelStudio import api
from GimelStudio.renderer import EvalInfo


class NoiseImageNode(api.NodeBase):
    def __init__(self, _id):
        api.NodeBase.__init__(self, _id)

    @property
    def NodeMeta(self):
        meta_info = {
            "label": "Noise Image",
            "author": "Correct Syntax",
            "version": (1, 1, 5),
            "supported_app_version": (0, 5, 0),
            "category": "INPUT",
            "description": "Generates a Gaussian noise image centered around 128."
        }
        return meta_info

    def NodeInitProps(self):
        self.sigma_prop = api.PositiveIntegerProp(
            idname="Sigma",
            default=50,
            min_val=1,
            max_val=400,
            widget=api.SLIDER_WIDGET,
            label="Sigma:",
        )
        self.size_prop = api.SizeProp(
            idname="Size",
            default=[255, 255],
            label="Image Size:"
        )

        self.NodeAddProp(self.sigma_prop)
        self.NodeAddProp(self.size_prop)

    def WidgetEventHook(self, idname, value):
        # if idname == "Sigma":
        img = self.NodeEvaluation(EvalInfo(self)).GetImage()
        self.NodeSetThumb(img, force_refresh=True)
        self.RefreshPropertyPanel()

    def NodeEvaluation(self, eval_info):
        sigma = eval_info.EvaluateProperty('Sigma')
        imgsize = eval_info.EvaluateProperty('Size')

        image = api.RenderImage()
        image.SetAsImage(
            Image.effect_noise((imgsize[0], imgsize[1]), sigma).convert("RGBA")
        )
        self.NodeSetThumb(image.GetImage())
        return image


api.RegisterNode(NoiseImageNode, "corenode_noiseimage")
