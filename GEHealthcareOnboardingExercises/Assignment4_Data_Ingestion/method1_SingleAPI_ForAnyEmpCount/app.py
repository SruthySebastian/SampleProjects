from __future__ import absolute_import
try:
    import os
    import sys
    import random
    import string

    import elasticsearch
    from elasticsearch import Elasticsearch
    from elasticsearch import helpers

    import pandas as pd
    import numpy as np
    import json
    from datetime import datetime
    from flask import Flask, jsonify, request

    print("All Modules Loaded! ")
except Exception as e:
    print(f"Some Modules are missing {e}")


class Employee:

    def __init__(self):
        self.name = emp_name()
        self.age = emp_age()
        self.location = emp_location()
        self.designation = emp_designation()
        self.salary = emp_salary(self.designation)

    def get_new_employee(self):
        emp = {"name": self.name,
               "age": self.age,
               "location": self.location,
               "designation": self.designation,
               "salary": self.salary
               }
        return emp


# -------------------------------------------------------------------

def random_string(l):
    return ''.join(random.choice(string.ascii_letters) for x in range(l))


# -------------------------------------------------------------------


def emp_name():
    first_name_length = random.randint(2, 10)
    last_name_length = random.randint(2, 10)
    first_name = random_string(first_name_length).capitalize()
    last_name = random_string(last_name_length).capitalize()
    full_name = first_name + " " + last_name
    return full_name


# -------------------------------------------------------------------
def emp_age():
    return random.randint(22, 60)


# -------------------------------------------------------------------
# create a dictionary, key is the state and value is the capital
capital_dic = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinios': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Neveda': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhoda Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}


def emp_location():
    states = list(capital_dic.keys())
    capitals = list(capital_dic.values())
    state = random.choice(states)
    capital = capital_dic[state]
    employee_location = f"{capital}, {state}"
    return employee_location


# Or
# Using State codes
state_codes = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE",
               "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
               "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT",
               "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH",
               "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT",
               "VT", "VA", "WA", "WV", "WI", "WY"]


def emp_location_code():
    return random.choice(state_codes)


# -------------------------------------------------------------------
designations \
    = ['Developer', 'Tester', 'Support Analyst', 'Team Lead', 'Project Manager', 'Engineering Manager',
       'Director']


def emp_designation():
    return random.choice(designations)


# -------------------------------------------------------------------
# Salary calculation based on random designation using switcher :
def emp_salary(emp_role):
    switcher = {
        'Developer': random.randint(60000, 75000),
        'Tester': random.randint(50000, 70000),
        'Support Analyst': random.randint(50000, 70000),
        'Team Lead': random.randint(60000, 85000),
        'Project Manager': random.randint(75000, 90000),
        'Engineering Manager': random.randint(80000, 100000),
        'Director': random.randint(90000, 120000)
    }
    return switcher.get(emp_role, 0)


# -------------------------------------------------------------------
# API:


app = Flask(__name__)
port = 5000


@app.route('/', methods=["GET"])  # Sample URL : http://192.168.1.151:5000
def helloWorld():
    response = f"<p>Hello World in Docker!, Port : {port} <p>"
    # response.status_code = 200
    return response, 200


# -- Data Ingestion script --

# single
@app.route('/api/v1/resources/employee')  # Sample URL : http://192.168.1.151:5000/api/v1/resources/employee
def getEmployee():
    e = Employee()
    response = jsonify(e.get_new_employee())
    # response.status_code = 200
    return response, 200


# bulk
@app.route('/api/v1/resources/employees')  # Sample URL : http://192.168.1.151:5000/api/v1/resources/employees?count=4
def getEmployees():
    emp_count = int(request.args.get('count'))
    emp_list = []
    response = f"<p>Hello.. {emp_count} employees!!! <p>"
    for i in range(0, emp_count):
        employee = Employee()
        emp_list.append(employee.get_new_employee())

    print(f"Employee list :\n {emp_list}")
    response = response + f"<p>{json.dumps(emp_list)}<p>"

    # response.status_code = 200
    return response, 200


# -------------------------------------------------------------------
# Data Ingestion

