#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Iain'
SITENAME = "Dodsworld"
SITEURL = 'https://distracted-snyder-1a6b70.netlify.app'


PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Photography & Video', 'http://iainweir.info/'),
         )

# Menu
MAIN_MENU = True
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/shutteritch'),
          ('linkedin', 'https://www.linkedin.com/in/iainweirphotography/'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "venv/lib/python3.7/site-packages/pelican/themes/Flex"
TWITTER_USERNAME = "shutteritch"

COPYRIGHT_NAME = "Iain Weir"
COPYRIGHT_YEAR = "2020"
