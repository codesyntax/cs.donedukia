"""Definition of the DonEdukia content type
"""

from zope.interface import implements, directlyProvides

try:
    from Products.LinguaPlone.public import *
except ImportError:
    from Products.Archetypes.atapi import *
    
from Products.ATContentTypes.content import folder, document
from Products.ATContentTypes.content import schemata

from cs.donedukia import donedukiaMessageFactory as _
from cs.donedukia.interfaces import IDonEdukia
from cs.donedukia.config import PROJECTNAME

DonEdukiaSchema = folder.ATFolderSchema.copy() + Schema((

    # -*- Your Archetypes field definitions here ... -*-
    TextField('text',
              required=False,
              searchable=True,
              primary=True,
              storage = AnnotationStorage(migrate=True),
              validators = ('isTidyHtmlWithCleanup',),
              #validators = ('isTidyHtml',),
              default_output_type = 'text/x-html-safe',
              widget = RichWidget(
                        description = '',
                        label = _(u'label_body_text', default=u'Body Text'),
                        rows = 25,
                        allow_file_upload = zconf.ATDocument.allow_document_upload),
    ),
    BooleanField('showcontents',
        required = False,
        languageIndependent = True,
        widget = BooleanWidget(
            label= _(
                u'help_showcontents', 
                default=u'Show contents?'),
            description = _(
                u'help_showcontents_description', 
                default=u'If selected, the contents of the elements will be shown in a listing at the bottom of the element.')
            ),
    ),

    

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

DonEdukiaSchema['title'].storage = atapi.AnnotationStorage()
DonEdukiaSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(DonEdukiaSchema, folderish=True, moveDiscussion=False)

class DonEdukia(document.ATDocument, folder.ATFolder):
    """A Folderish Page"""
    implements(IDonEdukia)

    portal_type = "DonEdukia"
    schema = DonEdukiaSchema

    title = ATFieldProperty('title')
    description = ATFieldProperty('description')
    text = ATFieldProperty('text')
    showcontents = ATFieldProperty('showcontents')

atapi.registerType(DonEdukia, PROJECTNAME)
