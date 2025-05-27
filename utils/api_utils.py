import curlify
import requests
from requests import Session
from logger.logger import Logger
import json

from utils.json_utils import JsonUtils


def log_response(func):
    def _log_response(*args, **kwargs) -> requests.Response:
        response = func(*args, **kwargs)
        Logger.info(f"Request: {curlify.to_curl(response.request)}")
        body = json.dumps(response.json(), indent=2) if JsonUtils.is_json(response.text) else response.text
        Logger.info(f"Response status code = '{response.status_code}', "
                    f""f"elapsed_time = '{response.elapsed}'\n{body}\n")
        return response
    return _log_response


class ApiUtils:
    def __init__(self, url, headers=None):
        if headers is None:
            headers = {}

        self.session = Session()
        self.session.headers.update(headers)
        self.url = url

    @log_response
    def get(self, endpoint, **kwargs):
        response = self.session.get(self.url + endpoint, **kwargs)
        return response

    @log_response
    def post(self, endpoint, data = None, json = None, **kwargs):
        response = self.session.post(url=self.url + endpoint,
                                     data=data, json=json, **kwargs)
        return response

    @log_response
    def delete(self, endpoint, **kwargs):
        response = self.session.delete(self.url + endpoint, **kwargs)
        return response