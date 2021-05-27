import cv2

from GimelStudio import api
from GimelStudio.utils.image import ArrayFromImage, ArrayToImage


class DilateErodeNode(api.NodeBase):
    def __init__(self, _id):
        api.NodeBase.__init__(self, _id)

    @property
    def NodeMeta(self):
        meta_info = {
            "label": "Dilate/Erode",
            "author": "Correct Syntax",
            "version": (0, 5, 0),
            "supported_app_version": (0, 5, 0),
            "category": "FILTER",
            "description": "Applies a morphological operation like Erosion, Dilation, Opening, Closing etc.",
        }
        return meta_info

    def NodeInitProps(self):
        operation = api.ChoiceProp(
            idname="Operation",
            default="Erode",
            choices=["Dilate", "Erode", "Opening", "Closing", "Top Hat", "Black Hat"],
            label="Operation:"
        )
        kernel_shape = api.ChoiceProp(
            idname="Kernel Shape",
            default="Rectangle",
            choices=["Rectangle", "Ellipse", "Cross"],
            label="Kernel Shape:"
        )
        kernel_size = api.PositiveIntegerProp(
            idname="Kernel Size",
            default=5,
            min_val=1,
            max_val=100,
            widget=api.SLIDER_WIDGET,
            label="Kernel Size:"
        )
        self.NodeAddProp(operation)
        self.NodeAddProp(kernel_shape)
        self.NodeAddProp(kernel_size)

    def NodeInitParams(self):
        image = api.RenderImageParam('Image')

        self.NodeAddParam(image)

    def NodeEvaluation(self, eval_info):
        image1 = eval_info.EvaluateParameter('Image')
        kernel_shape = eval_info.EvaluateProperty('Kernel Shape')
        kernel_size = eval_info.EvaluateProperty('Kernel Size')
        operation = eval_info.EvaluateProperty('Operation')

        image = api.RenderImage()

        img = ArrayFromImage(image1.GetImage())

        if kernel_shape == "Rectangle":
            kshape = cv2.MORPH_RECT
        elif kernel_shape == "Ellipse":
            kshape = cv2.MORPH_ELLIPSE
        elif kernel_shape == "Cross":
            kshape = cv2.MORPH_CROSS

        kernel_img = cv2.getStructuringElement(kshape, (kernel_size, kernel_size))

        if operation == "Erode":
            output_img = cv2.erode(img, kernel_img, iterations=1)
        elif operation == "Dilate":
            output_img = cv2.dilate(img, kernel_img, iterations=1)
        elif operation == "Opening":
            output_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel_img)
        elif operation == "Closing":
            output_img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel_img)
        elif operation == "Top Hat":
            output_img = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel_img)
        elif operation == "Black Hat":
            output_img = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel_img)

        image.SetAsImage(ArrayToImage(output_img).convert("RGBA"))

        self.NodeSetThumb(image.GetImage())
        return image


api.RegisterNode(DilateErodeNode, "corenode_dilateerode")
