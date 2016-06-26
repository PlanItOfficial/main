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
    'lang': 'en'
}

response = client.search('San Francisco', **params)
print (response.businesses[0].name)