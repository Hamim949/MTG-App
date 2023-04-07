"""controller.py will manage making API calls to the gutendex and format the results for display"""

# Import statements
import requests

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
    else:
        results = "There was an error. Please try later."

    return results

if __name__ == "__main__":
    call_results = make_call("Planeswalker")
    print(call_results)