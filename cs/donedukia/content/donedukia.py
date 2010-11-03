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
    
DonEdukiaSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
    atapi.TextField('text',
                    required=False,
                    searchable=True,
                    storage=atapi.AnnotationStorage(),
                    validators=('isTidyHtmlWithCleanup',),
                    default_content_type='text/html',
                    allowable_content_types =('text/html',),
                    default_output_type='text/x-html-safe',
                    widget=atapi.RichWidget(label=AT_(u"label_body_text", default=u'Body Text'),
                                            description= '',
                                            rows=25,
                                            allow_file_upload=False),
                    ),
    ))


    DonEdukiaSchema = DonEdukiaSchema.copy() + atapi.Schema((
    
        atapi.BooleanField('tableContents',
                           required = False,
                           widget = atapi.BooleanWidget(
                                      label= AT_(u'help_enable_table_of_contents', default=u'Table of contents'),
                                      description = AT_(u'help_enable_table_of_contents_description', default=u'If selected, this will show a table of contents at the top of the page.')
                                      ),
                           ),

    ))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

DonEdukiaSchema['title'].storage = atapi.AnnotationStorage()
DonEdukiaSchema['description'].storage = atapi.AnnotationStorage()

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
