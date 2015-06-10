##### PROJECT WRITEUP (ANSWERS) ######
Task 1 Explanation:
	Sessions reference a parent conference to simply identify where they came from. As there is no implementation
	yet in place for what to do with sessons, their relationships is kept loose. For similar reasons, speakers 
	are kept as simple strings, for simplicity. As far as I'm aware, Google DataStore uses Memcache by default
	where it deems necessary, so manually enabling it for Sessions is lost on me.

Task 3 Explanation:
	NEW QUERIES:
	There are two new endpoints/queries I have added. The first's purpose is to grab all sessions within a conference
	that last less than or equal to a prescribed duration. This enables conference-goers to better distinguish short and
	long sessions, depending on their needs. The second's purpose is to grab all conferences that the user has attended
	in the past. There is similar functionality already in place (GetConferencesToAttend) but this ONLY grabs past
	conferences. The advantage of this is viewing a quick historical display of conferences for a user.
	QUERY PROBLEM:
	The only "problem" I see with this query is that it requires two filters at once. This isn't too difficult to
	implement with existing functionality, though. Example query:
		sessions = ConferenceSession.query(ndb.AND(ConferenceSession.typeOfSession != "workshop", 
												   ConferenceSession.startTime.hour < 19.0))

##### INCLUDED SETUP INFORMATION ######
App Engine application for the Udacity training course.

## Products
- [App Engine][1]

## Language
- [Python][2]

## APIs
- [Google Cloud Endpoints][3]

## Setup Instructions
1. Update the value of `application` in `app.yaml` to the app ID you
   have registered in the App Engine admin console and would like to use to host
   your instance of this sample.
1. Update the values at the top of `settings.py` to
   reflect the respective client IDs you have registered in the
   [Developer Console][4].
1. Update the value of CLIENT_ID in `static/js/app.js` to the Web client ID
1. (Optional) Mark the configuration files as unchanged as follows:
   `$ git update-index --assume-unchanged app.yaml settings.py static/js/app.js`
1. Run the app with the devserver using `dev_appserver.py DIR`, and ensure it's running by visiting your local server's address (by default [localhost:8080][5].)
1. (Optional) Generate your client library(ies) with [the endpoints tool][6].
1. Deploy your application.


[1]: https://developers.google.com/appengine
[2]: http://python.org
[3]: https://developers.google.com/appengine/docs/python/endpoints/
[4]: https://console.developers.google.com/
[5]: https://localhost:8080/
[6]: https://developers.google.com/appengine/docs/python/endpoints/endpoints_tool
