import json as jsonlib

import os
from collections import deque
from concurrent import futures
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Dict, List, Optional, Union

import requests
from requests.adapters import HTTPAdapter, Retry
from urllib3 import Retry

import lotr
from lotr.error import CustomError
from lotr.logging import logger
from lotr.utils import is_api_key_valid, auth_formatter


class Client:
    """LOTR Client

    Args:
        api_key (str): API Key, see : https://the-one-api.dev/account
        check_api_key (bool): Whether to check the api key for validity on initialization.
        max_retries (int): maximal number of retries for requests.
        timeout (int): request timeout in seconds.
    """

    def __init__(
        self,
        api_key: str = None,
        check_api_key: bool = True,
        max_retries: int = 3,
        timeout: int = 10,
    ) -> None:
        self.api_key = api_key or os.getenv("LOTR_API_KEY")
        self.api_url = lotr.LOTR_API_URL
        self.endpoint = lotr.END_POINT
        self.max_retries = max_retries
        self.timeout = timeout
        self.sdk_meta = {'version':f"v{lotr.API_VERSION}", 'language': 'python'}

        if check_api_key:
            self.check_api_key()

    def check_api_key(self) -> Dict[str, bool]:
        """
        Checks the api key for validity
        """
        return {"valid": is_api_key_valid(self.api_key)}

  
    def get_movies(self):
        """
        Get list of movies
        """
        headers = auth_formatter(self.api_key)
        session = requests.Session()
        retries = Retry(total = self.max_retries, allowed_methods=['GET'], backoff_factor= 0.5, status_forcelist=lotr.RETRY_STATUS_CODES)
        session.mount('https://', HTTPAdapter(max_retries= self.max_retries))
        _url = self.api_url+self.endpoint
        try:
            response = session.request('GET', _url,
                                       headers=headers,
                                       json=None,
                                       timeout=self.timeout)
        except:
            raise CustomError(message=f'Request to LOTR api provider timed out after {self.max_retries}')
        try:
            json_response = response.json()
        except:
            raise CustomError(message='Failed to decode JSON body.')
        movie_list = json_response.get('docs',None)

        return jsonlib.dumps(movie_list)

    def get_movie_info(self, _id=None,  name=None):
        """
        Get list of movies either by name or id
        name (str): name of the movie in full or key words in the title.
        _id (str): movie id of the recieved list from get_movie function
        """
        if not name and not _id:
            return CustomError(message="No movie name or id is provided!")
        headers = auth_formatter(self.api_key)
        session = requests.Session()
        retries = Retry(total = self.max_retries, allowed_methods=['GET'], backoff_factor= 0.5, status_forcelist=lotr.RETRY_STATUS_CODES)
        session.mount('https://', HTTPAdapter(max_retries= self.max_retries))
        if not name:
            _url = self.api_url+self.endpoint+ str(_id)
        else:
            _url = self.api_url+self.endpoint+ f'?name=/{name}/i'
        try:
            response = session.request('GET', _url,
                                       headers=headers,
                                       json=None,
                                       timeout=self.timeout)
        except:
            raise CustomError(message=f'Request to LOTR api provider timed out after {self.max_retries}')
        try:
            json_response = response.json()
        except:
            raise CustomError(message='Failed to decode JSON body.')
        movie_list = json_response.get('docs',None)
        
        return jsonlib.dumps(movie_list)
    
    def get_movie_quote(self, _id):
        """
        Get movie quotes either by movie name or id
        name (str): name of the movie or part of the movie
        _id (str): movie id of the recieved list from get_movie function
        """
        headers = auth_formatter(self.api_key)
        session = requests.Session()
        retries = Retry(total = self.max_retries, allowed_methods=['GET'], backoff_factor= 0.5, status_forcelist=lotr.RETRY_STATUS_CODES)
        session.mount('https://', HTTPAdapter(max_retries= self.max_retries))
        _url = self.api_url+self.endpoint+ str(_id) +'/quote'
        try:
            response = session.request('GET', _url,
                                       headers=headers,
                                       json=None,
                                       timeout=self.timeout)
        except:
            raise CustomError(message=f'Request to LOTR api provider timed out after {self.max_retries}')
        try:
            json_response = response.json()
        except:
            raise CustomError(message='Failed to decode JSON body.')
        movie_list = json_response.get('docs',None)
        if not movie_list:
            raise CustomError(message='Quotes are only available for the LotR trilogy')
        
        quotes = deque() # faster for appending operation than list

        for elem in movie_list:
            quotes.appendleft(elem.get('dialog'))
            
        return jsonlib.dumps(list(quotes))