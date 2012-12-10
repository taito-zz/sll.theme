from Acquisition import aq_inner
from Acquisition import aq_parent
from collective.searchevent.browser.viewlet import SearchEventResultsViewlet
from five import grok
from sll.theme.browser.interfaces import ISllThemeLayer


grok.templatedir('viewlets')


class SLLSearchEventResultsViewlet(SearchEventResultsViewlet):
    grok.layer(ISllThemeLayer)
    grok.template('results')

    def parent(self, item):
        return aq_parent(aq_inner(item.getObject()))
