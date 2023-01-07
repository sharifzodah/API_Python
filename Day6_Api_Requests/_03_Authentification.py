import json
import requests
from BackEndAutomation.utils.configurations import *

# Authentication
se = requests.session()
se.auth = auth = ('Bearer', getToken())

gitHub_URL = "https://api.github.com/user"
github_request = se.get(gitHub_URL)
user_response = github_request.json()
user_name = user_response['login']
print(type(user_response))
# print(user_response)
assert github_request.status_code == 200
assert user_name == 'sharifzodah'

gitHub_users_URL = "https://api.github.com/users/"
sharifzodah_request = se.get(f'{gitHub_users_URL}{user_name}')
sharifzodah_response = sharifzodah_request.json()
# print(sharifzodah_response)
assert sharifzodah_request.status_code == 200

gitHubRepo_URL = "https://api.github.com/user/repos"
repo_request = se.get(gitHubRepo_URL)
repo_response = repo_request.json()
assert repo_request.status_code == 200
repoList = list(repo_response)

# Creating json file and saving response in it
for i in range(0, len(repoList)):
    with open('repos.json', 'w') as newFile:
        json.dump(repo_response, newFile)
