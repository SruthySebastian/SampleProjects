import random
import string


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


# e = Employee()
# print(e.get_new_employee())

