import requests
import pandas as pd
import json

client_id = 'ZBBlQj92l65SyjC6YzEH_g'
api_key = '41YvkoW5FMAgUGm8_585Kg2EzUMmkFc_nrbzMPl0uvOPQ0Wn_8wrbbvL0mlHx2RW1hTwEKd0q-LU2cjN9lv5fqt7pQ4jsHzczk27-YV0E8satnXmSJHiNxCQ93aAXHYx'

term = 'grill'
location = 'Los angeles CA'
SEARCH_LIMIT = 50
offset=501s
url = 'https://api.yelp.com/v3/businesses/search'

# for index in range(100):
# 	offset+=50

headers = {
        'Authorization': 'Bearer {}'.format(api_key),
    }

url_params = {
                'term': term.replace(' ', '+'),
                'location': location.replace(' ', '+'),
                'limit': SEARCH_LIMIT,
                'offset': offset
            }
response = requests.get(url, headers=headers, params=url_params)

#print(response.json()['region'])
df = pd.DataFrame.from_dict(response.json()['businesses'])
df.to_csv("yelpLosAngelesRestaurants.csv", mode = 'a' ,index=False ,sep=',')
print(len(df))
print(df.columns)
print(df.head())

#print(response)
#print(type(response.text))
#print(response.text[:1000])
