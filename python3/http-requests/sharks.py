# Credit for this example goes to one of my students, Patrick.
# Thanks for the cool example!

import twilio
from twilio.rest import Client
import json
import bs4
import requests
from pprint import pprint

data = json.loads(open('secret.json', 'r').read())

# secret.json should look like this:
"""
{
	"sid": '2f3414b12a341c23',
    "authToken": '89c7897f9788a9879c',
    "twilioNumber": '7752313234',
    "myNumber": '7732123190'
}
"""

res = requests.get('http://www.sharkresearchcommittee.com/pacific_coast_shark_news.htm')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = soup.select('body > div > div > center > table > tr > td:nth-of-type(2) > p:nth-of-type(8) > strong > font')
v = elems[0].text
pprint(elems)

accountSID = data['sid']
authToken = data['authToken']
twilioCli = Client(accountSID, authToken)

myTwilioNumber = data['twilioNumber']
myCellPhone = data['myNumber']

message = twilioCli.messages.create(body = 'Warning: Shark sighting off the coast of ' + v + 'Beach !', from_=myTwilioNumber, to=myCellPhone)



