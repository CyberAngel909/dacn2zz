from PIL import ImageFilter

from GimelStudio import api


class EffectSpreadNode(api.NodeBase):
    def __init__(self, _id):
        api.NodeBase.__init__(self, _id)

    @property
    def NodeMeta(self):
        meta_info = {
            "label": "Effect Spread",
            "author": "Correct Syntax",
            "version": (1, 1, 0),
            "supported_app_version": (0, 5, 0),
            "category": "FILTER",
            "description": "Randomly spreads the pixels in the image.",
        }
        return meta_info

    def NodeInitProps(self):
        p = api.PositiveIntegerProp(
            idname="Distance",
            default=1,
            min_val=0,
            max_val=50,
            widget=api.SLIDER_WIDGET,
            label="Distance:",
        )
        self.NodeAddProp(p)

    def NodeInitParams(self):
        p = api.RenderImageParam('Image')

        self.NodeAddParam(p)

    def NodeEvaluation(self, eval_info):
        image1 = eval_info.EvaluateParameter('Image')
        distance = eval_info.EvaluateProperty('Distance')

        image = api.RenderImage()
        image.SetAsImage(image1.GetImage().effect_spread(distance))
        self.NodeSetThumb(image.GetImage())
        return image


api.RegisterNode(EffectSpreadNode, "corenode_effectspread")
