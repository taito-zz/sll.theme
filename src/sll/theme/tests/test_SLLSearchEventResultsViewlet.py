from Products.CMFCore.utils import getToolByName
from sll.theme.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for SLLSearchEventResultsViewlet"""

    def setUp(self):
        self.portal = self.layer['portal']
        from plone.app.testing import TEST_USER_ID
        from plone.app.testing import setRoles
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_parent(self):
        from sll.theme.browser.viewlet import SLLSearchEventResultsViewlet
        from zope.publisher.browser import TestRequest
        doc = self.portal[self.portal.invokeFactory('Document', 'doc')]
        doc.reindexObject()
        viewlet = SLLSearchEventResultsViewlet(doc, TestRequest(), None, None)
        item = getToolByName(self.portal, 'portal_catalog')(id='doc')[0]
        self.assertEqual(viewlet.parent(item), self.portal)
