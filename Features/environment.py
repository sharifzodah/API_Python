import requests

from BackEndAutomation.utils.deletePayload import *
from BackEndAutomation.utils.configurations import *
from BackEndAutomation.utils.resources import *


def after_scenario(context, scenario):
    if "Library" in scenario.tags:
        delete_book_url = getURL() + ApiResources.deleteBook
        delete_book_request = requests.post(delete_book_url,
                                            json=deleteBookPayload(context.book_id),
                                            headers=context.headers, )
        delete_book_response = delete_book_request.json()
        print(delete_book_response)
        assert delete_book_request.status_code == 200
        assert delete_book_response['msg'] == "book is successfully deleted"
