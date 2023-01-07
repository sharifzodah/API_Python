from BackEndAutomation.utils.configurations import *
import random


def addBookPayload(isbn, aisle, author):
    body = {
        "name": "Build API BDD Framework with Python",
        "isbn": isbn,
        "aisle": aisle,
        "author": author
    }
    return body


def buildPayloadFromDB(query):
    add_body = {}
    db_record = getQuery(query)
    add_body['name'] = db_record[0]
    add_body['isbn'] = db_record[1]
    add_body['aisle'] = db_record[2]
    add_body['author'] = db_record[3]
    return add_body


def addPetPayload():
    body = {
        "id": random.randrange(1000001, 10000001),
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": f"Wolf{random.randrange(11, 101)}",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    return body
