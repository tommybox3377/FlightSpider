import requests
import re
import TravelVars as tv
import json
import Creds
import SkyScannerAPI
import MySQL


# make_all_combo_sessions()
# for key in keys:
#     poll_session(key)
#
# for price in prices:
#     print(price)


MySQL.my_cursor.execute("SELECT id FROM inq_req")
db_id = MySQL.my_cursor.fetchone()
while db_id:
    id = db_id[0]
    travel_vars = MySQL.get_skyscanner_search_vars(id)
    best_price = SkyScannerAPI.get_best_price(travel_vars)
    print(best_price)
    db_id = MySQL.my_cursor.fetchone()






