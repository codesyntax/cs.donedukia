"""Definition of the DonEdukia content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder, document
from Products.ATContentTypes.content import schemata
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget


from cs.donedukia import donedukiaMessageFactory as _
from Products.ATContentTypes import ATCTMessageFactory as AT_
from cs.donedukia.interfaces import IDonEdukia
from cs.donedukia.config import PROJECTNAME, ADD_PERMISSIONS

DonEdukiaSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
    atapi.TextField('text',
                    required=False,
                    searchable=True,
                    storage=atapi.AnnotationStorage(),
                    validators=('isTidyHtmlWithCleanup',),
                    default_output_type='text/x-html-safe',
                    widget=atapi.RichWidget(label=_(u"label_body_text", default=u'Body Text'),
                                            description=_(u"label_body_text_description", default=u'The content of this page'),
                                            rows=25,
                                            allow_file_upload=False),
                    ),
        atapi.BooleanField('tableContents',
                           required = False,
                           widget = atapi.BooleanWidget(
                                      label= AT_(u'help_enable_table_of_contents', default=u'Table of contents'),
                                      description = AT_(u'help_enable_table_of_contents_description', default=u'If selected, this will show a table of contents at the top of the page.')
                                      ),
                           ),
        atapi.BooleanField('showcontents',
                           required = False,
                           widget = atapi.BooleanWidget(
                                      label= _(u'label_showcontents', default=u'Show the contents?'),
                                      description = AT_(u'help_showcontents_description', default=u'If selected, the contents of this object will be shown in a listing'),
                                      ),
                           ),

    ))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

DonEdukiaSchema['title'].storage = atapi.AnnotationStorage()
DonEdukiaSchema['description'].storage = atapi.AnnotationStorage()

DonEdukiaSchema.changeSchemataForField('tableContents', 'settings')
DonEdukiaSchema.addField(schemata.relatedItemsField.copy())
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