from flask import *
import cgi
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from xml.dom import minidom

zipcode = ''

app = Flask(__name__)


def hello():
    print "hellfsjdla;fal;slkldsfkdsafklfdaskl;fdskl;fkl;asdfkdsa;o"

@app.route("/JSON")
def getrecs():
    auth = Oauth1Authenticator(
        consumer_key = "4mKzLgbw5zlE-O7Jle9kJg",
        consumer_secret = "xQVDkzJQmbr26heYvjmRT6vCyuY",
        token = "jStDNSrNExPPOYbafiRrnL01AphMONJH",
        token_secret = "EH3SLPVzI4qKGxPOtlYRyPgcpkI"
    )


    client = Client(auth)
    params = {
        'term': 'breakfast',
        'lang': 'en',
        'radius_filter': 10000
    }

    response = client.search(zipcode, **params)

    rate1 = str(response.businesses[0].rating)
    rate2 = str(response.businesses[1].rating)
    rate3 = str(response.businesses[2].rating)
    string = "data= {[" + response.businesses[0].name + "= { \"name\": " + response.businesses[0].name + ",\"rating\": "
    string += rate1 + ",\"image_url\": " + response.businesses[0].image_url + "}," + response.businesses[1].name
    string += ": {\"name\": " + response.businesses[1].name + "\"rating\": " + rate2 + ",\"image_url\": "
    string += response.businesses[1].image_url + "}," + response.businesses[2].name + ": {\"name\": " + response.businesses[2].name
    string += ",\"rating\": " + rate3 + ",\"image_url\": " + response.businesses[2].image_url + " }] }"
    return string

    # return repsonse.businesses


    # print (response.businesses[0].name)
    # print (response.businesses[1].name)
    # print (response.businesses[2].name)

@app.route('/', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':
        
        # print request.form['zipcode']
        global zipcode
        zipcode = request.form['zipcode']
        
        
        return render_template('conferences.html')

    else:
        return render_template('signup.html')

# @app.route("/JSON")
# def test(zipcode = 95129):
#     return getrecs(zipcode)

if __name__ == "__main__":
    app.run()

print zipcode






# getrecs('94089')
