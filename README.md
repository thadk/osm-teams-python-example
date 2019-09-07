# osm-teams-python-example

Flask example app for https://dev.mapping.team using https://docs.authlib.org/en/latest/client/flask.html and the related `loginpass` library. Mapping Teams implements the OAuth 2 and OpenID Connect standards. The OAuth 1 transaction with OpenStreetMap.org is handled entirely by the Mapping Teams server.

This example will use the app credentials you provide. For the users of this demo app, authentication will be verified by Mapping Teams. Then, the access key will be available which can be used as a bearer authentication header to e.g. create a new team at [https://dev.mapping.team](https://dev.mapping.team). 

0. clone this repository
1. `python3 -m  venv flask_venv` to create a new python venv environment.
2. `. flask_venv/bin/activate` to enter the environment
3. `pip install -r requirements.txt`
4. Create a new localhost testing app at [https://dev.mapping.team](https://dev.mapping.team) and keep the secret and ID information somewhere safe that you get when you create it. For the Callback Address, you should put in something like `http://localhost:5555/mappingteam/auth` – that is the callback Flask endpoint configured by `loginpass`.
5. `FLASK_APP=flask_example FLASK_ENV=development MAPPINGTEAM_CLIENT_ID= MAPPINGTEAM_CLIENT_SECRET= flask run -p 5555`, to start your app. Be sure to add the actual values for the Client ID and Secret you got from [https://dev.mapping.team](https://dev.mapping.team) . You will not need the Client Name.
6. `heroku create`
4. Create a new internet testing app at [https://dev.mapping.team](https://dev.mapping.team) and keep the secret and ID information somewhere safe that you get when you create it. You should use `https://yourherokudomain.herokuapp.com/mappingteam/auth` as the callback address, updating the domain as needed to match the app you just created.
7. `heroku config:set MAPPINGTEAM_CLIENT_ID= MAPPINGTEAM_CLIENT_SECRET=`, entering in the Client ID and Secret you just got for your internet testing app.
8. `git push heroku master`
9. Try out your app using your Heroku address. It should look something like the on at [https://polar-island-94689.herokuapp.com/](https://polar-island-94689.herokuapp.com/)A

An unfinished Django example is available on the Django_example branch, ready to follow the instructions with the loginpass library to use it. https://github.com/thadk/osm-teams-python-example/tree/django_example . The Loginpass example app may also be helpful: https://github.com/authlib/loginpass/tree/master/django_example