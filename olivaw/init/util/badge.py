"""Module providing functions related to the badges URIs"""

from olivaw.constants import REF, GIST_BADGE_PREFIX


def badge_url(dev: str, gist_id: str, badge: str) -> str:
    """Generates a badge URI

    :param dev: The developper username
    :type dev: `str`

    :param gist_id: The gist identifier
    :type gist_id: `str`

    :param badge: The badge type
    :type badge: `str`

    :returns: The badge URI
    :rtype: `str`
    """
    return f"{GIST_BADGE_PREFIX}/{dev}/{gist_id}/raw/{'_'.join(REF.split('/')[1:])}_{badge}.json"