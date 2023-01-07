import json
import requests
from BackEndAutomation.utils.addPayload import *
from BackEndAutomation.utils.deletePayload import *
from BackEndAutomation.utils.configurations import *
from BackEndAutomation.utils.resources import *

# Adding book
addBook_URL = getURL() + ApiResources.addBook
headers = {"Content-Type": "application/json"}

add_book_request = requests.post(addBook_URL,
                                 json=addBookPayload("Abduhamid"),
                                 headers=headers, )

addBook_response = add_book_request.json()
print(addBook_response)

assert add_book_request.status_code == 200
assert add_book_request.headers['Content-Type'] == 'application/json;charset=UTF-8'

#  Storing book ID
book_id = addBook_response['ID']
print(book_id)
print(type(book_id))

# Getting book by ID
getBookByID_URL = getURL() + ApiResources.getBookByID + book_id
getBook_request = requests.get(getBookByID_URL, headers=headers, )
getBook_response = getBook_request.json()
author_name = getBook_response[0]['author']
assert getBook_request.status_code == 200
assert author_name == 'Abduhamid'


# Getting book by author name
getBookByName_URL = getURL() + ApiResources.getBookByName + author_name
getBook_request = requests.get(getBookByName_URL, headers=headers,)
getBook_response = getBook_request.json()
assert getBook_request.status_code == 200


# Deleting book by ID
deleteBook_URL = getURL() + ApiResources.deleteBook
delete_book_request = requests.post(deleteBook_URL,
                                    json=deleteBookPayload(book_id),
                                    headers=headers,)
deleteBook_response = delete_book_request.json()
print(deleteBook_response)
assert delete_book_request.status_code == 200
assert deleteBook_response['msg'] == "book is successfully deleted"
