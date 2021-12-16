import urllib
import urllib2

# consumindo um web service rest - get
def get():
   url = 'http://www.acme.com/products/3322'
   response = urllib2.urlopen(url).read()

#usando um web service rest - post
def post():
   url = 'http://www.acme.com/users/details'
   params = urllib.urlencode({
     'firstName': 'John',
     'lastName': 'Doe'
   })
   response = urllib2.urlopen(url, params).read()

