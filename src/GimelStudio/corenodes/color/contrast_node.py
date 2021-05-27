from PIL import ImageEnhance

from GimelStudio import api


class ContrastNode(api.NodeBase):
    def __init__(self, _id):
        api.NodeBase.__init__(self, _id)

    @property
    def NodeMeta(self):
        meta_info = {
            "label": "Contrast",
            "author": "Correct Syntax",
            "version": (1, 2, 0),
            "supported_app_version": (0, 5, 0),
            "category": "COLOR",
            "description": "Adjusts the image contrast.",
        }
        return meta_info

    def NodeInitProps(self):
        p = api.PositiveIntegerProp(
            idname="Amount",
            default=1,
            min_val=1,
            max_val=50,
            widget=api.SLIDER_WIDGET,
            label="Amount:",
        )
        self.NodeAddProp(p)

    def NodeInitParams(self):
        p = api.RenderImageParam('Image')

        self.NodeAddParam(p)

    def NodeEvaluation(self, eval_info):
        image1 = eval_info.EvaluateParameter('Image')
        amount = eval_info.EvaluateProperty('Amount')

        image = api.RenderImage()
        enhancer = ImageEnhance.Contrast(image1.GetImage())
        image.SetAsImage(enhancer.enhance(amount).convert('RGBA'))

        self.NodeSetThumb(image.GetImage())
        return image


api.RegisterNode(ContrastNode, "corenode_contrast")
