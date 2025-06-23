# -*- coding: utf-8 -*-

# author: JaeHyuk Kim <goct8@naver.com>
# version: 0.0.7 / External ver.
# Copyright 2022. goct8(JaeHyuk Kim) All rights reserved.

import json
import time
import logging
import requests

from typing import Union, Literal, Optional

from common.exceptions import ExternalRequestError


class HTTPException(Exception):
    """Base class for HTTP exceptions."""
    def __init__(self, status_code: int, message: str = "Unknown HTTP error occurred"):
        self.status_code = status_code
        self.message = message
        super().__init__(f"[{status_code}] {message}")


class HTTPClientError(HTTPException):
    """Exception for HTTP 4xx client errors."""
    def __init__(self, status_code: int, message: str = "Client error occurred"):
        if not (400 <= status_code < 500):
            raise ValueError("HTTPClientError should have a 4xx status code")
        super().__init__(status_code, message)


class HTTPServerError(HTTPException):
    """Exception for HTTP 5xx server errors."""
    def __init__(self, status_code: int, message: str = "Server error occurred"):
        if not (500 <= status_code < 600):
            raise ValueError("HTTPServerError should have a 5xx status code")
        super().__init__(status_code, message)


class MaxRetryError(Exception):
    pass


class ExternalRequest:
    """
    A class to perform HTTP requests with features like retry logic, timeout handling, redirect handling, etc.

    :param total: The total number of attempts to make for a request.
    :param retry_interval: The interval between retries in seconds.
    :param timeout: The timeout for each individual request in seconds, not including the total time for retries.
    :param verify: Whether to verify the server's TLS certificate.
    :param redirect: Whether to follow redirects. If set to True, the class will follow redirects, otherwise, it won't.
    """
    def __init__(self, total: int = 3, retry_interval: float = 0.5,
                 timeout: int = 3, verify: bool = False, redirect: bool = True):
        self.logger = logging.getLogger("external")
        self.total = total
        self.retry_interval = retry_interval
        self.timeout = timeout
        self.verify = verify
        self.redirect = redirect

        requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

    def request(self, method: Literal["GET", "POST", "PUT", "PATCH", "HEAD", "OPTIONS", "DELETE"], url: str,
                params: Optional[dict] = None, headers: Optional[dict] = None, cookies: Optional[dict] = None,
                body: Union[str, dict, None] = None, **kwargs) -> Optional[requests.Response]:
        """
        Performs the HTTP request based on the given method.

        :param method: The HTTP method (GET, POST, PUT, PATCH, HEAD, OPTIONS, DELETE).
        :param url: The URL to send the request to.
        :param params: The URL parameters.
        :param headers: The request headers.
        :param cookies: The request cookies.
        :param body: The request body.
        :param kwargs: Arbitrary keyword arguments that can be passed to `requests.request`.
        :raises MaxRetryError: An HTTP request exceeded the maximum number of retries.
        :raises TypeError: If the provided `body` cannot be serialized to JSON.
        :return: The HTTP response if successful, None otherwise.
        """
        if params is None:
            params = {}
        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}
        if isinstance(body, (dict, list)):
            try:
                body = json.dumps(body)
                headers.setdefault("Content-Type", "application/json")
            except TypeError as error:
                raise TypeError(
                    "Failed to serialize `body` to JSON. Ensure it contains only JSON serializable types."
                ) from error

        for index in range(self.total):
            if index != 0:
                time.sleep(self.retry_interval)

            self.logger.info(
                f"{method}{f' - Retry({index}/{self.total-1})' if index != 0 else ''} - URL('{url}')"
                f"{f' - Params({params})' if params else ''}"
                f"{f' - Headers({headers})' if headers else ''}"
                f"{f' - Cookies({cookies})' if cookies else ''}"
                f"{f' - Body({body})' if body else ''}"
            )

            try:
                response = requests.request(
                    method=method,
                    url=url,
                    params=params,
                    headers=headers,
                    cookies=cookies,
                    data=body if method in ["POST", "PUT", "PATCH"] else None,
                    timeout=self.timeout,
                    verify=self.verify,
                    allow_redirects=self.redirect,
                    **kwargs
                )

                if 100 > response.status_code >= 600:
                    raise HTTPException(response.status_code)

                if 400 <= response.status_code < 500:
                    if index+1 == self.total:
                        return response
                    raise HTTPClientError(response.status_code)

                if 500 <= response.status_code < 600:
                    if index+1 == self.total:
                        return response
                    raise HTTPServerError(response.status_code)

                return response

            except Exception as error:
                if index+1 != self.total:
                    self.logger.warning(
                        f"{method}{f' - Retry({index}/{self.total-1})' if index != 0 else ''} - URL('{url}')"
                        f"{f' - Params({params})' if params else ''}"
                        f"{f' - Headers({headers})' if headers else ''}"
                        f"{f' - Cookies({cookies})' if cookies else ''}"
                        f"{f' - Body({body})' if body else ''}"
                        f" - Exception({error})"
                    )
                else:
                    self.logger.error(
                        f"{method}{f' - Retry({index}/{self.total-1})' if index != 0 else ''} - URL('{url}')"
                        f"{f' - Params({params})' if params else ''}"
                        f"{f' - Headers({headers})' if headers else ''}"
                        f"{f' - Cookies({cookies})' if cookies else ''}"
                        f"{f' - Body({body})' if body else ''}"
                        f" - Exception({error})"
                    )
                    # raise MaxRetryError(f"Maximum retry attempts exceeded - URL('{url}') - Total({self.total})")
                    raise ExternalRequestError()
        return None

    def get(self, url: str, params: Optional[dict] = None, headers: Optional[dict] = None,
            cookies: Optional[dict] = None, **kwargs) -> Optional[requests.Response]:
        """
        Perform a GET request.

        :param url: The URL to send the request to.
        :param params: The URL parameters.
        :param headers: The request headers.
        :param cookies: The request cookies.
        :param kwargs: Arbitrary keyword arguments that can be passed to `requests.request`.
        :return: The HTTP response if successful, None otherwise.
        """
        return self.request(
            method="GET",
            url=url,
            params=params,
            headers=headers,
            cookies=cookies,
            **kwargs
        )

    def post(self, url: str, params: Optional[dict] = None, body: Optional[dict] = None, headers: Optional[dict] = None,
             cookies: Optional[dict] = None, **kwargs) -> Optional[requests.Response]:
        """
        Perform a POST request.

        :param url: The URL to send the request to.
        :param params: The URL parameters.
        :param body: The request body.
        :param headers: The request headers.
        :param cookies: The request cookies.
        :param kwargs: Arbitrary keyword arguments that can be passed to `requests.request`.
        :return: The HTTP response if successful, None otherwise.
        """
        return self.request(
            method="POST",
            url=url,
            params=params,
            body=body,
            headers=headers,
            cookies=cookies,
            **kwargs
        )

    def put(self, url: str, params: Optional[dict] = None, body: Optional[dict] = None, headers: Optional[dict] = None,
            cookies: Optional[dict] = None, **kwargs) -> Optional[requests.Response]:
        """
        Perform a PUT request.

        :param url: The URL to send the request to.
        :param params: The URL parameters.
        :param body: The request body.
        :param headers: The request headers.
        :param cookies: The request cookies.
        :param kwargs: Arbitrary keyword arguments that can be passed to `requests.request`.
        :return: The HTTP response if successful, None otherwise.
        """
        return self.request(
            method="PUT",
            url=url,
            params=params,
            body=body,
            headers=headers,
            cookies=cookies,
            **kwargs
        )

    def patch(self, url: str, params: Optional[dict] = None, body: Optional[dict] = None,
              headers: Optional[dict] = None, cookies: Optional[dict] = None, **kwargs) -> Optional[requests.Response]:
        """
        Perform a PATCH request.

        :param url: The URL to send the request to.
        :param params: The URL parameters.
        :param body: The request body.
        :param headers: The request headers.
        :param cookies: The request cookies.
        :param kwargs: Arbitrary keyword arguments that can be passed to `requests.request`.
        :return: The HTTP response if successful, None otherwise.
        """
        return self.request(
            method="PATCH",
            url=url,
            params=params,
            body=body,
            headers=headers,
            cookies=cookies,
            **kwargs
        )

    def delete(self, url: str, params: Optional[dict] = None, headers: Optional[dict] = None,
               cookies: Optional[dict] = None, **kwargs) -> Optional[requests.Response]:
        """
        Perform a DELETE request.

        :param url: The URL to send the request to.
        :param params: The URL parameters.
        :param headers: The request headers.
        :param cookies: The request cookies.
        :param kwargs: Arbitrary keyword arguments that can be passed to `requests.request`.
        :return: The HTTP response if successful, None otherwise.
        """
        return self.request(
            method="DELETE",
            url=url,
            params=params,
            headers=headers,
            cookies=cookies,
            **kwargs
        )

    def head(self, url: str, params: Optional[dict] = None, headers: Optional[dict] = None,
             cookies: Optional[dict] = None, **kwargs) -> Optional[requests.Response]:
        """
        Perform a HEAD request.

        :param url: The URL to send the request to.
        :param params: The URL parameters.
        :param headers: The request headers.
        :param cookies: The request cookies.
        :param kwargs: Arbitrary keyword arguments that can be passed to `requests.request`.
        :return: The HTTP response if successful, None otherwise.
        """
        return self.request(
            method="HEAD",
            url=url,
            params=params,
            headers=headers,
            cookies=cookies,
            **kwargs
        )

    def options(self, url: str, params: Optional[dict] = None, headers: Optional[dict] = None,
                cookies: Optional[dict] = None, **kwargs) -> Optional[requests.Response]:
        """
        Perform a OPTIONS request.

        :param url: The URL to send the request to.
        :param params: The URL parameters.
        :param headers: The request headers.
        :param cookies: The request cookies.
        :param kwargs: Arbitrary keyword arguments that can be passed to `requests.request`.
        :return: The HTTP response if successful, None otherwise.
        """
        return self.request(
            method="OPTIONS",
            url=url,
            params=params,
            headers=headers,
            cookies=cookies,
            **kwargs
        )
