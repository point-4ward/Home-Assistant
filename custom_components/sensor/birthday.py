import datetime
import logging

import voluptuous as vol

from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import PLATFORM_SCHEMA


_LOGGER = logging.getLogger(__name__)


ICON = 'mdi:cake-variant'
CONF_NAME = 'name'
CONF_MONTH = 'month'
CONF_DAY = 'day'


PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_NAME):cv.string,
    vol.Required(CONF_MONTH):cv.positive_int,
    vol.Required(CONF_DAY):cv.positive_int
})


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the sensor platform."""

    name = config.get(CONF_NAME)
    month = config.get(CONF_MONTH)
    day = config.get(CONF_NAME)

    add_devices([Birthday(name, month, day)], True)


class Birthday(Entity):
    """Representation of a Sensor."""

    def __init__(self, name, month, day):
        """Initialize the sensor."""
        self._state = None
        self._name = name
        self._month = month
        self._day = day
        self._unit_of_measurement = "days"

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""

        check = datetime.datetime(datetime.datetime.now().year, self._month, self._day)
        now = datetime.datetime.now()

        if check - now < 0:
            birthday = check - now
        else:
            birthday = datetime.datetime(datetime.datetime.now().year + 1, self._month, self._day) - now

        return birthday

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return self._unit_of_measurement

    @property
    def icon(self):
        """Icon to use in the frontend, if any."""
        return ICON

    def update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        self._state = 23
