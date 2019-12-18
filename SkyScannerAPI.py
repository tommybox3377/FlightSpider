import re
import requests

import Creds
import TravelVars as tv

# #Notes:
# 1)get API key
# 2)get token  https://skyscanner.github.io/slate/#authentication
#  note https://skyscanner.github.io/slate/#getting-started for quotes vs routes vs dates vs grid
#       see what you get back with each. probably a combination for initial price history, then shoot live prices at time_check interval
# note: for dest/origin places : https://skyscanner.github.io/slate/#places
# 3)create live price session
#NOTE: LIVE Flight prices will only retunr a session that you have to poll
#        checkk for these first https://skyscanner.github.io/slate/#carhire-home-page-supported-parameters-schema
# 4)poll result
#       use a  paging and payload system cause we are really only looking for the cheapest flights
# 5) look into booking details
#Add no-follow attribut to deeplink??
#!!!Please do not cache the deeplinks as they are only valid while your session is active. Once the session has timed out you will need to create a new session and refresh all the results and deeplink urls.
#
#
#

keys = []
prices = []


def create_session(rtn, origin, destination, depart):
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/v1.0"

    payload = f"inboundDate={rtn}&country=US&currency=USD&locale=en-US&originPlace={origin}-sky&destinationPlace={destination}-sky&outboundDate={depart}&adults={tv.adults}"
    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': Creds.xrapid_key,
        'content-type': "application/x-www-form-urlencoded"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response)
    return response.headers["Location"]


def make_all_combo_sessions():
    # TODO make try catch cause this fail regularly
    for origin in tv.travel_origin:
        for destination in tv.travel_destination:
            for depart in tv.departure_dates:
                for rtn in tv.return_dates:
                    key = re.search(r"v1\.0/(.*)", create_session(rtn, origin, destination, depart))
                    keys.append(key[1])


def poll_session(key):
    #TODO probably delete this line
    import requests

    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/uk2/v1.0/" + key

    querystring = {
        "sortType": "price",
        "sortOrder": "asc",
        "duration": str(tv.max_duration),
        "stops": str(tv.max_stops),
        "pageIndex": "0",
        #TODO change/check this to 1 or 2 if we are just grabbing to lowest one
        "pageSize": "10"
    }

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': Creds.xrapid_key
    }
    print(url)
    response = requests.request("GET", url, headers=headers, params=querystring)

    try:
        prices.append([
            response.json()["Itineraries"][0]["PricingOptions"][0]["Price"],
            response.json()["Itineraries"][0]["PricingOptions"][0]["DeeplinkUrl"]
        ])
    except:
        prices.append([
            0, "Error for key:" + key
        ])
