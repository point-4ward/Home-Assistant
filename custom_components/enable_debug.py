DOMAIN = 'enable_debug'

async def async_setup(hass, config):
    hass.loop.set_debug(True)
    return True
