import requests
from behave import *
from utils.addPayload import *
from utils.configurations import *
from utils.resources import *


@given('the Book details which needs to be added to Library')
def step_impl(context):
    context.addbook_url = getURL() + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payload = addBookPayload("bcd4", "1006", "Abduhamid")


@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.addbook_url,
                                     json=context.payload,
                                     headers=context.headers, )


@then('book is successfully added')
def step_impl(context):
    addbook_response = context.response.json()
    print(addbook_response)

    assert context.response.status_code == 200
    assert context.response.headers['Content-Type'] == 'application/json;charset=UTF-8'
    assert addbook_response['Msg'] == "successfully added"

    #  Storing book ID
    context.book_id = addbook_response['ID']
    print(context.book_id)
    print(type(context.book_id))


# step for Scenario Outline
@given('the Book details with {isbn}, {aisle} and {author}')
def step_impl(context, isbn, aisle, author):
    context.addbook_url = getURL() + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payload = addBookPayload(isbn, aisle, author)
