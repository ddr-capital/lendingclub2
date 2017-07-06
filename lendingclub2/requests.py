# Filename: requests.py

"""
LendingClub2 Requests Module

Interface functions:
    get
    post
"""

# Requests
import requests

# Lending Club
from lendingclub2.error import LCError


def get(*args, **kwargs):
    """
    Wrapper around requests.get function.

    :param args: tuple - positional arguments for requests.get
    :param kwargs: dict - keyword arguments for requests.get
    :returns: instance of requests.Response
    """
    try:
        return requests.get(*args, **kwargs)
    except requests.ConnectionError as exc:
        fstr = "Cannot connect correctly"
        raise LCError(fstr, details=str(exc))


def post(*args, **kwargs):
    """
    Wrapper around requests.post function.

    :param args: tuple - positional arguments for requests.post
    :param kwargs: dict - keyword arguments for requests.post
    :returns: instance of requests.Response
    """
    try:
        return requests.post(*args, **kwargs)
    except requests.ConnectionError as exc:
        fstr = "Cannot connect correctly"
        raise LCError(fstr, details=str(exc))
