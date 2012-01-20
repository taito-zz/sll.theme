from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from plone.app.layout.viewlets.common import PathBarViewlet


class PathBarViewlet(PathBarViewlet):
    index = ViewPageTemplateFile('viewlets/path_bar.pt')


class FooterViewlet(ViewletBase):
    index = ViewPageTemplateFile('viewlets/footer.pt')
