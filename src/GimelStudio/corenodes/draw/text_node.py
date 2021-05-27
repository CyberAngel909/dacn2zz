import os
import sys
from PIL import Image, ImageFont, ImageDraw

from GimelStudio import api
from GimelStudio.renderer import EvalInfo


class TextNode(api.NodeBase):
    def __init__(self, _id):
        api.NodeBase.__init__(self, _id)

        self._cachedPath = ""

    @property
    def NodeMeta(self):
        meta_info = {
            "label": "Text",
            "author": "iwoithe",
            "version": (0, 0, 1),
            "supported_app_version": (0, 0, 1),
            "category": "DRAW",
            "description": "Adds text to an image"
        }
        return meta_info

    def NodeInitParams(self):
        image = api.RenderImageParam('Image')

        self.NodeAddParam(image)

    def NodeInitProps(self):
        pos_prop = api.SizeProp(
            idname="Text Position",
            default=[0, 0],
            label="Text Position:"
        )

        text_prop = api.StringProp(
            idname="Text",
            default="Text",
            label="Text:"
        )

        font_prop = api.FontProp(
            idname="Font",
            default="LiberationSans-Regular",
            label="Font:"
        )

        font_size_prop = api.PositiveIntegerProp(
            idname="Font Size",
            default=10,
            min_val=0,
            max_val=10000,
            widget=api.SPINBOX_WIDGET,
            label="Font Size:"
        )

        color_prop = api.ColorProp(
            idname="Font Color",
            default=(0, 0, 0, 255),
            label="Font Color:"
        )

        self.NodeAddProp(pos_prop)
        self.NodeAddProp(text_prop)
        self.NodeAddProp(font_prop)
        self.NodeAddProp(font_size_prop)
        self.NodeAddProp(color_prop)

    def NodeEvaluation(self, eval_info):
        main_image = eval_info.EvaluateParameter('Image')

        text_pos = eval_info.EvaluateProperty('Text Position')
        text = eval_info.EvaluateProperty('Text')
        font = eval_info.EvaluateProperty('Font')
        font_size = eval_info.EvaluateProperty('Font Size')
        font_color = eval_info.EvaluateProperty('Font Color')

        image = api.RenderImage()

        # Create separate image so it doesn't draw on the original image
        text_image = Image.new("RGBA", size=main_image.GetImage().size, color=(0, 0, 0, 1))
        #draw = ImageDraw.Draw(text_image)
        print("before font")
        # # Load the font
        # if sys.platform == "win32":
        #     font_path_prefix = "C:/Windows/Fonts/"
        # elif sys.platform == "linux":
        #     font_path_prefix = "/usr/share/fonts/TTF/"
        # else:
        #     print("WARNING: The text node does not currently support your operating system")
        #     return

        # font_path = font_path_prefix + font + ".ttf"
        #fnt = ImageFont.truetype("arial", font_size)
        # print("after")
        # TODO: Add support for all parameters from ImageDraw.Draw.text
        # Todo: Add support for multiline text
        #draw.multiline_text(text_pos, text, font=fnt, fill=font_color)

        print(font_size, "size")

        draw_text = ImageDraw.Draw(text_image)
        text_font = ImageFont.truetype(font="C:/Windows/Fonts/arial.ttf", size=30)

        # Draw the text
        draw_text.text(
            xy=(0, 0),
            text="text",
            font=text_font,
            fill="black",
            spacing=6,
            align='left',
            stroke_width=1,
            stroke_fill="blue"
        )

        # Composite the two images together
        composited_image = Image.alpha_composite(main_image.GetImage(), text_image)

        image.SetAsImage(composited_image)
        self.NodeSetThumb(image.GetImage())
        print("yes-past")
        return image


# Register the node
api.RegisterNode(TextNode, "corenode_text")
