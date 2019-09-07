The main Flask code can be found in this __init__.py

It takes advantage of the Flask blueprint endpoints that loginpass creates for any service it can handle using the name of the service.  If you bring this code into Django, it should create urlpatterns endpoints too.

I added a custom backend called "mappingteam" in "extra_backends/" to the 10 or 15 off-the-shelf backends found at https://github.com/authlib/loginpass/tree/master/loginpass .

It should be easy to compare and contrast different OpenID Connect loginpass example implementations to help you implement mappingteams in any library. Mapping Team is somewhere between Github and Auth0 in its setup: Github does not use OpenID Connect (oidc) but Auth0 does. Auth0 handles more domains where mappingteams does not need to. 

I kept the github example for trial purposes but you need to create a github app to use it and set the credentials in your settings using e.g. GITHUB_CLIENT_ID .