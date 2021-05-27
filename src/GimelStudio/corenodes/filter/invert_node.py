from PIL import ImageOps

from GimelStudio import api


class InvertNode(api.NodeBase):
    def __init__(self, _id):
        api.NodeBase.__init__(self, _id)

    @property
    def NodeMeta(self):
        meta_info = {
            "label": "Invert",
            "author": "iwoithe",
            "version": (0, 0, 1),
            "supported_app_version": (0, 5, 0),
            "category": "FILTER",
            "description": "Inverts the image.",
        }
        return meta_info

    def NodeInitParams(self):
        image = api.RenderImageParam("Image")
        self.NodeAddParam(image)

    def NodeEvaluation(self, eval_info):
        image1 = eval_info.EvaluateParameter('Image')

        image = api.RenderImage()
        image.SetAsImage(
            ImageOps.invert(image1.GetImage().convert("RGB")).convert("RGBA")
        )

        self.NodeSetThumb(image.GetImage())
        return image


api.RegisterNode(InvertNode, "corenode_invert")
