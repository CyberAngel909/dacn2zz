from GimelStudio import api


class OutputNode(api.NodeBase):
    def __init__(self, _id):
        api.NodeBase.__init__(self, _id)
        self.Model._isOutput = True
        self.Model.UpdateSockets()

        self.NodeSetThumb(self.Model.GetThumbImage())

    @property
    def NodeMeta(self):
        meta_info = {
            "label": "Output",
            "author": "Correct Syntax",
            "version": (0, 1, 3),
            "supported_app_version": (0, 5, 0),
            "category": "OUTPUT",
            "description": """The most important node of them all. :)
        This is registered here for the UI -the evaluation is handled elsewhere.
        This node should not be accessed by outside users.
        """
        }
        return meta_info

    def NodeInitParams(self):
        p = api.RenderImageParam('Image')
        self.NodeAddParam(p)

    def NodeEvaluation(self, eval_info):
        pass


api.RegisterNode(OutputNode, "corenode_outputcomposite")
