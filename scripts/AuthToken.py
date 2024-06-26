import os
import requests
import json

# Function to get the whole response object from the auth request to Learn
def auth_request():
    learn_domain = os.environ.get('LEARN_DOMAIN')
    app_key = os.environ.get('APP_KEY')
    app_secret = os.environ.get('APP_SECRET')

    auth_url = 'https://' + learn_domain + '/learn/api/public/v1/oauth2/token'
    data = {
        'grant_type': 'client_credentials',
    }

    return requests.post(auth_url, auth=(app_key, app_secret), data=data)

# Function to get the response from the response object
def get_auth_token():
    response = auth_request()
    return response.json()

#
def auth_request_verbose():
    response = auth_request()
    print("Request URL: " + response.request.url)
    print("Request Headers:")
    print(json.dumps(dict(response.request.headers), indent=4))
    print("Request Body: " + str(response.request.body))
    print("Response Status Code: " + str(response.status_code))
    print("Response Headers:")
    print(json.dumps(dict(response.headers), indent=4))
    print("Response Body:")
    print(json.dumps(response.json(), indent=4))

if __name__ == '__main__':
    auth_request_verbose()