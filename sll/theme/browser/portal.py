from five import grok
from sll.theme.browser.interfaces import ISllThemeLayer
from Products.CMFCore.interfaces._content import ISiteRoot


class View(grok.View):

    grok.context(ISiteRoot)
    grok.layer(ISllThemeLayer)
    grok.require('zope2.View')
    grok.name('sll-view')
