ENDPOINTS = {
        'api': 'http://www.behance.net/v2',
        'project': '/projects',
        'user': '/users'
        }

def url_join(*args):
    return "/".join(s.strip('/') for s in args)

from api import *
from project import *
from exceptions import *
