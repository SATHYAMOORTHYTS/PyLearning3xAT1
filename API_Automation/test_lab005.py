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

import pytest # pip install pytest
import allure # pip install allure-pytest
import requests

@allure.title("Test GET Request - RestFUL BOOKER Project#1")
@allure.description("TC#5 -> Verify that GET Request with ID works")
@allure.tag("regression", "smoke")
@allure.label("owner", "Pramod Dutta")
@allure.testcase("TC#5")
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData  = requests.get(url)
    print(responseData.text)
    print(responseData.headers)
    print(responseData.cookies)
    print(responseData.json())
    assert responseData.status_code == 200


