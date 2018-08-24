import os
import json
import requests

API_KEY = os.environ.get('OMDB_API_KEY', None)
API_VERSION = os.environ.get('OMDB_API_VERSION', 1)


class APIKeyError(Exception):
    pass


class APIKeyVersion(Exception):
    pass


class OMDB(object):
    uri = 'http://www.omdbapi.com'
    api_params = {'apikey': API_KEY, 'v': API_VERSION}

    def __init__(self):
        self.session = requests.Session()
        if not API_KEY:
            raise APIKeyError

        if not API_VERSION:
            raise APIKeyVersion

    def _request(self, params=None):
        params.update(self.api_params)
        response = self.session.get(self.uri, params=params)

        response.raise_for_status()
        response.encoding = 'utf-8'
        return response.json()

    def search(self, pattern):
        params = {'s': pattern}
        response = self._request(params)

        media = []

        if response['Response'] == 'True':
            media = response['Search']

            total_results = int(response['totalResults'])

            pages_left = int((total_results - 1) / 10)
            next_page = 2

            while pages_left > 0:
                params.update({'page': next_page})
                response = self._request(params)
                media += response['Search']

                pages_left -= 1
                next_page += 1

        return media

    def get_by_id(self, id):
        params = {'i': id}
        response = self._request(params)
        return response if response['Response'] == 'True' else {}

    def get_by_title(self, title):
        params = {'t': title}
        response = self._request(params)
        return response if response['Response'] == 'True' else {}
