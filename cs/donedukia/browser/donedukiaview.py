from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from cs.donedukia import donedukiaMessageFactory as _
from cs.donedukia.interfaces import IDonEdukia

class IDonEdukiaView(Interface):
    """
    donedukia view interface
    """

    def isPlone2():
        """ Return if this is Plone 2 """

    def isPlone3():
        """ Return if this is Plone 3 """


class DonEdukiaView(BrowserView):
    """
    donedukia browser view
    """
    implements(IDonEdukiaView)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()

    
    def isPlone2(self):
        from cs.donedukia.config import IS_PLONE2
        return IS_PLONE2

    def isPlone3(self):
        from cs.donedukia.config import IS_PLONE3
        return IS_PLONE3

    
