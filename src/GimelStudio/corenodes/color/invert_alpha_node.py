from PIL import ImageChops

from GimelStudio import api


class InvertAlphaNode(api.NodeBase):
    def __init__(self, _id):
        api.NodeBase.__init__(self, _id)

    @property
    def NodeMeta(self):
        meta_info = {
            "label": "Invert Alpha",
            "author": "Correct Syntax",
            "version": (1, 2, 0),
            "supported_app_version": (0, 5, 0),
            "category": "COLOR",
            "description": "Inverts the image alpha channel.",
        }
        return meta_info

    def NodeInitParams(self):
        p = api.RenderImageParam('Image')

        self.NodeAddParam(p)

    def NodeEvaluation(self, eval_info):
        image1 = eval_info.EvaluateParameter('Image')

        image = api.RenderImage()
        image.SetAsImage(ImageChops.invert(image1.GetImage()).convert('RGBA'))
        self.NodeSetThumb(image.GetImage())
        return image


api.RegisterNode(InvertAlphaNode, "corenode_invertalpha")
