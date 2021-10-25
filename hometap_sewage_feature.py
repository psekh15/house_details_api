#!/usr/bin/env python

import requests
import json

url = "https://5d6ece19-593e-4367-b15d-e4f27a41f4b7.mock.pstmn.io/v2/property/details"
api_key = {'x-api-key' : 'PMAK-61716a46a10f020058177108-1f4218e9b409133983d20c010f7bd1add6'}

def fetch_homecanaryapi_house_details(address, zipcode, url, api_key):
    params = { 'address' : address,
            'zipcode':  zipcode }
  
    house_details_response = requests.get(url, params=params, headers=api_key)
    
    if house_details_response is not None:
        return house_details_response.json()
    return None


def ask_additional_question(address, zipcode, url, api_key):
    house_details_json_data = fetch_homecanaryapi_house_details(address, zipcode, url, api_key)
    property_details = house_details_json_data['property/details']['result']['property']
    sewer_type = property_details['sewer']
    if sewer_type == 'septic':
        return True
    return False
    

def main():
    customers = []
    customer_1 = {'address': '123 Main St', 'zipcode' : '94132'}
    customer_2 = {'address': '124 Main St', 'zipcode' : '94132'}
    customers.append(customer_1)
    customers.append(customer_2)
    for customer in customers:
        print(f"\nFor The web app, should customer with {customer} be prompted with an additional question?")
        if ask_additional_question(customer['address'], customer['zipcode'], url, api_key):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()