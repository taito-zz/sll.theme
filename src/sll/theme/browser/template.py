from five import grok
from sll.templates.browser.template import BaseDocumentView
from sll.theme.browser.interfaces import ISllThemeLayer

grok.templatedir('templates')


class MonthlySupporterView(BaseDocumentView):
    grok.layer(ISllThemeLayer)
    grok.name('monthly-supporter')
    grok.template('monthly-supporter')
