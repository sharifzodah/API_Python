import json
import requests
from utils.addPayload import *
from utils.deletePayload import *
from utils.configurations import *
from utils.resources import *

# Adding book
addBook_URL = getURL() + ApiResources.addBook
headers = {"Content-Type": "application/json"}

# Updating data in Table
query = \
    "update Books set BookName = \'Java\', isbn = \'bndDB223\', aisle = \'122\'" \
    " where Author = \'Abduhamid\'"

updateQuery(query)

query = "select * from Books where Author = \'Abduhamid\'"

addbook_resp = requests.post(addBook_URL,
                             json=buildPayloadFromDB(query),
                             headers=headers, )
print(addbook_resp)
print(type(addbook_resp))
addbook_json_resp = addbook_resp.json()
print(addbook_json_resp)
print(type(addbook_json_resp))

assert addbook_resp.status_code == 200
assert addbook_resp.headers['Content-Type'] == 'application/json;charset=UTF-8'

#  Storing book ID
book_id = addbook_json_resp['ID']
print(book_id)
print(type(book_id))

# Getting book by ID
getBookByID_URL = getURL() + ApiResources.getBookByID + book_id
getBook_request = requests.get(getBookByID_URL, headers=headers, )
getBook_response = getBook_request.json()
print(getBook_response)
author_name = getBook_response[0]['author']
print(author_name)
assert getBook_request.status_code == 200
assert author_name == 'Abduhamid'

# Getting book by author name
getBookByName_URL = getURL() + ApiResources.getBookByName + author_name
getBook_request = requests.get(getBookByName_URL, headers=headers, )
getBook_response = getBook_request.json()
assert getBook_request.status_code == 200

# Deleting book by ID
deleteBook_URL = getURL() + ApiResources.deleteBook
delete_book_request = requests.post(deleteBook_URL,
                                    json=deleteBookPayload(book_id),
                                    headers=headers, )
deleteBook_response = delete_book_request.json()
print(deleteBook_response)
assert delete_book_request.status_code == 200
assert deleteBook_response['msg'] == "book is successfully deleted"
























