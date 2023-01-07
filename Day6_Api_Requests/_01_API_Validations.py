import json
import requests

base_uri = 'http://216.10.245.166'
get_response = requests.get(f'{base_uri}/Library/GetBook.php', params={'AuthorName': 'Rahul Shetty2'})
# print(get_response.text)
# print(type(get_response.text))
# dict_response = json.loads(get_response.text)
# print(dict_response)
# print(type(dict_response))
#
# isbn_data = dict_response[0]['isbn']
# print(isbn_data)

# .json() methods used instead of all above code
response_json = get_response.json()
print(response_json)
print(type(response_json))

status_code = get_response.status_code
assert status_code == 200

headers = get_response.headers
print(headers)
print(type(headers))

content_type = headers['Content-Type']
assert content_type == 'application/json;charset=UTF-8'

for actual_book in response_json:
    if actual_book['isbn'] == 'RGHCC':
        print(actual_book)
        print(type(actual_book))
        break


expected_book = {
        "book_name": "Learn Appium Automation with Java",
        "isbn": "RGHCC",
        "aisle": "22755"
    }
assert actual_book == expected_book
