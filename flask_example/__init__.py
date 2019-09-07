from flask import Flask,redirect, jsonify, url_for, session, escape, request
import requests
from authlib.flask.client import OAuth
from loginpass import create_flask_blueprint
# from loginpass import OAUTH_BACKENDS
import json
 
import os
from flask_example.extra_backends import OAUTH_BACKENDS
app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config['MAPPINGTEAM_CLIENT_ID'] = os.getenv('MAPPINGTEAM_CLIENT_ID')
app.config['MAPPINGTEAM_CLIENT_SECRET'] = os.getenv('MAPPINGTEAM_CLIENT_SECRET')
app.config['GITHUB_CLIENT_ID'] = os.getenv('GITHUB_CLIENT_ID')
app.config['GITHUB_CLIENT_SECRET'] = os.getenv('GITHUB_CLIENT_SECRET')

class Cache(object):
    def __init__(self):
        self._data = {}

    def get(self, k):
        return self._data.get(k)

    def set(self, k, v, timeout=None):
        self._data[k] = v

    def delete(self, k):
        if k in self._data:
            del self._data[k]


# Cache is used for OAuth 1 services. You MUST use a real
# cache service like memcache/redis on production.
# THIS IS JUST A DEMO.
oauth = OAuth(app, Cache())


@app.route('/')
def index():
    statusString = ""
    if 'user_info' in session:
         statusString = 'Logged in as %s' % escape(session['user_info']['preferred_username'])
    statusString = 'You are not logged in'
    tpl = '<li><a href="/{}/login">{}</a></li>'
    lis = [tpl.format(b.OAUTH_NAME, b.OAUTH_NAME) for b in OAUTH_BACKENDS]
    return '''<h3>Mapping Team</h3> <h5>Connect to</h5><ul>{}</ul><p>{}</p>
        <p>Be sure to match HTTPS of your app registration.</p>
        '''.format(''.join(lis),statusString)


def handle_authorize(remote, token, user_info):
    # Without more Flask setup, it does not persist sessions beyond the page.
    session['user_info'] = user_info

    if 'user_info' in session:
        access_token = token['access_token']
        osmId = user_info['sub']
        queryParam = "?access_token="+str(access_token) + "&osmId="+str(osmId)

        return '''
        <ul>
        <li><a href="/teams{}">Fetch your teams</a></li>
        <li><form method="post" action="/teams" method="get"">
            <p><input type=text name="teamname">
            <input type=hidden name="access_token" value="{}"/>
            </p>
            <p><input type=submit value="Create Team"></p>
        </form></li>
        <li><a href="/">Go home</a></li>
        </ul><p>Logged in as {}</p>
        '''.format(queryParam,access_token,escape(session['user_info']['preferred_username']))
    return jsonify(token)


for backend in OAUTH_BACKENDS:
    bp = create_flask_blueprint(backend, oauth, handle_authorize)
    app.register_blueprint(bp, url_prefix='/{}'.format(backend.OAUTH_NAME))

@app.route('/teams',methods=['GET','POST'])
def teams():
    if request.method == 'POST':
        session['teamname'] = request.form['teamname']
        # return jsonify(request.form)
        payload = {"name":session['teamname'],"location":"{\n          \"type\": \"Point\",\n          \"coordinates\": [-76.60766601562501,39.27478966170308]\n        }","hashtag":"#AnotherTeam"}
        return requests.post('https://dev.mapping.team/api/teams', data=json.dumps(payload), headers={'Authorization':"Bearer " + request.form['access_token'], 'content-type': 'application/json'}).content

    session['access_token'] = request.args.get("access_token")
    session['osmId'] = request.args.get("osmId")
    res = requests.get('https://dev.mapping.team/api/teams?').content
    return res