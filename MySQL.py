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


def get_skyscanner_search_vars(id):
    travel_vars = {
        "travel_origin": [],
        "travel_destination": [],
        "departure_dates": [],
        "return_dates": [],
        "adults": 1,
        "max_stops": 5,
        "max_duration": 720
    }
    my_cursor.execute(f"SELECT * FROM inq_req WHERE id = {id}")
    db_vars = my_cursor.fetchone()

    travel_vars["travel_origin"] = json.loads(db_vars[2])
    travel_vars["travel_destination"] = json.loads(db_vars[3])
    travel_vars["departure_dates"] = json.loads(db_vars[4])
    travel_vars["return_dates"] = json.loads(db_vars[5])
    travel_vars["adults"] = db_vars[6]
    travel_vars["max_stops"] = db_vars[7]
    travel_vars["max_duration"] = db_vars[8]

    return travel_vars


def get_email(id):
    my_cursor.execute(f"SELECT email FROM inq_req WHERE ID = {id}")
    return my_cursor.fetchone()



def add_test_data_to_db(id):
    l = [
        "2020-09-12"
    ]
    jl = json.dumps(l)
    my_cursor.execute(f"update inq_req SET return_dates = '{jl}' WHERE id = {id}")
    mydb.commit()


