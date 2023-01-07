import requests
import json
import random
from BackEndAutomation.utils.configurations import *
from BackEndAutomation.utils.resources import *
from BackEndAutomation.utils.addPayload import *

# Create Pet
url = getPetURL() + ApiResources.createPet
headers = {"Content-Type": "application/json"}
bodyPayload = addPetPayload()
# Sending request
post = requests.post(url, json=bodyPayload, headers=headers)
# Getting responses
jsonData = post.json()
statusCode = post.status_code
resHeaders = post.headers
petID = jsonData['id']
petStatus = jsonData['status']
petName = jsonData['name']
apiKey = resHeaders['Access-Control-Allow-Headers']
assert statusCode == 200
assert jsonData == bodyPayload
assert resHeaders['Content-Type'] == "application/json"
assert petStatus == 'available'

# Getting Pet by ID
url2 = getPetURL() + ApiResources.petByID + str(petID)
# Sending request
getResp = requests.get(url2, headers=headers)
# Getting responses
jsonData2 = getResp.json()
statusCode = getResp.status_code
resHeaders = getResp.headers
actualPetID = jsonData2['id']
assert statusCode == 200
assert petID == actualPetID

# Updating Pet by ID
updatePetPayload = {
    "name": f"Panther{random.randrange(11, 101)}",
    "status": petStatus}
headers = {"accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}
updateResp = requests.post(url2, json=updatePetPayload, headers=headers)
jsonData3 = updateResp.json()
statusCode = updateResp.status_code
resHeaders = updateResp.headers
actualPetID = jsonData3['message']
assert statusCode == 200
assert petID == int(actualPetID)
assert resHeaders['Content-Type'] == "application/json"

# Uploading an Image for the pet
url = getPetURL() + ApiResources.uploadImage + f'{petID}/uploadImage'
image = {'file': open('D:\\Downloads - 2017\\ToyBUS.jpg', 'rb')}
imageUpload = requests.post(url, files=image)
jsonData5 = imageUpload.json()
statusCode = imageUpload.status_code
resHeaders = imageUpload.headers
assert statusCode == 200
assert apiKey == resHeaders['Access-Control-Allow-Headers']


# Deleting Pet by ID
deleteResp = requests.delete(url2, params=apiKey, headers=headers)
jsonData4 = deleteResp.json()
statusCode = deleteResp.status_code
resHeaders = deleteResp.headers
assert statusCode == 200
assert resHeaders['Content-Type'] == "application/json"





