from utils.api_utils import ApiUtils


class BaseService:
    SERVICE_URL = None # Should be redefined

    def __init__(self, api_utils: ApiUtils):
        self.api_utils = api_utils