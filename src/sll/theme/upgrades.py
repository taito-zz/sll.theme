from abita.utils.utils import reimport_profile


PROFILE_ID = 'profile-sll.theme:default'


def reimport_cssregistry(context):
    """Reimport cssregistry"""
    reimport_profile(context, PROFILE_ID, 'cssregistry')


def reimport_browserlayer(context):
    """Reimport browserlayer"""
    reimport_profile(context, PROFILE_ID, 'browserlayer')
