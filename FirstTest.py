import cgi
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator


auth = Oauth1Authenticator(
    consumer_key = "4mKzLgbw5zlE-O7Jle9kJg",
    consumer_secret = "xQVDkzJQmbr26heYvjmRT6vCyuY",
    token = "jStDNSrNExPPOYbafiRrnL01AphMONJH",
    token_secret = "EH3SLPVzI4qKGxPOtlYRyPgcpkI"
)

client = Client(auth)

params = {
    'term': 'food',
    'lang': 'en',
    'radius_filter': 10000
}

response = client.search_by_coordinates(37.410095, -122.036015, **params)
print (response.businesses[0].name)
print (response.businesses[1].name)
print (response.businesses[2].name)
