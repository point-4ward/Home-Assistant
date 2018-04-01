"""
Support to check for pull requests related to current configuration.

Configuration:

developer:
  github_personal_token: 3456784235482398577563485739

get your token from https://github.com/settings/tokens

"""
import logging
from datetime import timedelta

import voluptuous as vol

from homeassistant.const import ATTR_FRIENDLY_NAME
from homeassistant.helpers.restore_state import async_get_last_state
from homeassistant.helpers import event
import homeassistant.helpers.config_validation as cv
import homeassistant.util.dt as dt_util

_LOGGER = logging.getLogger(__name__)

REQUIREMENTS = ['PyGithub']

HOMEASSITANT_ORGANIZATION = 'home-assistant'
HOMEASSITANT_REPO = 'home-assistant'

ATTR_LAST_UPDATED = 'last_updated'

NOTIFICATION_ID = 'developer_notification'

DOMAIN = 'developer'

FRIENDLY_NAME = 'Last reviewed PR'
ENTITY_ID = 'developer.last_signaled_pr'

CONF_GITHUB_PERSONAL_TOKEN = 'github_personal_token'

CONFIG_SCHEMA = vol.Schema({DOMAIN: {
    vol.Optional(CONF_GITHUB_PERSONAL_TOKEN, default=None): cv.string,
}}, extra=vol.ALLOW_EXTRA)

async def async_setup(hass, config):
    """Set up the hardware owner and developer component."""
    conf = config.get(DOMAIN, {})
    github_personal_token = conf[CONF_GITHUB_PERSONAL_TOKEN]
    _LOGGER.debug("Github token = %s", github_personal_token)

    last_state = await async_get_last_state(hass, ENTITY_ID)
    _LOGGER.debug("Last state: %s", last_state)
    if last_state:
        hass.states.async_set(ENTITY_ID, last_state.state,
                              {ATTR_FRIENDLY_NAME: FRIENDLY_NAME})

    def check_new_pullrequests(now):
        """Check on github for pull requests on platforms currently running."""
        from github import Github
        _LOGGER.debug("check_new_pullrequests")

        github_client = Github(github_personal_token)
        organization = github_client.get_organization(HOMEASSITANT_ORGANIZATION)
        repository = organization.get_repo(HOMEASSITANT_REPO)

        last_signaled_pr = hass.states.get(ENTITY_ID)
        _LOGGER.debug("Last signaled PR: %s", last_signaled_pr)

        installed_platforms = [p.split('.')[1] for p in list(hass.config.components) if "." in p]
        installed_platforms = set([p for p in installed_platforms if p not in ['homeassistant']])
        _LOGGER.debug(installed_platforms)

        pr_list = []
        for pull_request in repository.get_pulls():
            found = False
            _LOGGER.debug(pull_request.number)
            pr_list.append(pull_request.number)
            if last_signaled_pr and\
                pull_request.number <= int(last_signaled_pr.state):
                break

            for changed_file in pull_request.get_files():
                if found:
                    break
                for platform in installed_platforms:
                    if not found and\
                        platform in changed_file.filename.split('/')[-1]:
                        _LOGGER.debug("FOUND an interesting PR %s",
                                      pull_request.number)
                        hass.components.persistent_notification.create(
                            '&#35;{}: {}<br />'
                            '{}<br />'
                            'You are using {}'
                            ''.format(pull_request.number, pull_request.title,
                                      pull_request.html_url, platform),
                            title="New Pull Request",
                            notification_id="{}{}".format(NOTIFICATION_ID,
                                                          pull_request.number))
                        found = True

        _LOGGER.debug("Set %s to %s", ENTITY_ID, max(pr_list))
        hass.states.set(ENTITY_ID, max(pr_list),
                        {ATTR_FRIENDLY_NAME: FRIENDLY_NAME})

    # Update daily, start 1 hour after startup
    _dt = dt_util.utcnow() + timedelta(seconds=20)
    event.async_track_utc_time_change(
        hass, check_new_pullrequests,
        hour=_dt.hour, minute=_dt.minute, second=_dt.second)

    return True
