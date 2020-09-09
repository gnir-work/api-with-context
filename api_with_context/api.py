from api_with_context.context import Context


class ApiAlreadyLoadedWithContext(Exception):
    pass


class ApiWithoutContext(Exception):
    pass


class Api:
    def __init__(self):
        self._context = None

    def load_context(self, context: Context):
        if self._context is None:
            self._context = context
        else:
            raise ApiAlreadyLoadedWithContext

    @property
    def context(self):
        if self._context:
            return self._context
        else:
            raise ApiWithoutContext

    @property
    def id(self):
        return self.context.id

    @property
    def folder(self):
        return self.context.folder


awesome_api: Api = Api()
