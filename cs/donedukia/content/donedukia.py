"""Definition of the DonEdukia content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from cs.donedukia import donedukiaMessageFactory as _
from cs.donedukia.interfaces import IDonEdukia
from cs.donedukia.config import PROJECTNAME

DonEdukiaSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

DonEdukiaSchema['title'].storage = atapi.AnnotationStorage()
DonEdukiaSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(DonEdukiaSchema, folderish=True, moveDiscussion=False)

class DonEdukia(folder.ATFolder):
    """A Folderish Page"""
    implements(IDonEdukia)

    portal_type = "DonEdukia"
    schema = DonEdukiaSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

atapi.registerType(DonEdukia, PROJECTNAME)