# ENDPOINT = "http://localhost:9200/"
# es = Elasticsearch(timeout=600, hosts=ENDPOINT)
# OR
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
print(f"es.ping() : {es.ping()}")


def dataIngestion(data_count):
    print(f"dataIngestion data_count = {data_count}")
    if data_count and int(data_count) != 0:

        # To get all the index names
        resp = es.indices.get_alias('*')
        for index_name in resp:
            print(index_name)

        # create index
        if "employee" not in resp:
            es.indices.create(index="employee", ignore=400)
        else:
            pass  # index of this name already present

        singleInsert() if int(data_count) == 1 else bulkInsert(int(data_count))

    else:
        print("\n*** Please enter a valid non-zero number as count ***\n")


def singleInsert():
    print("singleInsert")

    e_single = Employee()
    # print(f"e_single.get_new_employee() : \n{e_single.get_new_employee()} ")

    # single record insertion
    res1 = es.index(index='employee', doc_type='testemployee', body=e_single.get_new_employee())
    print(f"res1 : \n{res1}")


def bulkInsert(bulk_data_count):
    print("bulkInsert")
    bulk_emp_list = []
    print(f"Hello.. {bulk_data_count} employees!!!")
    for i in range(0, bulk_data_count):
        employee = Employee()
        bulk_emp_list.append(employee.get_new_employee())
    print(f"bulk_emp_list :\n{bulk_emp_list}")

    # defining generator function
    def generator(bulk_data):
        print("\n Inside ELK data generator\n")
        for c, line in enumerate(bulk_data):
            yield {
                '_index': 'employee',  # name your index
                '_type': '_doc',  # type is document
                # '_id': line.get("<emp_id>", None),  # TODO : auto generate/increment unique emp_id
                '_source': {
                    "name": line.get("name", ""),
                    "age": line.get("age", ""),
                    "location": line.get("location", ""),
                    "designation": line.get("designation", ""),
                    "salary": line.get("salary", "")
                }
            }
        raise StopIteration

    # Converting employee dictionary list data into elasticsearch format
    my_elk_employees = generator(bulk_emp_list)

    # To verify a sample format
    print(f"next(my_elk_employees) : \n{next(my_elk_employees)}")

    # Upload data into elasticsearch using Bulk API
    # import elasticsearch
    # from elasticsearch import helpers
    try:
        res = helpers.bulk(es, generator(bulk_emp_list))
        print("Working")
    except Exception as e:
        print(f"Exception : \n{e}\n")
        # o/p : Exception : generator raised StopIteration
        pass

    # Go to Kibana and verify : GET _cat/indices , GET employee/_search

# -------------------------------------------------------------------

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1>" \
           "<p>The resource could not be found<p>" \
           "<p>Please check URL provided</p>", 404


@app.errorhandler(400)
def bad_request(e):
    return "<h1>400</h1>" \
           "<p>Bad Requestr</p>", 400


@app.errorhandler(500)
def internal_server_error(e):
    return "<h1>500</h1>" \
           "<p>Internal Server Error</p>", 500


@app.errorhandler(502)
def bad_gateway(e):
    return "<h1>502</h1>" \
           "<p>Bad Gateway r</p>", 502


@app.errorhandler(503)
def service_unavailable(e):
    return "<h1>503</h1>" \
           "<p>Service Unavailable</p>", 503


@app.errorhandler(504)
def gateway_timeout(e):
    return "<h1>504</h1>" \
           "<p>Gateway Timeout</p>", 504


if __name__ == "__main__":
    count = input("Hello!\n Please enter the count of employees you want to generate"
                  "\n -------------------------------------------------------------"
                  "\n Note"
                  "\n Enter 1 for  single insert"
                  "\n Enter an input > 1 for bulk insert"
                  "\n -------------------------------------------------------------"
                  "\n count : ")
    print(f"Count : {count}")
    dataIngestion(int(count))
    app.run(debug=True, host="0.0.0.0", port=5000)


# # -------------------------------------------------------------------

# Regarding assignment:-
# Implement multiple employee data ingestion 2 ways :-
# -1] create separate Apis for employee and employees ,call them according to the request # TODO : Doubt
# -2] call employee in 'for loop' 10 times ,append it to a list and return the result     # TODO : Done
#


# -------------------------------------------------------------------

