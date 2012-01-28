from Acquisition import aq_inner
from Acquisition import aq_parent
from Products.ATContentTypes.interfaces.document import IATDocument
from Products.ATContentTypes.interfaces.event import IATEvent
from Products.ATContentTypes.interfaces.folder import IATFolder
from Products.ATContentTypes.interfaces.news import IATNewsItem
from Products.CMFCore.interfaces import ISiteRoot
from Products.CMFCore.interfaces._content import ISiteRoot
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from five import grok
from plone.app.contentlisting.interfaces import IContentListing
from plone.app.kss.interfaces import IPortalObject
from plone.app.layout.viewlets.common import PathBarViewlet
from plone.app.layout.viewlets.common import ViewletBase
from sll.theme.browser.interfaces import ISllThemeLayer
from zope.component import getMultiAdapter


class PathBarViewlet(PathBarViewlet):
    index = ViewPageTemplateFile('viewlets/path_bar.pt')


class FooterViewlet(ViewletBase):
    index = ViewPageTemplateFile('viewlets/footer.pt')


class FeedViewlet(ViewletBase):
    index = ViewPageTemplateFile('viewlets/feed.pt')

    def items(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        limit = 3
        query = {
            'object_provides': (IATDocument.__identifier__, IATEvent.__identifier__),
            'sort_on': 'modified', 
            'sort_order': 'reverse',
            'sort_limit': limit,
            'Subject': 'top',
        }
        res = catalog(query)[:limit]
        ploneview = getMultiAdapter(
            (context, self.request),
            name=u'plone'
        )
        items = [
            {
                'title': item.Title(),
                'url': item.getURL(),
                'parent': aq_parent(item.getObject()).Title(),
                'parent_url': aq_parent(item.getObject()).absolute_url(),
                'description': self.description(item),
                'object': item.getObject(),
                'image': self.image(item),
                'date': ploneview.toLocalizedTime(item.ModificationDate()),
            } for item in IContentListing(res)
        ]
        return items

    def description(self, item):
        desc = item.Description()
        length = 200
        if len(desc) > length:
            ploneview = getMultiAdapter(
                (self.context, self.request),
                name=u'plone'
            )
            desc = ploneview.cropText(desc, length)
        return desc

    def image(self, item):
        html = item.getObject().restrictedTraverse('cropped-image')('leadImage', 'feed')
        if html is None:
            portal_state = getMultiAdapter(
                (self.context, self.request),
                name=u'plone_portal_state'
            )
            image_url = '{0}/++theme++sll.theme/images/feed-fallback.png'.format(portal_state.portal_url())
            html = '<div class="crop" style="width:170px;height:150px;">'
            html += '<img src="{0}" alt="{1}" title="{1}" />'.format(
                image_url,
                item.Title()
            )
            html += '</div>'
        return html


class NewsEventsFeedViewlet(ViewletBase):
    index = ViewPageTemplateFile('viewlets/news_events_feed.pt')


class SimpleFeedViewlet(ViewletBase):
    index = ViewPageTemplateFile('viewlets/simple_feed.pt')

    def feeds(self, identifier, limit=3):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        query = {
            'object_provides': identifier,
            'sort_on': 'modified', 
            'sort_order': 'reverse',
            'sort_limit': limit,
        }
        res = catalog(query)[:limit]
        ploneview = getMultiAdapter(
            (context, self.request),
            name=u'plone'
        )
        items = [
            {
                'title': item.Title(),
                'url': item.getURL(),
                'parent': aq_parent(item.getObject()).Title(),
                'parent_url': aq_parent(item.getObject()).absolute_url(),
                'date': ploneview.toLocalizedTime(item.ModificationDate()),
            } for item in IContentListing(res)
        ]
        return items


class NewsFeedViewlet(SimpleFeedViewlet):

    def items(self):
        return self.feeds(IATNewsItem.__identifier__)


class EventsFeedViewlet(SimpleFeedViewlet):

    def items(self):
        return self.feeds(IATEvent.__identifier__)


class FooterInfoViewlet(ViewletBase):
    index = ViewPageTemplateFile('viewlets/footer_info.pt')

    def items(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        # limit = 4
        query = {
            'object_provides': IATDocument.__identifier__,
            'path': {
                'query': '{0}/info'.format('/'.join(context.getPhysicalPath())),
            },
            # 'sort_limit': limit,
        }
        # res = catalog(query)[:limit]
        res = catalog(query)
        ploneview = getMultiAdapter(
            (context, self.request),
            name=u'plone'
        )
        items = [
            {
                'title': item.Title(),
                'url': item.getURL(),
                'description': item.Description(),
                'text': item.getObject().CookedBody(),
            } for item in IContentListing(res)
        ]
        return items


class FooterSubfoldersViewlet(ViewletBase):
    index = ViewPageTemplateFile('viewlets/footer_subfolders.pt')