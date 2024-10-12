# Request module
# module - package or library contains functions which you can use easily
# math, os, allure, pytest

# To make teh HTTP - Methods
# Request - Module
# GET, POST, PUT, PATCH , DELETE

# Request ( CLient - Server )
# GET request - Booking ID
# URL - https://restful-booker.herokuapp.com
# Auth? - no
# Payload? - no
# Content-type or header - not neededd
# query param - not needed
# path param - yes - 1

# respomse
# Body --. verify -assert., keys, values
# status code - verify
# time
# json schema, xml schema


import allure  # pip install allure
import pytest  # pip install pytest
import requests  # pip install requests
from django.contrib.gis.geometry import json_regex


#test case we are created
@allure.title("TC#1 - Create Booking CRUD Positive ")
@allure.description("TC#1 - Verify the create Booking!")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    # To make Request
    # URL
    # Method - POST
    # Headers - Content-type=Application/json
    # Payload / Data / Body - Dict / JSON
    # Auth(No)
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    responseData = requests.post(url=URL, headers=headers, json=payload) #positional parameter we are using
    responseData = responseData.json()

    # Response Body  Verification,
    # Headers
    # Status Code

    # verifying key one by one

    assert responseData["bookingid"] is not None
    firstname =  responseData["booking"]["firstname"]
    assert firstname == "Jim"
    assert responseData["booking"]["lastname"] == "Brown"
    last_name = responseData["booking"]["lastname"]

    checkin = responseData["booking"]["bookingdates"]["checkin"]
    assert checkin == "2018-01-01"
    checkout  = responseData["booking"]["bookingdates"]["checkout"]
    assert checkout == "2019-01-01"

    totalprice = responseData["booking"]["totalprice"]
    assert totalprice == 111
    depositpaid = responseData["booking"]["depositpaid"]
    assert depositpaid == False


@allure.title("TC#2- Create Booking CRUD Negative")
@allure.description("TC#2 - Verify Booking is not created with {} data ")
@pytest.mark.crud
def test_create_booking_negative_tc2():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    json_payload = {}
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    # Assertions
    assert response.status_code == 500


@allure.title("TC#3- NegativeCreate Booking CRUD Negative")
@allure.description("TC#3 - Verify booking with total price with string!")
@pytest.mark.crud
def test_create_booking_negative_tc3():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": "pramod", # putting string instead of int # output : NULL
        "depositpaid": "true",
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    responseData = requests.post(url=URL, headers=headers, json=json_payload)  # positional parameter we are using


    # Assertions
    assert responseData.status_code == 200