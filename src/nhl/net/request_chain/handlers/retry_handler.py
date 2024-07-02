import random

from typing import Optional, Tuple
from time import sleep
from .base_handler import BaseHandler
from ...transport.request import Request
from ...transport.response import Response
from ...transport.request_error import RequestError


class RetryHandler(BaseHandler):
    """
    Handler for retrying requests.
    Retries the request if the previous handler in the chain returned an error or a response with a status code of 500 or higher.

    :ivar int _max_attempts: The maximum number of retry attempts.
    :ivar int _delay_in_milliseconds: The delay between retry attempts in milliseconds.
    """

    def __init__(self):
        """
        Initialize a new instance of RetryHandler.
        """
        super().__init__()
        self._max_attempts = 3
        self._delay_in_milliseconds = 150

    def handle(
        self, request: Request
    ) -> Tuple[Optional[Response], Optional[RequestError]]:
        """
        Retry the request if the previous handler in the chain returned an error or a response with a status code of 500 or higher.

        :param Request request: The request to retry.
        :return: The response and any error that occurred.
        :rtype: Tuple[Optional[Response], Optional[RequestError]]
        :raises RequestError: If the handler chain is incomplete.
        """
        if self._next_handler is None:
            raise RequestError("Handler chain is incomplete")

        response, error = self._next_handler.handle(request)

        try_count = 0
        while try_count < self._max_attempts and self._should_retry(error):
            jitter = random.uniform(0.5, 1.5)
            delay = self._delay_in_milliseconds * (2**try_count) * jitter / 1000
            sleep(delay)
            response, error = self._next_handler.handle(request)
            try_count += 1

        return response, error

    def _should_retry(self, error: Optional[RequestError]) -> bool:
        """
        Determine whether the request should be retried.

        :param Optional[Response] response: The response from the previous handler.
        :param Optional[RequestError] error: The error from the previous handler.
        :return: True if the request should be retried, False otherwise.
        :rtype: bool
        """
        if not error:
            return False
        return error.status == 408 or error.status >= 500
