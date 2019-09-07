from authlib.django.client import OAuth

oauth = OAuth()

print(oauth.register(
    name='testApp3',
    client_id='9354646b-4d7a-4e5c-b3a2-61cdf02f373e',
    client_secret='nOpQdo3zABGA',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
    ))

def login(request):
    # build a full authorize callback uri
    redirect_uri = request.build_absolute_uri('/authorize')
    return oauth.github.authorize_redirect(request, redirect_uri)

def authorize(request):
    token = oauth.github.authorize_access_token(request)
    resp = oauth.github.get('user')
    profile = resp.json()
    # do something with the token and profile
    return '...'

def team_profile(request):
    token = OAuth2Token.objects.get(
        name='github',
        user=request.user
    )
    # API URL: https://api.github.com/user
    resp = oauth.github.get('user', token=token.to_token())
    profile = resp.json()
    return render_template('github.html', profile=profile)
