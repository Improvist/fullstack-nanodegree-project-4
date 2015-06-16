#!/usr/bin/env python

"""
main.py -- Udacity conference server-side Python App Engine
    HTTP controller handlers for memcache & task queue access

$Id$

created by wesc on 2014 may 24

"""

__author__ = 'wesc+api@google.com (Wesley Chun)'

import webapp2
from google.appengine.api import app_identity
from google.appengine.api import mail
from google.appengine.api import memcache
from google.appengine.ext import ndb

from conference import ConferenceApi
from conference import MEMCACHE_FEATURED_SPEAKERS_KEY
from models import ConferenceSession
class SetAnnouncementHandler(webapp2.RequestHandler):
    def get(self):
        """Set Announcement in Memcache."""
        ConferenceApi._cacheAnnouncement()
        self.response.set_status(204)


class SendConfirmationEmailHandler(webapp2.RequestHandler):
    def post(self):
        """Send email confirming Conference creation."""
        mail.send_mail(
            'noreply@%s.appspotmail.com' % (
                app_identity.get_application_id()),     # from
            self.request.get('email'),                  # to
            'You created a new Conference!',            # subj
            'Hi, you have created a following '         # body
            'conference:\r\n\r\n%s' % self.request.get(
                'conferenceInfo')
        )

class EstablishFeaturedSpeaker(webapp2.RequestHandler):
    def post(self):
        """Establish if a speaker is duplicated and adds it to the Featured Speaker memcache if it is."""
        confKey = ndb.Key(urlsafe=self.request.get('websafeConferenceKey'))
        sessions = ConferenceSession.query(ancestor=confKey).filter(ConferenceSession.speaker == self.request.get('speaker'))
        if(sessions.count() > 1):
            featured_speakers = '%s %s %s' % (
                'The featured speaker ',
                self.request.get('speaker'), 
                ' is hosting the following sessions:'
                ' '.join(sess.name for sess in sessions))
            memcache.set(MEMCACHE_FEATURED_SPEAKERS_KEY, featured_speakers)

app = webapp2.WSGIApplication([
    ('/crons/set_announcement', SetAnnouncementHandler),
    ('/tasks/send_confirmation_email', SendConfirmationEmailHandler),
    ('/tasks/establish_featured_speaker', EstablishFeaturedSpeaker)
], debug=True)
