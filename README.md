##### PROJECT WRITEUP (ANSWERS) ######
Task 1 Explanation:
	Sessions reference a parent conference to simply identify where they came from. As there is no implementation
	yet in place for what to do with sessons, their relationships is kept loose. For similar reasons, speakers 
	are kept as simple strings, for simplicity. As far as I'm aware, Google DataStore uses Memcache by default
	where it deems necessary, so manually enabling it for Sessions is lost on me.
	I use the Float property for duration so we can simply and easily represent all times based on a decimal 
	format, instead of using a "messy" Time property. 

Task 3 Explanation:
	NEW QUERIES:
	There are two new endpoints/queries I have added. The first's purpose is to grab all sessions within a conference
	that last less than or equal to a prescribed duration. This enables conference-goers to better distinguish short and
	long sessions, depending on their needs. The second's purpose is to grab all conferences that the user has attended
	in the past. There is similar functionality already in place (GetConferencesToAttend) but this ONLY grabs past
	conferences. The advantage of this is viewing a quick historical display of conferences for a user.
	QUERY PROBLEM:
	The problem with this is that if you have a not-equals comparison, you cannot have any other property
	filters. From their docs: 
		"The results are then merged, in order. A query can have no more than one not-equal filter, and a query 
		 that has one cannot have any other inequality filters."
	 The simplest way around this would be to add a field to the entity that in an amalgamation of 
	"startTime" and "sessionType" - basically it is a boolean field that says "true/false" if a case meets
	these criteria. This is a more-and-more common tradeoff of space for performance that is characterizing
	the modern data storage. Alternatively, you could write two separate queries (one for starttime after 7
	and one for typeofsession != workshop) and then use Python to find matches between them. For a mildly different
	flavor, depending on your data sizes, you could query for one of the sets (start time after 7 or type of session
	not equals to workshop) and then use python to filter out those that do not match your criteria.

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
