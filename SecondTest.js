// Request API access: http://www.yelp.com/developers/getting_started/api_access
var Yelp = require('yelp');

var yelp = new Yelp({
  consumer_key: "4mKzLgbw5zlE-O7Jle9kJg",
  consumer_secret: "xQVDkzJQmbr26heYvjmRT6vCyuY",
  token: "jStDNSrNExPPOYbafiRrnL01AphMONJH",
  token_secret: "EH3SLPVzI4qKGxPOtlYRyPgcpkI",
});

var data;
// See http://www.yelp.com/developers/documentation/v2/search_api
yelp.search({ term: 'pizza', location: 'San Jose' })
.then(function (data) {
  this.data = data;
})
.catch(function (err) {
  console.error(err);
});

console.log(data);

// See http://www.yelp.com/developers/documentation/v2/business
yelp.business('yelp-san-francisco')
  .then()
  .catch(console.error);

// A callback based API is also available:
yelp.business('yelp-san-francisco', function(err, data) {
  if (err) return console.log(error);
  console.log(data.name);
});
