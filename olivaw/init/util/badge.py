"""Module providing functions related to the badges URIs"""

from olivaw.constants import REF, GIST_BADGE_PREFIX


def badge_url(dev, gist_id, badge):
    return f"{GIST_BADGE_PREFIX}/{dev}/{gist_id}/raw/{'_'.join(REF.split('/')[1:])}_{badge}.json"