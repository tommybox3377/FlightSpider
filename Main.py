import requests
import re
import Travel_Vars as tv

keys = []
prices = []


def create_session(rtn, origin, destination, depart):
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/v1.0"

    payload = f"inboundDate={rtn}&country=US&currency=USD&locale=en-US&originPlace={origin}-sky&destinationPlace={destination}-sky&outboundDate={depart}&adults={tv.adults}"
    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': "",
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
        'x-rapidapi-key': ""
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


make_all_combo_sessions()
for key in keys:
    poll_session(key)

for price in prices:
    print(price)
