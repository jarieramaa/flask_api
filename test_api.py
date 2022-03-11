"""This module is for testing flack_challenge.py API"""

import requests
import pycurl
from io import BytesIO, StringIO
import json

def binary_to_dict(the_binary):
    jsn = ''.join(chr(int(x, 2)) for x in the_binary.split())
    d = json.loads(jsn)  
    return d

def test_multiply():
    """This is a test function for the API."""
    crl = pycurl.Curl()
    buffer = BytesIO()
    #buffer = StringIO()
    crl.setopt(crl.URL, "http://127.0.0.1:5000/multiply/56")
    crl.setopt(crl.WRITEDATA, buffer)
    crl.perform()
    crl.close()
    response = buffer.getvalue()
    my_dictonary = dict(json.loads(response.decode('utf-8')))
    print(my_dictonary)

def test_api():
    """This is a test function for the API."""

    my_result = requests.get(
        "http://127.0.0.1:5000/salary",
        params={
            "salary": 2500,
            "bonus": 2000,
            "taxes": 1800,
        },
    )
    print(my_result.text)

    my_result = requests.post(
        "http://127.0.0.1:5000/salary",
        params={
            "salary": 3000,
            "bonus": 1000,
            "taxes": 1500,
        },
    )
    print(my_result.text)


if __name__ == "__main__":
    test_api()
    test_multiply()

