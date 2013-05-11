from Acquisition import aq_inner
from Acquisition import aq_parent
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from collective.searchevent.browser.viewlet import SearchEventResultsViewlet


class SLLSearchEventResultsViewlet(SearchEventResultsViewlet):
    index = ViewPageTemplateFile('viewlets/search-event-results.pt')

    def parent(self, item):
        return aq_parent(aq_inner(item.getObject()))
