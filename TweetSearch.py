import requests as re
import json
import base64
import urllib 

# Twitter API credentials
Client_id = 'b0YwY2pzMDA3ak5oRWtuVm9mZXo6MTpjaQ'
Client_key = 'GmB-VefcAadlEWCuAhWY993L2V1hLurCadRTZ3cvHyLveHYPNP'
#url encode the credentials using RFC 1738
Client_id_encoded = urllib.parse.parse_qs(Client_id)
Client_key_encoded = urllib.parse.parse_qs(Client_key)

credential  = f"{Client_id_encoded}:{Client_key_encoded}"
credentials = base64.b64encode(credential.encode('utf-8')).decode('utf-8')
print(credentials)
#set the header with authorization and content type
headers = {'Authorization': 'Basic ' + credentials,
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Content-Length': '29'}
#set the url
url = 'https://api.twitter.com/oauth2/token'
#send a https post request to get the access token
print("sending the request")
#send a request with a body of grant_type=client_credentials
response = re.post(url, headers=headers, data='grant_type=client_credentials')
# response = re.post(url, headers=headers)
#parse the response to get the access token
print("received")
#store the response in a json format
res = response.json()
print(res)
#store them to a file
# with open('token.json', 'w') as f:
#     json.dump(res, f)
bearer = res['token_type'] + ' ' + res['access_token']
header_bearer = {'Authorization': bearer}
#set a get request to get the tweets
# url = 'https://api.twitter.com/1.1/search/tweets.json?q=from%3Aelonmusk&result_type=recent&count=10'
url = 'https://api.twitter.com/1.1/search/tweets.json?q=from%3Aelonmusk&result_type=recent&count=10'
#send a get request to get the tweets
response = re.get(url, headers=header_bearer)
