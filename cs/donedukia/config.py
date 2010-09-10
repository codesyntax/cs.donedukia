"""Common configuration constants
"""

PROJECTNAME = 'cs.donedukia'

ADD_PERMISSIONS = {
    # -*- extra stuff goes here -*-
    'DonEdukia': 'cs.donedukia: Add DonEdukia',
}

from Products.CMFPlone.utils import getFSVersionTuple

version = getFSVersionTuple()
IS_PLONE2 = False
IS_PLONE3 = False
IS_PLONE4 = False

if version[0] == 2:
    IS_PLONE2 = True
elif version[0] == 3:
    IS_PLONE3 = True
elif version[0] == 4:
    IS_PLONE4 = True
