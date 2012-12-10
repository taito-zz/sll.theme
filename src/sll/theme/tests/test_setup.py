from Products.CMFCore.utils import getToolByName
from sll.basetheme.tests.test_setup import get_css_resource
from sll.theme.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_package__installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('sll.theme'))

    def test_browserlayer(self):
        from sll.theme.browser.interfaces import ISllThemeLayer
        from plone.browserlayer import utils
        self.failUnless(ISllThemeLayer in utils.registered_layers())

    def test_cssregistry__sll_theme_main__applyPrefix(self):
        resource = get_css_resource(self.portal, '++theme++sll.theme/css/main.css')
        self.assertTrue(resource.getApplyPrefix())

    def test_cssregistry__sll_theme_main__authenticated(self):
        resource = get_css_resource(self.portal, '++theme++sll.theme/css/main.css')
        self.assertFalse(resource.getAuthenticated())

    def test_cssregistry__sll_theme_main__compression(self):
        resource = get_css_resource(self.portal, '++theme++sll.theme/css/main.css')
        self.assertEqual(resource.getCompression(), 'safe')

    def test_cssregistry__sll_theme_main__conditionalcomment(self):
        resource = get_css_resource(self.portal, '++theme++sll.theme/css/main.css')
        self.assertEqual(resource.getConditionalcomment(), '')

    def test_cssregistry__sll_theme_main__cookable(self):
        resource = get_css_resource(self.portal, '++theme++sll.theme/css/main.css')
        self.assertTrue(resource.getCookable())

    def test_cssregistry__sll_theme_main__enabled(self):
        resource = get_css_resource(self.portal, '++theme++sll.theme/css/main.css')
        self.assertTrue(resource.getEnabled())

    def test_cssregistry__sll_theme_main__expression(self):
        resource = get_css_resource(self.portal, '++theme++sll.theme/css/main.css')
        self.assertEqual(resource.getExpression(), 'request/HTTP_X_THEME_ENABLED | nothing')

    def test_cssregistry__sll_theme_main__media(self):
        resource = get_css_resource(self.portal, '++theme++sll.theme/css/main.css')
        self.assertEqual(resource.getMedia(), 'screen')

    def test_cssregistry__sll_theme_main__rel(self):
        resource = get_css_resource(self.portal, '++theme++sll.theme/css/main.css')
        self.assertEqual(resource.getRel(), 'stylesheet')

    def test_cssregistry__sll_theme_main__rendering(self):
        resource = get_css_resource(self.portal, '++theme++sll.theme/css/main.css')
        self.assertEqual(resource.getRendering(), 'link')

    def test_cssregistry__sll_theme_main__title(self):
        resource = get_css_resource(self.portal, '++theme++sll.theme/css/main.css')
        self.assertIsNone(resource.getTitle())

    def test_cssregistry__sll_theme_extra__applyPrefix(self):
        resource = get_css_resource(self.portal, '++theme++sll.theme/css/extra.css')
        self.assertTrue(resource.getApplyPrefix())

    def test_cssregistry__sll_theme_extra__authenticated(self):
        resource = get_css_resource(self.portal, '++theme++sll.theme/css/extra.css')
        self.assertFalse(resource.getAuthenticated())

    def test_cssregistry__sll_theme_extra__compression(self):
        resource = get_css_resource(self.portal, '++theme++sll.theme/css/extra.css')
        self.assertEqual(resource.getCompression(), 'safe')

    def test_cssregistry__sll_theme_extra__conditionalcomment(self):
        resource = get_css_resource(self.portal, '++theme++sll.theme/css/extra.css')
        self.assertEqual(resource.getConditionalcomment(), '')

    def test_cssregistry__sll_theme_extra__cookable(self):
        resource = get_css_resource(self.portal, '++theme++sll.theme/css/extra.css')
        self.assertTrue(resource.getCookable())

    def test_cssregistry__sll_theme_extra__enabled(self):
        resource = get_css_resource(self.portal, '++theme++sll.theme/css/extra.css')
        self.assertTrue(resource.getEnabled())

    def test_cssregistry__sll_theme_extra__expression(self):
        resource = get_css_resource(self.portal, '++theme++sll.theme/css/extra.css')
        self.assertEqual(resource.getExpression(), 'request/HTTP_X_THEME_ENABLED | nothing')

    def test_cssregistry__sll_theme_extra__media(self):
        resource = get_css_resource(self.portal, '++theme++sll.theme/css/extra.css')
        self.assertEqual(resource.getMedia(), 'screen')

    def test_cssregistry__sll_theme_extra__rel(self):
        resource = get_css_resource(self.portal, '++theme++sll.theme/css/extra.css')
        self.assertEqual(resource.getRel(), 'stylesheet')

    def test_cssregistry__sll_theme_extra__rendering(self):
        resource = get_css_resource(self.portal, '++theme++sll.theme/css/extra.css')
        self.assertEqual(resource.getRendering(), 'link')

    def test_cssregistry__sll_theme_extra__title(self):
        resource = get_css_resource(self.portal, '++theme++sll.theme/css/extra.css')
        self.assertIsNone(resource.getTitle())

    def test_metadata__dependency__collective_searchevent(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('collective.searchevent'))

    def test_metadata__dependency__plone_app_theming(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('plone.app.theming'))

    def test_metadata__dependency__sll_basetheme(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('sll.basetheme'))

    def test_metadata__dependency__sll_carousel(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('sll.carousel'))

    def test_metadata__dependency__sll_templates(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('sll.templates'))

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile('profile-sll.theme:default'), u'4')

    def test_uninstall(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['sll.theme'])
        self.failIf(installer.isProductInstalled('sll.theme'))

    def test_uninstall__browserlayer(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['sll.theme'])
        from sll.theme.browser.interfaces import ISllThemeLayer
        from plone.browserlayer import utils
        self.failIf(ISllThemeLayer in utils.registered_layers())
