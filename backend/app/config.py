

class Config:


    def __init__(self, *args, **kwargs):
        self.root_path = kwargs.get("root_path") or ""
