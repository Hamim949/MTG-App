"""controller.py will manage making API calls to the MTG App and format the results for display"""

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
    result_text = ''
    results = get_top_results(text)

    # loop through results to get display of each card
    for card in results:
        name = card.get("name")
        result_text += "<h3>" + name + "</h3>\n"
    return result_text


def get_top_results(text, num=2):
    text = str(text)
    results_dict = json.loads(text)
    cards = results_dict.get("cards")
    top_cards = cards[:num]
    return top_cards

if __name__ == "__main__":
    call_results = make_call("Planeswalker")
    print(call_results)


name_data = 'name'
manaCost_data = 'manacost'
cmc_data = 'cmc'
colors_data = 'colors'
colorIdentity_data = 'colorIdentity'
type_data = 'type'
supertypes_data = 'supertypes'
types_data = 'types'
subTypes_data = 'subtypes'
rarity_data = 'rarity'
set_data = 'set'
setName_data = 'setName'
text_data = 'text'
layout_data = 'layout'
loyalty_data = 'loyalty'
