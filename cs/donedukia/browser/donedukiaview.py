from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from cs.donedukia import donedukiaMessageFactory as _


class IDonEdukiaView(Interface):
    """
    donedukia view interface
    """

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

