class Config:

    def __init__(self, *args, **kwargs):
        self.root_path = kwargs.get("root_path") or ""
        self.app_version = kwargs.get("app_version") or "dev"
        self.app_env = kwargs.get("app_env") or "dev"
