from api_with_context.context import Context


class ApiAlreadyLoadedWithContext(Exception):
    pass


class Api:
    def __init__(self):
        self.context = None

    def load_context(self, context: Context):
        if self.context is None:
            self.context = context
        else:
            raise ApiAlreadyLoadedWithContext

    @property
    def id(self):
        return self.context.id

    @property
    def folder(self):
        return self.context.folder


awesome_api: Api = Api()

