from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('signup.html')

@app.route("/JSON")
def test(zipcode = 95129):
    return getRestaurants(latitude, longitude)

if __name__ == "__main__":
    app.run()

import cgi
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator


auth = Oauth1Authenticator(
    consumer_key = "4mKzLgbw5zlE-O7Jle9kJg",
    consumer_secret = "xQVDkzJQmbr26heYvjmRT6vCyuY",
    token = "jStDNSrNExPPOYbafiRrnL01AphMONJH",
    token_secret = "EH3SLPVzI4qKGxPOtlYRyPgcpkI"
)

def getRestaurants(zipcode):
    client = Client(auth)

    params = {
        'term': 'food',
        'lang': 'en',
        'radius_filter': 10000
    }

    response = client.search(zipcode, **params)
    return response.businesses
