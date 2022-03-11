# flask_api
This is a small Flask API excersice

# Description

A route that takes a number in the request and returns this number multiplied by 2

A POST route that takes this dictionary (in json format) and returns the computation of salary + bonus - taxes.
Make sure to return an error if the user enters a string instead of a number.
Make sure the user sends the 3 fields.
Input:

{
    "salary": 2500,
    "bonus": 200,
    "taxes": 400
}
Outputs:

If the user enters a valid input:

{
    "result": 2300 // salary + bonus - taxes
}
If the user enters a string:

{
    "error": "expected numbers, got strings."
}

If the user forgets a field: ```json { "error": f"3 fields expected (salary, bonus, taxes). You forgot: {FIELD_THE_USER_FORGOT_HERE}." }

# Installation
## Required modules and versions
There are modules that are needed to run this program. Here is a list of them and version that are tested with this program. Python version used is 3.9.10.



| Module        | Version  |
|---------------| ---------|
| geopandas     | 0.9.0    |