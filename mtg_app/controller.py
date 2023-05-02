"""controller.py will manage making API calls to the gutendex and format the results for display"""

# Import statements
import requests
from ast import literal_eval
import json
 

# set some variables to help our API call
domain = "https://api.magicthegathering.io/v1/"
endpoint ="cards?type="

# make an API call
def make_call(query: str) -> str:

    # create our url
    url = domain + endpoint + query 

    # make the call
    response =  requests.get(url)
    results = ""
    if response.ok:
       results = response.text
       results = process_results(results)
    else:
        results = "There was an error. Please try later."

    return results

def process_results(text):
    # Opening JSON file
    text = str(text)
    results_dict = json.loads(text)
    cards = results_dict.get("cards")
    top_5_cards = cards[:5]
    print(top_5_cards)
    return str(top_5_cards)

if __name__ == "__main__":
    call_results = make_call("Planeswalker")
    print(call_results)