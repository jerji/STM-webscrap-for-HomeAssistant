# custom_components/stm_metro_status/__init__.py
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

DOMAIN = "stm_metro_status"

async def async_setup(hass: HomeAssistant, config: ConfigType):
    """Set up the STM Metro Status integration."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry):
    """Set up STM Metro Status from a config entry."""
    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
    return True

async def async_unload_entry(hass: HomeAssistant, entry):
    """Unload STM Metro Status config entry."""
    await hass.config_entries.async_unload_platforms(entry, ["sensor"])
    return True