
from StringIO import StringIO

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import getFSVersionTuple

def install(self):
    out = StringIO()

    tool=getToolByName(self, "portal_setup")

    if getFSVersionTuple()[:3]>=(3,0,0):
        tool.runAllImportStepsFromProfile(
            "profile-cs.donedukia:default",
            purge_old=False)
    else:
        plone_base_profileid = "profile-CMFPlone:plone"
        tool.setImportContext(plone_base_profileid)
        tool.setImportContext("profile-cs.donedukia:plone-2.5")
        tool.runAllImportSteps(purge_old=False)
        tool.setImportContext(plone_base_profileid)

    print >> out, "cs.donedukia successfully installed"

    return out.getvalue()
    
