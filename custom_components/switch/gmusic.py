"""
"""
import asyncio
import logging
import time
import random
import pickle
import os.path
from datetime import timedelta

from homeassistant.const import ATTR_ENTITY_ID, SERVICE_TURN_OFF, EVENT_HOMEASSISTANT_START
from homeassistant.util import dt as dt_util
from homeassistant.components.switch import (
    ENTITY_ID_FORMAT, SwitchDevice, PLATFORM_SCHEMA)
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.event import track_state_change, track_time_change
from homeassistant.components.sensor.rest import RestData
from homeassistant.components.media_player import (
    SERVICE_PLAY_MEDIA, MEDIA_TYPE_MUSIC, ATTR_MEDIA_CONTENT_ID,
    ATTR_MEDIA_CONTENT_TYPE, DOMAIN as DOMAIN_MP)
from homeassistant.config import get_default_config_dir

import homeassistant.components.input_select as input_select

REQUIREMENTS = ['gmusicapi==10.1.2']
# The domain of your component. Should be equal to the name of your component.
DOMAIN = "gmusic"

DEPENDENCIES = ['group', ]

# Shortcut for the logger
_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the Gmusic switch."""
    add_devices([GmusicComponent(hass, config)])
    return True

class GmusicComponent(SwitchDevice):

    def __init__(self, hass, config):

        from gmusicapi import Mobileclient
        # https://github.com/simon-weber/gmusicapi/issues/424
        class GMusic(Mobileclient):
            def login(self, username, password, device_id, authtoken=None):
                if authtoken:
                    self.android_id               = device_id
                    self.session._authtoken       = authtoken
                    self.session.is_authenticated = True

                    try:
                        # Send a test request to ensure our authtoken is still valide and working
                        self.get_registered_devices()
                        return True
                    except:
                        # Faild with the test-request so we set "is_authenticated=False"
                        # and go through the login-process again to get a new "authtoken"
                        self.session.is_authenticated = False

                if device_id:
                    if super(GMusic, self).login(username, password, device_id):
                        return True

                # Prevent further execution in case we failed with the login-process
                raise SystemExit

        self.hass = hass
        authtoken_path = get_default_config_dir() + "gmusic_authtoken"
        if os.path.isfile(authtoken_path):
            with open(authtoken_path, 'rb') as handle:
                authtoken = pickle.load(handle)
        else:
            authtoken = None
        self._api = GMusic()
        logged_in = self._api.login(config.get('user'), config.get('password'), config.get('device_id'), authtoken)
        if not logged_in:
            _LOGGER.error("Failed to log in, check http://unofficial-google-music-api.readthedocs.io/en/latest/reference/mobileclient.html#gmusicapi.clients.Mobileclient.login")	
            return False
        with open(authtoken_path, 'wb') as f:
            pickle.dump(self._api.session._authtoken, f)
        

        self._playlist = "input_select." + config.get("playlist","")
        self._media_player = "input_select." + config.get("media_player","")
        self._entity_ids = []
        self._playing = False
        self._playlists = []
        self._tracks = []
        self._next_track_no = 0
        self._playlist_to_index = {}
        self._unsub_tracker = None
        self._name = "Google music"
        track_time_change(hass, self._update_playlist, hour=[15, 6], minute=46, second=46)
        hass.bus.listen_once(EVENT_HOMEASSISTANT_START, self._update_playlist)

    @property
    def icon(self):
        return 'mdi:music-note'

    @property
    def name(self):
        """Return the name of the switch."""
        return self._name

    @property
    def is_on(self):
        """Return true if device is on."""
        return self._playing

    @property
    def should_poll(self):
        """No polling needed."""
        return False

    def turn_on(self, **kwargs):
        """Fire the on action."""
        if self._playing:
            return
        self._play()

    def turn_off(self, **kwargs):
        """Fire the off action."""
        self._turn_off_media_player()

    def _update_playlist(self, now=None):
        if self.hass.states.get(self._playlist) is None:
            _LOGGER.error("%s is not a valid input_select entity.", self._playlist)
            return        
        self._playlists = self._api.get_all_user_playlist_contents()
        self._playlist_to_index = {}
        idx = -1
        for playlist in self._playlists:
            idx = idx + 1
            name = playlist.get('name','')
            if len(name) < 1:
                continue
            self._playlist_to_index[name] = idx
        data = {"options": list(self._playlist_to_index.keys()), "entity_id": self._playlist}
        self.hass.services.call(input_select.DOMAIN, input_select.SERVICE_SET_OPTIONS, data)

    def _turn_off_media_player(self):
        self._playing = False
        if self._unsub_tracker is not None:
            self._unsub_tracker()
            self._unsub_tracker = None
        data = {ATTR_ENTITY_ID: self._entity_ids}
#        self.hass.services.call(DOMAIN_MP, SERVICE_TURN_OFF, data, blocking=True)
        self.schedule_update_ha_state()
        
    def _update_entity_ids(self):
        media_player = self.hass.states.get(self._media_player)
        if media_player is None:
            _LOGGER.error("%s is not a valid input_select entity.", self._media_player)
            return False
        _entity_ids = "media_player." + media_player.state
        if self.hass.states.get(_entity_ids) is None:
            _LOGGER.error("%s is not a valid media player.", media_player.state)
            return False
        self._entity_ids = _entity_ids 
        return True

    def _next_track(self, entity_id=None, old_state=None, new_state=None, retry=3):
        if not self._playing:
            return
        if self._next_track_no >= len(self._tracks):
            self._next_track_no = 0
        track = self._tracks[self._next_track_no]
        if track is None:
            self._turn_off_media_player() 
            return
        print(track)
        try:
            url = self._api.get_stream_url(track['trackId'])
        except Exception as err:
            self._next_track_no = self._next_track_no + 1
            _LOGGER.error("Failed to get track (%s)", err)
            if retry < 1:
                self._turn_off_media_player()
                return
            return self._next_track(retry=retry-1)
        data = {
            ATTR_MEDIA_CONTENT_ID: url,
            ATTR_MEDIA_CONTENT_TYPE: "audio/mp3",
        }

        data[ATTR_ENTITY_ID] = self._entity_ids
        self.schedule_update_ha_state()
        self.hass.services.call(DOMAIN_MP, SERVICE_PLAY_MEDIA, data)
        self._next_track_no = self._next_track_no + 1

    def _play(self):
        if not self._update_entity_ids():
            return
        _playlist = self.hass.states.get(self._playlist)
        if _playlist is None:
            _LOGGER.error("%s is not a valid input_select entity.", self._playlist)
            return   
        option = _playlist.state
        idx = self._playlist_to_index.get(option)
        if idx is None:
            self._turn_off_media_player()
            return

        self._tracks = self._playlists[idx]['tracks']
        random.shuffle(self._tracks)
        self._next_track_no = 0
        self._playing = True
        self._next_track()
        self._unsub_tracker = track_state_change(self.hass, self._entity_ids, self._next_track, from_state='playing', to_state='idle')