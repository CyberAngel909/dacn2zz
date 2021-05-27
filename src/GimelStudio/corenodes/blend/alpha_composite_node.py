import cv2
import numpy as np
from GimelStudio.utils.image import ArrayFromImage, ArrayToImage
from GimelStudio.model.srgan import generator
from GimelStudio import api
from GimelStudio.model import resolve_single

class AlphaCompositeNode(api.NodeBase):
    def __init__(self, _id):
        api.NodeBase.__init__(self, _id)

    @property
    def NodeMeta(self):
        meta_info = {
            "label": "Alpha Composite",
            "author": "Correct Syntax",
            "version": (1, 2, 0),
            "supported_app_version": (0, 5, 0),
            "category": "BLEND",
            "description": "Creates a new image by interpolating between two input images, using a constant alpha.",
        }
        return meta_info

    def NodeInitParams(self):
        image = api.RenderImageParam('Image')

        self.NodeAddParam(image)

    def NodeEvaluation(self, eval_info):
        image1 = eval_info.EvaluateParameter('Image')

        image = api.RenderImage()

        img0 = ArrayFromImage(image1.GetImage())
        img = np.float32(img0)[:,:,:3]
        model = generator()
        model.load_weights('weights/srgan/gan_generator.h5')
        output_img = resolve_single(model, img)
        image.SetAsImage(ArrayToImage(output_img).convert('RGBA'))

        self.NodeSetThumb(image.GetImage())
        return image


api.RegisterNode(AlphaCompositeNode, "corenode_alphacomposite")
