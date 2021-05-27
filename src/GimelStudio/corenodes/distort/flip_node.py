from PIL import ImageOps

from GimelStudio import api


class FlipNode(api.NodeBase):
    def __init__(self, _id):
        api.NodeBase.__init__(self, _id)

    @property
    def NodeMeta(self):
        meta_info = {
            "label": "Flip",
            "author": "iwoithe",
            "version": (0, 0, 1),
            "supported_app_version": (0, 5, 0),
            "category": "DISTORT",
            "description": "Flips the image horizontally or vertically.",
        }
        return meta_info

    def NodeInitProps(self):
        p = api.ChoiceProp(
            idname="Direction",
            default="Horizontal",
            label="Direction:",
            choices=["Horizontal", "Vertical"],
        )
        self.NodeAddProp(p)

    def NodeInitParams(self):
        p = api.RenderImageParam('Image')

        self.NodeAddParam(p)

    def NodeEvaluation(self, eval_info):
        image1 = eval_info.EvaluateParameter('Image')
        direction = eval_info.EvaluateProperty('Direction')

        image = api.RenderImage()

        if direction == 'Horizontal':
            image.SetAsImage(ImageOps.mirror(image1.GetImage()))
        else:
            image.SetAsImage(ImageOps.flip(image1.GetImage()))

        self.NodeSetThumb(image.GetImage().convert("RGBA"))
        return image


api.RegisterNode(FlipNode, "corenode_flip")
