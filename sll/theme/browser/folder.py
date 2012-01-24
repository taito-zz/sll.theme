from Products.ATContentTypes.interfaces.folder import IATFolder
from Products.CMFCore.utils import getToolByName
from five import grok
from sll.theme.browser.interfaces import ISllThemeLayer


class View(grok.View):

    grok.context(IATFolder)
    grok.layer(ISllThemeLayer)
    grok.require('zope2.View')
    grok.name('sll-view')

    def image(self):
        return self.context.getField('leadImage').tag(self.context)

    def text(self):
        return self.context.CookedBody()
