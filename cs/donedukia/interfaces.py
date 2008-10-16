from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from Products.ATContentTypes.interface import IATDocument, IATFolder

from cs.donedukia import donedukiaMessageFactory as _

# -*- extra stuff goes here -*-

class IDonEdukia(Interface):
    """A Folderish page"""



