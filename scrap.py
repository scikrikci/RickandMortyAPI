from time import sleep
import requests
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get("https://rickandmortyapi.com/api")
print(response.status_code)

def location():
    location = response.json()["locations"] #'location'

    req = requests.get(location)
    print(req.status_code)

    results = req.json()

    page_count = results["info"]["pages"]

    for page in range(page_count): 
        page_url = f"https://rickandmortyapi.com/api/location?page={page + 1}"
        req = requests.get(page_url)
        for data in req.json()["results"]:
            data["name"]
#---------------------------------------------------------------------------#
def character(name_input):
    location = response.json()["characters"] #'location'

    req = requests.get(location)
    print(req.status_code)

    results = req.json()

    page_count = results["info"]["pages"]

    for page in range(page_count): 
        page_url = f"https://rickandmortyapi.com/api/character?page={page + 1}"
        req = requests.get(page_url)
        for char in req.json()["results"]:

            if name_input.lower() in char["location"]["name"].lower():
                jprint(char["name"])



location()
sleep(2)
name_input = input("Name giriniz \n")
character(name_input)



