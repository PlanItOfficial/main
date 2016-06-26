from flask import *


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        print request.form['zipcode']
        return render_template('signup.html')
    else:
        return render_template('signup.html')

@app.route("/JSON")
def test(zipcode = 95129):
    return getrecs(zipcode)

if __name__ == "__main__":
    app.run()

import cgi
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

def getrecs(zipcode):
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

    response = client.search(zipcode, **params)
    # return repsonse.businesses

    # print (response.businesses[0].name)
    # print (response.businesses[1].name)
    # print (response.businesses[2].name)

getrecs('94089')
