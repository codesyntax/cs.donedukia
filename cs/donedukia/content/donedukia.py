"""Definition of the DonEdukia content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder, document
from Products.ATContentTypes.content import schemata

from cs.donedukia.interfaces import IDonEdukia
from cs.donedukia.config import PROJECTNAME, IS_PLONE3, IS_PLONE4


try:
    from Products.ATContentTypes import ATCTMessageFactory as AT_
except ImportError:
    from zope.i18nmessageid import MessageFactory
    AT_ = MessageFactory('atcontenttypes')
    
DonEdukiaSchema = document.ATDocumentSchema.copy() + folder.ATFolderSchema.copy()

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

DonEdukiaSchema['title'].storage = atapi.AnnotationStorage()
DonEdukiaSchema['description'].storage = atapi.AnnotationStorage()
DonEdukiaSchema['text'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(DonEdukiaSchema, folderish=True, moveDiscussion=False)
# finalizeATCTSchema hides relatedItems for folderish items
DonEdukiaSchema['relatedItems'].widget.visible['edit'] = 'visible'


class DonEdukia(folder.ATFolder, document.ATDocument):
    """A Folderish Page"""
    implements(IDonEdukia)

    portal_type = "DonEdukia"
    schema = DonEdukiaSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    text = atapi.ATFieldProperty('text')

    
atapi.registerType(DonEdukia, PROJECTNAME)
