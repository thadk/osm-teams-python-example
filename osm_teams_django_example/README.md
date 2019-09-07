A basic django example app ready to add the `loginpass` library for `mappingteam` from the Flask example.

0. create new venv for the django app.
1. Create a second blank heroku app on the heroku-django branch.
2. `git subtree push --prefix pythonapp heroku-django master` will push just this folder to the new heroku branch.
3. add loginpass to the requirements.txt for django.
3. copy the `extra_backends` folder from the flask example and import as described in the documentation for loginpass.