from Acquisition import aq_inner
from Acquisition import aq_parent
from Products.ATContentTypes.interfaces.document import IATDocument
from Products.ATContentTypes.interfaces.folder import IATFolder
from Products.CMFCore.utils import getToolByName
from five import grok
from sll.theme.browser.interfaces import ISllThemeLayer
from plone.app.contentlisting.interfaces import IContentListing


class View(grok.View):

    grok.context(IATFolder)
    grok.layer(ISllThemeLayer)
    grok.require('zope2.View')
    grok.name('sll-view')

    def image(self):
        return self.context.getField('leadImage').tag(self.context)

    def text(self):
        return self.context.CookedBody()

    def items(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        limit = 4
        query = {
            'object_provides': IATDocument.__identifier__,
            'path': {
                'query': '/'.join(context.getPhysicalPath()),
            },
            'sort_on': 'modified', 
            'sort_order': 'reverse',
            'sort_limit': limit,
        }
        res = catalog(query)[:limit]
        items = [
            {
                'title': item.Title(),
                'url': item.getURL(),
                'parent': aq_parent(item.getObject()).Title(),
                'parent_url': aq_parent(item.getObject()).absolute_url(),
                'description': item.Description(),
                'object': item.getObject(),
            } for item in IContentListing(res)
        ]
        return items
