import cgi
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator


auth = Oauth1Authenticator(
    consumer_key = "4mKzLgbw5zlE-O7Jle9kJg",
    consumer_secret = "xQVDkzJQmbr26heYvjmRT6vCyuY",
    token = "jStDNSrNExPPOYbafiRrnL01AphMONJH",
    token_secret = "EH3SLPVzI4qKGxPOtlYRyPgcpkI"
)

def getRestaurants(latitude, longitude):
    client = Client(auth)

    params = {
        'term': 'food',
        'lang': 'en',
        'radius_filter': 10000
    }

    response = client.search_by_coordinates(latitude, longitude, **params)
    return response.businesses
