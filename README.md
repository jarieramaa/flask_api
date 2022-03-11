# flask_api
This is a small Flask API excersice

# Description

A route that takes a number in the request and returns this number multiplied by 2

A POST route that takes this dictionary (in json format) and returns the computation of salary + bonus - taxes.


# Installation
## Required modules and versions
There are modules that are needed to run this program. Here is a list of them and version that are tested with this program. Python version used is 3.9.10.

The actual API needs only one module: flask. However, there is also other program (test_api.py) for testing the API.


| flask_challenge.py | Version  |
|--------------------| ---------|
| flask              | 2.0.2    |

| test_api.py   | Version  |
|---------------| ---------|
| requests      | 2.27.1   |
| pycurl        | 7.44.1   |

# Usage
By running command 'python flask_challenge.py' the API is started. Please, see sections 'Multiply' and 'Salary' for the details how to use the API. 

## Multiply

URL: http://127.0.0.1:5000/multiply/\<number>

By replacing \<number> any number the API returns a dictionary with key 'value' and answer that is two times the original number

{"value": \<answer> }

## Salary

URL: http://127.0.0.1:5000/multiply/

Method: Post

Dictionary example:
{
    "salary": 2500,
    "bonus": 200,
    "taxes": 400
}

Response dictionary:
{ 
"result": 2300 // salary + bonus - taxes
}

### error messages:
If the user forgets a field: json 
{ 
"error": f"3 fields expected (salary, bonus, taxes). You forgot: \{FORGOTTEN\_FIELDS}." 
}

If the user gives a non numeric value:
{
    "error": "expected numbers, got strings."
}