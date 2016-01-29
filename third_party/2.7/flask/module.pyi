from .blueprints import Blueprint

class Module(Blueprint):
    def __init__(self, import_name, name=None, url_prefix=None,
                 static_path=None, subdomain=None): ...
