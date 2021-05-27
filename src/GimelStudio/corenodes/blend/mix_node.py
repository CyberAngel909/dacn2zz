from PIL import ImageChops, ImageOps

from GimelStudio import api


class MixNode(api.NodeBase):
    def __init__(self, _id):
        api.NodeBase.__init__(self, _id)

    @property
    def NodeMeta(self):
        meta_info = {
            "label": "Mix",
            "author": "Correct Syntax",
            "version": (1, 8, 5),
            "supported_app_version": (0, 5, 0),
            "category": "BLEND",
            "description": "Layers two images together using the specified blend type.",
        }
        return meta_info

    def NodeInitProps(self):
        p = api.ChoiceProp(
            idname="Blend Mode",
            default="Multiply",
            label="Blend Mode:",
            choices=[
                    'Add',
                    'Add Modulo',
                    'Subtract',
                    'Subtract Modulo',
                    'Multiply',
                    'Screen',
                    'Difference',
                    'Darker',
                    'Lighter',
                    'Soft Light',
                    'Hard Light',
                    'Overlay'
            ]
        )

        self.NodeAddProp(p)

    def NodeInitParams(self):
        p1 = api.RenderImageParam('Image')
        p2 = api.RenderImageParam('Overlay')

        self.NodeAddParam(p1)
        self.NodeAddParam(p2)

    def NodeEvaluation(self, eval_info):
        image1 = eval_info.EvaluateParameter('Image')
        image2 = eval_info.EvaluateParameter('Overlay')
        blendmode = eval_info.EvaluateProperty('Blend Mode')

        image = api.RenderImage()
        main_image = image1.GetImage()
        layer_image = ImageOps.fit(image2.GetImage(), main_image.size)

        if blendmode == 'Add':
            img = ImageChops.add(main_image, layer_image)

        elif blendmode == 'Add Modulo':
            img = ImageChops.add_modulo(main_image, layer_image)

        elif blendmode == 'Subtract':
            img = ImageChops.subtract(main_image, layer_image)

        elif blendmode == 'Subtract Modulo':
            img = ImageChops.subtract_modulo(main_image, layer_image)

        elif blendmode == 'Multiply':
            img = ImageChops.multiply(main_image, layer_image)

        elif blendmode == 'Screen':
            img = ImageChops.screen(main_image, layer_image)

        elif blendmode == 'Difference':
            img = ImageChops.difference(main_image, layer_image)

        elif blendmode == 'Darker':
            img = ImageChops.darker(main_image, layer_image)

        elif blendmode == 'Lighter':
            img = ImageChops.lighter(main_image, layer_image)

        elif blendmode == 'Soft Light':
            img = ImageChops.soft_light(main_image, layer_image)

        elif blendmode == 'Hard Light':
            img = ImageChops.hard_light(main_image, layer_image)

        elif blendmode == 'Overlay':
            img = ImageChops.overlay(main_image, layer_image)

        image.SetAsImage(img)
        self.NodeSetThumb(image.GetImage())
        return image


api.RegisterNode(MixNode, "corenode_mix")
