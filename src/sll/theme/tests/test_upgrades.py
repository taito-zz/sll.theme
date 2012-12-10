from sll.theme.tests.base import IntegrationTestCase

import mock


class TestCase(IntegrationTestCase):
    """TestCase for upgrade step"""

    def setUp(self):
        self.portal = self.layer['portal']

    @mock.patch('sll.theme.upgrades.reimport_profile')
    def test_reimport_cssregistry(self, reimport_profile):
        from sll.theme.upgrades import reimport_cssregistry
        reimport_cssregistry(self.portal)
        reimport_profile.assert_called_with(self.portal, 'profile-sll.theme:default', 'cssregistry')

    @mock.patch('sll.theme.upgrades.reimport_profile')
    def test_reimport_browserlayer(self, reimport_profile):
        from sll.theme.upgrades import reimport_browserlayer
        reimport_browserlayer(self.portal)
        reimport_profile.assert_called_with(self.portal, 'profile-sll.theme:default', 'browserlayer')
