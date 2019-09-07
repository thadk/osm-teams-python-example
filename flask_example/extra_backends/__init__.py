from loginpass._core import register_to
from loginpass._flask import create_flask_blueprint
from loginpass._consts import version, homepage
from loginpass._django import create_django_urlpatterns
from loginpass import OAUTH_BACKENDS
from .mappingteam import MappingTeam


# OAUTH_BACKEND 3 is GitHub, which was tested
OAUTH_BACKENDS = [OAUTH_BACKENDS[3]] + [MappingTeam]

__all__ = [
    'register_to',
    'MappingTeam',
    'create_flask_blueprint',
    'create_django_urlpatterns',
    'OAUTH_BACKENDS'
]

__version__ = version
__homepage__ = homepage