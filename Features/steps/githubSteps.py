import requests
from behave import *
from utils.resources import *

from utils.configurations import *


@given('I have GitHub auth credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = ('Bearer', getToken())


@when('I hit getRepo API of GitHub')
def step_impl(context):
    context.response = context.se.get(ApiResources.gitHubUser)
    user_response = context.response.json()
    user_name = user_response['login']
    print(type(user_response))
    assert user_name == 'sharifzodah'


@then('the status code of response should be {statusCode:d}')
def step_impl(context, statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode

