from homeassistant.helpers.discovery import async_load_platform

DOMAIN = "stm_metro_status"

async def async_setup(hass, config):
    """Set up the STM Metro Status integration."""
    hass.data[DOMAIN] = {}
    hass.async_create_task(
        async_load_platform(hass, "sensor", DOMAIN, {}, config)
    )
    return True