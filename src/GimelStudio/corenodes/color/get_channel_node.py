from PIL import Image, ImageOps, ImageChops

from GimelStudio import api


class GetChannelNode(api.NodeBase):
    def __init__(self, _id):
        api.NodeBase.__init__(self, _id)

    @property
    def NodeMeta(self):
        meta_info = {
            "label": "Get Channel",
            "author": "Correct Syntax",
            "version": (0, 5, 0),
            "supported_app_version": (0, 5, 0),
            "category": "COLOR",
            "description": "Gets a single channel from the image RGBA channels.",
        }
        return meta_info

    def NodeInitProps(self):
        p1 = api.ChoiceProp(
            idname="Image Channel",
            default="R",
            label="Image Channel:",
            choices=[
                    'R',
                    'G',
                    'B',
                    'A'
            ]
        )
        p2 = api.BooleanProp(
            idname="Greyscale",
            default=False,
            label="Greyscale:",
            cb_label="Greyscale image channel"
        )

        self.NodeAddProp(p1)
        self.NodeAddProp(p2)

    def NodeInitParams(self):
        image = api.RenderImageParam("Image")
        self.NodeAddParam(image)

    def NodeEvaluation(self, eval_info):
        image1 = eval_info.EvaluateParameter('Image')
        channel = eval_info.EvaluateProperty('Image Channel')
        greyscale = eval_info.EvaluateProperty('Greyscale')

        image = api.RenderImage()
        channel_img = image1.GetImage().getchannel(channel)

        if greyscale != True and channel != "A":
            if channel == "R":
                color = (255, 0, 0)
            elif channel == "G":
                color = (0, 255, 0)
            elif channel == "B":
                color = (0, 0, 255)
            final_img = ImageOps.colorize(channel_img, (0, 0, 0), color)

        elif channel == "A":
            inverted_img = ImageChops.invert(channel_img)
            new_img = Image.new("RGBA", inverted_img.size, (0, 0, 0, 0))

            layer_image = ImageOps.fit(new_img, inverted_img.size)
            mask_image = ImageOps.fit(image1.GetImage(), inverted_img.size)

            final_img = Image.composite(inverted_img, layer_image, mask_image)

        else:
            final_img = channel_img

        image.SetAsImage(final_img.convert("RGBA"))

        self.NodeSetThumb(image.GetImage())
        return image


api.RegisterNode(GetChannelNode, "corenode_getchannel")
