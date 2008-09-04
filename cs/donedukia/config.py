"""Common configuration constants
"""

PROJECTNAME = 'cs.donedukia'

ADD_PERMISSIONS = {
    # -*- extra stuff goes here -*-
    'DonEdukia': 'cs.donedukia: Add DonEdukia',
}

from Products.CMFPlone.utils import getFSVersionTuple

version = getFSVersionTuple()
if version[0] == 2:
    IS_PLONE2 = True
    IS_PLONE3 = False
elif version[0] == 3:
    IS_PLONE2 = False
    IS_PLONE3 = True
else: # What!!
    IS_PLONE2 = False
    IS_PLONE3 = False
