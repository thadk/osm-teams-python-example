"""
    loginpass.mappingteam
    ~~~~~~~~~~~~~~~~
    Loginpass Backend of MappingTeam (https://dev.mapping.team).
    Useful Links:
    - Create App: 
    - API documentation: 
    :copyright: (c) 2019 Thad Kerosky
    :license: BSD, see LICENSE for more details.
"""

from loginpass._core import UserInfo, OAuthBackend, parse_id_token

_host = 'https://dev.mapping.team'

class MappingTeam(OAuthBackend):
    OAUTH_TYPE = '2.0,oidc'
    OAUTH_NAME = 'mappingteam'
    OAUTH_CONFIG = {
        'api_base_url': 'https://dev.mapping.team',
        'access_token_url': 'https://dev.mapping.team/hyauth/oauth2/token',
        'authorize_url': 'https://dev.mapping.team/hyauth/oauth2/auth',
        'client_kwargs': {
            'redirect_uri': 'localhost:5000/callback',
            'scope': 'openid offline'
            },
    }

    JWK_SET_URL = 'https://dev.mapping.team/hyauth/.well-known/jwks.json'

    def profile(self, **kwargs):
        resp = self.get('user', **kwargs)
        resp.raise_for_status()
        data = resp.json()
        print("profile")
        params = {
            'sub': str(data['id']),
            'name': data['name'],
            'preferred_username': data['login'],
            'profile': data['html_url'],
            'picture': data['avatar_url'],
            'website': data.get('blog'),
        }
        return UserInfo(params)

    def parse_openid(self, token, nonce=None):
        return parse_id_token(
            self, token['id_token'],
            {},
            token.get('access_token'), nonce
        )
        # The email can be be None despite the scope being 'user:email'.
        # That is because a user can choose to make his/her email private.
        # If that is the case we get all the users emails regardless if private or note
        # and use the one he/she has marked as `primary`
        # if params.get("email") is None:
        #     resp = self.get("user/emails")
        #     resp.raise_for_status()
        #     data = resp.json()
        #     params["email"] = next(email["email"] for email in data if email["primary"])

