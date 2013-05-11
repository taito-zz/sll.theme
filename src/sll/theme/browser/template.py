from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from sll.templates.browser.template import BaseDocumentView


class MonthlySupporterView(BaseDocumentView):
    __call__ = ViewPageTemplateFile('templates/monthly-supporter.pt')
