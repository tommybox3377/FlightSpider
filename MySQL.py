import mysql.connector
import json
import Creds

mydb = mysql.connector.connect(
    host=Creds.host,
    user=Creds.user,
    password=Creds.password,
    database=Creds.database
)

my_cursor = mydb.cursor()

def get_vars(id):
    travel_vars = {
        "travel_origin": [],
        "travel_destination": [],
        "departure_dates": [],
        "return_dates": [],
        "adults": 1,
        "max_stops": 5,
        "max_duration": 1440
    }
    my_cursor.execute("SELECT * FROM inq_req WHERE email = 'twmaryniak@yahoo.com'")
    vars = my_cursor.fetchone()
    var_arr = json.loads(vars[2])
    print(type(vars[2]))
    for place in var_arr:
        print(type(place))
        print(place)
    return travel_vars



# j = json.dumps(return_dates)
# # print(travel_origin)
# print(j)
#
# col = "return_dates"
# val = j
#
# my_cursor.execute(f"UPDATE inq_req SET {col} = '{val}' WHERE email = 'twmaryniak@yahoo.com'")
# mydb.commit()

